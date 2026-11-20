---
name: "Sunreef · Materiał i formy"
description: "Shipyard material and mould tracker built like a sail loft's working system: every hull carries its sail number, every scan is a fix in time."
colors:
  ground: "#f3f5f6"
  stock: "#ffffff"
  wash: "#f6f8f9"
  rail: "#1a2026"
  rail-2: "#232b32"
  rail-3: "#2e3841"
  rail-ink: "#c3ccd3"
  rail-mute: "#8794a0"
  ink: "#12181d"
  ink-2: "#36414b"
  mute: "#5c6873"
  line: "#d3d9de"
  line-2: "#e5e9ec"
  seam: "#c4ccd2"
  sail: "#13315c"
  sail-wash: "#e4e9f1"
  sea: "#1f62b0"
  sea-ink: "#174c8a"
  sea-wash: "#e6eef8"
  gel: "#c75f0e"
  gel-ink: "#9c4a0a"
  gel-wash: "#fbede1"
  alert: "#c4282b"
  alert-ink: "#a11f22"
  alert-wash: "#fbe7e6"
  warn: "#8f5a00"
  warn-wash: "#fcf0d9"
  ok: "#1d7448"
  ok-wash: "#e2f1e8"
typography:
  display:
    fontFamily: "Barlow, system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.015em"
  headline-mobile:
    fontFamily: "Barlow, system-ui, sans-serif"
    fontSize: "21px"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Barlow, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 700
    letterSpacing: "-0.005em"
  item-title:
    fontFamily: "Barlow, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 700
    lineHeight: 1.3
  body:
    fontFamily: "Barlow, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.45
    fontFeature: "tnum"
  label:
    fontFamily: "Barlow, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 600
    letterSpacing: "0.01em"
  figure-display:
    fontFamily: "Barlow Condensed, Barlow, system-ui, sans-serif"
    fontSize: "46px"
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: "-0.01em"
  figure:
    fontFamily: "Barlow Condensed, Barlow, system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 700
    lineHeight: 1
  sail-number:
    fontFamily: "Barlow Condensed, Barlow, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.01em"
  wordmark:
    fontFamily: "Barlow Condensed, Barlow, system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.16em"
  code:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "0.86em"
    fontWeight: 500
    letterSpacing: "0.01em"
rounded:
  tick: "2px"
  sail-number: "3px"
  chip: "4px"
  control: "6px"
  sheet: "16px"
  pill: "10px"
  full: "50%"
spacing:
  xs: "6px"
  sm: "10px"
  md: "14px"
  lg: "18px"
  grid: "20px"
  mobile-gutter: "16px"
  page-x: "32px"
components:
  button:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0 14px"
    height: "38px"
  button-dark:
    backgroundColor: "{colors.rail}"
    textColor: "{colors.stock}"
    rounded: "{rounded.control}"
    padding: "0 14px"
    height: "38px"
  button-sm:
    height: "32px"
    padding: "0 11px"
  bigbtn:
    backgroundColor: "{colors.rail}"
    textColor: "{colors.stock}"
    rounded: "{rounded.control}"
    height: "58px"
    width: "100%"
  bigbtn-ghost:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    height: "58px"
  bigbtn-danger:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.stock}"
    rounded: "{rounded.control}"
    height: "58px"
  select:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.control}"
    padding: "0 10px 0 12px"
    height: "36px"
  field-mobile:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "8px 14px"
    height: "52px"
  field-mobile-readonly:
    backgroundColor: "{colors.wash}"
  panel:
    backgroundColor: "{colors.stock}"
    rounded: "0px"
    padding: "14px 18px"
  card-mobile:
    backgroundColor: "{colors.stock}"
    rounded: "{rounded.control}"
    padding: "14px"
  badge-alert:
    backgroundColor: "{colors.alert-wash}"
    textColor: "{colors.alert-ink}"
    rounded: "{rounded.chip}"
    height: "24px"
    padding: "0 8px"
  badge-ok:
    backgroundColor: "{colors.ok-wash}"
    textColor: "{colors.ok}"
    rounded: "{rounded.chip}"
  badge-warn:
    backgroundColor: "{colors.warn-wash}"
    textColor: "{colors.warn}"
    rounded: "{rounded.chip}"
  badge-sea:
    backgroundColor: "{colors.sea-wash}"
    textColor: "{colors.sea-ink}"
    rounded: "{rounded.chip}"
  badge-gel:
    backgroundColor: "{colors.gel-wash}"
    textColor: "{colors.gel-ink}"
    rounded: "{rounded.chip}"
  tag:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.chip}"
    padding: "3px 9px"
    height: "26px"
  sail-number:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.sail}"
    typography: "{typography.sail-number}"
    rounded: "{rounded.sail-number}"
    padding: "0 4px"
    height: "22px"
  sail-number-lg:
    typography: "{typography.figure}"
    height: "32px"
  nav-item:
    backgroundColor: "{colors.rail}"
    textColor: "{colors.rail-ink}"
    rounded: "{rounded.control}"
    padding: "0 12px"
    height: "40px"
  nav-item-hover:
    backgroundColor: "{colors.rail-2}"
    textColor: "{colors.stock}"
  nav-item-active:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.rail}"
  count:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.stock}"
    rounded: "{rounded.pill}"
    height: "22px"
  stepper-button:
    backgroundColor: "{colors.wash}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    size: "48px"
  toast:
    backgroundColor: "{colors.ok}"
    textColor: "{colors.stock}"
    rounded: "{rounded.control}"
    padding: "14px 16px"
---

# Design System: Sunreef · Materiał i formy

## Overview

**Creative North Star: "The Sail Loft"**

A sail loft is a working floor, not a showroom: cool white cloth laid flat under hard light, numbers stitched large enough to read from across the hall, every panel cut square and every seam a hairline. This system treats the shipyard's material and moulds the same way. The ground is cool sailcloth, the frame is carbon laminate, and the things that matter (which hull, how many, where it was last scanned) are set as sail-number figures in condensed bold. Everything else steps back into quiet grey.

Density is high but orderly, built for a production manager who reads a site plan in three seconds and a shop-floor worker who taps through a confirmation with gloves on. Desktop is a charcoal rail plus a white header over a sailcloth ground with square, hairline-bordered panels. Mobile flips the frame: the charcoal moves to the top bar and the primary action becomes a full-width 58px carbon slab. Colour is never decoration; every hue carries a job (material, mould, alert, ok, other hull), and those jobs hold on every screen.

The world explicitly refuses the grey SaaS dashboard with a single blue accent and a stock pin map. The site plan is a schematic drawn in the system's own materials (hairline grid, solid hall walls, dashed yard boundary), never a map tile.

**Key Characteristics:**
- Cool sailcloth ground, carbon-laminate rail, hairline seams.
- Five colours with fixed jobs; tinted washes carry them in badges and icon wells.
- Barlow for UI, Barlow Condensed bold for every count and sail number, JetBrains Mono for printed codes.
- Square desktop panels; 6px controls; small squared badges.
- The hull sail-number badge is the signature: every hull reference carries one.
- Location language is always "according to the last scan", never live.

## Colors

A cool, near-neutral loft palette where saturated colour appears only as a job marker.

### Primary
- **Carbon Laminate** (rail): the desktop side rail, mobile status and title bars, primary buttons, active segmented control, selected chips, avatar. The frame of the world; it holds everything else.
- **Sail Navy** (sail): the sail-number badge stroke and numerals, bars in loss-by-category charts, and the "used on another hull" state with its Sail Wash (sail-wash) tint. Navy means "a hull".

### Secondary
- **Sea Blue** (sea, text in sea-ink, tint sea-wash): material. Material batch markers on the plan (squares), material icon wells, material counts, links ("Pokaż historię"), focus ring.
- **Tooling Gelcoat** (gel, text in gel-ink, tint gel-wash): moulds. Mould markers on the plan (diamonds), mould icon wells and counts.

### Tertiary
- **Signal Red** (alert, text in alert-ink, tint alert-wash): something needs a reaction. Zone alert discs, nav and panel counts, loss badges, overrun bars, waste quantities, destructive "send loss report" button, outline ring around a flagged marker.
- **Hull Green** (ok, tint ok-wash): confirmed. Delivery badges, completed-stage nodes, scan-frame corners, save toast, matched inventory cells.
- **Amber** (warn, tint warn-wash): unexpected but not lost ("Nieoczekiwana" in stocktaking). Used sparingly.

### Neutral
- **Sailcloth** (ground): page background on both platforms.
- **Stock White** (stock): panels, cards, controls, sail-number badge fill.
- **Wash** (wash): table headers, read-only fields, the site-plan floor, stepper buttons.
- **Ink** (ink), **Ink 2** (ink-2), **Mute** (mute): primary text, secondary text, labels and metadata.
- **Line** (line), **Line 2** (line-2), **Seam** (seam): panel borders, inner row dividers, timeline axis and dashed slots.
- **Rail Ink / Rail Mute / Rail 2 / Rail 3**: text, icons, hover fill and dividers inside the carbon rail.

### Named Rules
**The Colour Has a Job Rule.** Sea is material, gelcoat is mould, red is react, green is done, navy is a hull. A colour never appears outside its job, and a job never borrows another's colour.

**The Wash Pairing Rule.** A semantic colour on a light surface comes as a pair: its wash for the fill and its -ink step for the text or glyph. Full-strength colour is reserved for markers, counts, bars and solid action fills.

## Typography

**Display Font:** Barlow (with system-ui)
**Body Font:** Barlow (with system-ui)
**Figure Font:** Barlow Condensed 700 (with Barlow)
**Label/Mono Font:** JetBrains Mono 500

**Character:** Barlow is a plain, slightly technical grotesk that reads like stencilled yard signage without costume. Barlow Condensed bold gives numbers the tall, tight presence of a sail number; JetBrains Mono marks anything that is printed on a label or document (batch codes, RW numbers, mould IDs).

### Hierarchy
- **Display** (700, 28px, 1.15, -0.015em): desktop page title, one per screen.
- **Headline mobile** (700, 21px): title inside the mobile carbon bar.
- **Title** (700, 16px): panel headers; 17px on the reaction panel and mobile cards, 20px for the bottom-sheet title.
- **Item title** (700, 15px, 1.3): list and timeline item headings.
- **Body** (400, 15px, 1.45, tabular numerals on): default text; 14 to 14.5px inside panels.
- **Label** (600, 13px, mute): field labels, stat labels, table headers (12.5px).
- **Figure display** (Condensed 700, 46px, 0.9): zone counts on the site plan; 54px in report tiles.
- **Figure** (Condensed 700, 28px): stepper values; 30px progress counts, 19 to 20px inside chips, bars and balances.
- **Code** (Mono 500, 0.86em): batch, mould and document codes inline in text.

### Named Rules
**The Sail Number Rule.** Every count that answers "how many" and every hull number is set in Barlow Condensed bold. Body Barlow never carries a headline quantity.

**The Printed Code Rule.** Mono is only for strings that physically exist on a label or document (M-24817, F-021, RW 1184/11/2026). It is never used for UI chrome or decoration.

## Layout

Desktop renders at 1440px: a 236px carbon rail, then a 60px white header with breadcrumbs and user, then the page at 26px top and 32px sides. Page head (title, lede, actions right) sits above a filter row of 36px selects with 10px gaps. Content uses explicit two- or three-column grids with a fixed side column (372px reaction panel, 340px side stack, 420px repair panel) and a 20px gutter.

Mobile renders at 390px: 44px carbon status bar, carbon title bar with a 36px back square, then a 16px-gutter body stacked with 14 to 16px gaps. Fields are 52px tall; the primary action is a full-width 58px slab, docked at the bottom with a hairline top border when the list scrolls.

Spacing moves in small even steps (6, 8, 10, 12, 14, 18, 20px). Panels pad 14px by 18px in their header and 18px in their body. Rows inside panels are separated by Line 2 hairlines, never by gaps.

The site plan is a drawn schematic: a 28px hairline grid on Wash, halls as white rectangles with 2px Ink 2 walls and an inset name tab, the outdoor yard as a 2px dashed Mute boundary with a faint 135° hatch, zones as Stock boxes with Seam hairlines.

## Elevation & Depth

Flat by default. Depth comes from tone (carbon frame, sailcloth ground, stock panels) and hairlines, not from shadow. Shadows appear only on things that float above the page on mobile, and as a halo ring that separates a marker from its background.

### Shadow Vocabulary
- **Toast lift** (`box-shadow: 0 10px 30px -8px rgba(18,24,29,.45)`): the save confirmation toast.
- **Sheet lift** (`box-shadow: 0 -12px 30px -10px rgba(0,0,0,.4)`): bottom sheet over a 55% Ink scrim.
- **Segment lift** (`box-shadow: 0 1px 3px rgba(0,0,0,.2)`): the active option in a segmented control.
- **Halo ring** (`box-shadow: 0 0 0 3px #fff`): zone alert discs on the plan; flagged markers use a double ring (`0 0 0 2px stock, 0 0 0 4px alert`).

### Named Rules
**The Flat Loft Rule.** Panels, cards, tables and buttons never cast shadows. If a surface is not floating over other content, it has no shadow.

## Shapes

Square where it is structure, slightly softened where it is touched. Desktop panels, tiles, status strips and the site plan have square corners and a 1px Line border. Controls (buttons, selects, fields, icon wells, mobile cards and lists, toast) use a 6px radius. Badges, tags and chips are 4px. The sail-number badge is 3px with a 1.5px navy stroke. Plan markers and bar ticks are 2px. The bottom sheet rounds its top corners at 16px. Count pills are fully rounded at 9 to 10px; the avatar and alert discs are circles.

Marker geometry carries meaning on the plan and legend: material is a square, mould is a square rotated 45° (a diamond), alert is a circle.

## Components

### Buttons
Practical and blunt; the dark slab is the one thing to press.
- **Shape:** 6px radius.
- **Default:** Stock fill, 1px Line border, Ink 600 14px text, 38px tall, 14px sides; border darkens to Mute on hover.
- **Dark:** Carbon fill and border, white text; hover goes to black.
- **Small:** 32px tall, 11px sides, 13.5px text.
- **Mobile primary (big):** 58px full-width Carbon slab, 700 17.5px, 22px icon; pressed goes to black. Ghost variant is Stock with a 1.5px Ink border; destructive variant is Signal Red fill.
- **Mobile text link:** 48px tall, centred, 600 Alert Ink with icon, for a secondary destructive path ("Zgłoś stratę materiału").

### Chips
- **Status badges:** 24px tall, 4px radius, 600 12.5px, Wash Pairing (wash fill, ink text) in alert, ok, warn, sea and gelcoat.
- **Tags:** 26px, Stock with Line border, Ink 2 13px text, optional muted 15px icon; for metadata (QR code, issued quantity, supplier).
- **Quantity chips:** 34px, 4px radius, semantic wash, with the figure in Condensed 19px.
- **Category choice chips (mobile):** 40px, 6px radius, Stock with Line border; selected becomes Carbon with white text and a check.

### Cards / Containers
- **Corner Style:** square on desktop panels; 6px on mobile cards and lists.
- **Background:** Stock on Sailcloth.
- **Shadow Strategy:** none (see Flat Loft Rule).
- **Border:** 1px Line outside, Line 2 hairlines between rows and below the header.
- **Internal Padding:** header 14px by 18px; body 18px; mobile 14px.

### Inputs / Fields
- **Desktop select:** 36px, Stock, Line border, 6px; "Label: **value**" with a muted chevron.
- **Mobile field:** 52px, Stock, Line border, 6px, 16px 500 text, leading muted icon, trailing chevron; read-only uses Wash.
- **Stepper:** 48px Wash squares with a 1.5px Line border either side of a Condensed 28px value plus a small unit; waste values turn Alert Ink.
- **Segmented control:** grey track with 3px inset, 46px options; active option is Carbon with white text.
- **Focus:** 2px Sea outline, 2px offset, on every focusable element.

### Navigation
- **Desktop rail:** Carbon, 236px. Wordmark in Condensed 700 22px with 0.16em tracking over a muted subtitle and a Rail 3 divider. Items are 40px, 500 14.5px Rail Ink with Rail Mute icons; hover fills Rail 2 and goes white; the active item inverts to a white slab with Carbon text and icon. Alert count sits right as a red pill.
- **Breadcrumbs:** 13.5px Mute in the white header; current page in Ink 500.
- **Tabs:** 600 14.5px Mute with a 2px underline that turns Ink when active.
- **Mobile:** Carbon status and title bars; back is a 36px Rail 2 square.

### Hull Sail-Number Badge (signature)
The hull's number set as a sail number: a Stock box with a 1.5px Sail Navy stroke, 3px corners, Condensed 700 16px navy numerals, 22px tall and at least 26px wide. The large variant is 32px tall with 24px numerals and a 2px stroke. It always precedes the full hull label "Model · jednostka NN" in a hull reference, and can stand alone in tight balance rows. It is hidden from assistive tech because the text label repeats the number.

### Site Plan Zone
A Stock box inside a hall, with the zone name in 700 14.5px, then one or more count markers (glyph, Condensed 46px figure in Sea Ink or Gel Ink, two-line label) above a grid of 14px unit glyphs. A 24px red disc with a white halo in the corner carries the zone's alert count; the flagged unit gets the double red ring.

### Reaction Item
A 34px 6px-radius icon well in the job's wash, then a 15px bold title, 14px Ink 2 detail, optional plan bar or "scanned / expected" pair, and a Sea Ink "Pokaż historię" link with a history icon. Items are separated by Line 2 hairlines.

### Timeline Event
Date and time right-aligned in a 118px column, a 2px Seam axis with 34px circular nodes (2px Ink 2 stroke), then the event body. "Used on another hull" switches the node to Sail Navy on Sail Wash with a navy-tinted justification box; completion fills the node Hull Green.

## Do's and Don'ts

### Do:
- **Do** attach the sail-number badge to every hull reference, followed by the exact text "Model · jednostka NN".
- **Do** set every headline count and hull number in Barlow Condensed 700.
- **Do** keep each semantic colour to its job: sea for material, gelcoat for moulds, red for react, green for done, navy for hulls.
- **Do** pair semantic colour with its wash and -ink step on light surfaces.
- **Do** mark material with a square and moulds with a diamond wherever both appear together.
- **Do** phrase every location as "according to the last scan" and show the scan time.
- **Do** use JetBrains Mono for codes printed on labels and documents.
- **Do** keep desktop panels square with a 1px Line border, and controls at 6px.

### Don't:
- **Don't** build the grey SaaS dashboard with one blue accent, or drop in a stock pin map; the plan is a drawn schematic.
- **Don't** put shadows on panels, cards, tables or buttons.
- **Don't** use a semantic colour as decoration or swap colours between material and moulds.
- **Don't** use mono for labels, headings or UI chrome.
- **Don't** imply live tracking or GPS position anywhere in the UI.
- **Don't** set a headline quantity in regular Barlow body weight.
