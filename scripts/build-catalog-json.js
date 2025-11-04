const fs=require('fs'); const matter=require('gray-matter'); const path=require('path');
function walk(dir){return fs.readdirSync(dir).map(f=>path.join(dir,f)).filter(p=>p.endsWith('.md'));}
const rows = walk('_threats').map(p=>{
  const fm = matter.read(p).data;
  return { id: fm.id, title: fm.title, slug: fm.slug, summary: fm.summary, tags: fm.tags, updated: fm.last_updated };
});
fs.mkdirSync('assets', {recursive:true});
fs.writeFileSync('assets/catalog.json', JSON.stringify(rows,null,2));
