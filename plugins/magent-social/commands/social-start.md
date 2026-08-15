---
description: Włącza obszar Social w MarketingAgent — rejestruje go, tworzy szkielet marki wizualnej i prowadzi za rękę przez podłączenie zernio (publikacja/planowanie za bramą decyzji).
---

# Start obszaru: Social

Właściciel właśnie zainstalował plugin `magent-social` i uruchamia go w module kursu. Prowadź za rękę, jeden krok naraz. Twoje zadanie:

## 1. Wyjaśnij krótko, co ten obszar robi
Social to **ręka dystrybucyjna**: bierze gotowy przekaz (z Treści albo od operatora) i składa z niego **kompletny post pod konkretny kanał** — tekst + grafikę w stylu Twojej marki + opcjonalny storyboard wideo — a potem przygotowuje go do publikacji przez zernio. **Nic nie publikuje samo.** Wszystko czeka na Twój klik w kolejce decyzji. Brzmienie tekstu nadaje osobno `@głos`.

Powiedz wprost dwie rzeczy, które ten obszar zmienia:
- **Grafiki za darmo**: agent robi grafikę jako szablon w stylu marki — nie potrzebujesz płatnego generatora.
- **Publikacja za bramą**: to pierwszy obszar, który potrafi realnie opublikować pod Twoją marką — dlatego trzyma twardą zasadę „nic nie wychodzi bez Twojego kliknięcia".

## 2. Zarejestruj obszar w katalogu zdolności
Dopisz do `system/obszary-zainstalowane.md`, w sekcji „## Obszary", wpis:

```
- **Social** (plugin `magent-social`) — zainstalowany [dzisiejsza data], skonfigurowany tak. Narzędzie: [zernio — niepodłączone / podłączone]. Media: [darmowe szablony HTML/SVG / konektor podłączony].
```

Jeśli w sekcji stoi placeholder „Brak zainstalowanych obszarów..." — zastąp go tym wpisem. Zaktualizuj datę na górze pliku. Utwórz też folder wyjść `outputs/social/` z `INDEX.md` (nagłówek + pusta tabela) i podfolder `outputs/social/kolejka/` (kolejka decyzji), jeśli ich nie ma.

## 3. Zbuduj „głos wizualny" marki (klucz do dobrych grafik)
Żeby grafiki trzymały styl, potrzebujemy kontekstu. Utwórz szkielet **`dane/marka_wizualna.md`** (jeśli go nie ma) i poproś właściciela o uzupełnienie tego, co ma pod ręką — braki są OK, wracamy do nich później:

```
# Marka wizualna

## Kolory (dokładne heksy)
- Główny: #......
- Akcent: #......
- Tło / tekst: #...... / #......

## Fonty
- Nagłówki: ...
- Tekst: ...

## Logo
- Plik/ścieżka: ...

## Ton wizualny
- (np. minimalny / odważny / ciepły; dużo powietrza / gęsto)

## Przykłady „tak / nie tak"
- Podoba mi się: ... (linki albo wgrane pliki do `dane/`)
- Unikać: ...
```

Zaproś też właściciela, żeby wrzucił do `dane/` **brand book**, **logo** i **kilka dawnych udanych postów** — im więcej kontekstu, tym wierniej trzymamy jego styl. Zaznacz: bez tego agent zrobi neutralny, czytelny szablon i nie będzie zmyślał kolorów marki.

## 4. Zapytaj o publikację przez zernio
Zapytaj, czy chce teraz podłączyć **zernio** (publikacja/planowanie na 15+ platformach, darmowy tier: 2 konta, bez karty).
- Chce teraz → skieruj do `POLACZENIA.md` w tym pluginie (instrukcja krok po kroku: konto zernio + OAuth kont social + serwer MCP `https://mcp.zernio.com/mcp`). Po podłączeniu zmień status w katalogu na „podłączone".
- Nie teraz → zostaje **tryb bez narzędzia**: obszar w pełni działa, oddaje kompletną paczkę (tekst + grafika + storyboard) do ręcznego wrzucenia. zernio dołączysz później.

Zapytaj też o **ścieżkę grafiki** — są dwie i obie są darmowe na starcie (szczegóły w `POLACZENIA.md`):
- **Canva** (oficjalny konektor MCP, `https://mcp.canva.com/mcp`) — agent tworzy on-brand projekt wprost w Canvie klienta (jego Brand Kit i szablony). Na darmowym koncie tworzenie działa; eksport robi właściciel ręcznie (1 klik), Autofill „na skalę" to Enterprise. Dobre dla kogoś, kto już żyje w Canvie i chce edytowalny projekt.
- **Szablon HTML/SVG** (domyślny) — agent oddaje gotowy plik obrazu, zero kont, darmowy łącznie z eksportem.
Jeśli właściciel wybierze Canvę → skieruj do `POLACZENIA.md` (dodanie serwera MCP + OAuth) i po podłączeniu zapisz status „podłączone (Canva)". Jeśli nie wybiera nic → zostaje HTML/SVG.

**Wideo** (wspominaj krótko, bez naciskania): domyślnie darmowy **storyboard** do nagrania telefonem — dla solo często lepszy niż wideo AI. Kto chce generować, może później podłączyć generator: **Invideo** (skrypt → gotowe wideo social, darmowy plan na start ze znakiem wodnym) albo **Higgsfield** (surowe klipy AI, ~150 darmowych kredytów/mies.). Szczegóły i uczciwe ograniczenia w `POLACZENIA.md`. Nie proponuj generatora z automatu — storyboard wystarcza na start.

## 5. Zaproponuj pierwszy ruch
Powiedz, że od teraz operator (`@marketing`) może zlecić Social złożenie posta. Zaproponuj jeden konkretny pierwszy krok pasujący do tego, co wiesz z `dane/` — np. jeden kompletny post (tekst + grafika) na główną platformę persony, z recyklingu ostatniej treści z `outputs/tresci/`, jeśli jest. Nie rób pięciu rzeczy naraz.

## Granica (powiedz to wprost)
Odczyt statystyk z zernio — swobodnie. **Publikacja i planowanie — zawsze przez kolejkę decyzji**: agent składa post gotowy do kliknięcia, a publikujesz Ty (klik w panelu zernio) albo autoryzujesz operatora jednym poleceniem na jeden konkretny post. Bez autopilota, bez publikacji serii na jedno „ok".
