# MarketingAgent — system marketingowy dla Claude Code

MarketingAgent prowadzi marketing jednoosobowej firmy. Ustala, skąd realnie wezmą się klienci, przygotowuje treści w Twoim stylu, buduje stronę, podłącza narzędzia i pilnuje wyników.

**Nic nie trafia do odbiorców bez Twojej decyzji** — agent przygotowuje materiał gotowy do wysłania, akceptujesz Ty.

Pełna instrukcja: [INSTRUKCJA-OBSLUGI.md](INSTRUKCJA-OBSLUGI.md)

## Instalacja

**Krok 1 — w terminalu** (zwykła powłoka systemu: „Terminal" na macOS, „PowerShell" na Windowsie — nie okno Claude Code):

```bash
claude plugin marketplace add dawlab/magent
```
```bash
claude plugin install magent-rdzen@magent
```

**Krok 2 — w oknie Claude Code**, otwartym w folderze Twojej firmy:

```
/magent-setup
```

Tworzy strukturę plików na dane firmy. Następnie uruchom Claude Code ponownie i wpisz:

```
/nauka-firmy
```

Agent pozna Twoją firmę i zapisze jej profil. Od tego momentu możesz pracować — a `/start` w każdej chwili podpowie następny krok.

Kolejne obszary dokładasz tak samo: w terminalu `claude plugin install magent-tresci@magent`, potem w Claude Code `/tresci-start`.

> `claude plugin …` to polecenia terminala. `/magent-setup`, `/start`, `/tresci-start` to komendy wpisywane w oknie Claude Code.

**Aktualizacje:** `claude plugin marketplace update magent`, potem `claude plugin update magent-rdzen@magent` (oraz zainstalowane obszary) i ponowne uruchomienie Claude Code. Dane firmy pozostają nietknięte.

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
.claude-plugin/marketplace.json   spis pluginów
plugins/magent-rdzen/             rdzeń: operator, styl, komendy, szablony startowe
plugins/magent-*/                 obszary dokładane w kursie
CLAUDE.md                         rozdzielnia: routing i zasady
INSTRUKCJA-OBSLUGI.md             pełna instrukcja dla użytkownika
```

Wersja 0.1.0.
