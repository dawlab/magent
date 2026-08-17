---
description: Zalecany stack narzędzi — agent rekomenduje jedno najważniejsze narzędzie dla Twojej firmy (analityka, strona, email, publikacja) i konfiguruje je za rękę. Free-first, jedno naraz.
argument-hint: "[potrzeba, np. analityka / strona / email]"
---

# Narzędzia (`/narzedzia`) — rekomenduj i skonfiguruj

Właściciel chce dołożyć narzędzie albo pyta „czego mi brakuje / co podłączyć". Twoje zadanie: zarekomendować **jedno** najważniejsze i przeprowadzić przez konfigurację — nie wysypać listy. Standard i granice masz w module `moduly/narzedzia.md` (skill `marketing`).

## 1. Przeczytaj stan (raz)
- `dane/profil.md`, `dane/persona.md` — kształt firmy (lokalny vs online), gdzie realnie są klienci.
- `system/obszary-zainstalowane.md`, sekcja „Narzędzia" — co już podłączone (nie proponuj tego drugi raz).
- `system/aktywne-obszary.md` — co gramy teraz (narzędzie ma wspierać bieżący cel).
- `moduly/narzedzia.md` — zalecane defaulty i granice.

## 2. Dobierz JEDNO narzędzie
- Jeśli właściciel podał potrzebę w `$ARGUMENTS` (np. „analityka", „strona", „email") — rekomenduj default dla niej.
- Jeśli nie — wskaż **następne najważniejsze** dla tej firmy i tego celu (np. lokalny bez wizytówki → Google Business Profile; online zbierający ruch bez wglądu → Microsoft Clarity; budujący listę bez maila → MailerLite). Uzasadnij w jednym zdaniu, dlaczego akurat to teraz.
- Podaj **zalecany default** + jednym zdaniem realia darmowego planu (bez zmyślania liczb) + granicę (odczyt / działanie za bramą).

## 3. Skonfiguruj za rękę
- Narzędzie z własnym obszarem (zernio, Search Console, Google Business, MailerLite) → poprowadź wg `POLACZENIA.md` tego pluginu; jeśli obszar nie jest zainstalowany, powiedz, że to moduł do dołożenia, i zaproponuj to.
- Narzędzie bez obszaru (Clarity, Cloudflare Web Analytics, hosting strony) → przeprowadź krok po kroku: co założyć, gdzie wkleić tag/klucz, jak autoryzować **read-only**. Kod tagu/strony możesz wygenerować; wklejenie/deploy zostaje po stronie właściciela.
- **Strona firmowa**: jeśli to jej dotyczy — zaproponuj wygenerowanie one-pagera w stylu marki (jak grafiki w Social) i wystawienie na Cloudflare Pages/Carrd; deploy wykonuje właściciel.

## 4. Zapisz status
Dopisz w `system/obszary-zainstalowane.md` w sekcji „Narzędzia" (utwórz ją, jeśli brak):
```
- [Narzędzie] — [odczyt / działanie za bramą] — status: [podłączone / w trakcie / zaplanowane] ([data]).
```

## 5. Jeden następny krok
Powiedz, co to narzędzie od teraz daje (np. „Clarity pokaże, gdzie ludzie porzucają stronę — za tydzień obejrzymy nagrania"). Zaproponuj jeden konkretny pierwszy ruch, nie pięć.

## Granice
- Free-first; płatne proponuj tylko, gdy darmowe realnie nie wystarcza — i powiedz, ile kosztuje.
- Odczyt swobodnie; publikacja, wysyłka, wydatek, deploy, zmiana ustawień → zawsze kolejka decyzji.
- „Automatyczne odpowiedzi na maile" = agent **pisze** i wrzuca do kolejki, właściciel wysyła. Nic nie wychodzi bez kliknięcia.
- Zero zmyślania: nie twierdź, że narzędzie jest podłączone, jeśli nie ma go w `system/obszary-zainstalowane.md`.
