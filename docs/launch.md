# Launch status

25 October 2026:

- Private repository created: https://github.com/arpit-sidana/girish-sidana
- GitHub Pages blocked by current account plan; keep source private.
- Domain girishsidana.com available at Hostinger; no purchase yet. Prepared
  one-year registration: $9.99 + $0.20 ICANN fee = $10.19 before any final tax
  adjustment. Renewal displayed at $19.99/year. Free privacy included; no paid
  hosting, email, or Domain Shield selected.

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
