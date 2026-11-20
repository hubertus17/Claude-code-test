---
version: 1
slug: "makiety-02-koszyk-html"
primary_target: "makiety/02-koszyk.html"
related_targets: ["makiety/01-pulpit.html","makiety/03-zamowienie.html","makiety/04-rejestracja.html","makiety/05-handlowiec-lecznice.html","makiety/06-handlowiec-oferta.html","makiety/07-strefa-lecznicy.html"]
---

# VetSpot – 7 ekranów do prezentacji dla zarządu

Scope: 7 desktopowych makiet 1440 px (makiety/01–07), jeden system. Mode: operate (sklep i panele robocze). Odbiorca: zarząd Grupy Fenix; użytkownicy w makietach: klient B2C, lecznica, handlowiec, administrator.
Constraints: tylko funkcje z briefu, cały copy po polsku, sprzedawcy „Fenix Pet”, „Fenix Vet”, „Marka własna grupy”, dane przykładowe.

## Direction contract
THESIS: Zamówienie to list zbiorczy złożony z listów przewozowych – każda część ma nadawcę (spółka + magazyn), numer części i własny dokument. Odrzucamy domyślny układ „białe karty z ikonką” i jednolity koszyk, który ukrywa podział.
OWN-WORLD: granat VetSpot #123a63 na powłoce, chłodne tło #e6ecf2, czysto biały papier etykiet z 1 px ramką bez zaokrągleń, linia perforacji (przerywana) pod nagłówkiem etykiety, czarny znacznik części w kroju mono („CZĘŚĆ 1/2”, „VS-26-04812/1”), sygnałowy pomarańcz #e8590c tylko dla głównej akcji i stanów wymagających ruchu, trzy kolory sprzedawców jako drobne znaczniki. Archivo + JetBrains Mono wyłącznie dla kodów, numerów i kwot w tabelach.
STORY: zarząd widzi, że klient ma jeden koszyk i jedną płatność, a każda spółka dostaje swoją część, fakturę, Optimę i pieniądze; lecznica zarabia, handlowiec działa.
FIRST VIEWPORT: (Koszyk) granatowy header ze sklepem i lecznicą, pasek nawigacji z krokami; po lewej etykiety sprzedawców z pozycjami, po prawej list zbiorczy z kwotą i pomarańczowym „Zamawiam i płacę” nad linią zgięcia.
FORM: kandydat 4 z 7 (list przewozowy / etykieta nadawcy); seed:9469864e8a59b8df. Signature move: etykieta części z perforacją i znacznikiem mono, wspólna dla koszyka, zamówienia, pulpitu i ofert.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
