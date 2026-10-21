# Open in VS Code

1. Extract `yoon-portfolio-v2-source.zip`.
2. Open the extracted `yoon-portfolio-v2` folder in VS Code.
3. Install Node.js 22 LTS or newer if needed.
4. Open Terminal → New Terminal and run:

```bash
npm ci
npm run dev
```

Open http://localhost:4173 in your browser. Stop the server with Ctrl+C.

## Build and check

```bash
npm run build
npm run verify
npm run preview
```

## Upload to Netlify

**Ready-made build:** Extract `yoon-portfolio-v2-netlify.zip`, then drag the extracted `dist` folder into Netlify’s manual deployment area. No local build is needed.

**After making changes:** Run `npm run build` and upload the newly generated `dist` folder.

**Git deployment:** Push this source folder to GitHub and import it into Netlify. Build command: `npm run build`. Publish directory: `dist`. The included `netlify.toml` configures routing.

## Change text or photos

Edit `src/content.ts` for skills, collection entries, experience, awards, activities, certificates, and contact information. Edit `src/App.tsx` for the hero, navigation, footer, and components. Edit `src/styles.css` for appearance and animation. Use `src/assets.json` for photo mappings. See README.md for detailed photo instructions.

The source ZIP includes the optimized photos required to run the website. Keep your original photo ZIP separately.
