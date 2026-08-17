# Połączenia — obszar Treści

Ten obszar działa w **dwóch trybach**. Tryb bez narzędzia jest domyślny i zawsze dostępny — narzędzie tylko go wzmacnia, nie jest warunkiem pracy.

## Tryb bez narzędzia (domyślny)
Obszar produkuje treść i strukturę na podstawie `dane/` (persona, oferta, profil) i researchu podagenta `zwiadowca`. Oddaje gotowy tekst do wklejenia. Nic nie ciągnie z zewnątrz, nic nie publikuje. To pełnoprawny tryb pracy — z niego startuje każdy klient.

## Tryb z narzędziem: Google Search Console (odczyt)
Po podłączeniu obszar czyta realne dane wyszukiwania i przestaje „pisać w ciemno":
- **jakie frazy** faktycznie wpisują ludzie, którzy trafiają na stronę (pod tematy treści i profil),
- **co już się wyświetla i klika** (Impressions / Clicks / CTR / pozycja) — gdzie jesteś blisko wejścia na górę i warto dopisać treść,
- frazy z **wysoką intencją** i długi ogon, którego nie wymyśliłbyś zza biurka.

### Zakres uprawnień: tylko odczyt
Ten obszar z narzędzia **wyłącznie czyta**. Nie zmienia ustawień, nie wysyła, nie publikuje. To wynika z twardej zasady MarketingAgent: czytanie danych — swobodnie; każde działanie na zewnątrz (publikacja treści) — po stronie właściciela, przez kolejkę decyzji.

### Jak podłączyć (do pokazania na wideo)
1. Dodaj konektor Google / Search Console w swoim kliencie (katalog konektorów albo wpis MCP).
2. Zaloguj się i autoryzuj **dostęp tylko do odczytu** do właściwej usługi (domeny) w Search Console.
3. Wróć do MarketingAgent i uruchom `/magent-tresci:start` ponownie albo powiedz operatorowi „podłączyłem Search Console" — zaktualizuje status w `system/obszary-zainstalowane.md` na „podłączone".
4. Od tej pory przy planie treści operator może poprosić Treści o oparcie tematów na realnych frazach.

### Techniczne
Gdy jest konkretny serwer MCP do Search Console, jego deklaracja trafia do `.mcp.json` w katalogu tego pluginu — wtedy narzędzie pojawia się automatycznie po instalacji. Wzorzec deklaracji: `connectors.example.json` (obok tego pliku). Do czasu podłączenia realnego konektora obszar działa w trybie bez narzędzia — nic się nie psuje.
