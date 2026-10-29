import copy
import datetime as dt
import unittest
from unittest.mock import patch
import observe_aliases as m

E = {'url': 'https://alias.example/', 'canonical': 'https://canonical.example/page/', 'redirect_status': 302}

class ObserverTests(unittest.TestCase):
    def run_probe(self, responses, entry=E, query=''):
        seen = []
        def fetch(url, method):
            seen.append(url)
            return responses.pop(0)
        return m.probe(entry, query=query, fetch=fetch), seen

    def test_200(self):
        self.assertIsNone(self.run_probe([{'status':200}], {'url':E['url'], 'canonical':E['url']})[0]['error'])

    def test_correct_redirect_and_query(self):
        result, seen = self.run_probe([{'status':302,'location':E['canonical']+m.QUERY},{'status':200}],query=m.QUERY)
        self.assertIsNone(result['error'])
        self.assertEqual(seen,[E['url']+m.QUERY,E['canonical']+m.QUERY])

    def test_wrong_destination_not_fetched(self):
        for target in ['https://other.example/', 'http://canonical.example/page/']:
            result, seen = self.run_probe([{'status':302,'location':target}])
            self.assertEqual(result['error'],'redirect_destination_or_query')
            self.assertEqual(len(seen),1)

    def test_dropped_query(self):
        self.assertEqual(self.run_probe([{'status':302,'location':E['canonical']}],query=m.QUERY)[0]['error'],'redirect_destination_or_query')

    def test_loop(self):
        self.assertEqual(self.run_probe([{'status':302,'location':E['url']}])[0]['error'],'redirect_loop')

    def test_limit(self):
        self.assertEqual(self.run_probe([{'status':302,'location':E['canonical']},{'status':302,'location':'https://third.example/'}])[0]['error'],'redirect_limit')

    def test_status(self):
        self.assertEqual(self.run_probe([{'status':503}])[0]['error'],'status_or_destination')

    def test_dns_and_tls(self):
        for error in ('dns','tls'):
            self.assertEqual(self.run_probe([{'error':error}])[0]['error'],error)

    def test_known_failure_deadline_and_recovery(self):
        entry={'known_issue':{'error':'tls','review_by':'2026-10-30T18:00:00+00:00'}}
        now=dt.datetime(2026,10,29,tzinfo=dt.timezone.utc)
        self.assertEqual(m.classify(entry,{'error':'tls'},now),'KNOWN_FAILURE')
        self.assertEqual(m.classify(entry,{'error':'tls'},now+dt.timedelta(days=2)),'KNOWN_FAILURE_OVERDUE')
        self.assertEqual(m.classify(entry,{'error':None},now),'RECOVERY_REVIEW')
        self.assertEqual(m.classify(entry,{'error':'dns'},now),'FAILURE')

    def test_curl_strict_and_bounded_retry(self):
        with patch.object(m.subprocess,'run') as run, patch.object(m.time,'sleep'):
            run.return_value.returncode=6
            self.assertEqual(m.request(E['url'],'HEAD')['error'],'dns')
            self.assertEqual(run.call_count,2)
            args=run.call_args.args[0]
            self.assertNotIn('--insecure',args)
            self.assertNotIn('--location',args)
            self.assertIn('--head',args)
        with patch.object(m.subprocess,'run') as run:
            run.return_value.returncode=60
            self.assertEqual(m.request(E['url'],'GET')['error'],'tls')
            self.assertEqual(run.call_count,1)

    def valid_results(self):
        entries = m.load_inventory()
        entries = [{k:v for k,v in entry.items() if k != 'known_issue'} for entry in entries]
        rows = [{**entry, 'checks': [{'method':method, 'query_probe':query,
                 'state':'HEALTHY', 'error':None, 'chain':[{'status':200}]}
                 for method, query in sorted(m.PLANNED_PROBES)]} for entry in entries]
        return entries, rows

    def test_exit_codes(self):
        entries, rows = self.valid_results()
        self.assertEqual(m.exit_code(rows, entries), 0)
        issue = m.load_inventory()[-1]['known_issue']
        for state, code in [('KNOWN_FAILURE',2), ('RECOVERY_REVIEW',2), ('FAILURE',1), ('KNOWN_FAILURE_OVERDUE',1)]:
            entries[-1]['known_issue'] = issue
            rows[-1]['known_issue'] = issue
            for check in rows[-1]['checks']:
                check['state'] = state
                check['error'] = None if state == 'RECOVERY_REVIEW' else 'tls'
            self.assertEqual(m.exit_code(rows, entries), code)

    def test_empty_inventory_and_results_fail_closed(self):
        with self.assertRaises(ValueError):
            m.validate_inventory([])
        self.assertEqual(m.exit_code([]), 1)
        self.assertEqual(m.exit_code([{'checks':[]}]), 1)
        self.assertEqual(m.exit_code([], []), 1)

    def test_incomplete_and_duplicate_coverage(self):
        entries, baseline = self.valid_results()
        variants = [[], baseline[:-1], baseline + [baseline[0]]]
        for count in (0, 1, 3):
            rows = copy.deepcopy(baseline)
            rows[0]['checks'] = rows[0]['checks'][:count]
            variants.append(rows)
        rows = copy.deepcopy(baseline)
        rows[0]['checks'][0] = rows[0]['checks'][1]
        variants.append(rows)
        rows = copy.deepcopy(baseline)
        rows[0] = rows[1]
        variants.append(rows)
        for rows in variants:
            self.assertEqual(m.exit_code(rows, entries), 1)

    def test_invalid_configuration(self):
        baseline = m.load_inventory()
        variants = [None, {}, [], baseline + [baseline[0]]]
        for key, value in [('name', ''), ('url', 'http://discovery.ziontechgroup.com/'),
                           ('canonical','https://evil.example/'), ('redirect_status',301),
                           ('unknown',True), ('url',42)]:
            entries = copy.deepcopy(baseline)
            entries[0][key] = value
            variants.append(entries)
        entries = copy.deepcopy(baseline)
        del entries[0]['canonical']
        variants.append(entries)
        entries = copy.deepcopy(baseline)
        entries[-1]['known_issue']['review_by'] = '2026-10-30T18:00:00'
        variants.append(entries)
        for entries in variants:
            with self.subTest(entries=entries), self.assertRaises((ValueError, TypeError)):
                m.validate_inventory(entries)

    def test_invalid_manifest_stops_before_network(self):
        with patch.object(m, 'load_inventory', side_effect=ValueError), patch.object(m, 'observe') as observe, patch('sys.argv',['observe_aliases.py']):
            self.assertEqual(m.main(),1)
            observe.assert_not_called()

    def test_unknown_state_or_missing_evidence_fails(self):
        entries, baseline = self.valid_results()
        for key, value in [('state','SKIPPED'),('chain',[]),('query_probe',1),('error','tls')]:
            rows = copy.deepcopy(baseline)
            rows[0]['checks'][0][key] = value
            self.assertEqual(m.exit_code(rows,entries),1)

if __name__ == '__main__':
    unittest.main()
