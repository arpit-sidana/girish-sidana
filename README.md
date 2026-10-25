# girish-sidana

Girish Sidana’s personal website: a life in business, education, mentoring,
and writing. Public source repository owned by `arpit-sidana`.

Live website: https://girishsidana.com/

## Structure

Plain HTML, shared CSS, local fonts, and a small feature configuration script,
matching the architecture of [arpitsidana.com](https://arpitsidana.com).
The original stylesheet is preserved byte-for-byte.

- `index.html`: legacy-focused biography
- `work.html`: life and work chapters, with optional milestone chronology
- `writes.html`: book and its origin
- `education.html`: vocational education and youth employability
- `mentoring.html`: sharing experience and connecting on LinkedIn
- `data/profile.json`: reviewed biography, milestones, education, and book facts
- `docs/profile-research.md`: sources, editorial choices, and uncertainties

## Edit and verify

```sh
python3 scripts/profile_sync.py --write
python3 scripts/site_styles.py --write
python3 scripts/build_site.py
python3 -m http.server 4173 --directory dist
```

No package install or framework build is required. Only `dist/` is deployed.

## GitHub Pages

The repository is public at Arpit’s request so it can use free GitHub Pages.
Select **GitHub Actions** as the Pages source. **Deploy GitHub Pages** runs on
pushes to `main` and can also be started manually from Actions.

The deployment workflow and a separate automatic validation workflow are included.
Project URL: `https://arpit-sidana.github.io/girish-sidana/`.

## Domain

`girishsidana.com` was registered through Cloudflare on 25 October 2026.
GitHub Pages is configured with this custom domain. Cloudflare DNS routes the
apex domain and `www` to GitHub Pages; hosting remains free.
Canonical URLs and the sitemap use the custom domain. No CNAME file is required
for the GitHub Actions deployment. See `docs/launch.md` for DNS and launch details.
