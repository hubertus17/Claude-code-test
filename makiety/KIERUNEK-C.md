# Kierunek C – „Przepływ”

Zestaw A bez zmian. Zestaw B odrzucony. C to nowy kierunek przygotowany ze skillem **ui-ux-pro-max**. Ze skilla pochodzą:
- typografia (para „Startup Bold”: Outfit + Rubik),
- rekomendacja wykresu przepływu (Sankey – „ilości płynące między węzłami; jedno źródło, wiele celów”),
- reguły jakości: kontrast, jeden główny przycisk na ekran, kolor nie jako jedyny nośnik informacji, cyfry tabelaryczne.

Styl, który skill przypisuje kategorii (Claymorphism dla „weterynarii”, Brutalism dla „marketplace”), **świadomie pominąłem**: nie wynikał z tego, co ekrany mają pokazać.

## 1. Research – 10 niezależnych źródeł (2025–2026)

1. **Nielsen Norman Group** – State of UX 2026 (16.01.2026). https://www.nngroup.com/articles/state-of-ux-2026/
   Trend: UI przestaje wyróżniać produkt, bo komponenty są tanie i ustandaryzowane. Wygrywa „projektowanie głębiej” – logika, zachowanie i to, co produkt naprawdę robi. **Pasuje:** w [Marka] wyróżnikiem jest mechanizm (jedna płatność, podział na spółki), więc ekrany pokazują mechanizm, a nie ozdobę.
2. **Smashing Magazine** (Vitaly Friedman) – Design Patterns For AI Interfaces (07.2025). https://www.smashingmagazine.com/2025/07/design-patterns-ai-interfaces/
   Trend: odejście od czatu na rzecz interfejsów zadaniowych, w których wynik podaje się w strukturze (tabela, dashboard, wizualizacja), a nie jako tekst. **Pasuje jako inspiracja:** pokazujemy wynik i stan od razu, bez nowych funkcji AI.
3. **Baymard Institute** – Checkout UX 2026: 10 Pitfalls (akt. 03.11.2026). https://baymard.com/blog/current-state-of-checkout-ux
   Trend: 59% sklepów ma przeciętny lub gorszy checkout. Zalecenia: zwijać zakończone kroki do podsumowań, przyciski do zmiany ilości, wszystkie opcje dostawy w jednym miejscu. **Pasuje:** koszyk C ma przyciski ilości, jedną listę kosztów i podsumowanie w jednym pasku.
4. **Figma** – 2025 AI report: perspectives (24.04.2025). https://www.figma.com/blog/figma-2025-ai-report-perspectives/
   Trend: dobry projekt jest kluczowym wyróżnikiem na zatłoczonym rynku; zespoły pytają „ile wyjaśnić z tego, co dzieje się za kulisami” i projektują z człowiekiem w pętli. **Pasuje:** C pokazuje, co dzieje się za kulisami zamówienia (części, ERP, zwroty), a decyzje zostawia człowiekowi („Ponów”, „Akceptuj”).
5. **Linear** – UI refresh (12.03.2026). https://linear.app/changelog/2026-03-12-ui-refresh
   Trend: spokojniejszy, spójny interfejs; ściszona nawigacja, żeby treść główna była wyraźniejsza; łatwiejsze skanowanie. **Pasuje:** nawigacja w C to cicha pigułka u góry, a treść dostaje całą szerokość.
6. **Apple** – Liquid Glass, Newsroom (09.06.2025). https://www.apple.com/newsroom/2025/06/apple-introduces-a-delightful-and-elegant-new-software-design/
   Trend: „większe skupienie na treści”, a kontrolki unoszą się nad treścią. **Częściowo pasuje:** przejęliśmy kontrolki nad mapą (C4) i pływający pasek płatności (C2, C6). Efektu szkła nie przejęliśmy, bo w panelach B2B obniża czytelność.
7. **StudioMeyer** – Web Design Trends 2026: May Reality Check (08.05.2026). https://studiomeyer.io/en/blog/webdesign-trends-2026-reality-check
   Trend: utrzymały się bento grid, dark mode i design systemy. Kinetyczna typografia i glassmorphism okazały się „polerką”, a jako kontrruch rośnie anty-grid i brutalizm. **Pasuje częściowo:** z bento bierzemy moduły o różnej wielkości według ważności, ciemne pola tylko jako akcent; szkła i animowanych tekstów nie używamy.
8. **The Shape of AI** (Emily Campbell) – biblioteka wzorców UX dla AI. https://www.shapeof.ai/
   Trend: wzorce „identifiers” i „trust builders” – wyraźne oznaczanie źródła i stanu treści, żeby budować zaufanie. **Pasuje jako inspiracja wizualna:** każda część zamówienia nosi czytelny znacznik spółki i stanu („/2 Marka własna · brak towaru”), bez dodawania AI.
9. **Lyssna** – UX design trends (17.12.2025, ankieta 100 projektantów). https://www.lyssna.com/blog/ux-design-trends/
   Trend: AI się normalizuje, dostępność jest „niepodlegająca negocjacji”, dominują praktyczne potrzeby nad modą. **Pasuje:** kontrast i statusy z ikoną plus tekstem, a nie samym kolorem.
10. **Google Design** – Expressive Design: Google's UX Research / Material 3 Expressive (2025). https://design.google/library/expressive-material-design-google-research
    Trend: ekspresyjny kolor, kształt, rozmiar i wyróżniona typografia budują hierarchię. W 46 badaniach (18 000 osób) kluczowe elementy znajdowano do 4× szybciej. **Pasuje najmocniej:** jedna „liczba-odpowiedź” w dużym rozmiarze na każdym ekranie.

## 2. Trzy rozważane koncepcje

**C-1 „Nagłówek-odpowiedź” (redakcyjna).**
- Każdy ekran otwiera jedno zdanie lub liczba odpowiadająca na pytanie z pierwszych 3 sekund, w bardzo dużej, ekspresyjnej typografii. Reszta to moduły o różnej wielkości (bento) według ważności.
- Paleta: jasny, kamienny grunt, czerń jako kolor akcji, kolory spółek jako akcenty. Typografia Outfit + Rubik.
- Trendy: M3 Expressive (10), bento (7), NN/g – głębia zamiast ozdoby (1).
- Ryzyko: sama typografia nie pokazuje mechanizmu podziału, więc może zostać „ładnym nagłówkiem”.

**C-2 „Przepływ” (wizualizacja mechanizmu).**
- Ekrany rysują to, co dzieje się z pieniędzmi i paczkami: jedna płatność rozpływa się wstęgami do spółek (Sankey). Zamówienie to tory paczek na osi czasu, a oferta to trzy równoległe kolumny spółek z należnościami na dole każdej.
- Paleta i typografia jak w C-1.
- Trendy: Smashing – wynik w strukturze (2), Figma – pokazać, co dzieje się za kulisami (4), Shape of AI – znaczniki źródła i stanu (8), Baymard – podsumowania (3).
- Ryzyko: diagramy mogą przytłoczyć ekran sklepu, dlatego w B2C przepływ jest mały i pomocniczy.

**C-3 „Ciemne centrum dowodzenia”.**
- Ciemne panele z unoszącymi się, półprzezroczystymi paskami narzędzi; dla sklepu jasna wersja.
- Trendy: Apple Liquid Glass (6), Linear (5), dark mode (7).
- Ryzyko: dwa różne motywy rozbijają spójność 7 ekranów; szkło obniża czytelność tabel (StudioMeyer); ciemny sklep weterynaryjny jest dla klientki B2C zimny. To głównie zmiana kolorów, czyli błąd zestawu B.

**Wybór: C-2 „Przepływ”, z głównym mechanizmem C-1 (liczba-odpowiedź na górze ekranu).**
- Zarząd ma zobaczyć, jak platforma rozwiązuje problem „jeden koszyk, kilka spółek, osobne rozliczenia”. C-2 pokazuje ten mechanizm wprost na każdym ekranie, a nie opisuje go tabelą.
- Liczba-odpowiedź z C-1 załatwia test 3 sekund.
- C-3 odrzucam, bo zmienia głównie kolory.

## 3. System wizualny C

- **Nawigacja:** górna, w kształcie pigułek, zamiast granatowego paska bocznego. W panelach jest drugi rząd pigułek (pulpit) albo pigułki w pasku (handlowiec).
- **Grunt i powierzchnie:** jasny kamień #EEF0EB, białe moduły zaokrąglone 20 px, bez cieni (oprócz pasków na dole). Ciemne pola (#15171C) tylko tam, gdzie coś wymaga uwagi: „Wymaga reakcji teraz”, nowa placówka, wybrana lecznica.
- **Kolor akcji:** czerń (przyciski główne). Ostrzeżenia bursztynowe, błędy czerwone, informacje niebieskie – żadne nie jest kolorem przycisku.
- **Kolory spółek:** Spółka A morski #0E7C86, Spółka B malinowy #B0287A, Marka własna grupy fioletowy #6D3FD8. Są wyraźnie różne od siebie i od granatu marki #164472.
- **Logo:** [Marka] w oryginalnych kolorach.
- **Typografia:** Outfit (liczby-odpowiedzi do 84 px, nagłówki) + Rubik (treść). Cyfry tabelaryczne, cały tekst w zwykłej wielkości liter, bez WERSALIKÓW znanych z dzisiejszego example.com.

## 4. Ekrany – czym różnią się od A

- **C1 Pulpit:** pas „Wymaga reakcji teraz” idzie na samą górę, w poziomie, zamiast prawej kolumny powiadomień. Pod nim liczba-odpowiedź, a obok przepływ sprzedaży do trzech spółek: każda ma kwotę, udział, magazyn, status ERP i własny mini-wykres dzienny. Zamówienia pokazują części jako łańcuch, nie jako tagi w tabeli.
- **C2 Koszyk:** zamiast listy po lewej i podsumowania po prawej są wstęgi „jedna płatność → dwie paczki + jedna dostawa”, dwie paczki obok siebie i pasek płatności przez całą szerokość na dole.
- **C3 Zamówienie:** zamiast listy etykiet z menu po lewej jest zdanie-odpowiedź („Paczka 1 czeka w paczkomacie. Za paczkę 2 oddaliśmy pieniądze.”) i dwa tory paczek na osi czasu. Pod nimi trzy kolumny: produkty, brak towaru, dokumenty z płatnością. Menu konta to poziome zakładki.
- **C4 Rejestracja:** zamiast formularza z małą mapą w środku mapa zajmuje lewą połowę ekranu. Wyszukiwarka i lista z numerami 1–4 unoszą się nad mapą, a formularz z pionowymi krokami jest po prawej.
- **C5 Handlowiec – lecznice:** zamiast samej tabeli na górze jest ciemny baner nowej placówki z mapą regionu (Gniezno wyróżnione). Tabela ma obrót jako pasek.
- **C6 Handlowiec – oferta:** zamiast etykiet jedna pod drugą są trzy równoległe kolumny spółek. Każda ma swój limit u góry i swoje przeterminowane faktury na dole. Suma oferty i „Wyślij” są w pasku na dole.
- **C7 Strefa lecznicy:** zamiast trzech kafelków i oferty w prawej kolumnie jest wielka kwota prowizji, a pod nią oferta jako szeroki pas z trzema spółkami i „Akceptuj”. Wykres podpisuje prowizję nad każdym miesiącem. Limity są po lewej, transakcje po prawej.

## 5. Spójność danych (poprawki względem A6/A7)

- Prowizja naliczona od początku roku = **4 912,60 zł**, czyli dokładnie suma prowizji na wykresie styczeń–listopad.
  - Rozliczona: 4 118,30 zł (styczeń–wrzesień).
  - Do rozliczenia: **794,30 zł** (październik–listopad) – kwota wyraźnie różna od części Spółka B w ofercie (1 168,00 zł).
  - Te same trzy kwoty są w C6.
- „Transakcje z rekomendacji” to tylko klienci Pod Lipami, bez kwoty 342,50 zł. Ann*** ma 140,00 zł i 14,00 zł prowizji ze statusem **„naliczana po odbiorze”**.
- Obrót Pod Lipami w C5 to 49 126 zł, czyli 10 × naliczona prowizja.

## 6. Test nałożenia i porównanie z example.com

- Zrzuty A i C zostały nałożone z przezroczystością 50%. W pierwszej wersji C1 (powiadomienia w prawej kolumnie), C2 (prawy górny róg) i C7 (oferta w prawej kolumnie) miały główny blok tam gdzie A, więc zostały przebudowane. W wersji końcowej żaden główny blok nie leży w tym samym miejscu co w A.
- Porównanie z example.com:

| | example.com dziś | C |
|---|---|---|
| Kolor | granatowe paski | jasny kamień, czerń jako kolor akcji |
| Litery | WERSALIKI | zwykła wielkość liter |
| Kształty | prostokątne kafle | zaokrąglone moduły i pigułki |
| Kroje | Montserrat | Outfit + Rubik |
| Dane | listy i kafle | wizualizacje przepływu |

  Wspólne zostały tylko logo i nazwa.
