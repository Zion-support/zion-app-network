'use strict';
const assert=require('node:assert/strict');
const {ids,repairCatalog,repairHub}=require('./repair-insurance-catalog.cjs');
const original='# Existing catalog\n\n**Total repositories: 1**\n\n[Preserve me](https://github.com/Zion-support/keep-this-repo)\n';
for(const kind of ['index','catalog']){
 const once=repairCatalog(original,kind),twice=repairCatalog(once,kind);
 assert.equal(once,twice);assert(ids(once).has('keep-this-repo'));assert.equal(ids(once).size,4);
 for(const slug of ['policy-comparison-ai','underwriting-copilot-ai','claims-automation-ai'])assert(ids(once).has(slug));
 assert.equal((once.match(/<!--insurance-catalog-note:start-->/g)||[]).length,1);
}
const hub='<html><body><a href="/preserve/">Keep</a><h2>Old content</h2><p>Do not remove</p></body></html>';
const once=repairHub(hub);assert.equal(once,repairHub(once));assert(once.includes('href="/preserve/"'));assert(once.includes('<p>Do not remove</p>'));
for(const prefix of ['', '/pt','/es','/fr','/de'])assert(once.includes('https://ziontechgroup.com'+prefix+'/apps/insurance-evidence-workbench.html'));
// Real hub is a Liquid capture template, not a plain HTML document.
// It contains an unmatched insurance start marker inside start_here plus an
// identical *quoted* marker in a Liquid replacement expression.
const liquid=[
  '---\nlayout: null\n---',
  '{% capture start_here %}<section id="network-start-here"><h2>Start here</h2></section><!--insurance-evidence-hub:start-->{% endcapture %}',
  "{% assign corrected = corrected | replace: '<!--insurance-evidence-hub:start-->', start_here %}",
  '{{ corrected }}',
  '<a href="/preserve-existing-link/">Keep</a>'
].join('\n');
const liquidOnce=repairHub(liquid);
assert.equal(liquidOnce,repairHub(liquidOnce),'Liquid repair must be idempotent');
assert.equal((liquidOnce.match(/id="insurance-evidence-hub"/g)||[]).length,1,'Exactly one inserted section');
assert(liquidOnce.includes('{% capture start_here %}'),'Liquid capture must be preserved');
assert(liquidOnce.includes("{% assign corrected = corrected | replace: '<!--insurance-evidence-hub:start-->', start_here %}"),'Quoted Liquid marker must not be consumed');
assert(liquidOnce.includes('href="/preserve-existing-link/"'),'Unrelated navigation preserved');

console.log('PASS: idempotent catalog merge, preserved entries/navigation, one card and five translated destinations.');
