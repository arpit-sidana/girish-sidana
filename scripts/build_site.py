#!/usr/bin/env python3
"""Check source consistency and export only public website assets for Pages."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
for script in ['profile_sync.py', 'site_styles.py', 'check_site.py']:
    subprocess.run([sys.executable, str(ROOT / 'scripts' / script)], check=True)
out = ROOT / 'dist'
if out.exists():
    shutil.rmtree(out)
out.mkdir()
for name in ['index.html', 'work.html', 'writes.html', 'education.html', 'mentoring.html',
             'site-config.js', 'robots.txt', 'sitemap.xml', '.nojekyll']:
    shutil.copy2(ROOT / name, out / name)
for path in ROOT.glob('styles-*.css'):
    shutil.copy2(path, out / path.name)
shutil.copytree(ROOT / 'assets', out / 'assets')
print('Built dist/ with public assets only.')
