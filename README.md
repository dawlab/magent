# MarketingAgent — instrukcja obsługi

MarketingAgent to asystent marketingowy dla jednoosobowej firmy. Zna Twoją ofertę, Twoich klientów i Twój sposób pisania. Podpowiada, co zrobić dalej, przygotowuje treści, buduje stronę i analizuje wyniki.

Pracujesz z nim przez rozmowę — piszesz, czego potrzebujesz, on to robi. Wszystko, co ma trafić do klientów, przygotowuje w formie gotowej do wysłania i czeka na Twoją decyzję.

---

## Spis treści

1. [Zanim zaczniesz](#1-zanim-zaczniesz)
2. [Instalacja](#2-instalacja)
3. [Pierwsze uruchomienie](#3-pierwsze-uruchomienie)
4. [Jak wydawać polecenia](#4-jak-wydawać-polecenia)
5. [Dwa tryby pracy](#5-dwa-tryby-pracy)
6. [Dokładanie obszarów](#6-dokładanie-obszarów)
7. [Co potrafi każdy obszar](#7-co-potrafi-każdy-obszar)
8. [Spis komend](#8-spis-komend)
9. [Podłączanie narzędzi](#9-podłączanie-narzędzi)
10. [Strona, audyty i Twój styl](#10-strona-audyty-i-twój-styl)
11. [Gdzie są Twoje dane](#11-gdzie-są-twoje-dane)
12. [Rytm pracy](#12-rytm-pracy)
13. [Zasady, których agent przestrzega](#13-zasady-których-agent-przestrzega)
14. [Poprawianie agenta](#14-poprawianie-agenta)
15. [Praca z kilkoma firmami](#15-praca-z-kilkoma-firmami)
16. [Aktualizacje](#16-aktualizacje)
17. [Najczęstsze pytania](#17-najczęstsze-pytania)
18. [Skrót na start](#18-skrót-na-start)

---

## 1. Zanim zaczniesz

Potrzebujesz trzech rzeczy:

**Claude Code.** Program, w którym działa MarketingAgent. Instalujesz go raz, jak każdą inną aplikację. Instrukcja instalacji jest w pierwszym module kursu.

**Adres MarketingAgenta.**

```
https://dawlab.github.io/magent/marketplace.json
```

Ten adres wskazuje Claude Code, skąd pobrać agenta. Nie otwierasz go w przeglądarce i niczego z niego nie ściągasz ręcznie — wklejasz go w poleceniu instalacyjnym.

**Folder na dane firmy.** Zwykły folder na dysku, na przykład `Moja Firma` w Dokumentach. MarketingAgent zapisze tam wszystko, czego się o Twojej firmie dowie, oraz materiały, które przygotuje.

Nie potrzebujesz żadnych dodatkowych programów poza Claude Code. Agent pobiera się sam i zapisuje we własnym katalogu — jedyny folder, który tworzysz Ty, to ten na dane firmy.

---

## 2. Instalacja

Instalację przechodzisz raz.

### Krok 1. Zainstaluj Claude Code

Jeśli jeszcze go nie masz, zacznij od tego. Film w kursie prowadzi przez instalację krok po kroku.

### Krok 2. Pobierz MarketingAgenta

Otwórz Claude Code w folderze swojej firmy. Wszystko poniżej wpisujesz w oknie Claude Code — tam, gdzie normalnie piszesz do asystenta.

Wklej poniższą linijkę i zatwierdź:

```
/plugin marketplace add https://dawlab.github.io/magent/marketplace.json
```

Następnie drugą:

```
/plugin install magent-rdzen@magent
```

Pierwsza wskazuje, skąd pobrać MarketingAgenta. Druga instaluje jego podstawową część.

> Jeśli Twoja wersja Claude Code nie przyjmuje tych poleceń w oknie asystenta, wykonaj je w Terminalu, dopisując na początku słowo `claude` i pomijając ukośnik:
> `claude plugin marketplace add https://dawlab.github.io/magent/marketplace.json`

### Krok 3. Przygotuj folder firmy

W tym samym oknie wpisz:

```
/magent-setup
```

MarketingAgent utworzy w tym folderze strukturę plików, w której będzie zapisywał wiedzę o firmie i przygotowane materiały.

Folder może znajdować się w dowolnym miejscu na dysku — jego lokalizacja nie wpływa na działanie agenta. Jedna zasada: jeden folder odpowiada jednej firmie (więcej w punkcie 15).

### Krok 4. Uruchom Claude Code ponownie

Zamknij program i otwórz go jeszcze raz. Dopiero wtedy wczytają się nowe komendy.

Po instalacji masz część podstawową. Kolejne obszary — treści, social media, sprzedaż — dokładasz osobno, w miarę postępów w kursie (punkt 6).

---

## 3. Pierwsze uruchomienie

Zacznij od przedstawienia firmy:

```
/nauka-firmy
```

MarketingAgent zada kilka pytań: czym się zajmujesz, do kogo kierujesz ofertę, co sprzedajesz, jakim językiem mówisz do klientów. Odpowiadasz własnymi słowami. Na podstawie tych odpowiedzi buduje profil firmy, z którego korzysta przy każdym późniejszym zadaniu.

Następnie sprawdź, czy trafił w Twój styl:

```
@głos napisz krótkie powitanie do klienta w moim stylu
```

Jeśli w którymkolwiek momencie nie wiesz, co zrobić dalej, wpisz:

```
/start
```

Dostaniesz podsumowanie sytuacji i propozycję jednego konkretnego kroku.

---

## 4. Jak wydawać polecenia

Z MarketingAgentem rozmawiasz, pisząc. Masz trzy sposoby:

**Zwykłe zdania.** „Napisz post o nowej ofercie", „zaproponuj temat na przyszły tydzień", „dlaczego nikt nie odpowiada na moje maile".

**Komendy zaczynające się od `/`.** Skróty do konkretnych zadań, na przykład `/start` albo `/stan`. Po wpisaniu ukośnika zobaczysz listę dostępnych.

**Wywołania zaczynające się od `@`.** Kierują zadanie do konkretnego pomocnika:
- `@marketing` — planowanie, pomysły, produkcja materiałów
- `@głos` — nadanie tekstowi Twojego tonu
- `@social` — przygotowanie postów (jeśli masz dodany obszar Social)

Nie musisz pamiętać całej listy. `/start` zawsze podpowie, co jest teraz sensowne.

---

## 5. Dwa tryby pracy

MarketingAgent pracuje w dwóch trybach:

**Rozbudowa** (`/rozbudowa`) — konfigurowanie: uczenie agenta firmy, dokładanie obszarów, uzupełnianie danych, podłączanie narzędzi.

**Praca** (`/praca`) — korzystanie z tego, co już jest: tworzenie treści, analiza wyników, rozwiązywanie konkretnego problemu.

Tryby przechodzą jeden w drugi. Jeśli podczas pracy zabraknie jakiegoś elementu, agent zaproponuje uzupełnienie go i wróci do przerwanego zadania.

---

## 6. Dokładanie obszarów

Obszar to zestaw umiejętności w jednej dziedzinie — na przykład tworzenie treści albo obsługa social mediów. Dokładasz je pojedynczo, wtedy gdy są potrzebne.

Dodanie obszaru to dwa polecenia w oknie Claude Code:

```
/plugin install magent-tresci@magent
```
```
/tresci-start
```

Drugie polecenie włącza obszar, konfiguruje go i wyjaśnia, co od tej pory jest możliwe.

**Kolejność, która sprawdza się najczęściej:**

1. **Treści** — żeby klienci mogli Cię znaleźć. Zwykle punkt wyjścia.
2. **Opinie** — zbieranie i wykorzystywanie opinii jako dowodu.
3. **Sprzedaż** — przechwytywanie kontaktu i maile prowadzące do zakupu.
4. **Polecenia** — system rekomendacji i współpracy z innymi firmami.
5. **Social media** — składanie i publikowanie postów.
6. **Reklama płatna** — dopiero gdy działania bezpłatne przynoszą efekty.

Nie musisz mieć wszystkich obszarów. Przy jednoosobowej firmie skuteczniejsze jest prowadzenie jednego lub dwóch konsekwentnie niż sześciu pobieżnie.

---

## 7. Co potrafi każdy obszar

| Obszar | Komenda włączająca | Zakres |
|---|---|---|
| **Treści** | `/tresci-start` | Posty, scenariusze filmów, plan treści, opisy profilu i strony, teksty pod wyszukiwarki i modele AI |
| **Opinie** | `/opinie-start` | Proszenie o opinie we właściwym momencie, przerabianie ich na materiał sprzedażowy |
| **Sprzedaż** | `/sprzedaz-start` | Materiał do pobrania w zamian za kontakt, strona zapisu, sekwencje maili, odzyskiwanie klientów |
| **Polecenia** | `/polecenia-start` | Mechanizm poleceń, skrypty rozmów, propozycje współpracy |
| **Social media** | `/social-start` | Kompletny post: tekst, grafika i opis publikacji; publikacja po Twojej akceptacji |
| **Reklama płatna** | `/reklama-start` | Teksty reklam, opis kreacji, plan budżetu testowego; kampanię uruchamiasz samodzielnie |

Każdy obszar działa również bez podłączonych narzędzi zewnętrznych — wtedy przekazuje gotowy materiał do skopiowania.

---

## 8. Spis komend

**Orientacja w sytuacji**

| Komenda | Działanie |
|---|---|
| `/start` | Podsumowanie sytuacji i propozycja następnego kroku |
| `/stan` | Stan marketingu firmy i najlepszy ruch w tym momencie |
| `/ruch` | Sam następny krok, bez szerszego omówienia |

**Planowanie i kontrola**

| Komenda | Działanie |
|---|---|
| `/strategia` | Co sprzedawać, do kogo kierować ofertę, czy dany pomysł się opłaca |
| `/sesja` | Prowadzenie przez jedną porcję pracy od briefu do podsumowania |
| `/audyt` | Wskazanie miejsc, w których marketing pochłania pieniądze bez efektu |
| `/korekta` | Zapisanie trwałej zasady, według której agent ma dalej pracować |

**Tworzenie**

| Komenda | Działanie |
|---|---|
| `/narzedzia` | Rekomendacja i konfiguracja jednego narzędzia dopasowanego do sytuacji |
| `/strona` | Zbudowanie strony-wizytówki w kolorystyce Twojej marki |
| `/checklista` | Ocena Twojej strony, oferty lub gotowej treści i lista 3–5 poprawek |

**Wywołania pomocników**

| Wpisujesz | Efekt |
|---|---|
| `@marketing …` | Planowanie i produkcja materiałów |
| `@głos …` | Przepisanie tekstu Twoim tonem |
| `@social …` | Przygotowanie materiału na social media |

**Włączanie obszarów:** `/tresci-start`, `/opinie-start`, `/sprzedaz-start`, `/polecenia-start`, `/reklama-start`, `/social-start`.

---

## 9. Podłączanie narzędzi

MarketingAgent może połączyć się z zewnętrznymi narzędziami — żeby odczytywać wyniki albo publikować przygotowane materiały. Nie jest to konieczne: bez połączeń przekazuje gotowe materiały do samodzielnego wykorzystania.

Żeby dobrać narzędzie, wpisz:

```
/narzedzia
```

Agent zaproponuje jedno narzędzie, które w Twojej sytuacji da najwięcej, i przeprowadzi przez konfigurację.

Dwie rzeczy dotyczące wszystkich połączeń:

- Do każdego narzędzia logujesz się samodzielnie, w jego własnym oknie logowania. MarketingAgent nie ma dostępu do Twoich haseł.
- Odczyt danych agent wykonuje samodzielnie. Publikacja, wysyłka i wydatki wymagają Twojej zgody za każdym razem.

**Narzędzia, które rekomendujemy** — wszystkie mają bezpłatną wersję na start:

| Zastosowanie | Narzędzie |
|---|---|
| Publikowanie i planowanie postów | zernio (bezpłatnie dla dwóch kont) |
| Grafiki do postów | Canva albo grafika przygotowana bezpośrednio przez agenta |
| Zachowanie odwiedzających na stronie | Microsoft Clarity |
| Frazy, po których trafiają do Ciebie klienci | Google Search Console |
| Wizytówka firmy w Google | Google Business Profile |
| Lista mailowa i wysyłka | MailerLite |

Osobna uwaga o odpowiadaniu na maile: MarketingAgent przygotowuje odpowiedź w Twoim tonie i zostawia ją gotową do wysłania. Wysyłasz ją Ty. Nie wysyła wiadomości samodzielnie.

---

## 10. Strona, audyty i Twój styl

**`/strona`** buduje stronę-wizytówkę: kim jesteś, dla kogo pracujesz, jaki jest pierwszy krok dla klienta, sekcja pytań i odpowiedzi. Powstaje w kolorystyce Twojej marki, z tekstami opartymi na profilu firmy. Publikacja strony w internecie odbywa się na Twoim koncie i Twojej domenie — agent prowadzi przez ten proces.

**`/checklista`** ocenia materiał, który już istnieje:
- `/checklista strona` — Twoja strona lub wizytówka: widoczność w wyszukiwarkach, czytelność oferty, elementy, które decydują o kontakcie
- `/checklista publikacja` — treść przed opublikowaniem
- `/checklista oferta` — strona oferty albo sekwencja maili

Wynik to zawsze 3–5 poprawek uszeregowanych według wpływu na efekt, a nie pełna lista uwag.

**`@głos`** przepisuje dowolny tekst tak, żeby brzmiał jak Ty. Nie zmienia treści ani argumentów — wyłącznie sposób wypowiedzi.

---

## 11. Gdzie są Twoje dane

Wszystko, co dotyczy Twojej firmy, znajduje się w Twoim folderze, w trzech katalogach:

- **`dane`** — profil firmy: oferta, odbiorcy, Twój styl wypowiedzi, liczby
- **`system`** — stan bieżący: nad czym pracujecie, Twoje zasady, historia
- **`outputs`** — gotowe materiały: posty, strony, analizy, uporządkowane chronologicznie

Agent prowadzi te pliki samodzielnie — nie musisz ich edytować. Możesz do nich zajrzeć w każdej chwili; są zwykłymi plikami tekstowymi na Twoim dysku.

---

## 12. Rytm pracy

Praca z MarketingAgentem opiera się na powtarzalnym cyklu:

1. **Ustal kierunek** — `/stan` albo `/ruch` wskazują, co przyniesie teraz największy efekt.
2. **Wykonaj** — agent przygotowuje materiał. Teksty kierowane do klientów warto przepuścić przez `@głos`.
3. **Sprawdź wynik** — `/sesja` zamyka porcję pracy podsumowaniem, `/checklista` ocenia konkretny materiał, `/audyt` pokazuje, co nie działa.

Największą różnicę robi regularność. Dwa kanały prowadzone systematycznie dają więcej niż sześć prowadzonych zrywami. `/start` pokazuje liczbę dni pracy pod rząd — to prosty sposób na utrzymanie rytmu.

---

## 13. Zasady, których agent przestrzega

**Nic nie trafia do odbiorców bez Twojej zgody.** Post, mail czy wydatek agent przygotowuje i zostawia do akceptacji. Decyzję podejmujesz Ty.

**Odczyt danych bez pytania, działanie zawsze za zgodą.** Agent może sprawdzić statystyki czy opinie. Publikacja, wysyłka, zmiana ustawień konta i wydatki wymagają Twojej akceptacji.

**Bez zmyślania.** Jeśli agent nie zna jakiejś liczby lub wyniku, powie o tym wprost, zamiast podać wartość przybliżoną.

**Po polsku.** Cała komunikacja i wszystkie materiały.

---

## 14. Poprawianie agenta

Jeśli coś Ci nie odpowiada, wystarczy powiedzieć — „pisz krócej", „nie zaczynaj postów od pytania", „zwracaj się do mnie na Ty". Możesz też użyć komendy:

```
/korekta pisz krótszymi akapitami, maksymalnie trzy zdania
```

Zasada zostaje zapisana na stałe i obowiązuje we wszystkich późniejszych materiałach. Nie musisz powtarzać tej samej uwagi.

Twoje zasady są przechowywane razem z danymi firmy, więc aktualizacje agenta ich nie usuwają.

---

## 15. Praca z kilkoma firmami

Jeśli prowadzisz więcej niż jedną firmę, każda potrzebuje własnego folderu. Folder decyduje o tym, na czyich danych agent pracuje — dane firm nie mieszają się, bo znajdują się w osobnych miejscach na dysku.

**Konfiguracja:**

1. Utwórz osobny folder dla każdej firmy, na przykład `Firma A` i `Firma B`.
2. W każdym folderze osobno otwórz Claude Code i wykonaj:

```
/magent-setup
/nauka-firmy
```

Każda firma otrzymuje własny profil, własny styl wypowiedzi, własną historię i własny zestaw obszarów.

**Przed rozpoczęciem pracy** upewnij się, że Claude Code jest otwarty w folderze właściwej firmy. To jedyny warunek rozdzielności.

**Jeśli firmy mają osobne konta** w narzędziach zewnętrznych — na przykład osobne konta do publikacji — podłącz je oddzielnie w każdym folderze. Agent poprowadzi przez to przy konfiguracji. Dzięki temu materiał jednej firmy nie trafi na konto drugiej.

Dwóch firm nie należy prowadzić w jednym folderze.

---

## 16. Aktualizacje

MarketingAgent bywa rozwijany — dochodzą nowe możliwości i usprawnienia. Nowe wersje publikujemy pod tym samym adresem, z którego instalowałeś agenta. Nic nie jest instalowane na Twoim komputerze bez Twojej wiedzy.

O każdej aktualizacji informujemy mailem i w kursie. Żeby ją pobrać, wpisz w oknie Claude Code:

```
/plugin marketplace update magent
```
```
/plugin update magent-rdzen@magent
```

Oraz to samo dla dodanych obszarów, na przykład `/plugin update magent-tresci@magent`.

Następnie uruchom Claude Code ponownie. Dane Twojej firmy pozostają bez zmian — aktualizacja obejmuje wyłącznie samego agenta.

---

## 17. Najczęstsze pytania

**Komendy zaczynające się od `/` nie pojawiają się na liście.**
Uruchom Claude Code ponownie. Nowe komendy wczytują się przy starcie programu — po instalacji i po `/magent-setup`.

**Agent mówi, że nie ma danego obszaru.**
Obszar trzeba najpierw zainstalować i włączyć (punkt 6). Agent nie udaje możliwości, których nie ma.

**Materiały są ogólne, jakby agent nie znał firmy.**
Uzupełnij profil przez `/nauka-firmy`. Im więcej konkretów w danych — nazwy usług, ceny, przykłady klientów — tym bardziej precyzyjne materiały.

**Nie wiem, od czego zacząć w danym momencie.**
`/start` podsumuje sytuację i zaproponuje jeden krok.

**Post miał zostać opublikowany, a nie został.**
Post czeka na Twoją akceptację. Publikacja zawsze wymaga potwierdzenia — to jedna z podstawowych zasad działania.

**Chcę zacząć od nowa z danymi firmy.**
`/magent-setup reset` przywraca stan początkowy w bieżącym folderze i tworzy wcześniej kopię zapasową dotychczasowych danych.

---

## 18. Skrót na start

W oknie Claude Code, otwartym w folderze firmy:

```
/plugin marketplace add https://dawlab.github.io/magent/marketplace.json
/plugin install magent-rdzen@magent
/magent-setup       → uruchom Claude Code ponownie
/nauka-firmy        → profil firmy
@głos [test]        → sprawdzenie stylu
/start              → następny krok
```

Dalej: dokładaj obszary w kolejności Treści → Opinie → Sprzedaż → Polecenia → Social → Reklama i pracuj cyklem *ustal kierunek → wykonaj → sprawdź wynik*.

Przy kilku firmach — osobny folder na każdą.

---

*Rozwijasz MarketingAgenta albo wydajesz nowe wersje? Proces wydawniczy i struktura repozytorium: [WYDANIE.md](WYDANIE.md).*
