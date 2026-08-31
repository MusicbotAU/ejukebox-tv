# ejukebox-tv

Source for **https://ejukebox.tv** - the eJukebox TV sister site.

**Jekyll on GitHub Pages**, built server-side by GitHub. No Actions, no local build step,
no Ruby needed on your machine - edit a file and push.

```
_config.yml                site settings, contact details and THE VIDEO SLOT
_layouts/default.html      the one layout: head, the entire site CSS, shared JS
_includes/nav.html         top bar - brand, nav, live clock, ON AIR dot
_includes/footer.html      site footer
_includes/cta.html         the closer block every page ends on
_includes/video-stage.html ROLL THE TAPE - the video slot
_includes/pic.html         a "photo", drawn in CSS and SVG (swap for real images)
index.html                 the home page - the screen product
functions.html             /functions/ - functions and events (body_class: functions)
demo.html                  /demo/ - see it live, the honest FAQ, contact
CNAME                      custom domain binding
```

## Putting the video in

Drop the file into `/assets/video/` and set it in `_config.yml`:

```yaml
video:
  url: "/assets/video/a-night-at-the-pub.mp4"
  poster: "/assets/video/poster.jpg"
  aspect: "16/9"     # use "9/16" for portrait phone footage from a function
  caption: "A Friday night, start to finish."
```

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

Page-scoped CSS lives in a single `<style>` block at the top of the page with a unique
class prefix (`fx-`, `dm-`). It may only reach for existing tokens - never define a new
colour there.

## No form on /demo/

GitHub Pages has no backend, so the demo page uses a pre-filled `mailto:` (venue, town,
how many screens, what is on them now, best time to ring) plus a `tel:` link, and says
plainly why there is no form. **This measurably costs conversions** and is worth
revisiting once `info@ejukebox.tv` is live and a form endpoint has been chosen.

## House rules for anything added here

- Australian English - organise, recognise, licence (noun) / license (verb), colour.
- Spaced hyphens " - " only. Never em dashes or en dashes, in any file.
- Nothing unbuilt is claimed as shipping. Roadmap items carry the diamond marker and an
  adjacent "not shipping yet" line, and render cooler and lower contrast than live ones.
- No pricing and no hardware cost anywhere on the site. The call to action is "talk to us".
- The photos are illustrations, not venue photography, and are labelled as such.

Before pushing, grep every file for em dashes, en dashes and dollar signs.

The main eJukebox site is a separate repo (`MusicbotAU/ejukebox-website`, `gh-pages` branch).
