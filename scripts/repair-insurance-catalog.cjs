'use strict';
// Deterministic catalog maintenance. No API calls, deletes or AI-readiness claims.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const version='2026-10-08-catalog-insurance-v1';
const concepts=[['policy-comparison-ai','Policy Comparison AI','Policy-comparison workflow concept; no AI engine implemented'],['underwriting-copilot-ai','Underwriting Copilot AI','Underwriting-intake workflow concept; no AI engine implemented'],['claims-automation-ai','Claims Automation AI','Claims-evidence workflow concept; no AI engine implemented']];
const ids=s=>new Set([...s.matchAll(/https:\/\/github\.com\/Zion-support\/([A-Za-z0-9_.-]+)/g)].map(m=>m[1]));
function repairCatalog(source,kind){
 const before=ids(source),missing=concepts.filter(([slug])=>!before.has(slug));
 let result=source;
 if(missing.length){const heading='\n\n## Insurance workflow concepts — documentation, not deployed AI\n\n';
 const rows=missing.map(([slug,name,description])=>kind==='index'?'| ['+name+'](https://github.com/Zion-support/'+slug+') | '+description+' | [Planning page](https://ziontechgroup.com/'+slug+'/) |':'- ['+name+'](https://github.com/Zion-support/'+slug+') — '+description+'. [Planning page](https://ziontechgroup.com/'+slug+'/).').join('\n');
 result+=heading+(kind==='index'?'| Repository | Current implementation | Planning page |\n|---|---|---|\n':'')+rows+'\n';}
 const after=ids(result);for(const id of before)assert(after.has(id),'Existing repository lost: '+id);
 for(const [slug] of concepts)assert(after.has(slug),'Missing concept '+slug);
 const note='<!--insurance-catalog-note:start-->\n[Insurance catalog status](CATALOG-INSURANCE-EVIDENCE.md) · [Free local evidence workbench](https://ziontechgroup.com/apps/insurance-evidence-workbench.html) · [Free Discovery](https://ziontechgroup.com/discovery/)\n\nInsurance entries below are documentation concepts, not functioning AI engines. The linked workbench is a local checklist, with no model inference, document upload or regulated decision. Legacy category counts are snapshots; a repository link is not evidence of a working app.\n<!--insurance-catalog-note:end-->';
 if(result.includes('<!--insurance-catalog-note:start-->'))result=result.replace(/<!--insurance-catalog-note:start-->[\s\S]*?<!--insurance-catalog-note:end-->/,note);
 else{assert(/^# .+\n/.test(result),'Catalog title missing');result=result.replace(/^(# .+\n)/,'$1\n'+note+'\n');}
 if(kind==='index')result=result.replace(/\*\*Total repositories: \d+\*\*/,'**Unique repository links in this index: '+after.size+'**');
 else result=result.replace(/^\d+ repositories in the Zion Tech Group network\.[^\n]*/m,'This catalog contains '+after.size+' unique linked repositories. It includes documentation concepts, tools and field playbooks; this is not a verified count of functioning apps.');
 return result;
}
const copy={
 en:['Insurance evidence: plan before automating','Record a synthetic example, owner, baseline, evidence gaps, qualified reviewer and stop rule. Download your brief locally. No upload, AI inference or insurance decision.','Open the free workbench','Free Discovery'],
 pt:['Evidências de seguros: planeje antes de automatizar','Registre exemplo sintético, responsável, linha de base, lacunas de evidência, revisor qualificado e regra de parada. Baixe o plano localmente. Sem upload, inferência de IA ou decisão de seguro.','Abrir o workbench gratuito','Discovery gratuito'],
 es:['Evidencias de seguros: planifique antes de automatizar','Registre un ejemplo sintético, responsable, línea base, carencias de evidencia, revisor cualificado y regla de parada. Descargue el plan localmente. Sin carga de datos, inferencia de IA ni decisiones de seguros.','Abrir el workbench gratuito','Discovery gratuito'],
 fr:['Preuves d’assurance : planifier avant d’automatiser','Documentez un exemple synthétique, un responsable, une référence initiale, les lacunes, un validateur qualifié et une règle d’arrêt. Téléchargez la fiche localement. Aucun envoi de données, inférence IA ou décision d’assurance.','Ouvrir l’atelier gratuit','Discovery gratuit'],
 de:['Versicherungsnachweise: vor der Automatisierung planen','Dokumentieren Sie ein synthetisches Beispiel, Verantwortliche, Ausgangswerte, Nachweislücken, qualifizierte Prüfung und Abbruchregel. Laden Sie den Plan lokal herunter. Kein Upload, keine KI-Inferenz und keine Versicherungsentscheidung.','Kostenlose Workbench öffnen','Kostenloses Discovery']};
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function repairHub(source){
 assert(source.includes('</body>'),'Hub body missing');
 const block='<!--insurance-evidence-hub:start--><section id="insurance-evidence-hub" data-catalog-release="'+version+'">'+Object.entries(copy).map(([l,c])=>{const prefix=l==='en'?'':'/'+l;return '<details lang="'+(l==='pt'?'pt-BR':l)+'" '+(l==='en'?'open':'')+'><summary>'+esc(c[0])+'</summary><p>'+esc(c[1])+'</p><p><a class="cta" href="https://ziontechgroup.com'+prefix+'/apps/insurance-evidence-workbench.html">'+esc(c[2])+'</a> · <a href="https://ziontechgroup.com'+prefix+'/discovery/">'+esc(c[3])+'</a></p></details>';}).join('')+'<p><a href="https://ziontechgroup.com/policy-comparison-ai/">Policy Comparison AI</a> · <a href="https://ziontechgroup.com/underwriting-copilot-ai/">Underwriting Copilot AI</a> · <a href="https://ziontechgroup.com/claims-automation-ai/">Claims Automation AI</a></p></section><!--insurance-evidence-hub:end-->';
 let result;
 if(source.includes('<!--insurance-evidence-hub:start-->'))result=source.replace(/<!--insurance-evidence-hub:start-->[\s\S]*?<!--insurance-evidence-hub:end-->/,block);
 else{assert(/<h2\b/.test(source),'Hub section anchor missing');result=source.replace(/<h2\b/,block+'\n<h2');}
 assert.equal((result.match(/id="insurance-evidence-hub"/g)||[]).length,1);
 for(const old of source.matchAll(/href="([^"]+)"/g))assert(result.includes('href="'+old[1]+'"'),'Existing navigation lost');
 return result;
}
function run(root){
 const files=['APPS_INDEX.md','CATALOG.md','index.html'];
 const originals=files.map(f=>fs.readFileSync(path.join(root,f),'utf8'));
 const updates=[repairCatalog(originals[0],'index'),repairCatalog(originals[1],'catalog'),repairHub(originals[2])];
 for(let i=0;i<files.length;i++)if(updates[i]!==originals[i])fs.writeFileSync(path.join(root,files[i]),updates[i]);
 const supplement=path.join(root,'CATALOG-INSURANCE-EVIDENCE.md');
 if(fs.existsSync(supplement)){let s=fs.readFileSync(supplement,'utf8');s=s.replace(/Merge these entries into APPS_INDEX\.md and CATALOG\.md while preserving other agents['’] edits\./,'The three entries have now been merged into APPS_INDEX.md and CATALOG.md by the consistency repair.');const marker='<!--insurance-master-merge:'+version+'-->';if(!s.includes(marker))s+='\n\n'+marker+'\nMaster catalog merge complete: all three concept repositories are linked in both files. Existing repository links were preserved and the legacy hub includes the five-language workbench card.\n';fs.writeFileSync(supplement,s);}
 console.log('PASS: three insurance concepts present in both master catalogs; existing links preserved; five-language hub card inserted once.');
}
module.exports={ids,repairCatalog,repairHub};
if(require.main===module)run(process.argv[2]||'.');
