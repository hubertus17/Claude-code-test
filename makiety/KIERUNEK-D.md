# Zestaw D – finalny kierunek (A + C)

Zestaw D łączy rozpoznawalność [Marka] i czytelne komponenty z zestawu A z podziałem ekranów i opowiadaniem z zestawu C. Zestawy A i C zostały bez zmian.

## Kolory

| Rola | Kolor |
|---|---|
| Kolor marki, ciemne panele, nagłówki | granat **#042F5B** |
| Przyciski główne, aktywne zakładki, akcenty | **#164472** |
| Kolor pomocniczy (wykresy, ikony, tła informacyjne) | błękit **#6B92BD** (tła **#E8EFF7**) |
| Tło strony | **#EEF2F6** |
| Karty | biel |
| Tekst | **#13243A** |
| Spółka A | teal **#0E7C86** |
| Spółka B | magenta **#B0287A** |
| Marka własna grupy | fiolet **#6D3FD8** |

- Statusy:
  - ostrzeżenie: bursztyn #8A4D00 na #FFF0D4;
  - błąd: czerwień #C42B1C na #FDE8E5;
  - sukces: zieleń #1B7A43 na #E3F4E8.
- Główny przycisk jest zawsze granatowy, nigdy bursztynowy ani czerwony. Czerni nie używamy jako koloru wiodącego.
- Logo [Marka] jest w oryginalnych kolorach albo białe na granacie.
- Kształty: zaokrąglenia 6–8 px, bez pigułek.
- Kwoty: najważniejsze do 34–38 px, bez „plakatowych” liczb.

## Fonty

**Outfit** w nagłówkach i kwotach, **Rubik** w treści, z cyframi tabelarycznymi. To para fontów z rekomendacji ui-ux-pro-max, ta sama co w C.

## Co z A, a co z C – ekran po ekranie

| Ekran | Z A | Z C |
|---|---|---|
| D1 Pulpit | panel boczny z licznikami; status ERP dla trzech spółek; słupkowy wykres dzienny podzielony na spółki; dane i tabela zamówień z częściami jako etykietami | „Wymaga reakcji” jako pierwszy pas na górze; kolejność sekcji (reakcja, ERP, sprzedaż grupy i spółek, zamówienia); udziały spółek jako osobne pozycje z kwotą, udziałem i magazynem |
| D2 Koszyk | cały układ: części „CZĘŚĆ 1/2 · Spółka A”, „CZĘŚĆ 2/2 · Marka własna grupy” po lewej (magazyn, wysyłka do 72 h, kto wystawi fakturę, suma); podpowiedź pod spodem; podsumowanie z płatnością po prawej; granatowy nagłówek sklepu | jeden komunikat na górze: „Jedno zamówienie, jedna płatność, dwie paczki” |
| D3 Zamówienie | granatowy nagłówek sklepu; produkty w częściach z ciemną etykietą „ZM-26-04831/1”, sprzedawcą, magazynem i statusem | poziome zakładki konta; nagłówek ze zdaniem-odpowiedzią i informacjami; „Koszt zamówienia po zwrocie” (mniejszy); osie czasu obu paczek; blok „Dokumenty i płatność” z kartami PDF i punktami |
| D4 Rejestracja | granatowy nagłówek sklepu; granatowy blok „Co zyskujesz · po założeniu konta” z trzema benefitami i ikonami | mapa na lewej połowie z wyszukiwarką i listą 1–4 zgodną z pinezkami; po prawej pionowe kroki, karta wybranej lecznicy, kod QR, pole „Nie ma Twojej lecznicy…” |
| D5 Handlowiec – lecznice | panel boczny; tabela z kolumnami z A | granatowa karta nowej placówki z siatką regionu i wyróżnionym Gnieznem; paski obrotu w tabeli; powiadomienie (10:30) małe w prawym górnym rogu nad kartą, nie zasłania tabeli |
| D6 Handlowiec – oferta | panel boczny; etykiety „CZĘŚĆ 1/3 · 2/3 · 3/3”; przy każdym produkcie cena hurtowa za sztukę, za opakowanie zbiorcze, ilość opakowań i wartość netto | nagłówek lecznicy z rozliczeniem prowizji obok; trzy kolumny sprzedawców z limitem, ofertą i przeterminowanymi fakturami; pasek na dole z sumą, podziałem i „Wyślij ofertę do strefy lecznicy”. W kolumnie Spółka B: „Przekracza limit kupiecki o 18,00 zł · ta część wymaga przedpłaty” |
| D7 Strefa lecznicy | w ofercie: etykiety „CZĘŚĆ 1/3”, wartość przy każdej pozycji i suma każdej części | nagłówek strefy (lecznica, opiekun, telefon) w granacie; prowizja naliczona z kartami „rozliczona” i „do rozliczenia” oraz „Wgraj fakturę prowizyjną”; oferta jako szeroki pas z kolumnami sprzedawców i „Akceptuj”; wykres z kwotą prowizji nad słupkami; na dole limity i transakcje. Ten sam komunikat o limicie Spółka B co w D6 |

## Spójność danych

- **Pulpit i koszyk:** dane jak w A, w tym ZM-26-04831 (249,99 zł, po zwrocie 148,99 zł) oraz Paczkomat 8,99 zł.
- **Pozostałe ekrany:** dane jak w C:
  - prowizja naliczona 4 912,60 zł, czyli suma miesięcy styczeń–listopad;
  - rozliczona 4 118,30 zł; do rozliczenia 794,30 zł;
  - Ann*** 140,00 zł, prowizja 14,00 zł, status „naliczana po odbiorze”;
  - oferta 5 259,60 zł netto.
- **Limit Spółka B:** 10 850 zł + 1 168,00 zł = 12 018 zł, czyli 18,00 zł ponad limit 12 000 zł.
