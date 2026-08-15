---
description: Sesja robocza MarketingAgent — brief, praca krok po kroku przez kanały, podsumowanie z pomiarem.
---

Uruchom skill **marketing** i przeprowadź pełną sesję roboczą. To główny tryb pracy: nie pojedyncza odpowiedź, tylko praca krok po kroku, aż zaplanowane na dziś działania są gotowe albo powiesz, że kończymy.

## Wejście
Zastosuj odczyt raz-na-sesję (CLAUDE.md). Przejrzyj `system/aktywne-obszary.md`, ostatni wpis `system/pomiar.md`, `system/roadmap.md` — co poszło ostatnio, co czeka.

## Brief (jeden ekran, czekaj na zgodę)
```
DZIŚ ROBIMY: [1–3 konkretne działania z aktywnych obszarów i celu]
AKTYWNE KANAŁY: [które i co robią]
CZEKAJĄ: [co świadomie dziś odkładamy i dlaczego, w jednym zdaniu]
CZEGO BRAKUJE: [dane lub decyzje, które nas blokują]
ZBIERAMY: [jakie liczby wrócą do pomiaru]
Zaczynamy tak? Możesz to potwierdzić, zmienić albo coś pominąć.
```

## Praca w pętli (po zgodzie)
Wykonuję działania po kolei, delegując do podagentów obszarów i skilla glos. Po każdym z nich krótko podsumowuję: co powstało, gdzie to leży i jaki jest następny krok lub pytanie. Publikacja, wysyłka i wydatek nigdy nie dzieją się same — przygotowuję rzecz do kliknięcia i dodaję do kolejki decyzji. Nie kończę po jednym kroku — pracuję, aż zaplanowane działania są gotowe albo powiesz, że kończymy.

## Podsumowanie na koniec
Podsumowuję, co powstało, co czeka na Twoje kliknięcie i jakie liczby wrócą do pomiaru. Dopisuję wpis do `system/changelog.md` i aktualizuję `system/roadmap.md`. Zostawiam też ślad dla następnego `/start`: linię „Ostatnio" (co zrobiliśmy → następny krok) i wpis „Historia" w `system/dziennik.md` (data, tryb „praca"). Na koniec proponuję jedną rzecz, która podniesie system o poziom — to obowiązkowy krok naprzód.
