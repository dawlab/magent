# Połączenia — obszar Reklama płatna

Dwa tryby. Tryb bez narzędzia jest domyślny; narzędzie daje odczyt metryk pod rekomendacje.

## Tryb bez narzędzia (domyślny)
Obszar projektuje kampanię, copy, brief kreatywny i budżet testowy na podstawie `dane/`. Wyniki z panelu podaje właściciel, a obszar je interpretuje. Zawsze dostępny.

## Tryb z narzędziem: Google Ads + Search Console (odczyt)
Po podłączeniu obszar czyta realne metryki i przestaje opierać się wyłącznie na tym, co poda właściciel:
- **Google Ads (odczyt)**: koszt leada, konwersje, wydatek, skuteczność kampanii — pod rekomendacje optymalizacyjne (co wyłączyć, gdzie przesunąć budżet — do wykonania przez właściciela).
- **Search Console (odczyt)**: frazy o wysokiej intencji i ich skuteczność — pod dobór słów kluczowych i landingów.

### Zakres uprawnień: tylko odczyt
Obszar **wyłącznie czyta** metryki. **Nie zakłada kampanii, nie zmienia budżetu, nie wgrywa kreacji, nie optymalizuje na żywo** — to robi właściciel w panelu. Twarda zasada MarketingAgent: odczyt swobodnie; każda zmiana w panelu i każdy wydatek — przez kolejkę decyzji.

### Jak podłączyć (do pokazania na wideo)
1. Dodaj konektory Google Ads i/lub Search Console w swoim kliencie.
2. Autoryzuj **dostęp tylko do odczytu** do właściwego konta reklamowego / usługi.
3. Wróć do MarketingAgent, uruchom `/magent-reklama:start` ponownie albo powiedz operatorowi „podłączyłem Google Ads" — zaktualizuje status w `system/obszary-zainstalowane.md` na „podłączone".

### Techniczne
Gdy są konkretne serwery MCP do Google Ads / Search Console, ich deklaracje trafiają do `.mcp.json` w katalogu tego pluginu. Wzorzec: `connectors.example.json`. Do tego czasu obszar działa w trybie bez narzędzia — nic się nie psuje.
