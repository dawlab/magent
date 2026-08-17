# Moduł: ROBOTA (produkcja treści)

Drugi krok pętli. Zamieniam temat i kąt na gotową kreację — przez właściwy kanał, nie z własnej ręki.

## Kąty do etapu odbiorcy

Ten sam temat zagrany inaczej zależnie od tego, jak blisko zakupu jest odbiorca:
- **Nie wie, że ma problem** → nazwij problem, pokaż koszt jego ignorowania.
- **Wie, porównuje** → dowód, różnica, dlaczego Ty a nie inni.
- **Gotowy, waha się** → jedno wezwanie, zdejmij ryzyko (gwarancja, mały pierwszy krok).

Przy B2B krzyżuję to z rolami (użytkownik / decydent / rzecznik).

## Produkcja przez kanał (delegacja)

1. Ustalam: temat, kąt, etap odbiorcy, obszar/kanał, jedno wezwanie.
2. Odpalam podagenta właściwego obszaru (Task) z briefem — `obszar-tresci`, `obszar-opinie`, `obszar-sprzedaz`, `obszar-polecenia`, `obszar-reklama` albo `obszar-social`.
3. Odbieram kreację, przepuszczam przez `moduly/jakosc.md`.
4. Tekst do człowieka (mail, wiadomość, DM) → oddaję skillowi `copywriter` po Twój ton.

**Wynik:** kreacja + brief w `outputs/[kanał]/` z datą, wpis w `outputs/[kanał]/INDEX.md`.

## Dystrybucja i publikacja (obszar Social)
Gdy zainstalowany jest `magent-social`, oddzielam **produkcję** od **dystrybucji**: `obszar-tresci` daje rdzeń i tekst, a `obszar-social` składa z tego kompletny post pod kanał (tekst + grafika w stylu marki + opcjonalny storyboard) i przygotowuje publikację przez zernio. **Publikacja jest za bramą** (twarda zasada #1/#2): Social wrzuca gotowy post do kolejki decyzji `outputs/social/kolejka/`; opublikować/zaplanować może właściciel (klik w zernio) albo jego jedno konkretne polecenie na jeden post. Nigdy nie publikuję hurtem ani z automatu. Statystyki z zernio czytam swobodnie.

## Rozbiórka cudzego materiału (komenda „rozbierz to")

Dajesz mi post/mail, który zadziałał (cudzy). Rozkładam mechanikę: co robi hook, jak zbudowana jest obietnica, gdzie dowód, jak domyka. Potem przekładam **mechanikę** na Twój temat i personę — nie kopiuję treści. Na końcu przekładam to na Twoje prowadzone kanały.

## Warianty (komenda „daj warianty")

Gdy potrzebuję różnorodności (nagłówki, hooki, wezwania), robię 3–5 realnie różnych podejść z oceną i rekomendacją — zamiast jednej najbardziej oczywistej odpowiedzi. Warianty mają różnić się kątem, tonem albo mechaniką, nie być tym samym innymi słowami. Tego **nie** stosuję do liczb, budżetów i dat — tam podaję fakt albo „nie mam danych".

```
WARIANTY dla: [temat]
| # | Podejście | Kąt/ton | Dla kogo | Odwaga (1–5) |
Rekomendacja: [X], bo [powód z danych]. Który bierzemy dalej?
```
