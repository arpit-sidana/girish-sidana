#!/usr/bin/env python3
"""Render the public pages from the reviewed profile. No third-party dependencies."""
import argparse
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = json.loads((ROOT / 'data/profile.json').read_text())
SITE_URL = 'https://girishsidana.com'
SECTIONS = [('work.html', 'Journey'), ('writes.html', 'Writing'),
            ('education.html', 'Education'), ('mentoring.html', 'Mentoring')]


def link(url, label):
    return f'<a href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(label)}</a>'


def entries(items, label):
    rows = []
    for i, (title, description) in enumerate(items, 1):
        rows.append(f'''      <article class="writing-entry">
        <p class="writing-number">{i:02}</p>
        <h2>{title}</h2>
        <p>{escape(description)}</p>
      </article>''')
    return f'<section class="writing-list" aria-label="{label}">\n' + '\n'.join(rows) + '\n    </section>'


def page(filename, title, description, body, home=False):
    canonical = SITE_URL + ('/' if filename == 'index.html' else '/' + filename)
    nav_items = []
    for path, label in SECTIONS:
        selected = ' class="is-active" aria-current="page"' if path == filename else ''
        nav_items.append(f'        <a{selected} href="{path}">{label}</a>')
    nav = '\n'.join(nav_items)
    active = ' class="site-brand is-active" aria-current="page"' if filename == 'index.html' else ' class="site-brand"'
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <link rel="canonical" href="{canonical}">
  <title>{escape(title)}</title>
  <link rel="icon" type="image/svg+xml" href="assets/icons/favicon.svg">
  <link rel="stylesheet" href="styles.css">
  <script src="site-config.js" defer></script>
</head>
<body>
  <main class="site-shell{' home' if home else ' writing-shell'}">
    <header class="site-header">
      <a{active} href="index.html">Girish Sidana</a>
      <nav class="site-nav" aria-label="Website sections">
{nav}
      </nav>
    </header>
    {body}
    <footer class="site-credit{'' if home else ' site-credit--subpage'}">
      <span>© 2026 Girish Sidana</span>
    </footer>
  </main>
</body>
</html>
'''


def render():
    p = PROFILE
    bio = '\n'.join(f'        <p>{escape(text)}</p>' for text in p['bio'])
    home = f'''<section class="home-intro" aria-label="About Girish Sidana">
      <h1 class="sr-only">Girish Sidana</h1>
      <div class="bio">
{bio}
        <div class="home-social-links" aria-label="Contact and social profiles">
          <a class="social-icon-link" href="{p['linkedin']}" target="_blank" rel="me noopener noreferrer" aria-label="Girish Sidana on LinkedIn" title="LinkedIn"><img src="assets/icons/social/linkedin.svg" alt=""></a>
        </div>
      </div>
    </section>'''
    journey = '<h1>A life in chapters</h1>\n    <p class="writing-intro">From engineering and business leadership to education, financial understanding, and helping others move forward.</p>\n    '
    journey += entries([(escape(c['title']), c['text']) for c in p['chapters']], 'Life and work')
    journey += '\n    <details class="resume-section"><summary>Milestones along the way</summary>\n      <dl>\n'
    journey += '\n'.join(f'        <dt>{escape(date)}</dt><dd>{escape(role)}</dd>' for date, role in p['timeline'])
    journey += '\n      </dl>\n    </details>'
    book = p['book']
    writing = f'''<h1>Writing</h1>
    <p class="writing-intro">On the human side of financial decisions, and the lessons that experience leaves us.</p>
    <section class="bio" aria-labelledby="book-title">
      <p class="eyebrow">Book · {book['published']}</p>
      <h2 id="book-title">{escape(book['title'])}</h2>
      <p>The market collapse of 2008 prompted me to look more closely at investing. I had avoided the worst largely because I had invested little. Recognising the role of luck set me on a long journey to understand the decisions behind financial outcomes.</p>
      <p>This book explores how emotional blind spots and mental shortcuts influence investors, and offers a practical framework for more thoughtful decisions. It brings together behavioural finance, psychology, and lessons from market thinkers.</p>
      <p>{link(book['url'], 'Find the book on Amazon India ↗')}</p>
      <p>{link(book['origin_post'], 'Read the story behind the book ↗')}</p>
    </section>'''
    education = '<h1>Education &amp; opportunity</h1>\n    <p class="writing-intro">Practical skills can open a path to employment, independence, and dignity. This is the focus of my work in vocational education.</p>\n    '
    education += entries([
        (link('https://www.linkedin.com/company/109613232/', 'Asha Education Trust ↗'), 'As a trustee since August 2024, I contribute to the trust’s strategic direction and growth. The work centres on healthcare and other vocational programmes, industry-relevant training, employer engagement, CSR partnerships, and career development.'),
        ('Healthcare and vocational learning', 'My involvement includes serving as Director of Vivo Healthcare Institute, Sector 14, Gurgaon, from 2018 to 2020, followed by work with Lalji Mehrotra Technical Institute in Gurugram from 2020 to March 2026.'),
        ('Skills, confidence, and self-reliance', 'Counselling and mentoring sit alongside formal learning. My interest is in helping individuals develop both the practical skills and the confidence to take their next step.')
    ], 'Education and youth empowerment')
    education += '\n    <section class="bio" aria-labelledby="foundations"><h2 id="foundations">My own foundations</h2>\n'
    education += '\n'.join(f'      <p>{escape(school)}<br>{escape(degree)} · {escape(date)}</p>' for date, school, degree in p['education'])
    education += '\n    </section>'
    mentoring = f'''<section class="mentoring-section" aria-labelledby="mentoring-heading">
      <h1 id="mentoring-heading">Mentoring</h1>
      <p>I’m interested in helping people build the skills, confidence, and judgement to find their own way. My mentoring draws on experience across business leadership, entrepreneurship, education, and personal finance.</p>
      <p>That can mean talking through a business challenge, a young person’s path from training to work, or the habits behind financial decisions. The aim is to make the next step clearer and help people become more self-reliant.</p>
      <p>{link(p['linkedin'], 'Connect with me on LinkedIn ↗')}</p>
    </section>'''
    pages = {
        'index.html': page('index.html', 'Girish Sidana', 'Girish Sidana — business leader, author, mentor, and trustee. A journey through business, education, and financial understanding.', home, True),
        'work.html': page('work.html', 'Journey — Girish Sidana', 'Chapters from Girish Sidana’s life in technology, business leadership, entrepreneurship, and education.', journey),
        'writes.html': page('writes.html', 'Writing — Girish Sidana', 'Behavioural Finance for Everyday Investors, a book by Girish Sidana on the psychology behind financial decisions.', writing),
        'education.html': page('education.html', 'Education — Girish Sidana', 'Girish Sidana’s involvement in youth employability, vocational education, and Asha Education Trust.', education),
        'mentoring.html': page('mentoring.html', 'Mentoring — Girish Sidana', 'Girish Sidana on sharing experience, building confidence, and helping people find their own path.', mentoring, True)
    }
    urls = [SITE_URL + ('/' if name == 'index.html' else '/' + name) for name in pages]
    pages['sitemap.xml'] = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(
        f'  <url><loc>{url}</loc></url>' for url in urls) + '\n</urlset>\n'
    return pages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    import re
    stale = []
    for name, expected in render().items():
        path = ROOT / name
        actual = path.read_text() if path.exists() else ''
        actual = re.sub(r'styles-[a-f0-9]+\.css', 'styles.css', actual)
        if actual != expected:
            if args.write:
                path.write_text(expected)
            else:
                stale.append(name)
    if stale:
        raise SystemExit('Stale profile pages: ' + ', '.join(stale))
    print('Profile pages match data/profile.json and the page templates.')


if __name__ == '__main__':
    main()
