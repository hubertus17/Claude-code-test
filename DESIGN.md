---
name: VetSpot
description: Closed veterinary marketplace of Grupa Fenix; one cart, many shipping slips.
colors:
  navy: "#123a63"
  sky: "#9fc0e3"
  sky-ink: "#cfe0f1"
  signal: "#c2410c"
  signal-ink: "#9a3412"
  signal-wash: "#fdeee6"
  seller-pet: "#0f6e74"
  seller-vet: "#5b3f9e"
  seller-own: "#a8640f"
  ok: "#1e7a4c"
  ok-wash: "#e4f3ea"
  warn: "#9a6200"
  warn-wash: "#fbf1dc"
  bad: "#b42318"
  bad-wash: "#fbe9e7"
  ink: "#14181d"
  ink-2: "#3a4450"
  mute: "#5b6673"
  line: "#cbd4de"
  line-2: "#e3e8ee"
  ground: "#e6ecf2"
  stock: "#ffffff"
  wash: "#f4f7fa"
  navy-wash: "#eef3f9"
typography:
  display:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "30px"
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  figure:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "26px"
    fontWeight: 800
    letterSpacing: "-0.02em"
    fontFeature: "tnum"
  headline:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "18px"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 700
  body:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 600
  mono:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "12px"
    fontWeight: 500
    letterSpacing: "0.02em"
  tag:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "11.5px"
    fontWeight: 600
    letterSpacing: "0.04em"
rounded:
  none: "0px"
  control: "6px"
  pill: "12px"
  round: "50%"
spacing:
  xxs: "4px"
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "20px"
  xl: "32px"
  gutter: "48px"
components:
  button-primary:
    backgroundColor: "{colors.signal}"
    textColor: "{colors.stock}"
    rounded: "{rounded.control}"
    padding: "0 16px"
    height: "40px"
  button-primary-hover:
    backgroundColor: "{colors.signal-ink}"
    textColor: "{colors.stock}"
  button-primary-lg:
    backgroundColor: "{colors.signal}"
    textColor: "{colors.stock}"
    rounded: "{rounded.control}"
    padding: "0 24px"
    height: "52px"
  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.stock}"
    rounded: "{rounded.control}"
    padding: "0 16px"
    height: "40px"
  button-default:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0 16px"
    height: "40px"
  button-sm:
    rounded: "{rounded.control}"
    padding: "0 12px"
    height: "32px"
  input:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.mute}"
    rounded: "{rounded.control}"
    padding: "0 12px"
    height: "42px"
  slip:
    backgroundColor: "{colors.stock}"
    rounded: "{rounded.none}"
  slip-header:
    backgroundColor: "{colors.stock}"
    padding: "10px 20px"
    height: "56px"
  slip-footer:
    backgroundColor: "{colors.wash}"
    textColor: "{colors.ink}"
    padding: "12px 20px"
  part-tag:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.stock}"
    typography: "{typography.tag}"
    rounded: "{rounded.none}"
    padding: "0 8px"
    height: "24px"
  part-chip:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0 8px 0 6px"
    height: "24px"
  status-pill-ok:
    backgroundColor: "{colors.ok-wash}"
    textColor: "{colors.ok}"
    rounded: "{rounded.pill}"
    padding: "0 9px"
    height: "24px"
  status-pill-signal:
    backgroundColor: "{colors.signal-wash}"
    textColor: "{colors.signal-ink}"
    rounded: "{rounded.pill}"
    padding: "0 9px"
    height: "24px"
  panel:
    backgroundColor: "{colors.stock}"
    rounded: "{rounded.none}"
    padding: "16px 20px"
  summary-bill:
    backgroundColor: "{colors.stock}"
    rounded: "{rounded.none}"
    padding: "18px 22px"
  shop-header:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.stock}"
    padding: "0 48px"
    height: "68px"
  side-nav:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.sky-ink}"
    width: "248px"
  side-nav-item-active:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.navy}"
    rounded: "{rounded.control}"
    height: "40px"
  table-header:
    backgroundColor: "{colors.wash}"
    textColor: "{colors.mute}"
    typography: "{typography.label}"
    padding: "10px 12px"
---

# Design System: VetSpot

## Overview

**Creative North Star: "The Consolidated Waybill"**

An order is a consolidated letter made of shipping slips. Every part has a sender (company plus warehouse), a part number and its own document, and the interface shows this literally: white label stock with a hairline frame, a perforation line under each label head, half-circle notches where the label would tear, a black mono part tag ("CZĘŚĆ 1/2", "VS-26-04812/1") and a barcode where a document is implied. The navy shell around it is the carrier; the cool blue-grey ground is the sorting table the slips lie on.

The system is dense and operational: desktop at 1440px, tables with tabular figures, small type steps, no hero scale. The largest type on any screen is the 30px page title. Colour is rationed. Navy carries the brand and the structure, the burnt-orange signal appears only on the one action that moves money or on a state that needs someone to act, and three seller colours appear only as small square swatches that tell the parts apart. The same slip anatomy serves the customer's cart, the order view, the admin dashboard's part chips and the rep's offer screen; that reuse is the system.

The world rejects the default "white rounded card with an icon on top" and the single undivided cart that hides who ships what.

**Key Characteristics:**
- Square white documents on a cool ground; rounded corners belong to controls only.
- Perforation (dashed rule) and notches mark where a document divides.
- Mono type for codes, part numbers and document IDs; Archivo for everything else.
- One signal colour, used sparingly; three seller swatches as identity markers.
- Flat: depth comes from borders, washes and the navy shell, never shadows.

## Colors

A disciplined navy-and-paper palette with one hot signal and three quiet seller markers.

### Primary
- **VetSpot Navy** (`navy`): the shell (shop header, app sidebar), page titles, links, the selected segment, active step, focus-adjacent selection fills, the top rule of the summary bill and the progress fill. Derived from and slightly deeper than the logo navy in PRODUCT.md.
- **On-navy hover** is a 7% white overlay on the navy, not a new hue.
- **Sky** (`sky`) and **Sky Ink** (`sky-ink`): icon and secondary-text colours on navy only (sidebar icons, clinic context, avatar fill). Never used on white.

### Secondary
- **Signal Orange** (`signal`): the primary action ("Zamawiam i płacę", "Ponów wysyłkę"), count badges, the focus ring, the "new" tag and the border of a part or option that needs action. Darkened from the planned #e8590c so white button text clears contrast.
- **Signal Ink** (`signal-ink`): primary-button hover, text on signal wash.
- **Signal Wash** (`signal-wash`): background of an urgent notification, a pending part chip, a highlighted figure.

### Tertiary
- **Fenix Pet Teal** (`seller-pet`), **Fenix Vet Violet** (`seller-vet`), **Own-Brand Ochre** (`seller-own`): seller identity. Shown as 10px squares (8px in part chips) beside the seller name, as chart series, as share bars and as the colour band on the generic product-pack illustrations. Never as text colour, button fill or large area.

### Neutral
- **Ink** (`ink`): primary text, the part tag fill, barcode.
- **Ink 2** (`ink-2`): secondary text in body copy, slip footer mono.
- **Mute** (`mute`): metadata, table headers, placeholders.
- **Line** (`line`): document frames, input and button borders, perforation dashes.
- **Line 2** (`line-2`): row dividers inside documents, meter track.
- **Ground** (`ground`): page background, also the fill of slip notches (so they read as cut-outs).
- **Stock** (`stock`): document paper and control fill.
- **Wash** (`wash`): slip footers, table header rows, thumbnails, secondary info boxes.
- **Navy Wash** (`navy-wash`): selected list row, selected payment method, suggestion strip, pet chip.

### Status
- **OK** / **Warn** / **Bad** each with a wash (`ok`, `ok-wash`, `warn`, `warn-wash`, `bad`, `bad-wash`): status pills, deltas, the refund notice, limit warnings, completed steps.

### Named Rules
**The One Signal Rule.** Signal orange marks the single money-moving action on a screen and states that require someone to act. If two orange buttons compete on one screen, one of them is wrong.

**The Swatch-Only Rule.** Seller colours identify; they never decorate. A seller colour appears as a small square, a chart series or a pack band, never as text, a fill behind text, or a button.

## Typography

**Display Font:** Archivo (variable 100–900, self-hosted, with system-ui fallback)
**Body Font:** Archivo
**Label/Mono Font:** JetBrains Mono (variable 100–800, self-hosted, with ui-monospace fallback)

**Character:** Archivo's slightly grotesque, compact forms give a confident, industrial tone at heavy weights and stay neutral at 15px; JetBrains Mono reads as printed on a label.

### Hierarchy
- **Display** (800, 30px, 1.15, −0.02em, navy): page title only, one per screen ("Twój koszyk", "Pulpit"). An order number inside a title switches to mono at 700.
- **Figure** (800, 26px, −0.02em, tabular): KPI numbers; totals on the bill run 24px/800 in navy, the offer send bar 22px.
- **Headline** (700, 18px, 1.25, −0.01em): panel and section titles.
- **Title** (700, 15px): sub-headings; the slip sender name runs 16px/600 with its swatch.
- **Body** (400, 15px, 1.45): default; tables 14px; secondary lines 13–13.5px; metadata 12.5px.
- **Label** (600, 12px, mute): table column headers, sentence case.
- **Mono** (500, 12px, +0.02em): order and part numbers, document IDs, sync codes.
- **Tag** (600 mono, 11.5px, +0.04em): text inside the black part tag and B2B/B2C tags.

### Named Rules
**The Label-Print Rule.** Mono is for things a machine printed: codes, part numbers, order and document IDs. Prices, quantities and prose stay in Archivo with tabular figures.

**The Tabular Rule.** Every number in a table, bill row, figure or price uses tabular numerals so columns align.

## Layout

Fixed desktop canvas at 1440px. Two shells:
- **Shop shell:** 68px navy header (logo, search up to 480px, clinic context, account and cart), then a 48px white nav bar that carries the checkout steps on the right. Content sits in a two- or three-column grid with 48px side gutters and 28px top padding; the cart uses a flexible main column plus a 412px summary, gap 32px.
- **App shell:** 248px navy sidebar, main area padded 28px 36px 40px. A title row (title, date-range context, segmented control, export button) precedes panels in a main-plus-aside grid (a 352–440px aside, gap 20px).

Spacing runs on a 4px base (4, 8, 12, 16, 20, 32, 48). Inside documents, content pads 16–20px horizontally; rows divide with hairlines rather than gaps. Between stacked documents the gap is 20px. Figures sit in equal three-column strips divided by vertical hairlines.

**The Divider-Not-Gap Rule.** Items inside one document are separated by 1px rules, not by whitespace cards; separate documents are separated by ground.

## Elevation & Depth

Flat. No surface in the system casts a shadow. Depth is conveyed by three things: the navy shell framing white stock, the cool ground showing between documents, and washes (wash, navy-wash, signal-wash) that tint a region of a document. Selection is drawn with an inset 1–2px ring (`inset 0 0 0 2px` navy for a selected row, `inset 0 0 0 1px` signal for an option needing action) layered on a coloured border, not with lift. The one shadow in the build belongs to a mocked operating-system notification, which imitates the OS and is not part of this system.

**The Paper-on-Table Rule.** Documents lie flat on the ground; they never float.

## Shapes

Two corner regimes, kept strictly apart:
- **Square (0px):** everything that is a document or a printed mark: slips, panels, the summary bill, cards in forms, thumbnails, part tags, part chips, seller swatches, meters, progress bars, payment-method tiles.
- **Gently rounded (6px):** everything you operate: buttons, inputs, quantity steppers, segmented controls, sidebar items. Inner segments run 4px; checkboxes 3px.
- **Fully round:** status pills (12px), count badges, step numbers, avatars, slip notches, radio buttons.

Signature geometry: the perforation (1.5px dashed `line` rule inset 14px under the slip head) with two half-circle notches at its ends filled with ground; a 4px navy top rule on summary documents; a dashed navy frame on a suggestion strip; a barcode drawn as SVG bars.

**The Torn-Here Rule.** A dashed rule means "this document divides here": under a slip head, before a total, between options. Don't use dashes as decoration.

## Components

### Buttons
Compact and businesslike.
- **Shape:** gently rounded (6px), 40px tall, 16px side padding, 600 weight at 14px; small 32px/13px; large 52px/16px for the checkout action, full-width in the summary.
- **Primary:** signal fill, white text; hover deepens to signal ink.
- **Navy:** navy fill, white text, for constructive secondary actions inside documents ("Dodaj").
- **Default:** white with a line border, ink text; hover turns border and text navy.
- **On navy shell:** white fill with navy text ("Zaloguj się").
- **Focus:** 2px signal outline, 2px offset, on every focusable element.
- **Link:** navy, 600, underlined with 3px offset, often followed by a small arrow icon.

### Status Pills and Tags
- **Status pill:** 24px tall, fully round, wash background with matching ink text and a 6px leading dot (ok, warn, bad, signal, info).
- **Part tag:** square black slab with white mono caps ("CZĘŚĆ 1/2"); light variant is white with a 1px ink border (B2C), the black variant marks B2B; signal fill marks "new".
- **Part chip:** square, 24px, white with line border, 8px seller swatch, "/1 Fenix Pet" and a status icon; pending parts take a signal border and signal wash.

### Slips (signature)
The shipping slip is the unit of the system.
- **Head:** min 56px, padded 10px 20px: black part tag, seller swatch and name (16px/600), a muted line naming warehouse and timing, optional barcode or actions at the end.
- **Perforation:** dashed rule under the head with ground-filled notches cut into both edges.
- **Body:** item rows (72px thumbnail, name and meta, quantity stepper, right-aligned price) divided by line-2 hairlines.
- **Footer:** wash band naming who issues the invoice and the part total.

### Panels and the Summary Bill
- **Panel:** square white document, 1px line border; head row 16px 20px with a line-2 divider, title left and controls right; body 16px 20px or a full-bleed table.
- **Summary bill:** a panel with a 4px navy top rule, per-seller rows with swatches, a dashed rule before the total, the total in navy 24px/800, payment tiles, then the primary action.

### Inputs / Fields
- **Style:** 42px tall, white, 1px line border, 6px radius, a leading 16–20px icon in mute, placeholder in mute and entered values in ink.
- **Quantity stepper:** 112px wide, 36px tall, minus and plus icons in mute around a 600-weight value.
- **Segmented control:** white with line border and 3px inner padding; the active segment is navy with white text.
- **Selection:** checkboxes are 18px, 1.5px ink-2 border; radios fill with a 5px navy ring; selected rows use navy wash plus a 2px inset navy ring.

### Tables
- Header row in wash, 12px/600 mute labels, a line rule beneath; body 14px with line-2 dividers, 20px outer padding, right-aligned numbers, codes in mono, a muted sub-line under primary cell text.

### Navigation
- **Shop:** navy header (logo, translucent search field with a white 14% fill, clinic context in sky ink), white nav strip with 600 category links and a step indicator: numbered 22px circles, navy when current, OK green with a check when done, joined by 28px hairlines.
- **App sidebar:** navy column; items 40px, 14px/500, sky icons; hover adds a 7% white overlay; the active item flips to white with navy text and icon; count badges are signal circles; the signed-in user sits at the bottom under a hairline with a sky avatar.

### Icons and Product Packs
- **Icons:** a single custom stroke set on a 24px grid, 1.75 stroke, round caps and joins, drawn at 20px (16px small) in currentColor.
- **Product packs:** generic, unbranded SVG packs (bag, can, pouch, bottle, tray) in white with a grey outline and the seller's colour as the band, on a wash thumbnail. No product photography and no third-party brands.

## Do's and Don'ts

### Do:
- **Do** show every order part as its own slip with tag, sender, warehouse and footer wherever documents, shipments or refunds are explained.
- **Do** keep documents square and controls at 6px.
- **Do** put codes, part numbers and document IDs in JetBrains Mono, and every number in tabular figures.
- **Do** separate rows inside a document with 1px hairlines and separate documents with 20px of ground.
- **Do** reserve signal orange for the money-moving action and for states someone must act on.
- **Do** use the self-hosted Archivo and JetBrains Mono and the supplied VetSpot logotype (white on navy, navy on white).

### Don't:
- **Don't** add drop shadows to documents, buttons or panels.
- **Don't** round slips, panels, tags or thumbnails.
- **Don't** use seller colours for text, fills behind text or buttons.
- **Don't** merge a multi-seller order into one undivided list where the split matters.
- **Don't** use the dashed perforation as decoration where nothing divides.
- **Don't** use photographs or third-party product brands for products; use the generic packs.
