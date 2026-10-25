# Girish Sidana website

Keep the source repository private. The website itself is intended for public access.

Preserve the shared HTML/CSS/static architecture and visual language of
arpitsidana.com. `styles.css`, its fingerprint helper, and the local font files
were reused from Arpit’s website. Do not introduce page-specific shell widths.

`data/profile.json` and `scripts/profile_sync.py` own public page content. Check
`docs/profile-research.md` before adding biographical claims. Never invent
awards, impact numbers, qualifications, testimonials, or investment performance.

After content changes run:

```sh
python3 scripts/profile_sync.py --write
python3 scripts/site_styles.py --write
python3 scripts/build_site.py
```

Keep internal research and source files outside the public `dist/` export.
Do not add a CNAME until the domain is registered and verified under Arpit’s control.
