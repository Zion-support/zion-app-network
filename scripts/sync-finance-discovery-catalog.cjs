'use strict';
// Add verified source-status entries without replacing or recounting the master catalog.
const fs=require('node:fs'),assert=require('node:assert/strict');
const entries=[['cash-flow-forecaster','Cash Flow Forecaster','Documented treasury concept; no forecast engine verified'],['ar-collections-copilot','AR Collections Copilot','Documented receivables concept; no collections engine verified'],['aml-screening-ai','AML Screening AI','Informational AML review concept; not verified live screening'],['fraud-transaction-monitor','Fraud Transaction Monitor','Informational transaction review concept; not verified live fraud scoring']];
for(const file of ['CATALOG.md','APPS_INDEX.md']){assert(fs.existsSync(file));let text=fs.readFileSync(file,'utf8');const missing=entries.filter(([slug])=>!text.includes('https://github.com/Zion-support/'+slug));if(!missing.length){console.log(file+': already linked');continue;}text+='\n## Finance Discovery paths — source review 2026-10-08\n\nThese entries describe inspected concepts, not certified production apps. Existing count statements were not recalculated.\n\n| App | Public concept | Source | Capability status |\n|---|---|---|---|\n'+missing.map(([slug,name,status])=>`| ${name} | [Explore](https://ziontechgroup.com/${slug}/) | [GitHub](https://github.com/Zion-support/${slug}) | ${status} |`).join('\n')+'\n\n[Benefits and translation matrix](DISCOVERY_CONSOLIDATION_2026-10-08.md) · [Content standard](CONTENT_PUBLICATION_STANDARD.md) · [Workflow guide](https://ziontechgroup.com/apps/discovery-workflow-paths.html) · [Free Discovery](https://ziontechgroup.com/discovery/).\n';fs.writeFileSync(file,text);console.log(file+': added '+missing.length+' source-status entries');for(const [slug] of entries)assert(text.includes('https://github.com/Zion-support/'+slug));}

// Approved Mining merge: documentation concepts, never certified safety tools.
const mining=[['mine-safety-sentinel','Mine Safety Sentinel'],['ore-grade-predictor','Ore Grade Predictor'],['mining-fleet-optimizer','Mining Fleet Optimizer'],['tailings-dam-monitor','Tailings Dam Monitor']];
const repoIds=s=>new Set([...s.matchAll(/https:\/\/github\.com\/Zion-support\/([A-Za-z0-9_.-]+)/g)].map(m=>m[1]));
function mergeMining(source){
 const before=repoIds(source),missing=mining.filter(([slug])=>!before.has(slug));
 let result=source;
 if(missing.length)result+='\n\n## Mining & Metals — documented concepts, not validated AI\n\nThe repositories provide documentation and network links; public destinations are landing pages. Do not use them for emergency response, dam-stability decisions, regulatory certification, safety approvals or autonomous equipment control. Qualified review and validated systems remain necessary.\n\n| Concept | Landing page | Source |\n|---|---|---|\n'+missing.map(([slug,name])=>'| '+name+' | [Explore](https://ziontechgroup.com/'+slug+'/) | [GitHub](https://github.com/Zion-support/'+slug+') |').join('\n')+'\n\n[Mining supplement and five translated guides](CATALOG-MINING.md) · [Catalog navigation](CATALOG-NAVIGATION.md) · [Free Discovery](https://ziontechgroup.com/discovery/).\n';
 const after=repoIds(result);for(const id of before)assert(after.has(id),'Existing source lost '+id);
 for(const [slug] of mining)assert(after.has(slug),'Missing Mining source '+slug);
 result=result.replace(/This catalog contains \d+ unique linked repositories\./,'This catalog contains '+after.size+' unique linked repositories.');
 return result;
}
const catalog=fs.readFileSync('CATALOG.md','utf8'),merged=mergeMining(catalog);
assert.equal(mergeMining(merged),merged,'Mining merge must be idempotent');
assert.equal(repoIds(merged).size,repoIds(catalog).size+mining.filter(([slug])=>!repoIds(catalog).has(slug)).length);
if(merged!==catalog)fs.writeFileSync('CATALOG.md',merged);
console.log('PASS Mining: all four source links present, existing links preserved, deterministic link count.');
