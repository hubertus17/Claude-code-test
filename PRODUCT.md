# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS: each screen is a separate HTML file with one shared stylesheet, plus 1440 px wide PNG exports for the presentation. The user chose this.

## Users

This repository holds desktop mockups for a sales presentation to the management of Grupa Weterynaryjna Fenix (Poland). The mockups show these platform users:

- **Pet owners (B2C):** buy veterinary diets, functional treats and pet products recommended by vets. They must register and assign themselves to a veterinary clinic.
- **Veterinary clinics (B2B):** buy wholesale, earn commission on purchases by their assigned customers, and accept offers from their sales representative in the clinic zone.
- **Sales representatives:** look after clinics in their region. They send offers built as a cart, track overdue invoices and handle new clinics.
- **E-commerce administrator and management:** see the whole group and each company separately.

The direct audience of the deliverable is group management, who will judge whether the new platform solves their problems.

## Product Purpose

VetSpot (vetspot.com) is the group's online store. Today it is connected to only one company. Because of that, a customer cannot buy products from several companies in one cart, and the group cannot settle such a sale separately for each company. The new VetSpot is a closed marketplace. The customer sees one brand, one cart, one payment and one delivery cost. The order is split into parts per company and warehouse, each part goes to that company's Comarch ERP Optima, and each company issues its own invoice and receives its own share of the payment.

The deliverable succeeds when management immediately sees, on 7 screens, how this works for each role.

## Positioning

The platform is a closed marketplace of one group, not an open one. It is one storefront for the customer with full settlement separation behind it: per company, warehouse, Optima instance, invoice and payment share. Each retail customer is tied to a clinic, which earns commission. This turns clinics from competitors into partners.

## Operating Context

- Sellers (names used everywhere): **Fenix Pet** (veterinary diets), **Fenix Vet** (supplements and nutraceuticals), **Marka własna grupy** (functional treats and foods under the group's own brand).
- Each company has its own warehouse and its own Comarch ERP Optima.
- Payments: Przelewy24 / BLIK / Apple Pay. Delivery: InPost.
- VETSPOT CLUB loyalty program (points; "10% wraca na kolejne zakupy").
- Sales representatives use contractor codes ("kod kontrahenta") and merchant credit limits per seller. Payment reminders go out 7 days before, 3 days before and on the due date.

## Capabilities and Constraints

- 7 screens: Pulpit grupy (admin), Koszyk, Zamówienie po płatności, Rejestracja: wybór lecznicy, Panel handlowca: nowa lecznica, Panel handlowca: oferta i należności, Strefa lecznicy.
- Desktop only, 1440 px wide. All UI copy is in Polish.
- Show only the functionality listed in the brief for each screen. Do not invent extra functions.
- One consistent visual system across all 7 screens. It must look clearly more modern than today's vetspot.com.
- Clinic privacy: the clinic sees a customer only as the first three letters of their name (e.g. "Ann***"), never their cart, address or phone.

## Brand Commitments

- The name **VetSpot / VETSPOT** and the existing logotype: `assets/vetspot-logo.svg` (taken from vetspot.com). Brand colors from the logo: navy `#164472`, light blue `#7A9DC2`.
- The current store uses Montserrat, navy accents and uppercase buttons. Treat this as a reference point for brand recognition, not a style to copy: the brief requires a clearly more modern look.
- The tagline from the current site: "Produkty rekomendowane przez lekarzy weterynarii".

## Evidence on Hand

- Names, amounts, order numbers and clinics are sample data from the brief (e.g. "Przychodnia Weterynaryjna Pod Lipami", "VS-26-04812", "Gabinet Weterynaryjny Animal, Gniezno").
- There are no product photos or visual references (the brief's reference links were empty). Do not fabricate real products from other brands. Products are generic descriptions from the brief.

## Product Principles

1. **One brand on the outside, separate settlements on the inside.** The customer sees one store and one payment. The division into sellers is visible wherever it explains documents, shipments and refunds, and nowhere else.
2. **Each company is visible separately, the group as a whole.** Every view has both: the group total and the breakdown per seller.
3. **The clinic is a partner.** Commission and the clinic assignment must be readable for every role, with the customer's privacy protected.
4. **Status comes from the parts.** An order's status follows from the state of its parts (shipments, Optima, refunds), not from a single flag.
