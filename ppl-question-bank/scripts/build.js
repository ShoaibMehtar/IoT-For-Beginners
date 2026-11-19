// Wraps app.html (the page body used for the hosted preview) into a standalone index.html.
const fs = require("fs");
const path = require("path");
const root = path.join(__dirname, "..");
const body = fs.readFileSync(path.join(root, "app.html"), "utf8");
const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>\n${body}\n</body></html>\n`;
fs.writeFileSync(path.join(root, "index.html"), html);
console.log("Wrote index.html");
