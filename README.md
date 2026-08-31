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
_includes/pic.html         a "photo", drawn in CSS and SVG (swap for real images)
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

## No form on /demo/

GitHub Pages has no backend, so the demo page uses a pre-filled `mailto:` (venue, town,
how many screens, what is on them now, best way to reach you). No phone number is published on
this site by design - Marc's mobile attracts cold calls. Says
plainly why there is no form. **This measurably costs conversions** and is worth
revisiting once `info@ejukebox.tv` is live and a form endpoint has been chosen.

## House rules for anything added here

- Australian English - organise, recognise, licence (noun) / license (verb), colour.
- Spaced hyphens " - " only. Never em dashes or en dashes, in any file.
- Nothing unbuilt is claimed as shipping. Roadmap items carry the diamond marker and an
  adjacent "not shipping yet" line, and render cooler and lower contrast than live ones.
- No pricing and no hardware cost anywhere on the site. The call to action is "talk to us".
- The photos are illustrations, not venue photography, and are labelled once per page.
- No claim that the product is running in real venues, and no claim that footage was shot
  in one, until that is true.
- Colour is never the only carrier of meaning - the roadmap tags carry a visually hidden
  "Coming soon, not shipping yet:" as well as the diamond.

Before pushing, grep every file for em dashes, en dashes and dollar signs.

The main eJukebox site is a separate repo (`MusicbotAU/ejukebox-website`, `gh-pages` branch).
