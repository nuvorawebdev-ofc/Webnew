# Nuvora.webdev — Implementation Plan

## Scope

Build a complete, inspectable, deployable static website for Nuvora.webdev using vanilla HTML, CSS, and JavaScript. The build will cover the homepage, portfolio, privacy policy, thank-you, English equivalents, custom 404, SEO files, local assets, bilingual switching, contextual WhatsApp CTAs, responsive navigation, accessibility, and documentation.

The final brief supplies the approved package names, prices, features, Extras, process, payment terms, FAQ requirements, and three official demo portfolio URLs. Those details are centralized in `assets/js/translations.js` and `assets/js/content.js`; screenshots captured from the verified demo URLs are stored locally under `assets/images/portfolio/`.

## Technical approach

- Use semantic static HTML pages with shared stylesheet and JavaScript modules.
- Use `assets/js/translations.js` as the single content dictionary and `assets/js/main.js` for page hydration, language persistence, navigation, FAQ, portfolio filters, and contextual WhatsApp links.
- Use data-driven services, pricing, extras, and portfolio modules in `assets/js/content.js`.
- Use deep relative paths so nested language and policy routes work on a static host.
- Use a CSS-first visual system: dark near-black surfaces, warm white text, deep purple glass accents, restrained neon lime indicators, rounded cards, and a cinematic local Pexels image for the hero.
- Keep the brand logo supplied by the user at `assets/images/nuvora-logo.png`; do not recreate it.
- Use no backend, no fake form submission, and no unnecessary dependency. Contact CTAs open WhatsApp, email, or Instagram directly.

## Design direction

Three possible styles considered:

1. **Midnight Signal / editorial glass** — 0.06 probability.
2. **Quiet Brutalism / monochrome utility** — 0.04 probability.
3. **Luminous Systems / cinematic interface** — 0.05 probability.

**Chosen movement:** Luminous Systems: a restrained, high-contrast digital atelier that treats every section as a focused surface in a larger system.

**Core principles:** clarity before decoration; dark space creates premium contrast; accents are signals, not wallpaper; every interaction should reduce uncertainty.

**Color philosophy:** #121212 carries the calm and confidence of a reliable foundation. #FAFAFA makes information feel precise and open. #811E60 introduces a distinctive premium atmosphere in glass and light. #D0FF00 is reserved for moments that need attention, such as availability, checkmarks, and selected CTAs.

**Layout paradigm:** a vertical sequence of offset editorial bands rather than a generic centered agency grid. Hero uses one centered glass panel, while lower sections alternate wide text rails, split feature bands, and modular card clusters.

**Signature elements:** a thin lime signal line used as a section marker; purple light pockets behind glass surfaces; compact metadata labels that make each interaction feel intentional.

**Interaction philosophy:** menus, filters, accordions, and language changes should be immediate and reversible. Hover states lift or brighten only enough to show affordance. Motion stops when the user requests reduced motion.

**Animation:** use short fades, 180–360ms scale/translate transitions, restrained reveal-on-scroll, and a slow hero background drift. No looping decorative motion should compete with reading.

**Typography system:** use `Inter` for UI/body and `Space Grotesk` for display headings through a single Google Fonts CSS import with system fallbacks. Headings are tight and confident; labels use uppercase tracking; body copy stays relaxed and readable.

**Brand essence:** Nuvora helps growing businesses turn digital presence into a clearer, more credible next step. Personality: assured, thoughtful, precise.

**Brand voice:** direct, warm, and never inflated. Example lines: “Buat kesan pertama yang bekerja lebih keras.” and “Kita mulai dari kebutuhan nyata, lalu merancang hal yang benar-benar berguna.”

**Wordmark & logo:** use the supplied official Nuvora wordmark in the floating navbar. The supplied mark is retained as a local optional asset for future favicon/app-icon use but is not redrawn.

**Signature brand color:** deep purple `#811E60`, used as the ownable atmosphere behind otherwise monochrome surfaces.

## Project structure

- `index.html`, `portfolio/index.html`, `privacy-policy/index.html`, `thank-you/index.html`, `404.html`
- `en/` equivalents for all public content pages
- `assets/css/style.css`, `responsive.css`, `animations.css`
- `assets/js/content.js`, `translations.js`, `language.js`, `navigation.js`, `portfolio.js`, `interactions.js`, `main.js`
- `assets/images/nuvora-logo.png`, `nuvora-mark.png`, `hero-background.jpg`, `portfolio/*.webp`
- `manus-routes.json`, `robots.txt`, `sitemap.xml`, `manifest.webmanifest`, `README.md`

## Delivery

Serve the static project on port 3000, run local code and link audits, commit to `main`, and leave the project ready for Preview and deployment. No public deployment will be claimed unless publication is explicitly confirmed by the platform.
