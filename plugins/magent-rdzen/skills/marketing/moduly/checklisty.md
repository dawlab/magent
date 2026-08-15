# Moduł: CHECKLISTY / AUDYTY (odpalane na realnych danych)

Trzy checklisty, które agent **przechodzi po Twoim realnym materiale** (strona, treść, oferta) — nie oddaje promptu do wklejenia. Zawsze ta sama zasada wyniku: **3–5 priorytetów wg wpływu, nie audyt na 40 uwag.** Największa dźwignia najpierw, z konkretnym „co zmienić".

Wywołanie: komenda `/checklista [strona|publikacja|oferta]`. Operator dobiera właściwą i prosi o to, czego brakuje (URL, treść, tekst oferty).

---

## 1. AUDYT STRONY / PROFILU (SEO + AEO + konwersja)

Wejście: URL strony albo wizytówka Google. Jeśli to strona — pobierz jej treść (WebFetch/odczyt). Jeśli podłączone: **Microsoft Clarity** (gdzie ludzie porzucają — nagrania/heatmapy) i **Search Console** (realne frazy) — oprzyj wnioski na nich, nie na przeczuciu. Braku narzędzia nie zmyślaj — powiedz, że bez niego oceniasz z samej treści.

Przechodzę po wymiarach (zaznaczam ✓/✗ i dlaczego):
- **Powyżej zgięcia**: czy w 3 sekundy widać „komu i w czym pomagasz" (nie stanowisko, nie ogólnik). Jeden jasny przekaz, nie pięć.
- **Jedno wezwanie**: jest widoczne, niskolękowe (mały pierwszy krok, nie „wycena" na zimno)? Jedno, nie pięć.
- **Dowód**: opinie, liczby, case, twarz człowieka — czy jest i czy blisko decyzji.
- **AEO (żeby cytowały modele AI)**: struktura H1→H2→H3, nagłówki jako pytania klienta, atomowe akapity (kluczowa rzecz w 1. zdaniu), sekcja **FAQ** (i FAQ schema), tabele/listy/definicje.
- **SEO podstawy**: title i opis, fraza o realnej intencji w tytule, szybkość ładowania, wersja mobilna.
- **Lokalni** (jeśli firma lokalna): Google Business Profile kompletny (kategoria, obszar, godziny, zdjęcia, świeże opinie), **Bing Places** (ChatGPT korzysta z Bing), spójność nazwa/adres/telefon w sieci.
- **Konwersja / tarcie**: długość formularzy, liczba kroków, czy zdjęte jest ryzyko (gwarancja, „bez zobowiązań"). Jeśli jest Clarity — wskaż realny punkt porzucenia.

Wynik: **3–5 poprawek priorytetowo** (wpływ × łatwość), każda z konkretem „zmień X na Y". Nie recytuj całej listy — pokaż, co ruszyć najpierw.

---

## 2. CHECKLISTA PRZED PUBLIKACJĄ (pre-flight)

Wejście: konkretna treść przed wrzuceniem w świat (post, mail, wideo-skrypt, grafika). To szybka bramka **zanim** rzecz trafi do kolejki decyzji — spójna z `moduly/jakosc.md` (ostateczną bramkę jakości trzyma operator; tu jest lista kontrolna do przejścia).

- **Jeden temat, jeden hook** w 1. linii / pierwszych 3 s. Bez „W dzisiejszych czasach…".
- **Jeden przekaz** (obietnica + dowód + jedno wezwanie) — nie pięć myśli naraz.
- **Jedno wezwanie**, konkretne, dopasowane do etapu odbiorcy.
- **Dowód nie zmyślony** — liczby/wyniki tylko z plików albo z narzędzi. Brak → „nie mam tej informacji", nie wymyślaj.
- **Format natywny** dla kanału (playbook w `obszar-tresci`/`obszar-social`), oszczędne formatowanie, zero maniery AI.
- **Alt-text** (jeśli grafika) i **link we właściwym miejscu** (na wielu kanałach: pierwszy komentarz, nie treść).
- **Ton** przeszedł przez `glos` (tekst do ludzi).
- **Zasady domu** z `system/korekty.md` zastosowane.

Wynik: ✓ gotowe do kolejki, albo lista konkretnych poprawek. **Publikacji nie wykonujesz** — rzecz idzie do kolejki decyzji, właściciel klika.

---

## 3. AUDYT OFERTY / SEKWENCJI EMAIL (konwersja)

Wejście: tekst strony oferty **albo** sekwencja maili (powitalna). Oceniam pod kątem „czy to zamienia zainteresowanego w klienta".

**Oferta / landing:**
- **Propozycja wartości**: dla kogo + jaki konkretny efekt (nie „kompleksowe usługi").
- **Zdjęcie ryzyka**: gwarancja, mały pierwszy krok, „bez zobowiązań".
- **Dowód** blisko wezwania (opinie, case, liczby).
- **Jedno CTA**, jeden pierwszy krok — nie menu wyborów.
- **Cena/pakiety** czytelne (jeśli są); jeśli świadomie ukryte — czy jest jasny powód kontaktu.
- **Powód „teraz"** — czemu nie odkładać.

**Sekwencja powitalna (email):**
- **Mail 1**: powitanie + natychmiastowe dostarczenie obietnicy lead magneta.
- **Środek (2–4)**: budowanie zaufania → wartość, historia klienta, zdjęcie obiekcji — jeden cel na mail, jedno CTA.
- **Domknięcie**: jasna oferta z jednym wezwaniem.
- **Segmentacja**: inny przekaz dla nowych vs klientów.
- Wysyłka: statystyki czytam swobodnie, **wysyłka zawsze przez kolejkę decyzji**.

Wynik: **3–5 rzeczy do dodania/wycięcia** priorytetowo, z konkretem. Materiał do ludzi → po ton do `glos`.

---

## Granica wspólna
Audyty czytają i oceniają — **nic nie publikują, nie wysyłają, nie wdrażają**. Poprawki idą jako rekomendacje; wdrożenie (zmiana strony, wysyłka, publikacja) zawsze po stronie właściciela / przez kolejkę decyzji. Zero zmyślania: jeśli brak narzędzia albo danych, nazwij to, nie zgaduj wyniku.
