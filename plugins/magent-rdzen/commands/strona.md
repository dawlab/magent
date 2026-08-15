---
description: Generuje stronę-wizytówkę (one-pager) w stylu Twojej marki i prowadzi przez darmowy deploy. Generacja swobodnie; publikacja/deploy zawsze po Twojej stronie.
argument-hint: "[cel strony, np. lead magnet / kontakt / oferta]"
---

# Generator strony (`/strona`) — one-pager w stylu marki

Budujesz właścicielowi prostą, konwertującą stronę-wizytówkę jako **samodzielny plik HTML** (jak grafiki w Social — darmowo, bez kreatora) i prowadzisz przez darmowy hosting. To capability, którego goły czat nie daje: realna, gotowa do wystawienia strona.

## 0. Najpierw uczciwe pytanie: czy strona jest teraz potrzebna?
Jeśli `dane/profil.md` wskazuje firmę **lokalno-usługową** — często ważniejszy jest kompletny **Google Business Profile** niż strona. Powiedz to wprost i zaproponuj GBP jako pierwszy krok (obszar Opinie / `/narzedzia`), zanim zbudujesz stronę. Nie wpychaj strony na siłę.

## 1. Zbierz materiał (raz)
`dane/profil.md` (branża, dla kogo), `dane/persona.md` (język, problem), `dane/oferta.md` (co sprzedajesz, pierwszy krok), `dane/marka_wizualna.md` (paleta, fonty, ton — jeśli jest; brak → neutralny czytelny styl, nie zmyślaj kolorów), `outputs/opinie/` (dowód, jeśli jest). Ustal **cel strony** (`$ARGUMENTS`): zapis na lead magnet / kontakt / prezentacja oferty.

## 2. Zbuduj one-pager (sekcje, które konwertują i które cytują modele AI)
Jeden plik HTML, responsywny, w stylu marki:
- **Hero**: nagłówek „komu i w czym pomagasz" (nie stanowisko) + jedno wezwanie (niskolękowy pierwszy krok).
- **Dowód**: opinie / liczby / logo klientów / twarz — blisko wezwania.
- **Co robisz / dla kogo**: konkret, nie ogólniki; jeden pierwszy krok.
- **FAQ** (realne pytania klienta) — dołóż **FAQ schema** (JSON-LD), bo modele AI z niej wyciągają.
- **Kontakt / CTA** powtórzone na dole.
- Podstawy SEO/AEO: sensowny `<title>` i opis, nagłówki H1→H2, tekst atomowy (kluczowa rzecz w 1. zdaniu), mobilnie czytelne.
Tekst do ludzi → przepuść przez `glos` po ton właściciela.

## 3. Zapisz
`outputs/strona/[data]-[cel]/index.html` + krótkie `README.md` (co to, jak wystawić). Wpis w `outputs/strona/INDEX.md`.

## 4. Poprowadź przez darmowy deploy (deploy = właściciel)
- **Cloudflare Pages** (darmowe): utwórz projekt → wgraj `index.html` (drag&drop w panelu albo z repo) → dostajesz adres `*.pages.dev`, potem podłączasz własną domenę. Krok po kroku, ale **wgranie/publikację robi właściciel** (jego konto, jego domena).
- **Carrd** (alternatywa dla nietechnicznych): tani, najprostszy — mogę oddać treść i układ do przeklejenia.
- Granica: **wygenerowanie strony — swobodnie; publikacja/deploy — zawsze po stronie właściciela.** Nic nie wystawiam sam.

## 5. Jeden następny krok
Po wystawieniu zaproponuj `/checklista strona` (audyt SEO+AEO+konwersja) i podpięcie **Microsoft Clarity**, żeby zobaczyć, gdzie ludzie się gubią.

## Granice
Generujesz i doradzasz; **nie publikujesz, nie kupujesz domeny, nie zmieniasz ustawień konta**. Zero zmyślania danych (opinie, liczby tylko z plików).
