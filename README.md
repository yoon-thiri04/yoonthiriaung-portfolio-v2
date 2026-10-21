# Yoon Thiri Aung — Portfolio V2

A complete responsive portfolio built with React, TypeScript and Vite. The approved Rosewood & Ivory direction uses Space Grotesk headings, Manrope body text, Noto Sans Myanmar support, ivory surfaces, wine-red accents, blush, and champagne tones.

## Run locally

Requires Node.js 22 or newer and npm. From this folder:

```bash
npm ci
npm run dev
```

Open the local URL printed by Vite (port 4173). Do not open `index.html` directly: this is the complete React application, unlike the earlier single-file design previews.

```bash
npm run build
npm run verify
npm run preview
```

`dist/` is the production output. TypeScript checking runs as part of the production build. `verify` checks the required collection order, every displayed asset reference, story outputs, skill logos, and future/past conference safeguards.

## Deploy to Netlify

### From GitHub

1. Create your GitHub repository and push the contents of this source folder (excluding `node_modules/` and `dist/`, already ignored).
2. In Netlify, choose **Add new project → Import an existing project**, and select the repository.
3. Build command: `npm run build`. Publish directory: `dist`. Use Node 22 or newer.
4. `netlify.toml` supplies the build and route settings. Activity URLs work when loaded or refreshed directly.
5. Set the social-image origin in `index.html` to the final public Netlify URL, then redeploy. You can replace both existing absolute social-image URLs with `https://YOUR-NETLIFY-HOST/social-preview.jpg`.

### Manual deployment

Build locally, then drag the **contents of `dist/`** (or the supplied Netlify-ready archive after extracting it) into Netlify's manual deployment area. Do not upload the source folder as a static site.

The `.openai/hosting.json` file belongs to the separately hosted private review site. Netlify ignores it. It contains no secrets.

## Update content

All editable text and records are in `src/content.ts`:

- `profile`: email, social links, portrait and avatar references.
- `builds`: seven entries in their required order, screenshots, links, technology tags, recognition, credits, and course context.
- `experience`: titles, employers, dates and only verified duties.
- `skillGroups`: text labels and local Devicon logo identifiers.
- `awards`: title, institution, ISO date, and one or more photos.
- `activities`: actual dates, covers, contribution notes, official references, and optional story content.
- `credentials`: exact titles, issuers, dates, thumbnails and associated photos. The mathematics certificate stays last by explicit request.

The homepage uses **Things I’ve Built**, **Collection** and **Explore the collection** instead of “Selected work” or “Projects.”

The Anipulse image is the newly supplied **Anime Analytics Across Devices-1.png**, mapped to `projects/01-anipulse/approved-new-cover.png`. The two earlier Anipulse images remain inventoried but are not displayed.

### Add a photo without regenerating everything

1. Put an optimized display image and a readable full-size copy in `public/media/` with unique names.
2. Add its record to `src/assets.json`, matching the structure of an existing entry (`src`, `srcSet`, `full`, `width`, `height`). Paths begin with `/media/`.
3. Reference that asset key from `src/content.ts`. Supply specific alt text, and a caption only when factual.
4. Run the build and checks.

### Regenerate the supplied image derivatives

Original uploads remain unmodified. The inventory maps all 65 source images to their output paths and SHA-256 hashes. Display derivatives have 640px and 1280px variants; full viewing preserves original certificate/paper files and uses large, high-quality photos. Galleries load images lazily, and only the active collection image is mounted.

To regenerate, install Python and Pillow, extract your original ZIP, and run:

```bash
python -m pip install Pillow
python scripts/prepare_assets.py --source-assets /path/to/portfolio-v2/assests --anipulse-cover /path/to/Anime-Analytics-Across-Devices-1.png
```

The original ZIP folder is spelled `assests`; that is intentional in this command. The script does not overwrite originals. Keep your original uploads as the source archive; the runnable package includes the optimized media needed by the site.

### Add an activity story

Add a `story` object to an activity in `src/content.ts`, and add its slug/title to `scripts/static-routes.mjs`. Only EBA Minamata, Venture Base, and Code2Career currently have story pages. Falcon has one image and no empty story page. Academic awards have inline sliders and lightboxes, not detail pages.

## Interaction and accessibility

- Collection arrows directly below the image, a visible current title and count, scoped Left/Right keyboard keys, and horizontal touch swipes. No autoplay. Vertical scrolling remains native.
- Fourth-year award has a two-photo inline slider.
- Native modal lightboxes with Escape, close controls, gallery arrows, keyboard navigation, and fit/100% size viewing for readable certificates and academic results.
- Fine-pointer cursor shows scroll progress/direction and contextual actions. Normal text-entry cursors remain available. Touch devices and reduced-motion preferences disable cursor effects.
- Staggered blur-to-focus scroll reveals, deliberate slide transitions, intro animation, restrained click feedback, and subtle portrait motion. Skills use translucent panels with scroll-reactive rose/champagne glows. Reduced motion makes the content immediately visible.
- Semantic landmarks, visible keyboard focus, image alt text, responsive image dimensions, and a working mobile menu.

## Content decisions and remaining checks

See `CONTENT_NOTES.md` for fact sources, the unavailable Udacity certificate image, and the supplied live-demo URL that could not be independently reached during checks.

The Download CV control has been removed at your request.
