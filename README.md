# MarketingAgent — lekki system marketingowy dla Claude Code

MarketingAgent to operator marketingu (`@marketing`) dla solo-przedsiębiorcy. Mieszka w Twoim folderze i działa w Claude Code. Namierza, skąd realnie wezmą się klienci, dobiera jeden obszar, prowadzi produkcję treści i pilnuje wyniku. **Nic nie wychodzi w świat bez Twojego kliknięcia** — operator przygotowuje rzecz gotową do wysłania, decyzję podejmujesz Ty.

Operatorowi możesz w pierwszej rozmowie nadać własne imię.

## Czym różni się od typowych „agentów w promptcie"

- **Lekki tokenowo.** Rdzeń to krótka rozdzielnia; procedury wczytują się dopiero, gdy są potrzebne. Dane firmy czytane raz na sesję, nie przy każdej odpowiedzi.
- **Prawdziwie modułowy.** Ciężka praca (research, kanały) idzie do podagentów z własnym, izolowanym kontekstem.
- **Instalowany etapami.** Nie dostajesz od razu wielkiego narzędzia, w którym nie wiadomo, co robić. Zaczynasz od rdzenia (@głos + nauka firmy), a kolejne obszary dokładasz razem z kursem — jeden moduł, jeden plugin.
- **Prawdziwy agent.** Obszary potrafią podłączać narzędzia (np. Search Console, Google Ads) i czytać z nich dane. Działanie na zewnątrz (publikacja, wydatek) zawsze zostaje do Twojego kliknięcia.
- **Opiniotwórczy, nie encyklopedyczny.** Kanały ułożone w 5 obszarów wzrostu; prowadzimy 1–2 do skutku, nie rozmieniamy się na dziesiątki.
- **Natywny pod Claude Code.** Pluginy, skille, podagenci, komendy — bez zewnętrznych licencji i telemetrii. Wersjonowanie przez git.

## Instalacja (etapami)

MarketingAgent instaluje się jako pluginy z marketplace'u MarketingAgent — stopniowo, wraz z kursem.

**Krok 1 — w terminalu** (zwykła powłoka systemu, np. Terminal na Macu — NIE okno Claude Code):

```bash
claude plugin marketplace add <repo-lub-ścieżka-magent>
```
```bash
claude plugin install magent-rdzen@magent
```

**Krok 2 — w oknie Claude Code** (tam, gdzie piszesz do asystenta):

```
/magent-setup
```
Stawia czystą instancję (`dane/`, `system/`, `CLAUDE.md`). Przeładuj Claude Code, a potem:

```
/start
```
MarketingAgent sprawdza stan i podpowiada pierwszy ruch (możesz też od razu `/nauka-firmy`).

Kolejne moduły kursu dokładają obszary tak samo: w **terminalu** `claude plugin install magent-tresci@magent`, potem w **Claude Code** `/tresci-start`.

> **Terminal vs Claude Code:** `claude plugin …` to polecenia **terminala**; `/magent-setup`, `/start`, `/tresci-start` to komendy w **oknie Claude Code**. Interaktywny `/plugin` w części środowisk nie działa — dlatego instalujemy z terminala.
>
> **Aktualizacje:** zainstalowany plugin jest zamrożony przy instalacji. Nowszą wersję pobierzesz przez `claude plugin update magent-rdzen@magent` (i restart Claude Code).

Wymaga tylko Claude Code. Rdzeń działa w trybie „przygotuj do kliknięcia" (bez kluczy); obszary opcjonalnie podłączają narzędzia.

## Dwa tryby (żeby się nie zgubić)

MarketingAgent działa w dwóch wyraźnych trybach — ta sama asystentura, inne zadanie:
- **Rozbudowa** — budujemy i stroimy narzędzie: nauka firmy, rozwój głosu, dokładanie obszarów, uzupełnianie plików. Prowadzi za rękę, krok po kroku.
- **Praca** — działamy tym, co już mamy: treści, analiza, rozwiązywanie problemów, pomiar.

Nie wiesz, od czego zacząć? Wpisz **`/start`** — MarketingAgent przypomni, na czym stanęliście, pokaże Twój **streak** (dni z rzędu z narzędziem) i rangę, i podpowie najlepszy następny ruch. Konsekwencja jest tu nagradzana, bo w marketingu rozpęd łatwiej utrzymać niż odbudować.

## Jak używać

| Komenda | Co robi |
|---|---|
| `/start` | Front door — gdzie jesteś i co najlepiej teraz zrobić |
| `/rozbudowa` | Tryb rozbudowy — dołóż/skonfiguruj (firma, głos, obszary) |
| `/praca` | Tryb pracy — działaj tym, co masz |
| `@marketing` | Operator (praca) — namierza, skąd klienci, dobiera ruch |
| `@głos` | Ubiera gotowy tekst w Twój ton |
| `/sesja` | Sesja robocza: brief → praca → podsumowanie |
| `/stan` | Gdzie jest firma i jaki jest najlepszy ruch |
| `/ruch` | Jeden najlepszy następny ruch (dla zabieganych) |
| `/audyt` | Gdzie firma przepala budżet |
| `/korekta` | Utrwal zasadę — „od teraz rób X" (agent uczy się raz, na stałe) |

Można też pisać po ludzku — np. „potrzebuję 30 zapisów na newsletter w miesiąc".

## Co wypełniasz Ty

Tylko folder `dane/` (profil, persona, oferta, dane marketingowe, styl). Reszta (`system/`, `outputs/`) prowadzi się sama w trakcie pracy. Zacznij od `@marketing`.

## Struktura

```
CLAUDE.md                       rozdzielnia (cienka, zawsze wczytana)
.claude-plugin/marketplace.json spis pluginów MarketingAgent
plugins/magent-rdzen/              rdzeń: skill marketing (operator + moduły), glos, komendy, zwiadowca
plugins/magent-tresci/         obszar Treści (podagent + komenda + połączenia)
plugins/magent-*/                  kolejne obszary — dokładane w kursie
dane/                           Twoje dane (wypełniasz przez /nauka-firmy)
system/                         stan: tożsamość, zainstalowane/aktywne obszary, pomiar, roadmap
outputs/                        wyniki per kanał
```

Dane (`dane/`, `system/`, `outputs/`) są Twoje i mieszkają w Twoim katalogu — pluginy ich nie dotykają przy instalacji/aktualizacji.

## Pętla pracy

**Namierz → Zrób → Zmierz.** Operator ustala, skąd wezmą się klienci, produkuje przez właściwy kanał i domyka pomiarem. Bez pomiaru marketing to koszt, nie inwestycja.

Wersja: 0.5.0 (model pluginowy, 5 obszarów, dwa tryby + strategia).
