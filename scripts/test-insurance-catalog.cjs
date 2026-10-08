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
console.log('PASS: idempotent catalog merge, preserved entries/navigation, one card and five translated destinations.');
