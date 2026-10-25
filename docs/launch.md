# Launch status

25 October 2026:

- Repository: https://github.com/arpit-sidana/girish-sidana
- Arpit requested public source and free GitHub Pages on 25 October 2026.
  GitHub Pro is not required for this public repository.
- Public visibility confirmed and Pages enabled using GitHub Actions.
- Production deployed successfully:
  https://arpit-sidana.github.io/girish-sidana/
  Deployment run: https://github.com/arpit-sidana/girish-sidana/actions/runs/40220047224
- Domain girishsidana.com registered through Cloudflare; purchase confirmed
  in Cloudflare’s dashboard on 25 October 2026.
- Pages custom domain saved as girishsidana.com. Ownership verified under the
  arpit-sidana GitHub account using its DNS TXT challenge.
- Cloudflare DNS uses four DNS-only apex A records: 185.199.108.153,
  185.199.109.153, 185.199.110.153, and 185.199.111.153.
- www is a DNS-only CNAME to arpit-sidana.github.io.
- Public DNS resolves correctly and the domain serves Girish’s home page.
  GitHub is issuing the HTTPS certificate; final HTTPS verification is pending.
- Canonical URLs, Open Graph URLs, robots.txt, and sitemap.xml use the custom domain.

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
- Initial production deployment succeeded.

## Domain maintenance

Manage registration and DNS in Cloudflare. Hosting and deployment remain on
GitHub Pages. Keep the GitHub domain verification TXT record in DNS.

The included GitHub Actions workflow uses the custom domain configured in
Pages settings. A CNAME file is neither required nor used for Actions deployments.
The apex domain is the canonical address; GitHub redirects www to it once TLS
is ready. Changes pushed to main automatically rebuild and deploy the site.

Reference: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
