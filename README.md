# ejukebox-tv

Source for **https://ejukebox.tv** - the eJukebox TV sister site.

**Jekyll on GitHub Pages**, built server-side by GitHub. No Actions, no local build step,
no Ruby needed on your machine - edit a file and push. The only plugin is
`jekyll-sitemap`, which is on the GitHub Pages whitelist and runs server-side.

```
_config.yml                site settings, contact details and THE VIDEO SLOT
_layouts/default.html      the one layout: head, the entire site CSS, shared JS
_includes/nav.html         top bar - brand, nav, live clock, ON AIR dot
_includes/footer.html      site footer
_includes/cta.html         the closer block every page ends on
_includes/video-stage.html ROLL THE TAPE - the video slot
_includes/pic.html         one photo - src="<file stem>", ratio, class, alt, eager, above, sizes, thumb
_data/pics.yml             pixel size of every image, so each <img> carries width/height
assets/img/                the images, .webp, ALL AI GENERATED - see MANIFEST.json for what each shows
assets/img/640/            640px copy of anything wider, served to phones through srcset
assets/img/thumb/          96px copy, for the 34px and 44px moderation-gate chips
assets/img/MANIFEST.json   what every image shows. Working material - excluded from the build
_tools/make-derivatives.py rebuilds assets/img/640 and assets/img/thumb - run after adding a photo
_includes/css-fx.html      page-scoped CSS for /functions/  (front matter: page_css)
_includes/css-dm.html      page-scoped CSS for /demo/       (front matter: page_css)
index.html                 the home page - the screen product
functions.html             /functions/ - functions and events (body_class: functions)
demo.html                  /demo/ - see it live, the honest FAQ, contact
404.html                   off-air page, links back to the three real pages
CNAME                      custom domain binding
.gitattributes             LF everywhere, so no editor produces a whole-file diff
```

## Putting the video in

Drop the file into `/assets/video/` and set it in `_config.yml`:

```yaml
video:
  url: "/assets/video/a-night-at-the-pub.mp4"
  poster: "/assets/video/poster.jpg"
  aspect: "16/9"     # use "9/16" for portrait phone footage from a function
  caption: "A Friday night, start to finish."
  badge: ""          # optional second caption. EMPTY ON PURPOSE - see below
  captions: ""       # path to a .vtt subtitles file, if there is one
```

Any container the browser can play works - the `<source>` carries no hard-coded MIME
type, so `.webm`, `.mov` and `.m4v` are fine as well as `.mp4`.

`badge` is deliberately empty. Nothing is claimed about where or how the footage was
shot unless you type that claim into `badge` yourself. Do not put "filmed in a real
venue" there until a venue shoot has actually happened.

Every video stage on the site fills at once. Nothing else changes and no page reflows -
the frame reserves its aspect in the placeholder state as well as the loaded one.

## The three pages

| Page | URL | Job |
|---|---|---|
| `index.html` | `/` | Sell the screen to a venue owner by demonstrating it - the marquee and its programme rail, the three-second timeline, the instant slide composer, the programme schedule, reliability, roadmap. |
| `functions.html` | `/functions/` | Win function bookings. The wall that fills, the run sheet, host mode, the arrivals slideshow, branding both ways, the revenue argument, the moderation gate. |
| `demo.html` | `/demo/` | Close. What a demo is, what we need, the FAQ (including an honest answer on cost with no figure), what happens after yes. |

`functions.html` sets `body_class: functions` in its front matter. That is the only thing
that switches `--accent` to the functions pink - never add a second stylesheet and never
put the pink in `:root`. Primary CTAs stay amber on every page by design.

Page-scoped CSS lives in its own include with a unique class prefix (`fx-`, `dm-`),
named in the page's front matter as `page_css: css-fx.html`. The layout pulls it into
`<head>` immediately after the site CSS, so the cascade order is unchanged and the
document stays valid - `<style>` is only conforming in `<head>`. It may only reach for
existing tokens; never define a new colour there.

## Motion

Everything that moves registers with one controller in `_layouts/default.html`, and the
`.playbtn` "Pause the demo" buttons drive all of it at once - the hero marquee, the slide
composer, the moderation gate, the wall reveals and the header clock. It is visible to
every visitor, not only under `prefers-reduced-motion`, because WCAG 2.2.2 requires a way
to stop auto-playing motion. `prefers-reduced-motion` is not a separate mode: it starts
the same control in the paused position and the button reads "Play the demo" instead.

Every frame on the site has to read correctly while paused. That is the design gate.

## How people reach us

Every route to us is the form in `_includes/contactform.html`, which posts to the Azure
Function. There is deliberately no email address and no phone number anywhere on either
site - not in the pages, not in the structured data, not in a `mailto:` fallback, and not
in this repo. Publishing either attracts scrapers and cold calls, which is the whole point
of the rule. The form fails visibly and offers a retry rather than falling back to a
`mailto:`, because a fallback would put an address in the page source.

If the form endpoint ever needs changing, change it in the include. Do not add a
`mailto:` or a `tel:` as a stopgap.

## House rules for anything added here

- Australian English - organise, recognise, licence (noun) / license (verb), colour.
- Spaced hyphens " - " only. Never em dashes or en dashes, in any file.
- Nothing unbuilt is claimed as shipping. Roadmap items carry the diamond marker and an
  adjacent "not shipping yet" line, and render cooler and lower contrast than live ones.
- No pricing and no hardware cost anywhere on the site. The call to action is "talk to us".
- **The images are AI generated.** The footer legal row carries a permanent site-wide line
  reading "Images illustrative - AI generated, not photographs of real customers", so the
  disclosure reaches every page including 404. On top of that, every page that shows a photo
  carries a small mono line saying "Illustrative - the photos on this site are AI generated,
  not photographs of real customers"; photos used at size carry a short "Illustrative - AI
  generated" caption; and any band that could read as real personal photographs - the
  arrivals slideshow, the crop trio, the moderation gate - carries its own local label.
  Never drop that disclosure, and never describe them as real customers or a real venue.
- No claim that the product is running in real venues, and no claim that footage was shot
  in one, until that is true.
- Colour is never the only carrier of meaning - the roadmap tags carry a visually hidden
  "Coming soon, not shipping yet:" as well as the diamond.

Before pushing, grep every file for em dashes, en dashes and dollar signs.

The main eJukebox site is a separate repo (`MusicbotAU/ejukebox-website`, `gh-pages` branch).
