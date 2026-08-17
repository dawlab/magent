---
description: Stawia czystą instancję MarketingAgent w bieżącym folderze (pliki dane/system/outputs + CLAUDE.md). Opcjonalnie resetuje do stanu fabrycznego.
argument-hint: "[reset]"
---

# Rozstawienie MarketingAgent (bootstrap instancji)

Twoim zadaniem jest postawić czystą, działającą instancję MarketingAgent w **bieżącym katalogu roboczym** na podstawie szablonów startowych z rdzenia. Szablony leżą w `"$CLAUDE_PLUGIN_ROOT/starter"` (pliki: `CLAUDE.md`, `dane/`, `system/`, `outputs/`).

Argument: `$ARGUMENTS` (pusty = tryb instalacji; `reset` = przywrócenie stanu fabrycznego).

## Tryb domyślny (bez argumentu) — instalacja nieniszcząca

Dokładasz tylko to, czego brakuje. **Niczego nie nadpisujesz.**

1. Dla każdego pliku ze `starter/` sprawdź, czy istnieje już w bieżącym folderze (ta sama ścieżka względna).
2. Skopiuj tylko brakujące. Istniejące zostaw nietknięte — mogą zawierać dane właściciela.
3. Zrób to np. tak (kopiuje bez podmiany istniejących):
   ```bash
   cd "$CLAUDE_PLUGIN_ROOT/starter" && find . -type f | while read f; do
     dest="./${f#./}"
     if [ ! -e "$OLDPWD/$dest" ]; then mkdir -p "$OLDPWD/$(dirname "$dest")"; cp "$f" "$OLDPWD/$dest"; fi
   done
   ```
   (Uruchamiaj z katalogu roboczego klienta; `$OLDPWD` to ten katalog.)
4. Podsumuj: co utworzono, co pominięto (bo już było).
5. Powiedz właścicielowi: **przeładuj Claude Code**, żeby wczytał się `CLAUDE.md` (router), a potem zacznij od `/start` albo `/nauka-firmy`.

## Tryb `reset` — przywrócenie stanu fabrycznego (destrukcyjne)

Używane, gdy właściciel chce wyczyścić instancję do stanu jak po zakupie (albo Ty czyścisz instancję dev).

1. **Najpierw ostrzeż i poczekaj na wyraźne „tak".** To skasuje dane firmy i wygenerowane materiały w tym folderze.
2. **Zrób kopię zapasową** obecnych `dane/`, `system/`, `outputs/`, `CLAUDE.md` do `./_backup-magent-[data-godzina]/` (albo poza projekt, jeśli tak wolisz) — zanim cokolwiek nadpiszesz.
3. Nadpisz z `starter/` pliki instancji klienta: `CLAUDE.md`, `dane/*`, `system/*` (tylko te ze startera: tozsamosc, aktywne-obszary, obszary-zainstalowane, dziennik, pomiar), `outputs/*/INDEX.md`. **Usuń** wygenerowane materiały w `outputs/` (pliki datowane), zostawiając same INDEX-y.
4. **Nie ruszaj** plików, których nie ma w starterze, jeśli należą do warsztatu (np. `system/changelog.md`, `system/roadmap.md`) — chyba że właściciel wprost prosi.
5. Podsumuj, co przywrócono i gdzie leży kopia zapasowa. Przypomnij o przeładowaniu.

## Granice
- Nie nadpisuj danych właściciela bez trybu `reset` i wyraźnej zgody.
- Nie ruszaj katalogu `plugins/` ani `.claude-plugin/` — to produkt, nie instancja.
- Zero zmyślania: jeśli `"$CLAUDE_PLUGIN_ROOT/starter"` jest niedostępny, powiedz to wprost, nie twórz plików „z głowy".
