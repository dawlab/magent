# Wydawanie i rozwój MarketingAgenta

Dokument dla autora produktu. Instrukcja dla użytkownika: [README.md](README.md).

## Struktura repozytorium

```
.claude-plugin/marketplace.json   katalog źródłowy (ścieżki względne, do pracy lokalnej)
plugins/magent-rdzen/             rdzeń: operator, głos, przewodnik, komendy, starter
plugins/magent-*/                 obszary: tresci, opinie, sprzedaz, polecenia, reklama, social
docs/                             katalog dystrybucyjny (GitHub Pages)
  marketplace.json                  katalog dla klientów, źródła typu archive
  paczki/*.zip                       spakowane wtyczki
publikuj.py                       generuje docs/ z plugins/
CLAUDE.md                         rozdzielnia: routing i twarde zasady
README.md                         instrukcja obsługi dla użytkownika
```

Katalogi `dane/`, `system/`, `outputs/` w katalogu głównym to instancja deweloperska. Są wykluczone z repozytorium przez `.gitignore` — źródłem prawdy dla czystej instalacji jest `plugins/magent-rdzen/starter/`.

## Jak działa dystrybucja

Klient nie klonuje repozytorium. Instaluje z adresu, który serwuje katalog:

```
https://dawlab.github.io/magent/marketplace.json
```

Katalog wskazuje wtyczki jako archiwa `.zip` pobierane przez HTTPS (typ źródła `archive`). Dzięki temu instalacja nie wymaga gita, npm ani konta GitHub — wystarczy Claude Code w wersji **2.1.224 lub nowszej**.

GitHub Pages serwuje katalog `docs/` z gałęzi `main`. Każdy `git push` aktualizuje to, co widzą klienci.

## Lista kontrolna wydania

1. **Zmiany w kodzie** — edytuj pliki w `plugins/`.
2. **Podnieś numer wersji** w obu miejscach dla każdej zmienionej wtyczki:
   - `plugins/magent-X/.claude-plugin/plugin.json` → pole `version`
   - `.claude-plugin/marketplace.json` → pole `version` przy tej wtyczce
3. **Zaktualizuj README.md**, jeśli zmiana dotyczy czegoś, co widzi użytkownik: nowa komenda, nowy obszar, zmiana instalacji.
4. **Zbuduj paczki**:
   ```bash
   python3 publikuj.py
   ```
5. **Wyślij**:
   ```bash
   git add -A && git commit -m "wydanie 0.2.0" && git push
   ```
6. **Powiadom klientów** — mailem albo w kursie. Aktualizacja nie instaluje się sama; klient wpisuje `/plugin marketplace update magent`, potem `/plugin update magent-rdzen@magent` i uruchamia Claude Code ponownie.

### Pułapka: numer wersji jest sygnałem aktualizacji

Jeśli zmienisz zawartość wtyczki, ale nie podniesiesz numeru wersji, klienci zostaną przy dotychczasowej paczce mimo nowego pliku na serwerze. Numer wersji musi rosnąć przy każdym wydaniu, które ma do nich dotrzeć.

## Praca lokalna

Do testowania zmian bez wydawania używaj katalogu źródłowego:

```bash
claude plugin marketplace add /Volumes/Dysk/Projekty/Osobiste/ag1
```

Marketplace nosi wtedy tę samą nazwę `magent`, co wersja dystrybucyjna — nie rejestruj obu naraz na jednym koncie, bo nazwy się zduplikują. Pełny test instalacji od zera wykonuj na osobnym koncie albo w osobnym środowisku, tak jak zrobi to klient.

## Dodanie nowego obszaru

1. `plugins/magent-X/` z podkatalogami `.claude-plugin/`, `agents/`, `commands/`.
2. Podagent `agents/obszar-X.md` — sekcja „Tryby pracy (narzędzie)" i bramka jakości.
3. `.claude-plugin/plugin.json` — nazwa, wersja, opis, informacja o zależności od `magent-rdzen`.
4. `commands/X-start.md` — wyjaśnia obszar, dopisuje wpis do `system/obszary-zainstalowane.md`, pyta o narzędzie, proponuje pierwszy ruch.
5. Jeśli obszar ma narzędzie: `POLACZENIA.md` i `connectors.example.json`.
6. Wpis w `.claude-plugin/marketplace.json`.
7. Uzupełnij README.md: tabela obszarów i zalecana kolejność.
8. Sprawdź, że podagent czyta wyłącznie ścieżki danych klienta (`dane/`, `system/`, `outputs/`).

## Zasady konstrukcyjne

**Kod osobno, dane osobno.** Wtyczki zawierają zdolności. Dane klienta żyją w jego katalogu roboczym i nie są dotykane przy instalacji ani aktualizacji.

**Routing sterowany manifestem.** Operator nie ma zaszytej listy obszarów — czyta `system/obszary-zainstalowane.md` i oferuje wyłącznie to, co realnie zainstalowane.

**Trwałe korekty idą do danych, nie do kodu.** Zasady właściciela zapisujemy w `system/korekty.md` i `dane/glos_styl.md`. Moduły wtyczek są nadpisywane przy aktualizacji.
