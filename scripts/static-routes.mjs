import {readFile,writeFile,mkdir,copyFile} from 'node:fs/promises';
const base=await readFile('dist/index.html','utf8');
const routes=[['eba-minamata-2026','EBA Minamata Fieldwork 2026'],['venture-base-2025','Venture Base Hackathon 2025'],['code2career-2024','Code2Career Hackathon 2024']];
for(const [slug,title] of routes){const dir=`dist/activities/${slug}`;await mkdir(dir,{recursive:true});await writeFile(`${dir}/index.html`,base.replace(/<title>.*?<\/title>/,`<title>${title} — Yoon Thiri Aung</title>`).replace('property="og:title" content="Yoon Thiri Aung — Portfolio"',`property="og:title" content="${title} — Yoon Thiri Aung"`));}
await copyFile('dist/index.html','dist/404.html');
console.log('Static activity URLs generated: '+routes.length);
