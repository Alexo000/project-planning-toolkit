"""Run from the repo root: python3 src/build_site.py. Builds site/index.html from template.html + ops.json: a full HTML document for GitHub Pages."""
t = open('src/template.html', encoding='utf-8').read()
ops = open('src/ops.json', encoding='utf-8').read().replace('</', '<\\/')
page = t.replace('/*OPS*/[]', ops)
cut = page.rfind('</style>') + len('</style>')
head, body = page[:cut], page[cut:]
doc = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Take a project of your own from a hunch to something made: spin for a way in, write a brief, get research methods, try things out, plan, and look back.">
<meta name="author" content="Alejandro Ramos Saavedra">
<link rel="canonical" href="https://toolkit.ramos-saavedra.com/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Alejandro Ramos Saavedra">
<meta property="og:title" content="Project Planning Toolkit: from a hunch to something made">
<meta property="og:description" content="Take a project of your own from a hunch to something made: spin for a way in, write a brief, get research methods, try things out, plan, and look back.">
<meta property="og:url" content="https://toolkit.ramos-saavedra.com/">
<meta property="og:image" content="https://toolkit.ramos-saavedra.com/share.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The toolkit's eight steps as pictograms, from Discover to Principles">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
{head}
<style>body{{margin:0}}[hidden]{{display:none!important}}</style>
</head>
<body>{body}
</body>
</html>
'''
open('site/index.html', 'w', encoding='utf-8').write(doc)
open('site/CNAME', 'w').write('toolkit.ramos-saavedra.com\n')
open('site/.nojekyll', 'w').write('')
open('site/robots.txt', 'w').write('User-agent: *\nAllow: /\nSitemap: https://toolkit.ramos-saavedra.com/sitemap.xml\n')
open('site/sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>https://toolkit.ramos-saavedra.com/</loc></url>\n</urlset>\n')
print(len(doc))
