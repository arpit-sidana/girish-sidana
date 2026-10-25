# girish-sidana

Girish Sidana’s personal website: a life in business, education, mentoring,
and writing. Public source repository owned by `arpit-sidana`.

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
Expected project URL once enabled: `https://arpit-sidana.github.io/girish-sidana/`.

## Domain

`girishsidana.com` was available at Hostinger on 25 October 2026 and returned
HTTP 404 from the Verisign .com RDAP lookup. Availability is not a reservation.
No CNAME is committed until purchase and domain ownership are verified.
See `docs/launch.md` for DNS and launch steps.
