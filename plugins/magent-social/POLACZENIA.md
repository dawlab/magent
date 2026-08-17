# Połączenia — obszar Social

Ten obszar działa w **trzech warstwach**. Warstwa bez narzędzia jest domyślna i zawsze dostępna — narzędzia tylko ją wzmacniają, nie są warunkiem pracy. Publikacja zawsze zostaje **za bramą decyzji** (patrz niżej).

## Warstwa 1 — bez narzędzia (domyślna, darmowa)
Obszar składa kompletny post: tekst natywny dla kanału + grafikę jako **szablon HTML/SVG w stylu marki** + (opcjonalnie) storyboard wideo. Wszystko do ręcznego wrzucenia przez właściciela. Nic nie ciągnie z zewnątrz, nic nie publikuje. To pełnoprawny tryb pracy — z niego startuje każdy klient.

Żeby grafika trzymała styl marki, właściciel dokłada do `dane/`:
- **`dane/marka_wizualna.md`** — paleta (dokładne heksy), fonty, ton wizualny, proporcje. Szkielet tworzy `/magent-social:start`.
- opcjonalnie: **brand book** (PDF/obraz), **logo**, **przykłady dawnych, udanych postów** — im więcej kontekstu, tym wierniej trzymamy „głos wizualny" marki (analogicznie do `dane/glos_styl.md` dla tekstu).
Bez tych plików obszar robi neutralny, czytelny szablon i nazywa brak — nie zmyśla kolorów marki.

## Warstwa 2 — publikacja: zernio (MCP)
**zernio** to developer-first API + hostowany serwer MCP do publikacji i planowania na 15+ platformach (Instagram, TikTok, YouTube, X, LinkedIn, Facebook, Threads, Bluesky i in.).
- **Darmowy tier: 2 konta social, bez karty, pełne API** — nie zmuszamy właściciela do kolejnego płatnego narzędzia.
- Konta social autoryzuje **właściciel** (OAuth w panelu zernio) — MarketingAgent nigdy nie widzi haseł ani tokenów platform.

### Jak podłączyć (do pokazania na wideo)
1. Załóż konto na **zernio.com** (darmowe, bez karty) i podłącz swoje konta social w panelu zernio (OAuth „Połącz konto" dla każdej platformy — do 2 kont w darmowym tierze).
2. Dodaj serwer MCP zernio do swojego klienta Claude:
   - **Claude web/desktop**: Ustawienia → Konektory → dodaj własny konektor → `https://mcp.zernio.com/mcp` → zaloguj się przez OAuth (rekomendowane — bez wklejania kluczy).
   - **Claude Code**: zadeklaruj serwer w `.mcp.json` tego pluginu (wzorzec: `connectors.example.json` obok tego pliku). Wariant OAuth (rekomendowany) albo Bearer (klucz z `zernio.com/dashboard/api-keys`).
3. Wróć do MarketingAgent i uruchom `/magent-social:start` ponownie albo powiedz operatorowi „podłączyłem zernio" — zaktualizuje status w `system/obszary-zainstalowane.md` na „podłączone".
4. Od tej pory operator może przygotować post w zernio i **zaplanować** go — ale publikacja idzie przez bramę decyzji.

### Techniczne
Endpoint MCP: `https://mcp.zernio.com/mcp`. Uwierzytelnianie: OAuth (rekomendowane) albo `Authorization: Bearer <klucz>`. Serwer wystawia wiele narzędzi (rdzeń widoczny + reszta przez `search_tools`) pokrywających publikację, planowanie, statystyki i DM. Deklaracja trafia do `.mcp.json` w katalogu tego pluginu — wtedy narzędzie pojawia się po instalacji. Do czasu podłączenia obszar działa bez narzędzia — nic się nie psuje.

## Warstwa 3 — grafika: dwie darmowe ścieżki (wybór właściciela)
Masz dwie w pełni działające drogi do grafiki. Obie są darmowe na starcie — różnią się tym, czy chcesz edytowalny projekt w Canvie, czy gotowy plik bez żadnego konta.

### Ścieżka A — Canva (konektor MCP, działa na darmowym koncie)
Jest **oficjalny konektor Canva ↔ Claude**. Agent tworzy on-brand projekt (post, karuzela, infografika) **bezpośrednio w Twojej Canvie** — korzystając z Twojego Brand Kitu i szablonów. Na darmowym koncie Canva:
- **Tworzenie projektu działa** — to jest ta wartość, o którą chodzi.
- **Eksport przez API jest płatny** → na free **eksportujesz ręcznie z Canvy** (otwierasz projekt → Udostępnij/Pobierz, jedno kliknięcie). Zero kosztów, tylko jeden ruch więcej.
- **Autofill szablonów „na skalę" (dane → wiele grafik hurtem) to Enterprise** — tej jednej funkcji na free nie ma. Pojedyncze projekty robisz normalnie.

Jak podłączyć:
1. Załóż/miej konto Canva (darmowe wystarcza) — najlepiej z uzupełnionym **Brand Kitem** (logo, kolory, fonty), żeby projekty były od razu w Twoim stylu.
2. Dodaj serwer MCP Canva do klienta:
   - **Claude Code**: `claude mcp add canva --transport http https://mcp.canva.com/mcp` (albo wpis w `.mcp.json` tego pluginu — wzorzec w `connectors.example.json`).
   - **Claude web/desktop**: Ustawienia → Konektory → dodaj `https://mcp.canva.com/mcp`. (Uwaga: gotowy konektor „klik" w Claude bywa na planie płatnym Claude; ścieżka przez serwer MCP działa bez tego.)
   - Przy pierwszym użyciu Canva otworzy okno OAuth — logujesz się i autoryzujesz. Agent nie widzi hasła.
3. Powiedz operatorowi „podłączyłem Canvę" → status w `system/obszary-zainstalowane.md` na „podłączone (Canva)".

Endpoint MCP: `https://mcp.canva.com/mcp`. Funkcje: tworzenie projektów, upload materiałów, foldery, eksport (płatny), import, wyszukiwanie, komentarze.

### Ścieżka B — szablon HTML/SVG (lokalny, w 100% darmowy, bez konta)
Agent produkuje grafikę jako samodzielny plik **HTML/SVG w stylu marki** (z `dane/marka_wizualna.md`) i zapisuje do `outputs/social/`. Zero zależności, darmowy **łącznie z eksportem** — plik jest od razu obrazem. Nie edytujesz go w Canvie, ale masz gotowy materiał bez logowania gdziekolwiek.

### Którą wybrać
- Żyjesz w Canvie / chcesz edytowalny, designerski projekt spójny z Brand Kitem → **Canva**.
- Chcesz zero setupu, zero kont, gotowy plik od ręki → **HTML/SVG**.
Można trzymać obie i wybierać per post.

Status podłączonej ścieżki (Canva / model) zapisujemy w `system/obszary-zainstalowane.md` — obszar sprawdza go, zanim cokolwiek zaproponuje.

## Warstwa 4 — wideo: storyboard (darmowy) + opcjonalny generator
Uczciwie: wideo to **najmniej dojrzały klocek** w tym obszarze. Przy generacji AI „darmowe" prawie zawsze znaczy **znak wodny + limit sekund/kredytów + zmienna jakość**. Żadne narzędzie wideo nie jest tak bezproblemowe jak zernio. Dlatego trzymamy trzy ścieżki, od najprostszej:

### Ścieżka domyślna — storyboard (darmowy, zawsze działa)
Agent oddaje **storyboard**: ujęcia, tekst na ekranie, napisy, sugestię audio, długość pod kanał. Właściciel nagrywa telefonem albo składa w dowolnym edytorze. Dla solo to często **lepszy** wybór niż wideo AI — autentyczna twarz niesie się na Reelsach mocniej niż materiał generowany. Zero kosztów, zero kont.

### Ścieżka A — Invideo AI (skrypt → gotowe wideo social)
Bierze skrypt/prompt i składa **kompletne wideo** (stock + klipy AI + napisy w 50+ językach + lektor) pod Reels/TikTok/Shorts. Najlepiej domyka nasz łańcuch „post → wideo z tego samego rdzenia". Hostowany serwer MCP, darmowy plan na start (ze znakiem wodnym/limitem), potem tani.
- **Podłączenie:** dodaj serwer MCP Invideo w kliencie (jak zernio/Canva). **Aktualny endpoint MCP i sposób logowania weź z dokumentacji Invideo** (help.invideo.io — sekcja „Model Context Protocol Server") i wpisz do `.mcp.json` tego pluginu. Nie zgadujemy adresu z pamięci.

### Ścieżka B — Higgsfield (surowe klipy AI z promptu)
Generuje **klipy AI** z promptu (7 modeli), narzędzia m.in. `generate_video`, `generate_image`, `get_generation_status`. Najhojniejszy darmowy tier: **150 kredytów/mies.**, hostowany MCP, szybki setup w Claude Code. To „materiał" (ujęcia), nie gotowy post z napisami — składasz z tego wideo sam albo w Invideo/edytorze.
- **Podłączenie:** dodaj serwer MCP Higgsfield w kliencie. **Aktualny endpoint i komendę setupu weź z dokumentacji Higgsfield** i wpisz do `.mcp.json`. Placeholder w `connectors.example.json`.

### Którą wybrać
- Chcesz gotowe wideo z posta, minimum roboty → **Invideo**.
- Chcesz generować własne ujęcia AI, najwięcej darmowych kredytów → **Higgsfield**.
- Chcesz autentyczności / zero narzędzi → **storyboard** (i telefon).
Status podłączonego generatora zapisujemy w `system/obszary-zainstalowane.md`. Wideo, tak jak reszta, wychodzi w świat tylko **przez bramę decyzji** (niżej).

## BRAMA DECYZJI (zakres działania narzędzi)
To pierwszy obszar, którego narzędzie potrafi **działać na zewnątrz** — opublikować coś pod marką właściciela. Dlatego, zgodnie z twardymi zasadami MarketingAgent (`CLAUDE.md` #1 i #2):
- **Odczyt — swobodnie.** Statystyki, zasięgi, statusy kont z zernio operator czyta bez pytania.
- **Każde działanie na zewnątrz — do kolejki decyzji.** Publikacja i planowanie w zernio, wysłanie DM, zmiana ustawień konta — **nigdy z automatu**. Operator składa kompletny post, zapisuje go i wrzuca pozycję do `outputs/social/kolejka/`. Publikację/zaplanowanie wykonuje **właściciel** (klik w panelu zernio) albo autoryzuje operatora **jednym poleceniem na jeden konkretny post**. Jedno „ok" = jeden post. Bez autopilota, bez publikacji serii na jedno „ok".
