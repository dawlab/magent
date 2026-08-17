---
description: Aktualizuje MarketingAgent i wszystkie zainstalowane obszary naraz do najnowszej wersji. Po zakończeniu uruchom Claude Code ponownie.
---

# Aktualizacja MarketingAgent (`/aktualizuj`)

Aktualizujesz rdzeń i **wszystkie zainstalowane obszary** jednym poleceniem, żeby właściciel nie musiał wpisywać ich po kolei. Pod spodem to natywne `claude plugin update` — nic więcej. Danych właściciela (`dane/`, `system/`, `outputs/`) to nie rusza.

## Kroki

1. Odśwież katalog i zaktualizuj każdą zainstalowaną wtyczkę `@magent`. Uruchom:
   ```bash
   claude plugin marketplace update magent
   claude plugin list | grep -oE '[a-z0-9-]+@magent' | sort -u | while read -r p; do
     echo "== aktualizuję $p =="
     claude plugin update "$p"
   done
   ```
2. Zbierz wynik każdej komendy. Jeśli któraś zwróci błąd (brak sieci, konflikt, brak `claude` w tym środowisku) — **nie udawaj sukcesu**: pokaż błąd właścicielowi i co z tym zrobić (np. „sprawdź połączenie i wpisz `/aktualizuj` ponownie"). Zero zmyślania, że coś się zaktualizowało.
3. Podsumuj krótko, które wtyczki i do jakiej wersji (z `claude plugin list`).
4. Powiedz wprost: **uruchom Claude Code ponownie**, żeby nowe wersje się załadowały. Po restarcie `/start` pokaże „co nowego".

## Granice
- Jedyne, co ta komenda robi, to natywna aktualizacja zainstalowanych wtyczek. Bez serwera, bez licencji, bez ruszania danych klienta.
- Jeśli `claude` nie jest dostępne w tym środowisku (część konfiguracji), podaj właścicielowi komendy do ręcznego wpisania w oknie Claude Code: `/plugin marketplace update magent`, potem `/plugin update magent@magent` i to samo dla każdego dodanego obszaru.
