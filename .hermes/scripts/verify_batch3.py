import json, os, re

tools = json.load(open('tools/tools.json'))
targets = ['adcreative-ai','ai-business-skills','ai-marketing-claude','albert-ai','alwrity',
           'analytics-tracking-automation','anyword','bloomreach','brandwatch','buffer',
           'chatbotx','chatfuel','clerk-io','codex-seo','contentbot','copy-ai','django-crm',
           'dynamic-yield','email-marketing-bible','freshsales','google-meta-ads-ga4-mcp',
           'growth-lab','heap','hootsuite','hypotenuse-ai','jasper','krayin-crm',
           'line-harness','langchain','laudspeaker']

issues = []
checked = []
for s in targets:
    f = f'tools/{s}/index.html'
    if not os.path.exists(f):
        issues.append((s, 'no page generated'))
        continue
    html = open(f).read()
    n_hands = html.count('Hands-on notes')
    n_verdict = html.count('>Verdict<')
    checked.append((s, n_hands, n_verdict))
    if n_hands != 1:
        issues.append((s, f'hands-on sections={n_hands}'))
    if n_verdict != 1:
        issues.append((s, f'verdict sections={n_verdict}'))

print('Sample pages (slug, hands_on, verdict):')
for row in checked[:6]:
    print(' ', row)
print('All 30 target pages present with both sections:', 'YES' if not issues else 'NO')
print('Issues:', issues if issues else 'NONE')

# em dash / AI vocab sweep across the whole tools.json deep_dive corpus (batch + existing)
bad = []
for t in tools:
    for k, v in (t.get('deep_dive') or {}).items():
        paras = v if isinstance(v, list) else [v]
        for para in paras:
            if not isinstance(para, str):
                continue
            if '\u2014' in para:
                bad.append((t['slug'], k, 'em dash'))
            for w in ['actually','additionally','crucial','delve','leverage','utilize','seamless',
                      'robust','game-changing','revolutionary','landscape','testament',
                      'underscore','intricate','foster','elevate']:
                if w in para.lower():
                    bad.append((t['slug'], k, w))
print('humanizer (full corpus):', bad if bad else 'CLEAN')
print('total tools with deep_dive:', sum(1 for t in tools if t.get('deep_dive')))