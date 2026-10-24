# Yoon Thiri Aung — Portfolio V2

A complete responsive portfolio built with React, TypeScript and Vite. 

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

## Update content

All editable text and records are in `src/content.ts`:

- `profile`: email, social links, portrait and avatar references.
- `builds`: seven entries in their required order, screenshots, links, technology tags, recognition, credits, and course context.
- `experience`: titles, employers, dates and only verified duties.
- `skillGroups`: text labels and local Devicon logo identifiers.
- `awards`: title, institution, ISO date, and one or more photos.
- `activities`: actual dates, covers, contribution notes, official references, and optional story content.
- `credentials`: exact titles, issuers, dates, thumbnails and associated photos. The mathematics certificate stays last by explicit request.

## Interaction and accessibility

- Collection arrows directly below the image, a visible current title and count, scoped Left/Right keyboard keys, and horizontal touch swipes. No autoplay. Vertical scrolling remains native.
- Fourth-year award has a two-photo inline slider.
- Native modal lightboxes with Escape, close controls, gallery arrows, keyboard navigation, and fit/100% size viewing for readable certificates and academic results.
- Fine-pointer cursor shows scroll progress/direction and contextual actions. Normal text-entry cursors remain available. Touch devices and reduced-motion preferences disable cursor effects.
- Staggered blur-to-focus scroll reveals, deliberate slide transitions, intro animation, restrained click feedback, and subtle portrait motion. Skills use translucent panels with scroll-reactive rose/champagne glows. Reduced motion makes the content immediately visible.
- Semantic landmarks, visible keyboard focus, image alt text, responsive image dimensions, and a working mobile menu.

