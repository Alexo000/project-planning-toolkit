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
<meta name="robots" content="noindex, nofollow">
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
open('site/robots.txt', 'w').write('User-agent: *\nDisallow: /\n')
print(len(doc))
