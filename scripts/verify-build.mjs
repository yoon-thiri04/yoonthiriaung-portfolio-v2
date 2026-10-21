import {readFile,access,readdir} from 'node:fs/promises';
import {build} from 'esbuild';
import assert from 'node:assert/strict';
const result=await build({entryPoints:['src/content.ts'],bundle:true,platform:'node',format:'esm',write:false});
const content=await import('data:text/javascript;base64,'+Buffer.from(result.outputFiles[0].text).toString('base64'));
assert.deepEqual(content.builds.map(p=>p.name),['Anipulse','WolfEye+','UCSY Intellichat','Flavour Forge','PathFinder','Ink2Text-MM','EnvironNet']);
assert.equal(content.builds[0].photo.key,'projects/01-anipulse/approved-new-cover.png');
for(const item of content.builds){for(const url of [item.github,item.demo].filter(Boolean))assert.equal(new URL(url).protocol,'https:');}
const photos=[...content.builds.map(p=>p.photo),...content.awards.flatMap(a=>a.photos),...content.activities.flatMap(a=>[a.cover,...(a.story?.photos||[]),...(a.story?.certificate?[a.story.certificate]:[])]),...content.credentials.flatMap(c=>c.photos||[])];
for(const photo of photos){const asset=content.asset(photo.key);assert(photo.alt.length>10);for(const src of [asset.src,asset.full])await access('public'+src);}
for(const slug of content.storySlugs)await access(`dist/activities/${slug}/index.html`);
assert.equal(content.activities.find(a=>a.id==='falcon-hackathon').start,'2024-07-26');
assert.equal(content.eventStatus(content.activities[0],new Date('2026-10-20T00:00:00Z')),'Upcoming');
assert.equal(content.eventStatus(content.activities[0],new Date('2026-11-06T00:00:00Z')),'Paper accepted');
assert.equal(content.credentials.at(-1).last,true);
assert.equal(content.credentials.filter(c=>!c.photos).length,1);
for(const icon of content.skillGroups.flatMap(g=>g.items).map(s=>s.icon).filter(Boolean))await access(`public/icons/${icon}.svg`);
for(const skill of content.skillGroups.flatMap(g=>g.items))if(skill.iconFile)await access('public'+skill.iconFile);
const source=await readFile('src/App.tsx','utf8');assert(!source.includes('Selected work'));assert(!source.includes('Departing for EBA'));
const dirs=await readdir('dist');assert(dirs.includes('index.html'));assert(dirs.includes('_redirects'));
console.log(`PASS: 7 builds in order; ${photos.length} image references; 3 directly loadable stories; all skill logos; date/status safeguards; supplied links; Netlify routing.`);
