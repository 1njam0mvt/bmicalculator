# BMI Calculator website: setup guide

A complete static website. No build step, no database, no installs. Total **33 files**.

## Set up in 5 steps
1. **Unzip** this folder.
2. **Set your domain** (needed for SEO tags). In a terminal inside the folder run:
   `python3 set-domain.py yourdomain.com`
   (No Python? Open each `.html`, `sitemap.xml`, `robots.txt`, `llms.txt` and `docs/SEO-PACK.md` and replace `https://example.com` with your domain.)
3. **Upload everything** to the **root** of your host (Netlify, Vercel, Cloudflare Pages, GitHub Pages with a custom domain, or `public_html` on cPanel). Keep the folder structure exactly as listed below. Icons use root paths like `/favicon.ico`, so the site must live at the domain root.
4. **Check it**: open `https://yourdomain.com/`, switch language, open `/es/`, `/ar/`, and `https://yourdomain.com/robots.txt` and `/sitemap.xml`.
5. **Tell search engines**: add the site in Google Search Console and Bing Webmaster Tools and submit `https://yourdomain.com/sitemap.xml`. Test a page in Google's Rich Results Test.

## Folder structure
```
/                      index.html (English), sitemap.xml, robots.txt, llms.txt, og-bmi.png, icons, manifest
/es /zh /hi /ar /pt /fr /de    one index.html each
/source                your original logo
/docs                  SEO-PACK.md
```

## File list (33 files)
| # | File | What it is |
|---|---|---|
| 1 | `index.html` | English home page (also the x-default). Contains the BMI calculator plus all 200+ calculator pages |
| 2 | `ar/index.html` | Arabic version (right-to-left) |
| 3 | `de/index.html` | German version |
| 4 | `es/index.html` | Spanish version |
| 5 | `fr/index.html` | French version |
| 6 | `hi/index.html` | Hindi version |
| 7 | `pt/index.html` | Portuguese version |
| 8 | `zh/index.html` | Chinese version |
| 9 | `llms.txt` | Summary of the site for AI assistants |
| 10 | `og-bmi.png` | Social share image (1200x630), used by og:image |
| 11 | `robots.txt` | Allows search and AI crawlers, points to the sitemap |
| 12 | `site.webmanifest` | Web app manifest (name, icons, theme colour) |
| 13 | `sitemap.xml` | Sitemap with hreflang for all 8 languages (submit to Google and Bing) |
| 14 | `apple-touch-icon.png` | iPhone/iPad home-screen icon (180 px) |
| 15 | `favicon-16x16.png` | Favicon 16 px |
| 16 | `favicon-32x32.png` | Favicon 32 px |
| 17 | `favicon-96x96.png` | Favicon 96 px |
| 18 | `favicon-dark-16x16.png` | Favicon for dark browser themes, 16 px |
| 19 | `favicon-dark-32x32.png` | Favicon for dark browser themes, 32 px |
| 20 | `favicon-dark-96x96.png` | Favicon for dark browser themes, 96 px |
| 21 | `favicon-light-16x16.png` | Favicon for light browser themes, 16 px |
| 22 | `favicon-light-32x32.png` | Favicon for light browser themes, 32 px |
| 23 | `favicon-light-96x96.png` | Favicon for light browser themes, 96 px |
| 24 | `favicon.ico` | Favicon, multi-size (16/32/48/64) |
| 25 | `favicon.svg` | Vector favicon, switches for light and dark browsers |
| 26 | `logo.png` | Cropped logo, 512 px, transparent corners |
| 27 | `logo.svg` | Cropped logo, vector |
| 28 | `source/BMI_logo.webp` | Your original logo file (kept for reference) |
| 29 | `docs/SEO-PACK.md` | Keyword map and per-language tags |
| 30 | `set-domain.py` | One-command script: puts your real domain into all files |
| 31 | `web-app-manifest-192x192.png` | Android/PWA icon 192 px |
| 32 | `web-app-manifest-512x512.png` | Android/PWA icon 512 px |
| 33 | `README-SETUP.md` | This guide |

## Good to know
- Every language page contains the full app: the BMI calculator plus the other calculators, which open through `#` links inside the page.
- The other calculators are not separate pages for Google yet. Real URLs per calculator are the next SEO step.
- Opening files by double-click works, but the icons only show once the site is online at the domain root.
- Medical text should be reviewed by a health professional before launch.
