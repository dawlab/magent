# Połączenia — obszar Sprzedaż

Dwa tryby. Domyślny (bez API) jest w pełni funkcjonalny; konektor mailingowy to krok roadmapy.

## Tryb bez API (domyślny, obecny)
Obszar oddaje gotowy tekst do wklejenia: lead magnet, copy landingu i formularza, sekwencje maili, newsletter, DM. Formularz, zapis kontaktów i wysyłkę robi właściciel w swoim narzędziu. To pełnoprawny tryb pracy — z niego startuje każdy klient.

## Tryb z narzędziem mailingowym (roadmap)
Po podłączeniu konektora (np. MailerLite / inne narzędzie mailingowe) obszar będzie mógł:
- **czytać** listę i statystyki (zapisy, otwarcia, kliknięcia, wypisy) i pod nie projektować sekwencje oraz segmenty,
- przygotować kampanię gotową do wysłania.

### Zakres uprawnień: odczyt swobodnie, wysyłka zawsze gated
Odczyt listy i statystyk — w porządku. **Każda wysyłka (newsletter, sekwencja, pojedynczy mail) zostaje za kliknięciem właściciela**, przez kolejkę decyzji. To twarda zasada MarketingAgent: przygotowanie treści swobodnie, działanie na zewnątrz — nigdy samodzielnie. Zapis cudzych kontaktów i zgody marketingowe (RODO) pilnuje właściciel.

### Jak podłączyć (gdy konektor będzie dostępny)
1. Dodaj konektor swojego narzędzia mailingowego w kliencie.
2. Autoryzuj zakres odczytu listy/statystyk (bez uprawnień do samodzielnej wysyłki, jeśli narzędzie to rozróżnia).
3. Wróć do MarketingAgent, powiedz operatorowi „podłączyłem mailing" — zaktualizuje status w `system/obszary-zainstalowane.md`.

### Techniczne
Gdy jest konkretny serwer MCP do narzędzia mailingowego, deklaracja trafia do `.mcp.json` w katalogu tego pluginu. Wzorzec: `connectors.example.json`. Do tego czasu obszar działa w trybie bez API — nic się nie psuje.
