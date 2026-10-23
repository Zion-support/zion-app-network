"""Offline supply-chain guard regression fixtures; no secrets or GitHub API."""
import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, main

spec = importlib.util.spec_from_file_location('guard', Path(__file__).with_name('workflow_supply_chain_guard.py'))
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class WorkflowSupplyChainTests(TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)

    def check(self, yaml, name='sample.yml', allowlist=None):
        (self.directory / name).write_text(yaml, encoding='utf-8')
        return guard.scan_workflows(self.directory, {} if allowlist is None else allowlist)

    def test_pinned_step_accepted(self):
        self.assertEqual(self.check('jobs:\n  a:\n    steps:\n      - uses: actions/checkout@' + 'a'*40 + '\n'), [])

    def test_mutable_step_ref_rejected(self):
        self.assertTrue(any('not pinned' in s for s in self.check('jobs:\n  a:\n    steps:\n      - uses: actions/checkout@v4\n')))

    def test_job_level_reusable_workflow_ref_rejected(self):
        self.assertTrue(any('not pinned' in s for s in self.check('jobs:\n  build:\n    uses: sample/cicd/.github/workflows/verify.yml@main\n')))

    def test_job_level_reusable_workflow_sha_accepted(self):
        self.assertEqual(self.check('jobs:\n  build:\n    uses: sample/cicd/.github/workflows/verify.yml@' + 'b'*40 + '\n'), [])

    def test_docker_digest_allowed_but_tag_rejected(self):
        valid = 'jobs:\n  a:\n    steps:\n      - uses: docker://alpine@sha256:' + 'a'*64 + '\n'
        self.assertEqual(self.check(valid), [])
        self.assertTrue(self.check('jobs:\n  a:\n    steps:\n      - uses: docker://alpine:latest\n'))

    def test_local_reusable_workflow_accepted(self):
        self.assertEqual(self.check('jobs:\n  test:\n    uses: ./.github/workflows/reuse.yml\n'), [])

    def test_uses_inside_shell_block_ignored(self):
        self.assertEqual(self.check('jobs:\n  a:\n    steps:\n      - run: |\n          echo "uses: sample/cicd@main"\n          uses: sample/cicd@latest\n'), [])

    def test_unsupported_expression_uses_fails_closed(self):
        self.assertTrue(self.check('jobs:\n  a:\n    uses: ${{ inputs.action }}\n'))

    def test_unreviewed_contents_write_rejected(self):
        self.assertTrue(any('contents: write' in s for s in self.check('permissions:\n  contents: write\n')))

    def test_restricted_writer_allowed(self):
        content='permissions:\n  contents: write\njobs:\n  a:\n    steps:\n      - uses: actions/checkout@'+'a'*40+'\n'
        self.assertEqual(self.check(content,name='known.yml',allowlist={'known.yml':{'contents'}}), [])

    def test_extra_write_permission_rejected_on_allowlisted_writer(self):
        content='permissions:\n  contents: write\n  actions: write\n'
        self.assertTrue(any('actions: write' in s for s in self.check(content,name='known.yml',allowlist={'known.yml':{'contents'}})))

    def test_writer_permission_removed_fails_closed(self):
        self.assertTrue(any('expected reviewed' in s for s in self.check('permissions:\n  contents: read\n',name='known.yml',allowlist={'known.yml':{'contents'}})))

    def test_inline_permissions_enforced(self):
        self.assertTrue(self.check('permissions: {contents: write, issues: read}\n'))

    def test_write_all_permission_rejected(self):
        self.assertTrue(self.check('permissions: write-all\n'))

    def test_quoted_action_with_trailing_comment(self):
        self.assertEqual(self.check("jobs:\n  a:\n    uses: 'sample/ci@" + 'f'*40 + "' # pinned\n"), [])

    def test_trailing_comments_cannot_bypass_write_scope_check(self):
        self.assertTrue(any('issues: write' in s for s in self.check('permissions:\n  issues: write # harmless-looking note\n')))

    def test_trailing_comments_cannot_bypass_write_all_check(self):
        self.assertTrue(any('write-all' in s for s in self.check('permissions: write-all # comment\n')))

    def test_empty_directory_does_not_pass(self):
        self.assertTrue(any('No workflow' in s for s in guard.scan_workflows(self.directory, {})))


if __name__ == '__main__':
    main()
