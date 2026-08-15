# MarketingAgent — system marketingowy dla Claude Code

MarketingAgent prowadzi marketing jednoosobowej firmy. Ustala, skąd realnie wezmą się klienci, przygotowuje treści w Twoim stylu, buduje stronę, podłącza narzędzia i pilnuje wyników.

**Nic nie trafia do odbiorców bez Twojej decyzji** — agent przygotowuje materiał gotowy do wysłania, akceptujesz Ty.

Pełna instrukcja: [INSTRUKCJA-OBSLUGI.md](INSTRUKCJA-OBSLUGI.md)

## Instalacja

Wszystko wpisujesz w oknie Claude Code, otwartym w folderze Twojej firmy. Nie potrzebujesz gita, konta GitHub ani Terminala — wtyczki pobierają się jako archiwa przez HTTPS.

```
/plugin marketplace add https://dawlab.github.io/magent/marketplace.json
```
```
/plugin install magent-rdzen@magent
```
```
/magent-setup
```

`/magent-setup` tworzy strukturę plików na dane firmy. Następnie uruchom Claude Code ponownie i wpisz `/nauka-firmy`, żeby agent poznał Twoją firmę. Od tego momentu `/start` w każdej chwili podpowie następny krok.

Kolejne obszary dokładasz tak samo: `/plugin install magent-tresci@magent`, potem `/tresci-start`.

> Te same polecenia działają w Terminalu — dopisz na początku `claude` i pomiń ukośnik: `claude plugin marketplace add https://dawlab.github.io/magent/marketplace.json`.

**Aktualizacje:** `/plugin marketplace update magent`, potem `/plugin update magent-rdzen@magent` (oraz zainstalowane obszary) i ponowne uruchomienie Claude Code. Dane firmy pozostają nietknięte.

**Wymagania:** Claude Code w wersji 2.1.224 lub nowszej (starsze wersje nie obsługują wtyczek dystrybuowanych jako archiwa).

## Instalacja etapami

Agent nie przychodzi w całości. Zaczynasz od rdzenia, a obszary dokładasz stopniowo — jeden moduł kursu, jeden obszar. Dzięki temu w każdym momencie wiadomo, co jest do zrobienia.

| Obszar | Instalacja | Włączenie | Zakres |
|---|---|---|---|
| Rdzeń | `magent-rdzen` | `/magent-setup` | Operator marketingu, Twój styl wypowiedzi, planowanie, strona, audyty |
| Treści | `magent-tresci` | `/tresci-start` | Posty, scenariusze wideo, plan treści, teksty pod wyszukiwarki i modele AI |
| Opinie | `magent-opinie` | `/opinie-start` | Zbieranie opinii i przerabianie ich na materiał sprzedażowy |
| Sprzedaż | `magent-sprzedaz` | `/sprzedaz-start` | Materiał w zamian za kontakt, strona zapisu, sekwencje maili |
| Polecenia | `magent-polecenia` | `/polecenia-start` | System poleceń i współpraca z innymi firmami |
| Social media | `magent-social` | `/social-start` | Kompletny post z grafiką, publikacja po akceptacji |
| Reklama płatna | `magent-reklama` | `/reklama-start` | Teksty reklam, plan budżetu testowego |

## Komendy

| Komenda | Działanie |
|---|---|
| `/start` | Podsumowanie sytuacji i propozycja następnego kroku |
| `/rozbudowa` | Konfigurowanie: firma, styl, obszary, narzędzia |
| `/praca` | Praca tym, co już skonfigurowane |
| `/stan` | Stan marketingu i najlepszy ruch w tym momencie |
| `/ruch` | Sam następny krok, bez omówienia |
| `/strategia` | Co sprzedawać, do kogo kierować ofertę, czego zaniechać |
| `/sesja` | Prowadzenie przez jedną porcję pracy od briefu do podsumowania |
| `/audyt` | Gdzie marketing pochłania pieniądze bez efektu |
| `/narzedzia` | Rekomendacja i konfiguracja jednego narzędzia |
| `/strona` | Strona-wizytówka w kolorystyce Twojej marki |
| `/checklista` | Ocena strony, oferty lub treści — 3–5 poprawek |
| `/korekta` | Trwała zasada, według której agent ma dalej pracować |

Do tego dwa wywołania kierujące zadanie do konkretnego pomocnika: `@marketing` (planowanie i produkcja) oraz `@głos` (nadanie tekstowi Twojego tonu). Możesz też pisać zwykłymi zdaniami — „potrzebuję 30 zapisów na newsletter w miesiąc".

## Zasady działania

- **Decyzje należą do Ciebie.** Publikacja, wysyłka i wydatki wymagają akceptacji za każdym razem.
- **Odczyt danych bez pytania, działanie za zgodą.** Agent sprawdzi statystyki samodzielnie; opublikować czy wysłać — nie.
- **Bez zmyślania.** Nieznanej liczby agent nie zastąpi przybliżeniem, tylko powie, że jej nie ma.
- **Jeden lub dwa kanały prowadzone konsekwentnie**, zamiast wszystkich naraz.
- **Bez zewnętrznych licencji i telemetrii.** Wymaga wyłącznie Claude Code; narzędzia zewnętrzne są opcjonalne.

## Twoje dane

Wiedza o firmie i gotowe materiały zostają w Twoim folderze:

```
dane/      profil firmy, odbiorcy, oferta, Twój styl wypowiedzi
system/    stan bieżący, Twoje zasady, historia pracy
outputs/   gotowe materiały: posty, strony, analizy
```

Instalacja i aktualizacje pluginów nie dotykają tych plików. Przy kilku firmach prowadź osobny folder dla każdej.

## Struktura repozytorium

```
.claude-plugin/marketplace.json   spis pluginów (źródło, instalacja lokalna)
plugins/magent-rdzen/             rdzeń: operator, styl, komendy, szablony startowe
plugins/magent-*/                 obszary dokładane w kursie
docs/                             katalog dystrybucyjny (GitHub Pages): marketplace.json + paczki zip
publikuj.py                       wydanie nowej wersji: pakuje wtyczki i generuje docs/
CLAUDE.md                         rozdzielnia: routing i zasady
INSTRUKCJA-OBSLUGI.md             pełna instrukcja dla użytkownika
```

**Wydanie nowej wersji:** podnieś numer w `plugin.json` i `.claude-plugin/marketplace.json`, uruchom `python3 publikuj.py`, następnie `git add -A && git commit && git push`. Numer wersji jest sygnałem aktualizacji dla klientów — bez jego podniesienia zostaną przy dotychczasowej paczce.

Wersja 0.1.0.
