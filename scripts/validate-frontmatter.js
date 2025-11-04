const fs = require('fs'); const path = require('path'); const matter = require('gray-matter');
const required = ["id","title","slug","summary","tags","last_updated"];
function walk(dir){return fs.readdirSync(dir).flatMap(f=>{const p=path.join(dir,f);return fs.statSync(p).isDirectory()?walk(p):[p];});}
const md = walk(".").filter(p=>p.endsWith(".md") && !p.includes("node_modules") && !p.includes("_site"));
let ok = true;
for (const file of md) {
  const fm = matter.read(file).data || {};
  if (file.startsWith("_threats/")) {
    const missing = required.filter(k => !(k in fm));
    if (missing.length) { ok=false; console.log(`MISSING in ${file}: ${missing.join(",")}`); }
    if (fm.slug && !/^[a-z0-9-]+$/.test(fm.slug)) { ok=false; console.log(`BAD SLUG in ${file}: ${fm.slug}`); }
  }
}
if (!ok) process.exit(3);
console.log("FRONTMATTER_OK");
