from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
import hashlib,json,re,shutil,argparse
parser=argparse.ArgumentParser(description='Generate portfolio media derivatives without changing originals.')
parser.add_argument('--source-assets',type=Path,required=True,help='Extracted assests directory from the supplied ZIP')
parser.add_argument('--anipulse-cover',type=Path,required=True,help='Approved replacement Anipulse PNG')
args=parser.parse_args()
source=args.source_assets.resolve();out=Path(__file__).resolve().parent.parent
media=out/'public/media';media.mkdir(exist_ok=True)
files=sorted(p for p in source.rglob('*') if p.suffix.lower() in ('.jpg','.jpeg','.png'))
files.append(args.anipulse_cover.resolve())
records={};inventory=[]
for path in files:
 key=str(path.relative_to(source)) if source in path.parents else 'projects/01-anipulse/approved-new-cover.png'
 raw=path.read_bytes();sha=hashlib.sha256(raw).hexdigest()[:12]
 im=ImageOps.exif_transpose(Image.open(path));w,h=im.size
 is_cert='certifications/' in key or 'certificate' in key or 'cerfiticate' in key or 'invitation' in key or 'myGPA' in key or 'icait' in key
 versions=[]
 for size in [640,1280]:
  display=im.copy();display.thumbnail((size,size*2));name=f'{sha}-{size}.webp';display.save(media/name,'WEBP',quality=92 if is_cert else 86)
  versions.append({'src':'/media/'+name,'width':display.width})
 if is_cert:
  full_name=sha+'-full'+path.suffix.lower();shutil.copy2(path,media/full_name)
 else:
  full=im.copy();full.thumbnail((2560,2560));full_name=sha+'-full.webp';full.save(media/full_name,'WEBP',quality=94)
 record={'src':versions[-1]['src'],'srcSet':', '.join(f"{v['src']} {v['width']}w" for v in versions),'full':'/media/'+full_name,'width':w,'height':h}
 records[key]=record
 inventory.append({'original':key,'source_filename':path.name,'sha256':hashlib.sha256(raw).hexdigest(),'category':key.split('/')[0],'display':record,'note':'Approved replacement Anipulse image' if key.endswith('approved-new-cover.png') else ''})
(out/'src/assets.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
(out/'asset-inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2))
(out/'public/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="15" fill="#f1dde0"/><text x="13" y="44" font-family="Arial,sans-serif" font-size="42" font-weight="bold" fill="#241c20">y.</text></svg>')
share=Image.new('RGB',(1200,630),'#faf7f2');d=ImageDraw.Draw(share)
d.rectangle((0,0,1200,10),fill='#7d243d');d.rectangle((65,390,740,432),fill='#f1dde0')
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
f=lambda size:ImageFont.truetype(font,size)
d.text((65,125),'Yoon Thiri',font=f(69),fill='#241c20');d.text((65,215),'Aung.',font=f(69),fill='#241c20');d.text((68,350),'AI ENGINEERING & SOFTWARE DEVELOPMENT',font=f(21),fill='#7d243d');d.text((68,460),'Computer vision · NLP · Data mining',font=f(24),fill='#6e5c62')
portrait=Image.open(source/'profile/portrait.jpg');portrait.thumbnail((310,465));share.paste(portrait,(840,80));share.save(out/'public/social-preview.jpg',quality=90)
print('Mapped',len(records),'image assets; optimized media MB:',round(sum(p.stat().st_size for p in media.iterdir())/1024**2,1))
