# Launch status

25 October 2026:

- Private repository created: https://github.com/arpit-sidana/girish-sidana
- GitHub Pages blocked by current account plan; keep source private. The
  GitHub upgrade screen offers Pro at $4/month ($48/year if paid annually).
  Upgrade is pending explicit spending approval and billing information.
- Domain girishsidana.com available at Hostinger; no purchase yet. Prepared
  one-year registration: $9.99 + $0.20 ICANN fee = $10.19 before any final tax
  adjustment. Renewal displayed at $19.99/year. Free privacy included; no paid
  hosting, email, or Domain Shield selected.
- Hostinger login is required. Automated Google sign-in was rejected by
  approval review because the specific Google account and sign-in method
  were not explicitly authorized. Do not retry without user authorization.

## Verification completed

- Original CSS matches the live Arpit site SHA-256 byte-for-byte.
- Profile generation, stylesheet fingerprint, local links/assets/headings,
  and public-only static build passed locally.
- GitHub validation succeeded for commit c8fd247:
  https://github.com/arpit-sidana/girish-sidana/actions/runs/40214391178
- Browser checked home, Journey, Writing, Education, and Mentoring.
- Desktop, 375px mobile, and 768px tablet reviewed. The tablet shell is 720px,
  consistent with Arpit’s shared shell rule; no horizontal overflow observed.
- Milestone disclosure opens and shows the 11 source-backed roles.
- Domain registration and production deployment remain pending, not complete.

## After domain registration and Pages activation

1. In GitHub Pages settings choose GitHub Actions and run the deployment workflow.
2. Confirm the site loads at https://arpit-sidana.github.io/girish-sidana/.
3. Add girishsidana.com as the Pages custom domain, and verify domain ownership
   through GitHub’s displayed TXT record before pointing DNS at GitHub.
4. Use the current GitHub Pages DNS values. The documented apex A records at
   preparation time are 185.199.108.153, 185.199.109.153, 185.199.110.153,
   and 185.199.111.153. Reverify against GitHub’s official docs before writing DNS.
5. Point www to arpit-sidana.github.io, not a repository path.
6. With the included Actions workflow, configure the custom domain in Pages
   settings. A CNAME file is neither required nor used for Actions deployments.
7. Wait for DNS validation and TLS issuance, then enable Enforce HTTPS.
8. Add the final canonical URLs and sitemap after the working domain is confirmed.

Reference: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
