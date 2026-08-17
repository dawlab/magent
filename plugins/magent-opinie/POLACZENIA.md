# Połączenia — obszar Opinie

Dwa tryby. Tryb bez narzędzia jest domyślny i zawsze dostępny.

## Tryb bez narzędzia (domyślny)
Obszar pracuje na materiale od właściciela: surowych cytatach klientów i wskazanych zadowolonych klientach. Produkuje system próśb o opinię, szablony, testimoniale/case z surowca, ekspozycję dowodu. Nic nie ciągnie z zewnątrz, nic nie publikuje.

## Tryb z narzędziem: Google Business Profile (odczyt)
Po podłączeniu obszar czyta istniejące opinie z profilu Google, żeby:
- przerobić realne wypowiedzi na testimoniale i mini-case (bez podkręcania),
- zobaczyć, gdzie jest dowód, a gdzie luka — o co jeszcze poprosić i kogo.

### Zakres uprawnień: tylko odczyt
Obszar **wyłącznie czyta** opinie. Nie odpowiada na opinie, nie publikuje, nie prosi automatycznie. Wynika to z twardej zasady MarketingAgent: odczyt swobodnie; wysyłanie próśb, odpowiadanie i publikacja dowodu — po stronie właściciela, przez kolejkę decyzji.

### Jak podłączyć (do pokazania na wideo)
1. Dodaj konektor Google / Business Profile w swoim kliencie.
2. Autoryzuj **dostęp tylko do odczytu** do właściwej wizytówki (lokalizacji).
3. Wróć do MarketingAgent, uruchom `/magent-opinie:start` ponownie albo powiedz operatorowi „podłączyłem opinie Google" — zaktualizuje status w `system/obszary-zainstalowane.md` na „podłączone".

### Techniczne
Gdy jest konkretny serwer MCP do Google Business Profile, jego deklaracja trafia do `.mcp.json` w katalogu tego pluginu. Wzorzec: `connectors.example.json`. Do tego czasu obszar działa w trybie bez narzędzia — nic się nie psuje.
