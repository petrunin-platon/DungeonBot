# Hero Wars: Knowledge Engine Bot

Cześć! To program, który sam przechodzi dla ciebie Lochy Tytanów w grze Hero Wars. Włączasz go, zajmujesz się swoimi sprawami — a on otwiera drzwi, zbiera drużyny i odbiera nagrody.

Ten podręcznik został napisany tak, aby każdy mógł go zrozumieć. Nieznane słowa wyjaśniamy od razu, a na końcu każdego rozdziału podpowiadamy, dokąd iść dalej.

## Co potrafi bot

Bot nie jest bezmyślnym „klikaczem”. Patrzy na ekran gry tak samo, jak patrzyłbyś ty, i sam decyduje, co zrobić dalej. Oto co potrafi:

- :eye: **Widzi ekran.** Co ułamek sekundy robi zrzut ekranu okna gry i rozpoznaje na nim przyciski, drzwi oraz wrogów.
- :door-open: **Wybiera drzwi.** Idzie do komnat w kolejności, którą ustaliłeś, i omija te, w których jest teraz niebezpiecznie.
- :users: **Ustawia drużynę.** Dla każdej komnaty ma swój „pak” (tak nazywamy drużynę pięciu tytanów). Bot sam rozstawia tytanów na miejsca.
- :heart-pulse: **Mnoży uwagę na zdrowie.** Po każdej walce sprawdza PŻ (zdrowie) i energię tytanów oraz decyduje, czy pak jest gotowy do następnej walki.
- :swords: **Wzywa ciebie, jeśli walka poszła źle.** Pojawia się okno «Wymagana interwencja»: możesz powtórzyć walkę innym pakiem, zaakceptować ją lub przejść ręcznie. Jeśli odejdziesz od komputera, bot może zdecydować sam.
- :chart-no-axes-column: **Uczy się na swoich walkach.** Zapamiętuje, który pak pokonał których wrogów, i następnym razem wybiera go od razu.
- :send: **Pisze na Telegramie.** Jeśli chcesz, wyśle podsumowanie sesji oraz powiadomienie, gdy coś pójdzie nie tak.

> [!note] Przykład. Araji wszedł do walki z 36% zdrowia, a po walce spadł do 8%. Bot to widzi, rozumie, że walka była zła, i albo pyta ciebie, albo sam cofa walkę i powtarza ją innym pakiem.

### Czego bot nie robi

- Przechodzi **tylko Lochy Tytanów**. Inne tryby gry są mu nieznane.
- **Nie gra „w chmurze”**. Gra działa na twoim telefonie z systemem Android, a PC z systemem Windows patrzy na ekran telefonu i klika na nim przez kabel USB. Potrzebny jest zarówno telefon, jak i komputer.
- Nie jest czarodziejem: jeśli nie ma połączenia z grą, uczciwie czeka, aż powróci, i pisze ci o tym.

### Czy to jest bezpieczne dla konta?

Bot stara się zachowywać jak żywy człowiek, a nie jak robot:

- każde kliknięcie trafia w **losowy punkt** przycisku, a nie w ten sam;
- przed kliknięciem zachowuje **pauzę reakcji** — od 0,3 do 0,8 sekundy po pojawieniu się przycisku;
- klika **nie częściej niż dwa razy na sekundę**.

> [!warning] Żaden program nie może dać pełnej gwarancji: zasady gry ustala jej wydawca. Bot nie robi niczego „nieludzko szybkiego”, ale decyzja o korzystaniu z niego należy do ciebie.

### Co dalej w podręczniku

- **Co będzie potrzebne i instalacja** — co kupić i zainstalować jeden raz.
- **Podłączamy telefon** — pierwsze uruchomienie farmienia.
- **Strona główna i mini-bar** — jak czytać okno i mały panel pod grą.
- **Pauza i zatrzymanie** — przyciski i skróty klawiszowe.
- **Kreator reguł** — jak nauczyć bota twoich paków i kolejności drzwi.
- **Gdy walka poszła źle** — okna interwencji i jak bot decyduje sam.
- **Telegram, statystyki, gdy coś poszło nie tak** — cała reszta.

> [!done] Teraz wiesz, co potrafi bot. Dalej — co trzeba zainstalować, jeden raz. [Następny rozdział →](#2)

## Co będzie potrzebne i instalacja

To robi się **jeden raz**. Potem po prostu uruchamiasz program dwukrotnym kliknięciem. Poświęć na to około piętnastu minut — dalej będzie już łatwo.

### Co musisz posiadać

- :monitor: **Komputer z systemem Windows.** Na nim działa program i bot.
- :smartphone: **Telefon z systemem Android i grą Hero Wars.** Gra działa na telefonie, a komputer patrzy na jego ekran i klika na nim.
- :terminal: **Kabel USB.** Najlepiej ten, którym ładujesz telefon i przesyłasz pliki: bywają kable „tylko do ładowania”, przez które komputer nie zobaczy telefonu.
- :folder: **Archiwum z programem** (plik `.zip`, w którym znajduje się `HeroWarsBot.exe`).

> [!note] Gra pozostaje na telefonie. Bot nie instaluje w niej niczego zbędnego i nie ingeruje w pliki gry: tylko patrzy na ekran i klika na nim tak, jak ty robiłbyś to palcem.

### Kroki A. Rozpakuj program

1. **Rozpakuj archiwum** — kliknij na nie prawym przyciskiem myszy i wybierz „Wyodrębnij wszystkie…”. Wybierz zwykły folder bez znaków specjalnych, np. `C:\HeroWarsBot`.
2. **Sprawdź, czy pliki są na miejscu** — w folderze powinien znajdować się plik `HeroWarsBot.exe` obok innych plików i folderów.

> [!warning] Najpierw rozpakuj archiwum, a dopiero potem uruchamiaj program. Jeśli otworzysz plik `.exe` bezpośrednio z archiwum, pozostałe pliki programu będą niedostępne i nie zadziała on prawidłowo.

> [!tip] Ten folder to „dom” bota. Obok `HeroWarsBot.exe` sam utworzy swoje pliki: ustawienia, statystyki, historię walk. Dlatego nie przenoś pliku `.exe` osobno od reszty plików, a jeśli zmieniasz lokalizację — przenieś cały folder.

### Krok B. Zainstaluj scrcpy

scrcpy to mały program, który pokazuje ekran telefonu w oknie na komputerze. Bot „patrzy” właśnie na to okno. Razem z nim instaluje się też **adb** — pomocnik, przez którego bot klika na ekranie telefonu.

1. **Pobierz scrcpy** — na [stronie projektu](https://github.com/Genymobile/scrcpy/releases) wybierz najnowszą wersję dla Windows (archiwum `.zip` z „win64” w nazwie).
2. **Rozpakuj archiwum** — najlepiej do zwykłego folderu bez spacji i znaków specjalnych, na przykład `C:\scrcpy`. Wewnątrz powinny znajdować się pliki `scrcpy.exe` i `adb.exe`.
3. **Dodaj folder do PATH** — dzięki temu Windows będzie wiedział, gdzie szukać tych programów. Jak to zrobić, zobacz poniżej.

**Jak dodać folder do PATH:**

1. **Otwórz ustawienia** — naciśnij klawisz Windows, wpisz „zmienne środowiskowe” i wybierz „Edytuj zmienne środowiskowe systemu”.
2. **Znajdź „Path”** — w otwartym oknie kliknij „Zmienne środowiskowe”, na górnej liście wybierz wiersz `Path` i kliknij „Edytuj”.
3. **Dodaj folder** — kliknij „Nowy”, wpisz `C:\scrcpy` (twój folder, jeśli jest inny) i zamknij wszystkie okna przyciskiem „OK”.

> [!note] PATH to lista folderów, w których Windows szuka programów, gdy wywołujesz je po nazwie. Gdy dodasz folder do listy — `scrcpy` i `adb` znajdą się z dowolnego miejsca.

### Krok C. Sprawdź, czy scrcpy został zainstalowany

1. **Otwórz „Wiersz polecenia”** — klawisz Windows, wpisz `cmd`, naciśnij Enter. Jeśli okno było otwarte przed instalacją, zamknij je i otwórz ponownie: stare okno nie wie o nowych folderach.
2. **Sprawdź scrcpy** — wpisz `scrcpy --version` i naciśnij Enter. Powinna pojawić się wersja programu.

Jeśli zamiast wersji Windows napisze „nie jest rozpoznawana jako polecenie wewnętrzne lub zewnętrzne”, oznacza to, że folder nie trafił do PATH. Wróć do kroku B i sprawdź, czy w PATH wpisany jest folder, w którym leży `scrcpy.exe`.

### Krok D. Skonfiguruj telefon

Telefon musi zezwolić komputerowi na sterowanie nim. Nazywa się to „debugowanie USB” (tryb stworzony dla twórców aplikacji). Bot używa go do klikania na ekranie.

1. **Otwórz opcje programistyczne** — wejdź w „Ustawienia” → „O telefonie” i **7 razy z rzędu** kliknij w „Numer kompilacji”. Telefon napisze, że zostałeś programistą.
2. **Znajdź „Opcje programistyczne”** — ta pozycja pojawi się w ustawieniach (czasami wewnątrz „System” lub „Dodatkowe ustawienia”).
3. **Włącz dwa ustawienia** — „Debugowanie USB” **oraz** „Debugowanie USB (ustawienia bezpieczeństwa)”.
4. **Podłącz kabel** — gdy telefon zapyta „Zezwalać na debugowanie USB z tego komputera?”, zaznacz „Zawsze zezwalaj” i kliknij „OK”.

![Sekcja „Opcje programistyczne” z dwoma włączonymi ustawieniami debugowania](images/usb_debug.png)

> [!warning] Włącz **obie** opcje. Jeśli włączona jest tylko pierwsza, obraz z telefonu trafi na komputer, ale kliknięcia nie dotrą do gry: bot będzie „klikał”, a gra niczego nie zauważy.

Teraz sprawdźmy połączenie. Podłącz telefon kablem, otwórz „Wiersz polecenia” i wpisz `adb devices`. Na liście powinien pojawić się wiersz ze słowem `device` obok numeru telefonu.

- :check: `device` — wszystko w porządku, telefon jest gotowy.
- :triangle-alert: `unauthorized` — telefon czeka na twoje pozwolenie. Spójrz na jego ekran i kliknij „Zezwól”.
- :triangle-alert: lista jest pusta — komputer nie widzi telefonu. Spróbuj użyć innego kabla lub innego gniazda USB.

### Krok E. Pierwsze uruchomienie programu

1. **Otwórz folder z programem** — ten, do którego rozpakowałeś archiwum.
2. **Kliknij dwukrotnie w `HeroWarsBot.exe`** — otworzy się okno programu.
3. **Rozejrzyj się** — po lewej stronie znajduje się pasek z sekcjami, pośrodku strona główna. Dopóki telefon nie jest podłączony, w nagłówku jest napisane «Oczekiwanie na telefon» — to normalne.

> [!tip] Zawsze uruchamiaj program z jego folderu (lub utwórz skrót do `HeroWarsBot.exe`: prawy przycisk myszy → „Wyślij do” → „Pulpit”). Wtedy odnajdzie swoje ustawienia i pliki.

> [!done] Wszystko gotowe: program rozpakowany, scrcpy i telefon skonfigurowane. Teraz podłączymy telefon i uruchomimy pierwsze farmienie. [Następny rozdział →](#3)

## Podłączamy telefon i первый farm

Teraz podłączymy telefon i uruchomimy bota po raz pierwszy — całość zajmie około pięciu minut. Na początku zapamiętaj: na monitorze będą **dwa okna**.

- :monitor: **Okno programu** — to, w którym czytasz ten poradnik. Znajdują się w nim przyciski, ustawienia i dziennik (tak nazywa się pasek wiadomości, w którym bot zapisuje to, co robi).
- :smartphone: **Okno gry** — „lustro” ekranu telefonu na monitorze, nazywa się `HeroWarsBot_Arena`. Bot „patrzy” właśnie w nie.

### Co znajduje się na stronie głównej przy pierwszym uruchomieniu

Dopóki ani razu nie zapisałeś ustawień, na stronie głównej (pierwszy przycisk na lewym pasku) znajduje się karta „Od czego zacząć” z podpisem „3 kroki · około 5 minut”.

![Pierwsze uruchomienie: karta „Od czego zacząć”, czerwony napis „Oczekiwanie na telefon…” i niebieski przycisk „Podłącz telefon”](images/connect_phone.png)

- :smartphone: **„Podłącz telefon”** — oznaczony słowem „teraz”. Gdy telefon się połączy, numer kroku zmieni się w zieloną fajkę. Tym się teraz zajmiemy.
- :sliders-vertical: **„Sprawdź paki w komnatach”** — link „Otwórz →” prowadzi do „Kreator reguł” (drugi przycisk na lewym pasku, ikona z suwakami). Tam mówisz botowi, jakimi tytanami wchodzić do każdej komnaty.
- :send: **„Skonfiguruj Telegram do SOS”** — opcjonalnie. Bot napisze do Ciebie na Telegramie, jeśli będzie potrzebował pomocy.

> [!warning] Paki są najważniejsze przed pierwszym farmem. Bot wystawia do każdej z czterech komnat (woda, ziemia, ogień i mieszana) ten pakiet, który jest zapisany w „Kreator reguł”, a Twoich tytanów nie potrafi odgadnąć. Jak to skonfigurować — opisano w sekcji o „Kreator reguł” w dalszej części poradnika. Karta „Od czego zacząć” zniknie, gdy po raz pierwszy zapiszesz ustawienia w „Kreator reguł”.

### Krok A. Podłącz telefon

1. **Przygotuj telefon** — podłącz go kablem i odblokuj ekran. Obie opcje debugowania USB muszą być włączone, tak jak w [sekcji 2](#2).
2. **Kliknij „Podłącz telefon”** — to duży niebieski przycisk po prawej stronie na górze. Dopóki program szuka telefonu, jest na nim napisane „Łączę…”. Oczekiwanie może trwać do 20 sekund.
3. **Znajdź okno gry** — pojawi się nowe okno `HeroWarsBot_Arena` z ekranem telefonu. Nie widać go? Mogło schować się za oknem programu: poszukaj go na pasku zadań na dole ekranu.
4. **Sprawdź plakietkę w nagłówku** — czerwony napis „Oczekiwanie na telefon…” powinien zmienić się na zielony: „połączono”. A niebieski przycisk zamieni się w zielony „Zacznij farmić”. (Nagłówek — górny pasek okna, plakietka — prostokąt z napisem.)

![Telefon podłączony: zielony napis „połączono”, przycisk „Zacznij farmić” i obok okno gry](images/phone_connected.png)

Okno się nie pojawiło, a w dzienniku jest napisane „Окно scrcpy не появилось или утилита не найдена!”? Sprawdź po kolei:

- :smartphone: Ekran telefonu jest odblokowany, kabel jest mocno włożony. Spróbuj innego gniazda USB.
- :terminal: W wierszu poleceń `adb devices` pokazuje słowo `device` obok Twojego telefonu. Jeśli jest tam `unauthorized` — zezwól na debugowanie na ekranie telefonu.
- :terminal: W wierszu poleceń `scrcpy --version` odpowiada wersją. Nie odpowiada? Folder ze scrcpy nie trafił do PATH — wróć do [sekcji 2](#2). Po edycji PATH program należy zamknąć i otworzyć ponownie.

### Krok B. Wejdź do korytarza Podziemi

Podziemia tytanów — tryb gry, w którym schodzisz po piętrach i w każdej komnacie walczysz z wrogami. **Korytarz** — ekran między walkami: widać na nim drzwi z chorągiewką i nic więcej nie jest otwarte. Bot zaczyna właśnie od korytarza.

1. **Otwórz grę** — na telefonie uruchom Hero Wars i wejdź do Podziemi tytanów.
2. **Wejdź do korytarza** — jeśli trwa walka, dokończ ją sam i zamknij okno wyniku. Potrzebny jest spokojny ekran z drzwiami i chorągiewką.

![Korytarz Podziemi tytanów: przy drzwiach widać chorągiewkę](images/dungeon_corridor.png)

> [!warning] Nie uruchamiaj farmu w trakcie walki. Najpierw bot przegląda ekran i porządkuje sytuację: jeśli zobaczy walkę — wycofa się z niej; jeśli zobaczy okno wyniku z przyciskiem „Jeszcze raz” — anuluje tę walkę i zagra komnatę ponownie; jeśli zobaczy wybór drużyny — przeprowadzi walkę i natychmiast ją anuluje. Będzie potem działać, ale Twoje zwycięstwo przepadnie na marne.

### Krok C. Rozpocznij farm

> [!warning] **Język programu musi быть taki sam jak język gry.** Przyciski z napisami („Атаковать”, „ОК”, „Ещё раз”) oraz chorągiewkę przy drzwiach bot rozpoznaje po obrazkach w tym języku, który został wybrany w programie. Jest to przycisk z dwoma literami („RU”) na dole lewego paska. Jeśli gra jest po rosyjsku — w programie musi być ustawione „RU”. Jeśli języki są różne, bot po prostu nie znajdzie przycisków.

1. **Kliknij „Zacznij farmić”** — zielony przycisk w miejscu „Podłącz telefon”. Program sam dostosuje okno gry do odpowiedniego rozmiaru i umieści je w lewym górnym rogu ekranu.
2. **Nie bój się, że okno programu zniknęło** — zwinęło się na pasek zadań, a pod grą pojawił się wąski pasek — **mini-pasek**. Widać na nim, co robi bot. Aby przywrócić okno: ikona „Rozwiń okno programu” na mini-pasku (najechać myszką — pojawi się podpowiedź) lub przycisk na pasku zadań.
3. **Obserwuj grę** — po kilku sekundach bot kliknie drzwi i rozpocznie się pierwsza komnata. Jedna komnata zajmuje około pół minuty — minutę.
4. **Zapamiętaj, jak zatrzymać bota** — klawisz F10 zatrzymuje go natychmiast, F9 wstrzymuje (bot dokończy komnatę i poczeka). Klawisze działają, gdy aktywne jest okno gry lub okno programu.

Po rozwinęciu okna programu zajrzyj do dziennika. Przed każdym wierszem znajduje się tam czas — pominęliśmy go. Oto co powinno się pojawić:

- `[УМНЫЙ СТАРТ] Сканирую экран для восстановления контекста...` — bot rozgląda się.
- `[УМНЫЙ СТАРТ] Контекст не требует экстренных действий. Начинаю с HALLWAY.` — wszystko w porządku, zaczyna od korytarza („HALLWAY” to „korytarz” po angielsku).
- `[СТАТИСТИКА] Комнат: 1` — pierwsza komnata ukończona. Wszystko działa!
- :triangle-alert: `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` — bot czeka, aż okno gry znowu stanie się główne. Kliknij je myszką, a praca będzie kontynuowana.

Minęła minuta, a bot nic nie klika? Sprawdź:

- :gamepad-2: W grze jest teraz korytarz Podziemi tytanów, a nie menu, sklep czy walka.
- :globe: Język programu zgadza się z językiem gry (ostrzeżenie wyżej).
- :maximize-2: Okno gry jest w całości na ekranie: nie jest rozciągnięte, rozciągnięte/zmaksymalizowane, nie wyjechało za krawędź. W przeciwnym razie zatrzymaj bota (F10), kliknij „Resetuj rozmiar okna gry” i zacznij od nowa.
- :terminal: W dzienniku nie ma wierszy z „[ОШИБКА]”. Jeśli są — przeanalizujemy je w sekcji „Jeśli coś poszło nie tak”.

### Gdy bot działa

- :monitor: Okno gry musi być widoczne: nie zasłaniaj go innymi oknami i nie minimalizuj. Kliknąłeś w inne okno — bot zatrzyma się i poczeka.
- :smartphone: Nie zamykaj okna gry i nie szarp za kabel. Okno zniknęło — program sam zatrzyma bota („Окно scrcpy закрыто — останавливаю бота”).
- :maximize-2: Nie rozciągaj ani nie maksymalizuj okna gry: bot mierzy je podczas uruchamiania i dalej korzysta z tej miary.
- :gamepad-2: Nie klikaj samodzielnie na ekranie telefonu: bot klika przez ADB i będziemy sobie przeszkadzać. Chcesz pograć ręcznie — wstrzymaj bota (F9) i poczekaj, aż stanie w korytarzu.
- :triangle-alert: Nie blokuj komputera (Win+L): na zablokowanym komputerze bot nie widzi ekranu i czeka, aż wrócisz.
- :moon: Do nocnego farmu wyłącz uśpienie komputera: w „Ustawieniach” Windows otwórz „System” → „Zasilanie” i dla ekranu oraz uśpienia wybierz „Nigdy”. Uśpiony lub wygaszony monitor to to samo co zablokowany: bot zatrzyma się i będzie czekać. Nazwy opcji zależą od wersji systemu Windows.

### Przyciski w nagłówku

Po prawej stronie na górze, obok plakietki, znajdują się trzy ikony. Najechanie myszką na którąkolwiek spowoduje wyświetlenie podpisu.

![Nagłówek okna: plakietka telefonu, trzy przyciski i przyciski okna](images/header_buttons.png)

- :moon: **„Wyłącz экран телефона”** — gasi ekran telefonu, ale gra toczy się dalej i bot wszystko widzi. Wygodne w nocy: mniejsze obciążenie ekranu i baterii. Program wysuwa okno gry na przód i wciska w nim Alt+O (w ten sposób scrcpy gasi ekran). Przywrócenie ekranu — przyciskiem włączania w telefonie. Także na mini-pasku znajduje się taki przycisk.
- :refresh-cw: **„Uruchom ponownie scrcpy”** — zamyka okno gry i otwiera je na nowo. Przydaje się, jeśli obraz z telefonu zamarł. Działa tylko z oknem, które uruchomił sam program. Nie klikaj go, gdy bot działa: zniknięte okno program uzna za zerwanie połączenia i zatrzyma bota.
- :maximize-2: **„Resetuj rozmiar okna gry”** — przywraca oknu `HeroWarsBot_Arena` rozmiar 1606 × 748 i umieszcza je w lewym górnym rogu. Jest to wzorcowy rozmiar: pod niego skonfigurowano wyszukiwanie przycisków. Jeśli rozciągnąłeś lub zmaksymalizowałeś okno — kliknij przycisk przed „Zacznij farmić” (chociaż „Zacznij farmić” robi to samo automatycznie). Okno jest szerokie: na monitorze Full HD (1920 × 1080) mieści się w całości, a bot widzi tylko to, co znajduje się na ekranie.

### Okno programu bez ramki Windows

Okno programu nie ma zwykłej ramki Windows, dlatego ma własne przyciski, po prawej stronie na górze za cienką linią:

- :minus: **„Minimalizuj”** — ukrywa okno na pasek zadań.
- :square: **„Maksymalizuj”** — okno na cały ekran; potem przycisk nazywa się „Przywróć rozmiar”. Dwukrotne kliknięcie nagłówka robi to samo.
- :x: **„Zamknij”** — zamyka program, a wraz z nim okno gry, jeśli zostało przez niego otwarte. Jeśli bot działa, najpierw zapyta „Zatrzymać bota?”; przycisk „Zatrzymaj i zamknij” zatrzyma go natychmiast, a podsumowanie sesji nie zostanie wysłane na Telegram.
- :grip-vertical: **Przesuwanie okna** — za nagłówek: za puste miejsce na górze lub za tytuł.
- **Zmiana rozmiaru** — za róg po prawej stronie na dole (trzy ukośne kreski). Okno nie stanie się bardzo małe.

> [!note] Nie myl „Minimalizuj” i „Zwiń do mini-paska”. „Minimalizuj” po prostu chowa okno na pasek zadań. „Zwiń do mini-paska” — to przycisk na stronie głównej, gdy bot działa: dodatkowo pokazuje mini-pasek pod grą.

> [!done] Telefon jest podłączony, bot przeszedł pierwszą komnatę — podstawa jest gotowa. Dalej dowiemy się, co pokazuje strona główna i jak czytać dziennik. [Następna sekcja →](#4)

## Strona główna i dziennik

Strona główna — to pierwszy przycisk na lewym pasku i to ją widzisz najczęściej. Przypomina deskę rozdzielczą w samochodzie: na górze — liczby („dokąd jedziemy” i „jak jedziemy”), na dole — dziennik, w którym bot sam pisze, co robi. Przeanalizujmy, co gdzie leży i jak nie pogubić się w wierszach dziennika.

### Karta na górze: sama zmienia wygląd

W górnej części strony głównej znajduje się jedna duża karta, ale pokazuje różne rzeczy — w zależności od tego, co dzieje się z botem:

- :sliders-vertical: **«Konfiguracja startu»** — bot stoi, a ustawienia są już zapisane. To informacje „z czym bot pójdzie do walki”: cel, tryb i progi.
- :activity: **«Bieżąca sesja»** — bot pracuje. Na żywo wyświetlane liczby: ile zebrano, ile ukończono, ile czasu minęło.
- :file-text: **«Podsumowanie sesji»** — bot zatrzymał się. Karta pokazuje, co udało się osiągnąć i dlaczego się zatrzymał.
- :list: **«Od czego zacząć»** — tylko wtedy, gdy ani razu nie zapisałeś ustawień (opisana w [rozdziale 3](#3)).

Sesja — to jedno uruchomienie bota: od «Zacznij farmić» do zatrzymania.

### Konfiguracja startu

Cztery plakietki, z których każda odpowiada na jedno pytanie. Liczby pochodzą z twoich ustawień, więc jeśli coś ci się nie podoba, kliknij «Zmień w kreatorze reguł →» po prawej stronie u góry karty: otworzy się «Kreator reguł».

![Strona główna przed uruchomieniem: karta „Konfiguracja startu” i pusty dziennik](images/main_config.png)

- :target: **«Cel sesji»** — kiedy bot powinien się zatrzymać. Cel jest **jeden**: tytanit, komnaty, piętra lub czas. Jeśli w ustawieniach podano kilka, bierze się pierwszy w kolejności „tytanit → komnaty → piętra → czas”. Nic nie zmieniałeś — celem jest 120 tytanitu, co daje 10–20 komnat. «Bez limiту» oznacza, że wszystkie cele wynoszą zero i bot będzie szedł, dopóki go nie zatrzymasz.
- :shield-check: **«Tryb»** — plakietka «Bot decyduje sam» z adnotacją «WŁ» lub «WYŁ». Włączone: przy złej walce bot sam powtórzy walkę innym pakiem. Wyłączone: wezwie ciebie. Szczegóły — w sekcjach dotyczących «Kreatora reguł».
- :heart-pulse: **«Próg paniki PŻ»** — na przykład 40%. Jeśli po walce u któregokolwiek z tytanów zostało mniej zdrowia, walka uważana jest za złą. Pak — to drużyna pięciu tytanów; PŻ — zdrowie.
- :calendar: **«Reset dnia»** — na przykład 05:00. Od tej godziny w grze rozpoczyna się nowy dzień: bot liczy statystyki za dzień i zapomina, ile zdrowia tytani mieli wczoraj.

> [!note] Bot odczytuje ustawienia **jeden raz, gdy naciskasz «Zacznij farmić»**. Zmieniłeś coś w trakcie pracy — bot dowie się o tym dopiero przy następnym uruchomieniu. Dlatego podczas pracy bota na karcie pokazywane są dokładnie te ustawienia, z którymi wystartował.

### Bieżąca sesja

Gdy bot jest uruchomiony, karta zmienia się w «Bieżącą sesję». Po prawej stronie u góry świeci się stan:

- :activity: **«Farmienie trwa»** — wszystko w porządku, bot pracuje.
- :pause: **«Pauza»** — nacisnąłeś «Pauza» (lub bot sam przeszedł w miękką pauzę). Przycisk zmienił się na «Kontynuuj».
- :triangle-alert: **«Czeka na twoją decyzję»** — na ekranie okno «Wymagana interwencja», bot czeka na odpowiedź.
- :refresh-cw: **«Uruchamiam bota…»** — pierwsze sekundy po kliknięciu «Zacznij farmić».

![Farmienie trwa: plakietki sesji z paskami postępu celu](images/main_session.png)

Plakietki są cztery:

1. **«Tytanit w sesji»** — ile tytanitu bot zebrał. To **wynik, a nie odczyt z ekranu**: 6 za komnatę i 12, jeśli w grze świeci się ikona „x2”. Jeśli celem jest tytanit, obok pojawią się wartości „zebrano / potrzeba”, procenty i pasek.
2. **«Piętra ukończone»** — piętro zalicza się, gdy bot odebrał nagrodę przy punkcie zapisu (tak nazywa się miejsce na końcu piętra, gdzie naciska się „Aktywuj” i „Odbierz”). Obok napisane jest, do jakich drzwi wchodził jako ostatnich: woda, ziemia, ogień czy mieszana.
3. **«Walki w sesji»** — na przykład «12 zwycięstw z 14». Zwycięstwo — zaliczona komnata. Cofnięcie — walka, którą bot powtórzył: ona też liczy się jako walka, dlatego „łącznie” bywa więcej niż „zwycięstw”.
4. **«Czas sesji»** — godziny:minuty:sekundy i drobnym drukiem «komnata średnio 28 s». Średnia liczona jest po komnatach, bez postoju przy punkcie zapisu.

> [!tip] Jeśli celem są komnaty lub czas, procenty znajdują się po prawej stronie w formie „35% z 100” lub „35% z 120 min” — w samą liczbę cel się nie mieści. Pasek pod plakietką jest taki sam.

> [!note] Gdy cel zostanie osiągnięty, bot nie porzuca piętra w połowie. Napisze w dzienniku `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.`, przejdzie pozostałe komnaty i zatrzyma się przed punktem zapisu, nie naciskając „Aktywuj”: nagrodę za piętro odebierze w pierwszej kolejności przy następnym uruchomieniu. Wyjątek — cel dotyczący pięter: wtedy bot zatrzymuje się natychmiast po nagrodzie.

### Podsumowanie sesji

Bot zatrzymał się — karta pokazuje podsumowanie, a okno samo rozwija się z mini-paska. Na górze wpisana jest przyczyna zatrzymania: przycisk «STOP», zamknięte okno scrcpy, zwykłe zakończenie pracy lub to, co bot napisał sam (na przykład, że cel został osiągnięty).

![Podsumowanie sesji: przyczyna zatrzymania, liczby i przycisk „Szczegóły”](images/main_summary.png)

Te same cztery plakietki co w sesji, ale teraz są to ostateczne liczby; w sekcji «Walki» dodano „okien SOS: N” (ile razy bot ciebie wzywał). Przycisk **«Szczegóły»** otwiera okno z pełnym raportem bota: średnie czasy na etapach, najdłuższe komnaty, ile było cofnięć i ile z nich bot wykonał **bez ciebie**. Ikona ✕ po prawej ukrywa podsumowanie i zamiast niego znowu widać «Konfigurację startu». Klikniesz «Zacznij farmić» — podsumowanie zniknie samo.

> [!note] Jeśli Telegram jest skonfigurowany, podsumowanie trafi tam samo przy każdym zwykłym zatrzymaniu. Przycisk «STOP» (F10) zabija bota błyskawicznie, dlatego podsumowanie na Telegramie w tym przypadku nie zostanie wysłane.

### Dziennik: co w nim jest i jak czytać

Dolna część strony głównej — to **«Dziennik pracy»**. Bot zapisuje w nim każdy swój krok, a program pokazuje to w oknie. Nie bój się liczby wierszy: nie musisz czytać wszystkiego, dziennik jest potrzebny, gdy coś poszło nie tak lub gdy po prostu jesteś ciekawy.

Każdy wiersz zbudowany jest tak samo:

`10:26:17.486 [НАВИГАЦИЯ] Двери (слева направо): EARTH (0.98), FIRE (0.97)`

1. **Czas** — na szaro. Godziny:minuty:sekundy i tysięczne części sekundy.
2. **Etykieta w nawiasach kwadratowych** — „kto mówi” i w jakiej sprawie. Jest pokolorowana: kolor podpowiada, do jakiej sekcji dziennika należy wiersz.
3. **Tekst** — co dokładnie się stało. Długi wiersz jest przenoszony, a ciąg dalszy ustawia się pod tekstem, a nie pod czasem.

Wiersz bez etykiety (na przykład ` ---> HYPERION: ХП 100%, Энергия 79%`) — to kontynuacja wiersza powyżej i znajduje się w tej samej sekcji.

### „Pigułki”-filtry

Nad dziennikiem znajduje się pięć przycisków-„pigułek”. Kliknij jeden — a w dzienniku zostaną tylko wiersze z tej sekcji. Wybór jest zapamiętywany: otworzysz program jutro, ta sama pigułka będzie wybrana.

![Dziennik z pigułkami „Wszystko”, „Walki”, „Reguły”, „System” i „Błędy”](images/journal_pills.png)

- **«Wszystko»** — wszystko po kolei.
- **«Walki»** (zielone etykiety) — przebieg: komnaty, czas, zdrowie tytanów, cofnięcia. Etykiety `[КОМБАТ]`, `[СТАТИСТИКА]`, `[ВРЕМЯ]`, `[СОСТОЯНИЕ]`, `[АНАЛИЗАТОР]`, `[ОТКАТ]`, `[ЛИМИТ]`, `[ИТОГ]`.
- **«Reguły»** (żółte etykiety) — decyzje bota: jaki pak ustawić, dlaczego cofnął walkę, co zapamiętał. Etykiety `[ТАКТИКА]`, `[КОМАНДА]`, `[ПРАВИЛА]`, `[ОБУЧЕНИЕ]`, `[SOS_CLOSE]`.
- **«System»** (jasnoniebieskie etykiety) — cała reszta: korytarz i drzwi (`[НАВИГАЦИЯ]`), uruchomienie (`[УМНЫЙ СТАРТ]`), połączenie. Wiersze samego programu z etykietą `[GUI]` są szare, ale znajdują się również tutaj.
- **«Błędy»** (czerwone etykiety) — wszystko, co wymaga uwagi: `[ОШИБКА]`, `[ВНИМАНИЕ]`, `[СТОРОЖ]`, `[SOS]`. Obok nazwy znajduje się liczba — ile takich wierszy się zebrało.

> [!warning] Czerwona liczba przy «Błędy» — to nie zawsze awaria. Trafia tam również `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` — bot po prostu czeka, aż przywrócisz okno gry na pierwszy plan. Czytaj tekst wiersza, a nie bój się koloru.

### Przykłady prawdziwych wierszy

Oto wiersze z realnej sesji bota (czas dla zwięzłości pominięto). Naucz się czytać te pięć — a zrozumiesz każdy dziennik.

- `[НАВИГАЦИЯ] Выбрана комната EARTH (порядок: water → mix → earth → fire)` — bot wybrał drzwi ziemi. W nawiasie — twoja kolejność drzwi. Liczba w wierszu „Двери (слева направо)” powyżej — jak bardzo bot jest pewny, że rozpoznał drzwi (1 — absolutnie).
- `[ВРЕМЯ] Комната 2 (earth): коридор 12.8 с | сборка 3.3 с | бой 8.0 с | результат 9.1 с | всего 33.2 с` — raport o komnacie: ile czasu poszło na drogę do drzwi, złożenie drużyny, walkę i zamknięcie okna wyniku.
- `[СТАТИСТИКА] Комнат: 3 | Титанит: 36` — trzecia komnata ukończona, zebrał 36 tytanitu. Te liczby trafiają na plakietки sesji.
- `[ТАКТИКА] Откатываю бой сам и переиграю паком [...] (взят: ваш список запасных паков).` — walka wyszła zła i bot (w trybie «Bot decyduje sam») powtarza ją zapasowym pakiem. Jeśli zapasowy sobie poradzi: `[ТАКТИКА] Запасной пак [...] справился. Запоминаю его против этих врагов.`
- `[ОТКАТ] Запускаю протокол отката боя...` — początek cofnięcia: „Jeszcze raz” → pauza → „Wycofaj się”. Każdy taki wiersz dodaje jedną walkę na plakietce «Walki w sesji».

> [!tip] Na początku każdej sesji bot pisze `[ТАКТИКА] Плохой бой: ХП ниже 30% | потеря больше 60% | ...` — progi, według których będzie oceniał walki. Jeśli coś poszło „nie tak, jak się spodziewałeś”, najpierw porównaj ten wiersz ze swoimi ustawieniami.

### Przyciski pod dziennikiem

![Przyciski pod dziennikiem: „Zapisz log”, „Wyślij log autorowi”, „Wyczyść”](images/journal_buttons.png)

- :save: **«Zapisz log»** — zapisze cały dziennik do pliku tekstowego. Program sam zaproponuje nazwę `gui_log_...txt` oraz folder `bot_data/logs`; możesz wybrać inny.
- :mail: **«Wyślij log autorowi»** — najpierw to samo zapisanie, potem otworzy się twój program pocztowy z gotową wiadomością. **Plik do wiadomości dołącz sam** (oraz `battle_log.csv` z tego samego folderu): program nie może tego zrobić. Nie masz programu pocztowego? Napisz do autora na adres z sekcji «O programie».
- :x: **«Wyczyść»** — usuwa wiersze z okna, ale najpierw zapyta «Wyczyścić dziennik?». To bezpieczne: pełny log bot sam zapisuje w folderze `bot_data/logs`, a liczby sesji nie są resetowane.

Zaznaczyć tekst w dzienniku można myszką, skopiować — Ctrl+C lub prawym przyciskiem myszy («Kopiuj»). Zmieniać dziennika nie można — jest tylko do odczytu. Jeśli przwinąłeś dziennik do góry, aby poczytać, nie „ucieknie” on w dół z nowymi wierszami; przewiń do końca — a znowu zacznie przesuwać się razem z botem.

> [!note] Okno pamięta ostatnie 50 000 wierszy, a pokazuje 4000 ostatnich — inaczej przy długim farmieniu zacząłby zacinać. Cała reszta znajduje się w pliku `bot_data/logs/bot_log_...txt`: bot prowadzi go sam i zapisywanie dziennika ręcznie zazwyczaj nie jest potrzebne.

Dopóki dziennik jest pusty, w jego miejscu widnieje napis «Dziennik jest pusty». Wiersze pojawią się po podłączeniu telefonu. Pusta pigułka pisze «Na razie pusto» oraz «Takich wierszy jeszcze nie było» — dla «Błędy» to dobra wiadomość.

> [!done] Teraz czytasz stronę główną jak deskę rozdzielczą: wiesz, co oznaczają plakietki i kolory etykiet dziennika. Dalej — mini-bar, mały panel pod grą. [Następny rozdział →](#5)

## Mini-pasek pod grą

Gdy bot pracuje, główne okno programu zazwyczaj nie jest ci potrzebne. Dlatego samo znika na pasku zadań, a pod obrazem gry pojawia się wąski panel — **mini-pasek**. To jak deska rozdzielcza w samochodzie: rzutem oka widać, czy bot jedzie, co robi teraz, ile już przeszedł i czy cię nie wzywa.

![Mini-pasek pod oknem gry podczas farmienia](images/mini_bar.png)

### Kiedy się pojawia i где stoi

- :monitor: **Pojawia się sam.** Bot wystartował („Zacznij farmić”) — okno programu się zwija, a pod grą pojawia się mini-pasek. Jeśli rozwinąłeś okno programu i chcesz je znowu schować, gdy bot pracuje — kliknij „Zwiń do mini-paska” na ekranie głównym.
- :smartphone: **Stoi tuż pod grą** i ma dokładnie tę samą szerokość, co obraz gry. Gdy przesuwasz okno gry — mini-pasek podąża za nim (program sprawdza to dwa razy na sekundę).
- :eye: **Nie zasłania gry ani o piksel.** To ważne: bot „patrzy” na ekran, robiąc zrzuty okna. Gdyby panel zasłonił grę, bot zobaczyłby go zamiast przycisków.
- :maximize-2: **Brak места на dole** (okno gry przy dolnej krawędzi ekranu) — panel ustawi się nad nagłówkiem okna. Jeśli tam też nie ma miejsca — nie pojawi się, a okno programu pozostanie na pasku zadań. Gdy zwiniesz okno gry — panel się schowa i wróci razem z nim.

> [!tip] Nie widać mini-paska, a bot pracuje? Przesuń okno gry wyżej: pod nim potrzeba około 100 pikseli wolnego miejsca. Przesuwać okno można, ale zmieniać jego rozmiaru nie wolno (omawialiśmy to w sekcji 3).

### Co jest na panelu: pięć kolumn od lewej do prawej

- :activity: **Stan.** Słowo i kolorowa kropka, która „oddycha”, gdy wszystko jest w porządku: „START”, „FARMA TRWA”, „PAUZA”, „PAUZA DEBUGOWANIA” lub czerwone „SOS”. Poniżej — **co bot robi в tej chwili** i ile sekund: na przykład „Bitwa · Ogień · 12 s”. Potem „Komnat: 12 · pięter: 2” oraz czas sesji, na przykład „Czas 00:42:17”.
- :target: **Cel.** Nazwa celu, ile zrobiono, ile potrzeba i pasek postępu. Poniżej — „~28 s na komnatę” (średni czas; przed pierwszą komnatą jest tam „czas komnaty — po pierwszej”) oraz prognoza „do celu ≈ 1 godz. 10 min”. Prognozę bot liczy na podstawie prędkości **tej** sesji, dlatego na początku się waha, a potem stabilizuje. Gdy nie ma celu („Bez limitu”) — paska nie ma, a zamiast prognozy wyświetla się „≈ N tytanitu na godzinę”.
- :heart-pulse: **Zdrowie drużyny.** Kwadraty tytanów z ostatniej bitwy i ich PŻ po niej — w takiej kolejności, w jakiej stoją na ekranie gry. Przed pierwszą bitwą widnieje napis „jeszcze nie było bitew”. Kolor cyfry podpowiada: czerwony — PŻ poniżej progu paniki (ogólnego lub indywidualnego), żółty — poniżej progu leczenia tytana, zwykły kolor — wszystko w normie. Myślnik „—” oznacza, że nie udało się odnaleźć ikony tytana w oknie wyniku.
- :list: **Zdarzenia.** Cztery ostatnie wiersze, najnowszy na górze i nieco większy. Po lewej kolorowy znacznik, po prawej czas.
- :gamepad-2: **Przyciski.** Cztery przyciski ułożone w kwadrat 2×2.

### Co bot может „robić teraz”

W первой kolumnie bot sam podaje swój etap. Oto co oznaczają te słowa:

- **„Korytarz”**, **„Wybór drzwi”**, **„Ustawianie drużyny”**, **„Bitwa”**, **„Okno wyniku”** — zwykły cykl jednej komnaty. Do etapów „Ustawianie drużyny”, „Bitwa”, „Okno wyniku” oraz „Odwrót” dopisywany jest żywioł komnaty: „Bitwa · Woda · 12 s”.
- **„Punkt zapisu”** — piętro zaliczone, bot odbiera nagrodę.
- **„Odwrót”** — bitwa poszła źle, bot wycofuje się i przygotowuje powtórkę.
- **„Sprawdza ekran”** — po uruchomieniu bot rozgląda się i decyduje, od czego zacząć (to „inteligentny start”).
- **„Pauza w korytarzu”**, **„Czeka na twoją decyzję”**, **„Grasz sam”** — bot stoi, ponieważ wcisnąłeś pauzę, zapytał cię o coś lub wybrałeś „Przejdź ręcznie”.
- **„Czeka na okno gry”** i **„Czeka na połączenie”** — bot czeka: albo gra nie jest na pierwszym planie (patrz niżej), albo brak połączenia z serwerem gry.

Jeśli ten sam napis utrzymuje się dłużej niż zwykle — liczba sekund po prawej rośnie i podpowiada, że bot tak naprawdę stoi.

### Zdarzenia: znaczniki i co oznaczają

Znacznik po lewej pokazuje, czego dotyczy zdarzenie:

- **Nazwa żywiołu** („Woda”, „Ziemia”, „Ogień”, „Mieszana”) — komnata zaliczona. Wiersz typu „Komnata 45 zaliczona · 28 s · najmniej PŻ: Araji 36%” mówi, ile sekund zajęła komnata i kto pozostał z najniższym zdrowiem.
- **„Piętro”** — piętro zaliczone („Piętro zaliczone, razem 3”).
- **„Odwrót”** — bitwa jest powtarzana. **„SOS”** — powód wezwania prostymi słowami.
- **„Pauza”** — „Pauza: bot dokończy bitwę i poczeka”, a potem „Bot czeka w korytarzu”.
- **„Bot”** — „Bot uruchomiony”, „Pauza zdjęta, bot gra dalej”, „Brak odpowiedzi od 10 min — bot zdecydował sam”.
- **„Limit”** — sesja osiągnęła cel, bot dokańcza grę do punktu zapisu.
- **„Uwaga”** — „Okno gry nieaktywne — bot czeka. Kliknij grę”.
- **„Błąd”** — tekst błędu tak, jak napisał go bot.

Długie wiersze są skracane wielokropkiem. Pełny tekst jest zawsze dostępny w dzienniku na ekranie głównym.

### Przyciski

Najedź myszą — pojawi się podpis. Wszystkie przyciski robią to samo, co ich odpowiedniki na ekranie głównym i w nagłówku.

- :pause: **Pauza / Kontynuuj** — „Miękka pauza: bot dokończy walkę i poczeka (F9)”. Podczas pauzy ikona zmienia się w zielony trójkąt, a ten sam przycisk wznawia grę. Gdy bot dopiero startuje, przycisk jest niedostępny.
- :square-filled: **STOP** — „Awaryjny stop: bot zatrzyma się od razu, bez podsumowania w Telegramie (F10)”.
- :moon: **Ekran telefonu** — „Wyłącz ekran telefonu”, gra toczy się przy tym dalej.
- :maximize-2: **Maksymalizuj** — „Rozwiń okno programu”. Mini-pasek zniknie. Ten sam rezultat daje przycisk okna programu na pasku zadań. Chcesz przywrócić panel — kliknij przycisk „Zwiń do mini-paska” na ekranie głównym.

> [!note] Gdy bot wzywa cię, mini-pasek czerwienieje, a okno „Wymagana interwencja” pojawia się samo, na środku obrazu gry — nie musisz rozwijać okna programu. Pierwszy przycisk w tym momencie nie włącza pauzy ani nie „kontynuuje”: pokazuje okno SOS, jeśli znalazło się ono pod innymi oknami (podpis — „Pokaż okno SOS: bot czeka na twoją decyzję”). Gdy odpowiesz w oknie — mini-pasek wraca do normy. Jak odpowiadać, omówimy w sekcji o oknach SOS.

![Mini-pasek podczas SOS](images/mini_bar_sos.png)

### Główna zasada: bot работает tylko wtedy, gdy gra jest na первом planie

Bot robi zrzuty ekranu i szuka na nich przycisków. Jeśli na grę nałoży się inna przeglądarka, komunikator lub eksplorator plików, na zrzucie pojawią się one, a nie gra: bot może kliknąć „nie tam, где треба”. Dlatego gdy tylko aktywne staje się inne okno, zatrzymuje się i czeka. W dzienniku pojawia się wiersz «[ВНИМАНИЕ] Окно игры перекрыто … Бот ждет фокуса…», w mini-pasku — znacznik «Uwaga» i etap «Czeka na okno gry». Kliknąłeś w grę — «[ИНФО] Окно снова активно. Продолжаем работу.»

- :monitor: **Kliknięcia w mini-pasek nie zatrzymują bota.** Mini-pasek został zaprojektowany tak, aby nie stawać się aktywnym oknem: gra pozostaje „główna”, dopóki wciskasz przyciski na panelu.
- :triangle-alert: **„Maksymalizuj” zatrzymuje bota na chwilę.** Okno programu stało się aktywne, a gra nie — bot zatrzyma się na najbliższym kroku. Gdy skończysz, kliknij okno gry, a bot pójdzie dalej. Czasu takiego oczekiwania strażnik nie uważa za „zawieszenie”.
- :gamepad-2: Chcesz pracować przy komputerze, gdy bot farmi? Otwieraj inne okna **obok**, a nie na grze, i nie klikaj w nie. Albo odłóż sprawę do pauzy (F9).

> [!warning] Klawisze skrótu F9 i F10 działają tylko wtedy, gdy aktywne jest okno gry lub okno programu. Wcisnąłeś F10 w przeglądarce — bot się nie zatrzyma: klawisze nie reagują, gdy zajmujesz się czymś innym. Więcej szczegółów — w sekcji o pauzie i zatrzymaniu.

> [!done] Teraz czytasz mini-pasek jak deskę rozdzielczą i wiesz, dlaczego nie wolno chować gry pod innymi oknami. Dalej — pauza, zatrzymanie i klawisze skrótu. [Następna sekcja →](#6)

## Pauza, zatrzymanie i klawisze skrótu

Bot chodzi po Lochach sam, ale czasami треба go zwolnić: chcesz zagrać ręcznie, odejść w swoich sprawach lub po prostu zakończyć. Do tego służą **cztery sposoby**, które różnią się tym, **jak łagodnie** bot się zatrzymuje. Wyobraź sobie samochód: „pauza” to zjechanie na pobocze i wyłączenie silnika, a „awaryjny stop” to wyciągnięcie kluczyka w trakcie jazdy. Oba działają, ale w różny sposób.

### Miękka pauza: „Pauza F9”

Najbardziej oszczędny sposób. Kliknij przycisk „Pauza” na ekranie głównym, na mini-pasku lub wciśnij klawisz **F9**.

1. **Wciśnij „Pauza” lub F9.** W dzienniku pojawi się wiersz `[GUI] Сигнал 'Мягкая пауза' отправлен. Бот остановится перед следующей дверью.`
2. **Poczekaj, aż bot skończy komnatę.** Bitwy, która już trwa, nie porzuca: dokończy ją, zamknie okno wyniku i zapisze podsumowanie komnaty.
3. **Bot zatrzymuje się w korytarzu.** W dzienniku: `[МЯГКАЯ ПАУЗА] Бот ждет в коридоре...`. Stan na ekranie głównym — „Pauza”, na mini-pasku — „PAUZA”, a przycisk zmienił się na zielony „Kontynuuj”.
4. **Zrób co musisz i kliknij „Kontynuuj” (lub ponownie F9).** Bot pisze `[ИНФО] Пауза снята. Кэш составов и здоровья очищен. Включаю механизм Умного Старта.` i idzie dalej.

> [!note] „Pamięć podręczna wyczyszczona” oznacza, że bot **zapomniał**, какие drużyny były ustawione i ile zdrowia mieli tytani: gdy zajmowałeś się grą, wszystko mogło się zmienić. Przed następną bitwą ponownie spojrzy na ekran wyboru drużyny i odczyta z niego zdrowie. „Inteligentny start” to sytuacja, w której bot najpierw sprawdza, co aktualnie znajduje się na ekranie, a dopiero potem decyduje, co zrobić (na przykład zamyka zapomniane okno wyniku).

- :eye: **Podczas pauzy można patrzeć na telefon i zmieniać ustawienia w oknie programu.** Ale ustawienia bot weźmie dopiero przy następnym „Zacznij farmić” (szczegóły w sekcji o ekranie głównym).
- :door-open: **Jeśli coś kliknąłeś w grze — przywróć ją do korytarza Lochów** (gdzie widać chorągiewkę przy drzwiach), a potem kliknij „Kontynuuj”. W ten sposób bot na pewno zrozumie, gdzie się znajduje.
- :gauge: **Czas płynie również podczas pauzy.** Jeśli celem sesji jest czas („120 minut”), pauza zużyje część tego czasu. Za to „strażnik” (ten, kto pilnuje, czy bot się nie zawiesił) nie wlicza czasu pauzy i nie podniesie alarmu.

> [!tip] Chcesz odejść na noc lub na dłużej? Miękka pauza nie jest do tego potrzebna: ustaw cel (tytanit, komnaty, piętra lub czas) na ekranie głównym, a bot sam dojdzie do punktu zapisu, zatrzyma się i wyśle podsumowanie.

### Kiedy bot włącza pauzę sam

Czasami bot prosi o pomoc i sam przechodzi w stan miękkiej pauzy. Wtedy przycisk również pokazuje „Kontynuuj”, a w dzienniku pojawia się `[ВНИМАНИЕ] Бот на мягкой паузе: ...` z podaniem przyczyny. Dzieje się tak, gdy:

- bot trzy razy z rzędu nie przeszedł żadnej komnaty w ciągu 5 minut (strażnik uznał, że się zawiesił);
- odwrót z bitwy nie powiódł się (ekran nie został rozpoznany, przyciski nie zostały wciśnięte);
- bitwa w ogóle się nie rozpoczęła, nawet po długim oczekiwaniu;
- nie odpowiedziałeś na okno „Brak pasującego paku”, a brakuje drużyny zapasowej.

W takich przypadках najpierw **spójrz na ekran telefonu**, napraw to, co uległo awarii (zamknij zbędne okno, wróć do korytarza), a dopiero potem kliknij „Kontynuuj”. Jeśli Telegram jest skonfigurowany, bot wyśle wiadomość ze zrzutem ekranu.

### Awaryjny stop: „STOP F10”

Czerwony przycisk „STOP” (lub klawisz **F10**) zatrzymuje bota **natychmiast**: program zabija proces bota. W dzienniku — `[GUI] ЭКСТРЕННЫЙ СТОП. Процесс убит.`, a na karcie podsumowania powód „zatrzymany przyciskiem «STOP»”.

> [!warning] Co się traci przy F10: bot nie zdąży zapisać bloku `[ИТОГ]` w dzienniku i **nie wyśle podsumowania sesji w Telegramie**. Jeśli w tym momencie był w trakcie bitwy, walka w grze będzie toczyć się dalej (lub pozostanie na ekranie) — zobaczysz to na telefonie. Zaliczone już komnaty w statystykach zostaną zachowane: bot zapisuje je natychmiast po każdej komnacie.

Kiedy potrzebny jest właśnie ten przycisk: bot zachowuje się dziwnie (klika nie tam, gdzie trzeba, nie reaguje na „Pauza”) lub trzeba natychmiast wszystko przerwać. W pozostałych przypadkach lepiej użyć pauzy lub Ctrl+Q.

### Klawisze skrótu: co где działa

- :pause: **F9** — pauza / „Kontynuuj” (to samo, co przycisk „Pauza” na ekranie głównym).
- :square-filled: **F10** — „STOP”.
- :gamepad-2: **Ctrl+Q** — zatrzymać się **z podsumowaniem**: bot dokończy rozpoczętą komnatę, stanie w korytarzu, zatrzyma się i wyśle podsumowanie sesji. W dzienniku: `[ИНФО] Команда 'Ctrl+Q' принята! Бот завершит бой и остановится.`, powód zatrzymania — „Ręczne zatrzymanie przez użytkownika (Ctrl+Q)”.
- :triangle-alert: **Ctrl+Shift+Q** — zatrzymać się **natychmiast, ale z podsumowaniem**: bot drukuje `[ЭКСТРЕННАЯ ОСТАНОВКА]`, zapisuje `[ИТОГ]` i wykonuje **jedną** próbę wysłania podsumowania do Telegramu (bez powtórzeń, aby nie zwlekać).

Ważne szczegóły, przez które klawisze czasami „nie działają”:

- **F9 i F10 nasłuchuje okno programu** i tylko wtedy, gdy **aktywne jest okno gry lub okno programu**. Wcisnąłeś F10 w przeglądarce lub komunikatorze — nic się nie stanie. Jeśli gra jest zminimalizowana lub zasłonięta innym oknem, używaj przycisków na mini-pasku: działają zawsze, ponieważ mini-pasek nie odbiera aktywności grze.
- **Ctrl+Q i Ctrl+Shift+Q nasłuchuje sam bot**, a nie okno programu, dlatego działają one tak długo, jak bot jest uruchomiony, nawet jeśli aktywne jest inne okno.
- **Te skróty są znane również innym programom.** Ctrl+Q zamyka wiele programów (Word, Telegram Desktop), a Ctrl+Shift+Q — przeglądarki. Dopóki bot pracuje, nie wciskaj ich w innych oknach: bot również to „usłyszy” i się zatrzyma.
- **Ctrl+Q bot sprawdza, gdy jest w korytarzu** przed następnymi drzwiami. Podczas miękkiej pauzy stoi i niczego nie sprawdza, dlatego Ctrl+Q zadziała dopiero po kliknięciu „Kontynuuj”. A jeśli bot czeka na twoją odpowiedź w oknie SOS, Ctrl+Q zatrzyma go natychmiast.
- **Przytrzymanie klawisza niczego nie powtarza:** jedno wciśnięcie — jedna komenda.
- Wcisnąłeś F9 lub F10, gdy bot nie jest uruchomiony — w dzienniku pojawi się `[GUI] Нажата F9, но бот не запущен.`

### Krzyżyk okna i zamykanie scrcpy

- :x: **Krzyżyk okna programu, gdy bot pracuje.** Otworzy się pytanie „Zatrzymać bota?”. Przycisk „Zatrzymaj i zamknij” zamknie program i bota, a okno gry (scrcpy) — jeśli otworzył je sam program, natychmiast — podsumowanie do Telegramu nie wpłynie. Jeśli tego nie chcesz — zamknij okno pytania i najpierw zatrzymaj bota łagodnie.
- :smartphone: **Zamknąłeś okno gry (`HeroWarsBot_Arena`) sam.** Program napisze `[GUI] Окно scrcpy закрыто — останавливаю бота (он напишет итог и пришлёт его в Telegram).` Bot sam dokończy podsumowanie sesji i wyśle je do Telegramu; jeśli nie odpowie w ciągu 10 sekund — program zatrzyma go tak, jak przy F10.
- :pencil: Jeśli w „Kreatorze reguł” są niezapisane zmiany, krzyżyk najpierw zapyta „Zapisać zmiany?”.

### Co wybrać

- **Chcę zrobić przerwę i wrócić** — „Pauza” (F9). Kliknij „Kontynuuj”, gdy będziesz gotowy.
- **Chcę skończyć i otrzymaть podsumowanie** — Ctrl+Q (bot dokończy komnatę, zatrzyma się, wyśle podsumowanie do Telegramu).
- **Muszę zatrzymać się natychmiast, ale potrzebuję podsumowania** — Ctrl+Shift+Q.
- **Bot się zepsuł lub zachowuje się dziwnie** — „STOP” (F10), a potem sprawdzaj dziennik.
- **Bot wezwał cię oknem SOS i chcesz skończyć** — przycisk „Zatrzymaj bota” w tym oknie: bot sam się zatrzyma i wyśle podsumowanie. Okno SOS omówimy oddzielnie.

### Podsumowanie sesji w Telegramie

Jeśli Telegram jest skonfigurowany, podsumowanie przychodzi przy każdym zatrzymaniu, **z wyjątkiem przycisku «STOP»** oraz zamknięcia okna programu: bot pisze, czy zatrzymałeś go sam („Bot zatrzymany przez ciebie”), czy osiągnął cel („Farmienie zakończone”) lub wyłożył się z błędem, ile minęło czasu, ile komnat, pięter i tytanitu, czy były odwroty i okna SOS. Jeśli brak połączenia z Internetem, bot spróbuje wysłać podsumowanie jeszcze dwa razy (po 10 i 30 sekundach), a potem się wyłączy. Jak podłączyć Telegram — w osobnym rozdziale.

> [!done] Teraz wiesz, jak łagodnie zwolnić bota i jak zatrzymać go na stałe, oraz który klawisz co robi. Dalej — konfiguracja reguł: jak nauczyć bota ustawiania odpowiednich drużyn. [Następna sekcja →](#7)

## Kreator reguł: „Baza i pokoje”

„Kreator reguł” — drugi przycisk na lewym pasku (ikona z suwakami). Tutaj wyjaśniasz botowi trzy rzeczy: **kiedy się zatrzymać**, **co uważać za złą bitwę** oraz **jaką drużyną chodzić do każdej komnaty**. Drużyna to zespół składający się z 3–5 tytanów. Strona jest podzielona na trzy zakładki na górze: „Baza i pokoje”, „Autotaktyka i PŻ” oraz „Reguły i przechwyty”. W tej sekcji — pierwsza, najważniejsza: bez niej bot nie wie nawet, kogo wystawić do bitwy.

![Zakładka „Baza i pokoje”: na górze dwie karty z ustawieniami, niżej cztery wiersze z drużynami](images/rules_base.png)

Na górze — „Parametry sesji” (dwie karty), niżej — „Drużyny według pokojów”. Na dole strony, tak samo na każdej zakładce, znajduje się szary pasek z przyciskami: „Zapisz ustawienia” oraz „Przywróć / Resetuj”. O nim — na końcu sekcji. Najważniejsze, co musisz zapamiętać od razu: **dopóki nie klikniesz „Zapisz ustawienia”, nic nie zostanie zapisane** — żadna zmiana nie dotrze do bota.

### Karta „Cele i limity”

- :target: **„Cel sesji”** — kiedy bot powinien skończyć. Cel jest zawsze **jeden**, z czterech: „Tytanit”, „Komnaty”, „Piętra” lub „Czas” (czas — w minutach). Wybierz typ z listy i wpisz liczbę w polu. Pole akceptuje tylko cyfry. Podpis „0 — bez limitu” oznacza: zero wyłącza cel, a bot będzie grał, dopóki go nie zatrzymasz. Okrągła strzałka po prawej stronie („Wyzeruj cel”) ustawia 0.
- :gem: **Tytanit bot liczy sam**, a nie odczytuje z ekranu: 6 za zwykłą komnatę i 12, jeśli w oknie wyniku znajduje się ikona „x2”. Dlatego „120 tytanitu” to w przybliżeniu 20 komnat bez „x2”. Dopóki ani razu nie zapisałeś ustawień, bot sam przyjmuje cel „120 tytanitu”.
- :layers: **Bot nie porzuca piętra w połowie.** Po osiągnięciu celu „Tytanit”, „Komnaty” lub „Czas” nie zatrzymuje się w miejscu: pisze w dzienniku `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.`, przechodzi pozostałe komnaty piętra i staje przed punktem zapisu, nie klikając „Aktywuj”. Dzięki temu piętro nie pozostaje niedokończone, a nagrodę bot odbierze i piętro zaliczy w pierwszej kolejności przy następnym uruchomieniu. Jeśli punkt zapisu nie zostanie odnaleziony w ciągu 6 komnat (na piętrze jest ich 5), bot zatrzyma się tak, jak jest. Cel „Piętra” działa natychmiast po przejściu punktu zapisu.
- :gauge: **Czas płynie również podczas pauzy.** Cel „Czas — 120” oznacza 120 minut od kliknięcia przycisku „Zacznij farmić”, razem ze wszystkimi pauzami.
- :calendar: **„Godzina resetu dnia (czas lokalny)”** — o której godzinie zaczyna się u ciebie nowy dzień w grze. Domyślnie 05:00. Od tego zależy, do którego dnia zaliczają się bitwy w statystykach, a także pamięć bota o zdrowiu tytanów: żyje ona w granicach jednego dnia gry, a w nowy dzień bot zaczyna z czystą kartą. Ustaw godzinę, po której uważasz dzień za nowy (na przykład gdy idziesz spać).
- :send: **„Skonfiguruj Telegram”** — otwiera osobne okno, w którym włącza się łączność z komunikatorem. Obok przycisku znajduje się kropka i podpis: zielony „Powiadomienia SOS włączone” lub szary „Telegram nieskonfigurowany”. Jak połączyć, omówimy w sekcji o Telegramie. Tutaj ważne jest jedno: przycisk „Zastosuj” w tamtym oknie zmienia tylko tę stronę. Aby ustawienie trafiło do pliku, musisz dodatkowo kliknąć „Zapisz ustawienia”.

> [!tip] Jaki cel wybrać? „Czas” jest wygodny, gdy masz wolną chwilę w grafiku („niech bot popracuje godzinę, podczas gdy przygotowuję kolację”). „Tytanit” — gdy musisz zebrać określoną ilość nagrody. „Komnaty” i „Piętra” — gdy chcesz przejść dokładnie tyle. Nie jesteś pewien — zostaw „Tytanit” i 120: to krótkie uruchomienie próbne.

### Karta „Bezpieczeństwo i tryb”

Tutaj decyduje się, **co oznacza zła bitwa**. Bot odczytuje zdrowie tytanów w oknie wyniku i porównuje dwie liczby z twoimi.

- :heart-pulse: **„Próg paniki PŻ, %”** — poniżej jakiego poziomu zdrowia po bitwie walka uważana jest za złą. Domyślnie 40.
- :swords: **„Delta utraty PŻ, %”** — ile zdrowia jeden tytan może stracić podczas jednej bitwy. Domyślnie 30.

Oba pola akceptują liczby całkowite od 0 do 100; jeśli wpiszesz coś innego, pole zaczerwieni się z podpisem „Wpisz liczbę od 0 do 100” i zapisanie ustawień nie będzie możliwe, dopóki tego nie poprawisz.

Praktyczny przykład z progiem 40 i deltą 30:

- Araji wszedł do bitwy ze 100%, wyszedł z 80% — **wszystko w porządku**: stracił 20, pozostał powyżej 40.
- Araji wszedł ze 100%, wyszedł z 55% — **zła bitwa**. 55 jest powyżej progu, ale stracono 45, a dopuszczalne jest 30.
- Araji wszedł z 50%, wyszedł z 35% — **zła bitwa**. Stracił tylko 15, ale 35 jest poniżej progu paniki.
- Dowolny tytan zginął lub nie odnaleziono go w oknie wyniku — **zła bitwa** zawsze, bez względu na to, co ustawisz.

Straty są liczone od poziomu zdrowia, z jakim tytan **wszedł** do bitwy, a nie od 100%. Dlatego ranny tytan „uderza” w próg wcześniej niż zdrowy. Im wyższy próg i im mniejsza delta, tym surowszy jest bot i tym częściej cię wzywa; zero w progu wyłącza sprawdzanie „poniżej progu” (z wyjątkiem poległych), a 100 w delcie wyłącza sprawdzanie strat.

> [!note] Próg i delta są wspólne dla wszystkich tytanów. Dla pojedynczego tytana można ustawić własny próg, a także włączyć regułę „jeśli trzech straciło dużo — zła bitwa”. Robi się to na sąsiedniej zakładce „Autotaktyka i PŻ”.

Poniżej znajdują się dwa przełączniki:

- :shield-check: **„Bot decyduje sam”** („Cofa złe walki i dobiera drużynę”) — domyślnie **wyłączony**. Wyłączony: zła bitwa → okno „Wymagana interwencja”, bot czeka na ciebie. Włączony: bot bez pytań cofa bitwę i powtarza ją drużyną zapasową, a także sam dobiera skład na podstawie zdrowia tytanów. Szczegóły — w sekcji o autonomicznej pracy bota. Włączaj, gdy obejrzałeś już bota przy pracy i ufasz drużynom zapasowym.
- :swords: **„Ręczna kontrola superumiejętności Angusa”** („Globalnie, we wszystkich pokojach”) — domyślnie **wyłączony**, i wtedy każda bitwa, w tym z Angusem, toczy się w trybie automatycznym. Włączony — dla składów z Angusem bot klika „Do walki”, na parę sekund włącza auto-bitwę ze względu na superumiejętność Angusa i znowu wyłącza. Takiej bitwy bot sam nie cofa, lecz wzywa ciebie. Podczas uruchamiania w dzienniku widać, co wybrano: `[ТАКТИКА] Ангус: ...`.

### Drużyny według pokojów

Pod podpisem «Najpierw drużyna główna, zapasowe po kolei, если walka idzie źле» znajdują się cztery wiersze — według pokojów: „Ziemia”, „Woda”, „Ogień” i „Mieszana”. Każdy z nich to osobna karta.

- :users: **Drużyna główna** — kwadraty tytanów pod nazwą komnaty. Bot wystawia ją, jeśli nie ma powodów postąpić inaczej (na przykład zadziałała reguła z zakładki „Reguły i przechwyty”). Tytani są pokazani od lewej do prawej, **tak jak stoją na ekranie gry**. Brak drużyny — zamiast kwadratów pojawia się napis „Skład nie ustawiony”.
- :pencil: **Ołówek („Zmień drużynę”)** — otwiera okno „Zbierz skład”.
- :list: **„Drużyny zapasowe”** z liczbą „N szt.” — rozwijana lista (strzałka w dół/w górę). Drużyny zapasowe bot sprawdza po kolei, jeśli bitwa poszła źle i decyduje sam („Bot decyduje” jest włączony lub nie odpowiedziałeś na okno w porę). W każdej komnacie jest ich do 5. Wewnątrz każda drużyna zapasowa to wiersz `#1`, `#2` i tak dalej, a po prawej stronie krzyżyk („Usuń drużynę”). Przycisk „Dodaj drużynę” otwiera to samo okno „Zbierz skład”.
- :plus: **„Warunek”** — „+ Warunek”: szybka ścieżka do reguły dla tej komnaty, na przykład „jeśli przeciwko Angusowi — ustaw taką drużynę”. Otworzy się okno „Nowa reguła” z już wybraną komnatą. Jak je wypełniać, omówimy w sekcji o regułach.

Ustaw drużynę główną we wszystkich czterech pokojach **przed pierwszym farmieniem**: bot sam nie zna twoich tytanów i „prosto z pudełka” nie posiada żadnych drużyn.

Jak zebrać skład:

1. **Kliknij ołówek** w odpowiednim pokoju. Otworzy się okno „Zbierz skład”.
2. **Klikaj tytanów**, których chcesz wystawić. Kliknąłeś ponownie — usunąłeś. Na górze licznik: „Wybrano: 3 / 5” oraz podpowiedź „Można zastosować” (przy dwóch jest napisane „Minimum 3 · brakuje 1”).
3. **Bierz pod uwagę żywioł komnaty.** Do „Ziemi”, „Wody” i „Ognia” wchodzą tylko tytani tego żywiołu, a do „Mieszanej” — wszyscy, razem z Metydą (jest elaritem i do innych pokojów nie chodzi: „Metyda — tylko w komnacie mieszanej”). Gdy wybrano 5, pozostali tytani zostają zablokowani.
4. **Kliknij „Zastosuj”** (lub „Anuluj”, jeśli zmieniłeś zdanie; „Wyczyść” usuwa wszystkich tytanów naraz).

![Okno „Zbierz skład” dla komnaty „Woda”: wybrano trzech tytanów, na dole „Zastosuj”](images/rules_picker.png)

> [!warning] „Zastosuj” w oknie „Zbierz skład” zmienia tylko stronę: drużyna nie jest jeszcze **zapisana** w pliku. Zostanie zapisana, gdy klikniesz „Zapisz ustawienia”. Drużyna główna każdej komnaty znajduje się w pliku `bot_data/rules/<стихия>.yml`, zapasowe i wszystkie liczby — w `profile.yml`. Nie musisz edytować tych plików ręcznie.

Zapasowej drużyny, która już znajduje się na liście (w dowolnej kolejności tytanów), nie można dodać po raz drugi: pojawi się powiadomienie „Taka drużyna zapasowa już jest”.

> [!tip] Jakie drużyny ustawiać jako zapasowe? Daj botowi wybór: niech drużyna zapasowa różni się od głównej przynajmniej parą tytanów. Jeśli u ciebie Araji często wychodzi z bitwy ranny, umieść w drużynie zapasowej tych, którzy lepiej znoszą ciosy.

### Zapisywanie i „Przywróć / Resetuj”

Dolny pasek pokazuje stan: „Wszystkie zmiany zapisane” (zielony ptaszek) lub „Są niezapisane zmiany” (żółty znacznik). Gdy bot pracuje, obok widnieje napis „Bot weźmie nowe ustawienia przy następnym uruchomieniu”.

- :save: **„Zapisz ustawienia”** zapisuje tylko to, co zmieniłeś, i wyświetla powiadomienie „Ustawienia zapisane”. Dopóki przycisk nie zostanie wciśnięty, bot nie wie o twoich zmianach. W dzienniku pojawi się `[GUI] Профиль настроек сохранен!`.
- :rotate-ccw: **„Przywróć / Resetuj”** — czerwony przycisk; najpierw zapyta „Przywrócić ustawienia?”. Ustawienia wrócą do **ostatnio zapisanych** (kopia `bot_data/profile.yml.bak`). Jeśli kopii nie ma, `profile.yml` zostanie usunięty, a bot przyjmie wartości domyślne. Niezapisane zmiany przepadną. Głównych drużyn i reguł w plikach `bot_data/rules` ten przycisk nie dotyka, ale formularz strony odczyta je ponownie z dysku.
- :triangle-alert: **Jeśli opuścisz stronę z niezapisanymi zmianami** (przejdziesz do innej sekcji lub klikniesz krzyżyk okna), wyskoczy „Zapisać zmiany?” z przyciskami „Zapisz”, „Nie zapisuj” i „Anuluj”.

Bot odczytuje ustawienia **raz, gdy klikasz „Zacznij farmić”**. Możesz je zmieniać podczas pracy, ale zadziałają one dopiero po zatrzymaniu i ponownym uruchomieniu. Nawet „Pauza” i „Kontynuuj” ich nie odświeżają. Karta „Konfiguracja startu” na ekranie głównym pokazuje dokładnie te ustawienia, z którymi bot aktualnie pracuje.

> [!warning] Jeśli plik `profile.yml` jest uszkodzony, na górze dziennika na ekranie głównym pojawi się `[ОШИБКА] Файл profile.yml поврежден!`, na stronie znajdą się wartości standardowe, a „Zapisz ustawienia” odmówi zapisu („profile.yml jest uszkodzony — ustawienia nie zostały zapisane”). Kliknij „Przywróć / Resetuj”.

> [!done] Teraz wiesz, jak ustawić cel, progi i drużyny dla każdej komnaty. Dalej — zakładka „Autotaktyka i PŻ”: kolejność drzwi oraz to, jak bot leczy i zmienia tytanów. [Następna sekcja →](#8)

## Kreator reguł: «Autotaktyka i PŻ»

Druga zakładka «Kreatora reguł». Na первой («Baza i pokoje») ustaliłeś składy i ogólne progi. Tutaj wyjaśniasz botowi, **jak ma się zachować, gdy coś pójdzie nie tak**: do których drzwi wejść jako pierwszych, co uznać za złą bitwę, ile razy spróbować innego składu, jak długo na ciebie czekać i jak leczyć rannych tytanów. Wszystkie pola są już wypełnione rozsądnymi liczbami, więc bot działa nawet bez twoich poprawek. Zmieniaj je, gdy zobaczysz, że zachowuje się inaczej, niżbyś chciał.

![Zakładka «Autotaktyka i PŻ»: pasek na górze, czworo drzwi, dwie karty obok siebie i osobiste progi na dole](images/tactics_tab.png)

Tak jak na первой zakładce, **nic nie zostanie zapisane, dopóki не klikniesz «Zapisz ustawienia»**, a bot odczytuje ustawienia tylko raz, gdy klikasz «Zacznij farmić». Jeśli zmienisz coś podczas farmy, zadziała to dopiero po zatrzymaniu i ponownym uruchomieniu.

### Niebieski pasek на górze

Krótko wyjaśnia, co bot robi w przypadku złej bitwy: wycofuje ją i powtarza zapasowym składem, a udany skład zapamiętuje w regule.

Jeśli na первой zakładce wyłączony jest przełącznik «Bot decyduje sam», do paska dodawane jest jeszcze jedno zdanie. Jest оно ważne, więc omówimy je osobno. **Bez «Bot decyduje sam» nie działają две вещи: składy zapasowe i skład leczący.** Cała reszta na tej zakładce działa всегда:

- :door-open: kolejność drzwi;
- :gauge: oczekiwanie na twoją odpowiedź w oknie SOS (okno, w którym bot wzywa cię, gdy bitwa jest zła);
- :triangle-alert: kryteria złej bitwy;
- :heart-pulse: osobiste progi paniki.

### «Kolejność drzwi»

W korytarzu bot często widzi od razu kilka drzwi: po jednych na żywioł (woda, ziemia, ogień) lub «Mieszana». Wewnątrz komnaty czekają wrogowie, a skład dla każdego żywiołu jest inny. Kolejność decyduje, **które drzwi bot otworzy jako pierwsze**. Domyślnie jest to: «Woda», «Mieszana», «Ziemia», «Ogień».

Cztery miejsca idą od lewej do prawej, między nimi są strzałki; na każdym znajduje się numer od 1 do 4. Kliknij miejsce i wybierz żywioł. Powtórzeń nie ma: jeśli wybierzesz żywioł, który już znajduje się w innym miejscu, po prostu **zamienią się miejscami**. Było „Woda, Mieszana, Ziemia, Ogień”, wybrałeś na pierwsze место „Ogień” — zrobi się „Ogień, Mieszana, Ziemia, Woda”.

Dwa zastrzeżenia, abyś nie był zaskoczony w grze:

- Jeśli drzwi są **zakazane regułą «Skip»** (o nich — w sekcji o «Regułach i przechwytach»), bot je pominie, nawet gdy są pierwsze w kolejности. Jeśli wszystkie drzwi są zakazane — wybierze pierwsze w kolejności.
- Jeśli włączony jest «Bot decyduje sam», bot czasami **sam wybierze inne drzwi**, poza kolejnością: tam, gdzie zadziała leczenie dla rannego tytana, lub omijając drzwi niebezpieczne dla rannych. Taki wybór jest widoczny w dzienniku w wierszu `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...`.

### Karta «Kryteria złej bitwy i SOS»

- :swords: **«Ile składów zapasowych próbować w pokoju»** — ile razy w jednej komnacie bot może sam wycofać bitwę i powtórzyć innym składem. Od 1 do 3, domyślnie 2. Wykorzystał próby, a bitwa nadal jest zła — bot wzywa ciebie. Działa tylko przy włączonym «Bot decyduje sam». Więcej niż trzy nie można: powtarzanie jednej bitwy dziesięć razy nie ma sensu, a każda próba zajmuje czas.
- :gauge: **«Limit czasu okna SOS bez odpowiedzi, min»** — ile minut bot czeka na twoją odpowiedź w oknie «Wymagana interwencja», zanim zdecyduje sam. Od 0 do 60, domyślnie 10. Podpis pod polem głosi «0 — czekać всегда»: **zero означает „czekać zawsze”**, bot będzie stał i czekał na ciebie choćby do rana. Działa to również **bez** «Bot decyduje sam». Co dokładnie bot zdecyduje sam (wycofa bitwę, zaakceptuje ją czy wstrzyma pracę) — opisano w sekcji o oknach SOS.
- :users: **«Uznać bitwę za złą, если»** — ogólne straty składu: „tytanów ≥ 3” i „stracili ≥ 40” «% PŻ каждый». Takie sprawdzenie wyłapuje przypadek, gdy **każdy z osobna trzyma się**, ale razem skład się „posypał”. Trzy tytany straciły po 40% i więcej — bitwa jest zła, chociaż żaden nie spadł poniżej progu paniki. Podpis «0 tytanów — nie sprawdzać» oznacza: wpisz w pierwsze pole 0, a sprawdzanie się wyłączy. Pierwsze pole — od 0 do 5, drugie — od 0 do 100.

Praktyczny przykład. Skład: Araji, Hyperion, Rigel, Iyari, Lumira. Po bitwie Araji stracił 45%, Rigel 42%, Iyari 40%, a pozostali po 10%. Trzej stracili „40 i więcej” — bitwa jest zła, nawet jeśli u każdego zostało więcej niż próg paniki. Gdyby Iyari stracił только 35%, takich tytanów byłoby dwóch i ogólne sprawdzenie nie miałoby zastrzeżeń.

> [!note] Pozostałe oznaki złej bitwy — próg paniki i tolerancja strat — znajdują się na первой zakładce «Baza i pokoje». Bitwa jest zła, jeśli zadziałał **co najmniej jeden** warunek: ktoś zginął lub nie został znaleziony w oknie, ktoś ma PŻ poniżej progu, ktoś stracił więcej niż tolerancja lub zadziałało sprawdzanie strat ogólnych.

Jeśli wpisałeś неprawidłową liczbę (literę lub liczbę spoza zakresu), pole zaczerwieni się, pod nim pojawi się «Liczba od … do …» i nie będzie można zapisać ustawień, dopóki tego nie poprawisz.

### Karta «Automatyczny skład leczący w pokoju Mieszanym»

Często bywa tak: jeden tytan przez dwie bitwy z rzędu obrywa i chodzi z połową zdrowia. Prędzej czy później spadnie poniżej progu i bitwa stanie się zła. „Leczenie” zachodzi wtedy, gdy bot **sam zbiera specjalny skład**, aby ranny został podleczony (umieszcza w nim uzdrowiciela, który podnosi zdrowie rannego). Takie zestawienie bot zbiera только dla pokoju «Mieszana», ponieważ можно там вставить кого угодно.

Działa to tylko przy włączonym «Bot decyduje sam» i только тогда, gdy twoja własna reguła leczenia nie zadziałała (reguła ma wyższy priorytet).

- :heart-pulse: **«Leczyć tytana, если PŻ poniżej, %»** — domyślnie 60. Tytan zdrowszy niż ta liczba jest uważany za zdrowego. **0 wyłącza** cały skład leczący. Jest jednak dolna granica: jeśli tytan ma PŻ już **poniżej progu paniki**, w pokoju «Mieszana» go nie wyleczy i bot go nie dotyka.
- :users: **«Kogo usunąć ze składu dla rannego»** — trzy miejsca ze strzałkami. Gdy trzeba wstawić rannego, a w składzie nie ma miejsca, ktoś musi odejść. Kliknij miejsce i wybierz tytana: lista jest podzielона na kolumny według żywiołów. **«— auto —»** (tak jest domyślnie) означает: bot usuwa od końca składu, ale **uzdrowicieli nie dotyka**. Dla składu „Hyperion, Rigel, Iyari, Lumira, Amon” będą to Amon, a potem Lumira. Jeśli wybierzesz tytana, który już znajduje się w innym miejscu — zamienią się miejscami.

Jak bot leczy, w prostych słowach:

1. Sprawdza, kto ma PŻ poniżej 60%, ale powyżej progu paniki, i kogo z nich nie zakazały reguły «Skip».
2. Leczy **po jednym**, zaczynając od tego, kto jest najbliżej swojego progu. Najpierw głównych (z podstawowych składów), potem zapasowych.
3. Jeśli rannego nie ma w składzie — wchodzi on na miejsce usuniętego. Jednak tytanów, którzy i tak są leczeni w „swoim” pokoju (wodnych i ziemnych: w ich podstawowym składzie jest uzdrowiciel), bot nie wyciąga do pokoju «Mieszana», chyba że przez dwie bitwy z rzędu nie podnoszą się выше порога. Ognistych nie ma czym leczyć w ich pokoju, dlatego dla nich leczenie włącza się od razu.
4. Jeśli ranny jest już w składzie, ale przez dwie bitwy z rzęду nie podnosi się — zamiast usuniętego wchodzi **zdrowy i naładowany uzdrowiciel** (PŻ od 80%, energia od 60%).
5. Skład nie jest wybierany, jeśli nie zostało w nim uzdrowiciela, przegrywa z tymi wrogami, jest niebezpieczny dla rannych lub wymaga walki ręcznej (Angus).

Dlaczego bot jest tak ostrożny? Leczyć kogoś, kogo nigdzie nie wskazałeś, nie będzie: tytana, którego nie ma w twoich składach i regułach, bot sam nie ustawi. Jeśli nie удалось собрать пак (tytan nie wszedł do slotu) — bot nie zatrzymuje się, stawia обычный skład и **до конца запуска этого титана больше не лечит**.

W dzienniku jest to widoczne w wierszach `[ТАКТИКА] Пак отхила (бот собрал сам): ...` oraz `[ТАКТИКА] Отхил: ...` (dlaczego ranny nie jest leczony).

### Karta «Osobiste progi paniki tytanów, % PŻ»

Ogólny próg paniki (domyślnie 40) dotyczy wszystkich. Są jednak tytani, których szkoda stracić wcześniej niż innych, oraz tacy, którzy spokojnie znoszą niskie PŻ. Dla них можно задать **свой порог**.

- Na dole находится podpis «Pozostałe tytany — wspólny próg 40%» (liczba z первой вкладки). Dopóki nie ma osobistych progów, wyświetla się «Brak osobistych progów — wszystkie tytany mają wspólny próg».
- Kliknij «Ustaw osobisty próg tytanowi». Otworzy się małe okno «Osobisty próg paniki»: wybierz tytana z listy i wpisz liczbę od 0 do 100. Kliknij «Zastosuj». Okno под подсказывает «Wspólny próg — 40%», чтобы тебе было с чем сравнить. Na liście znajdują się tylko tytani, którzy nie mają ещё osobistego progu.
- Każdy ustawiony próg to plakietka z tytanem i żółtą liczbą. Kliknij plakietkę, aby изменить próg (tytana nie można zmienić, trzeba go usunąć i dodać ponownie). **Krzyżyk** na plakietce usuwa próg i tytan ponownie działa według progu ogólnego.

Bitwa jest zła, jeśli PŻ tego tytana po bitwie jest **poniżej jego osobistego progu**. Przykład: ogólny próg wynosi 40, a u Rigela ustawiono 60. Rigel wyszedł z 55% — bitwa jest zła, chociaż dla pozostałych 55% byłoby w porządku.

> [!tip] Od czego zacząć? Nic nie zmieniaj, dopóki nie zobaczysz kilkudziesięciu komnat. Zauważyłeś, że bot wzywa cię z powodu tego samego tytana — ustaw mu niższy osobisty próg. Bot zbyt często zmienia skład dla leczenia — **zmniejsz** liczbę w «Leczyć tytana, если PŻ poniżej». Jeśli nie chcesz, aby leczył w ogóle — wpisz 0.

> [!warning] Jeśli ustawiłeś limit czasu okna SOS na 0 i poszedłeś spać, a bot wezwał cię w oknie, będzie czekał do rana. Lepiej zostaw 10–15 minut i skonfiguruj Telegram: тогда ты узнаешь о проблеме сразу, а если не успеешь, бот решит сам.

> [!done] Teraz wiesz, jak ustalić kolejność drzwi, co uznać za złą bitwę i jak bot leczy rannych. Dalej — Telegram i okna, które wzywają cię na pomoc. [Następna sekcja →](#9)

## Kreator reguł: «Reguły i przechwyty»

Druga zakładка «Kreatora reguł». Na первой ustaliłeś **podstawowy skład** dla każdego pokoju, na drugiej — jak bot zachowuje się w razie kłopotów. Tutaj uczysz go **wyjątków**: „zwykle stawiaj podstawowy skład, ale если stało się to — zrób иначе”. Każdy taki wyjątek nazywa się **regułą**. A „przechwyt” zachodzi тогда, gdy reguła „przechwytuje” wybór składu od podstawowego i stawia swój.

Reguła jest zawsze odczytyвана так само: **«jeśli [warunek] — to [akcja]»**. Например:

- :heart-pulse: „Jeśli Araji ma PŻ poniżej 50% — postaw skład z uzdrowicielem Sigurdem”.
- :swords: „Jeśli w komnacie są Angus, Sylva i Verdok — postaw ten skład”.
- :door-open: „Jeśli Araji ma PŻ poniżej 30% — nie wchodź do pokoju «Ogień»”.
- :users: „Jeśli w komnacie są Angus, Avalon i Eden — zatrzymaj się i zapytaj mnie”.

![Zakładka «Reguły i przechwyty»: filtry żywiołów, lista reguł z ikonami, składami i przełącznikami](images/rules_intercepts.png)

Każdy żywioł ma własne reguły: «Ziemia», «Woda», «Ogień» i «Mieszana» mają oddzielne listy. Gdy bot wejdzie do drzwi pokoju «Ogień», sprawdza tylko reguły dla pokoju «Ogień». Tak jak na innych zakładkach, **nic nie zostanie записане, dopóki не klikniesz «Zapisz ustawienia»**, a bot odczytuje reguły только раз, когда ты нажимаешь «Zacznij farmić».

> [!note] Wielu reguł w ogóle nie będziesz musiał pisać. Jeśli włączony jest «Bot decyduje sam», bot **sam zapamiętuje** udane składy po wycofaniu i sam dodaje „złote reguły”. Pojawią się one na tej samej liście (o nich — poniżej). Własne reguły są potrzebne, gdy już wiesz, że „tak robić nie wolno” lub „w takiej sytuacji potrzebny jest właśnie ten skład”.

### Jakie są rodzaje reguł

Warunek reguły jest jednym z trzech, a akcja — jedną z trzech. Razem dają znane typy:

- :heart-pulse: **Ratowanie według PŻ lub energii.** Warunek — „PŻ (lub energia) danego tytana poniżej N%”, akcja — postawienie innego składu. Na liście ikona **«LECZENIE»** (wg PŻ) lub **«ENERGIA»**. Tak robi się leczenie: gdy tytan jest ranny, stawia się skład z uzdrowicielem.
- :swords: **Przeciwko tym wrogom.** Warunek — „w komnacie są wszyscy ci wrogowie”, akcja — postawienie swojego składu. Ikona **«WROGOWIE»**. Wrogów można выбрать spośród 13, которых бот узнаёт в Подземелье.
- :door-open: **«Skip» — zakaz.** Warunek — „PŻ lub energia tytana poniżej N%”, akcja — nie stawiać tego tytana i nie wchodzić do tej komnaty. Ikona **«SKIP»**, po prawej adnotacja «Pominąć komnatę».
- :users: **«Zapytać ciebie».** Dowolny warunek, a akcja — nie decydować samemu, lecz wezwać ciebie. Po prawej adnotacja **«Zapytać ciebie»**, a ikona zależy od warunku («PŻ», «ENERGIA», «WROGOWIE»). Gdy zadziała, bot otworzy okno «Brak odpowiedniego składu» i będzie czekał na twoją odpowiedź. Jeśli nie odpowiesz w czasie określonym w «Autotaktyka i PŻ», zdecyduje sam.

Ikona «PŻ» (a nie «LECZENIE») oznacza, że warunek dotyczy PŻ, a akcja to «Zapytać ciebie». Jeśli nie ma żadnego warunku, nie ma ikony, a pod nazwą widnieje napis «Brak warunku — reguła nigdy nie zadziała».

Teraz о «Skip», ponieważ ma dwa zadania naraz. Przykład: w pokoju «Ogień» ustawiona jest reguła „Araji, PŻ poniżej 30%”.

1. **Drzwi.** Dopóki Araji ma mniej niż 30%, bot nie wejdzie do pokoju «Ogień» i wybierze inne drzwi. Jeśli wszystkie drzwi są zakazane, bot wybierze pierwsze w kolejności.
2. **„Czarna lista”.** W tej komnacie Araji nie zostanie postawiony: każdy skład, w którym się znajduje, bot odrzuci i weźmie następny. Jeśli również **podstawowy** skład содержит запрещённого титана, нечего ставить — bot zatrzyma się i otworzy okno «Brak odpowiedniego składu».

> [!warning] «Skip» nie można ustawić według wrogów. Bot dowiaduje się o wrogach **dopiero po** wejściu przez drzwi, więc nie może wybrać drzwi na ich podstawie. W oknie reguły dla opcji «Wg wrogów» pole wyboru «Skip» jest niedostępne. Jeśli chcesz ominąć komnatę z określonymi wrogami — ustaw regułę «Zapytać ciebie», тогда решение будет за тобой.

### W jakiej kolejności bot sprawdza reguły

Gdy rozpoczyna się bitwa, bot przegląda reguły komnaty **w następującej kolejności**:

1. **«Skip».** Najpierw bot tworzy „czarną listę” tytanów: kogo zakazała skazana na działanie reguła «Skip». Skład z takim tytanem nie będzie pasować, nawet если правило само его просит (это называют вето: запрет сильнее любого правила).
2. **Ratowanie.** Reguły, w których warunku znajduje się PŻ lub energia tytana. Należą tu również reguły „przeciwko wrogom, при Араджи < 50% ХП” (wrogowie plus PŻ): są one sprawdzane od razu, **przed** zwykłymi regułami dotyczącymi wrogów.
3. **Przeciwko wrogom.** Reguły, w których w warunku są tylko wrogowie.
4. **Podstawowy skład** komnaty — jeśli nic nie pasowało.

Wewnątrz każdej grupy bot idzie **od góry do dołu** i wybiera pierwszą regułę, która zadziałała. Dlatego potrzebne są strzałki: jeśli dwie reguły dotyczące wrogów pasują jednocześnie, wygra ta znajdująca się wyżej. Natomiast reguła „Ratowanie” jest всегда silniejsza niż „Przeciwko wrogom”, niezależnie od tego, где они ни стояли в списке. **Wyłączone** reguły nie biorą udziału w sprawdzaniu.

Warunki są porównywane z tym, co bot wie o twoich tytanach (PŻ i energię pobiera z ekranu wyboru drużyny i po bitwach). Jeśli bot nie widział jeszcze zdrowia tytana, uważa je za pełne, a reguła „poniżej N%” nie zadziała. Jeśli w warunku jest kilku tytanów (tak bywa przy regułach, które bot zapamiętał sam), muszą zostać spełnione **wszystkie** warunki naraz. Z wrogami jest tak samo: reguła zadziała tylko wtedy, gdy w komnacie znajdują się **wszyscy** wymienieni.

### Lista reguł: co znajduje się w wierszu

Na górze — «Aktywne reguły» i szary pasek z liczbą reguł, po prawej podpowiedź: «Wybierz jeden żywioł, aby zmienić kolejność» (pokazano wszystkie) lub «Reguła wyżej na liście jest sprawdzana jako pierwsza» (wybrano jeden). Niżej przyciski-filtry «Wszystko», «Ziemia», «Woda», «Ogień», «Mieszana» i przycisk «Nowa reguła». Pod nimi nagłówki kolumn „№”, «Warunek», «Akcja», «Wł».

W każdym wierszu od lewej do prawej:

- **Numer** — miejsce na liście swojego żywiołu. Im mniejszy numer, tym wcześniej sprawdzana jest reguła. Gdy wybrano **jeden** żywioł, obok numeru pojawiają się strzałki «Wyżej» i «Niżej». Wybrano «Wszystko» — strzałek nie ma: żywioły są pokazane po kolei i nie rywalizują ze sobą.
- **Ikony** — żywioł komnaty i typ reguły («LECZENIE», «PŻ», «ENERGIA», «WROGOWIE», «SKIP»).
- **Nazwa** i szary wiersz pod nią — warunek w słowach, na przykład «Araji: PŻ poniżej 50%» lub «Wrogowie w komnacie: Angus, Sylva».
- **Akcja** — strzałka i kwadraty tytanów składu (od lewej do prawej, jak w grze) z podpisem «zmiana paku». Lub plakietka «Zapytać ciebie» / «Pominąć komnatę».
- **Przełącznik «Wł»** — włączenie lub wyłączenie reguły.
- **Ołówek** «Zmień» i **krzyżyk** «Usuń».

Jeśli nie ma reguł, w miejscu listy jest napisane: „Brak reguł. Kliknij «Nowa reguła» — lub bot sam zapamięta regułę po wycofaniu.”

### Przełącznik, strzałki, krzyżyk i «Wyczyść»

- :check: **Przełącznik.** Wyłączona reguła staje się blada, ale **pozostaje na liście**, a bot po prostu ją pomija. To najlepszy sposób, aby „usunąć regułę na jakiś czas”: nie trzeba układać składu na nowo. Podczas uruchamiania w dzienniku pojawi się wiersz `[ПРАВИЛА] Выключено правил: N, бот их пропускает.`.
- :chevron-up: **Strzałki «Wyżej» i «Niżej»** zamieniają regułę miejscami z sąsiadem. Są potrzebne, gdy dwie reguły z tej samej grupy mogą pasować jednocześnie i ważne jest, która zostanie sprawdzona jako pierwsza.
- :x: **Krzyżyk «Usuń».** Na dole появится powiadomienie „Reguła «…» została usunięta” z przyciskiem **«Przywróć»**. Dopóki powiadomienie jest na ekranie, regułę można przywrócić na to samo miejsce.
- :trash-2: **«Wyczyść wszystkie reguły»** usuwa tylko to, co jest **widoczne teraz**. Wybrano «Woda» — usuną się reguły wody, wybrano «Wszystko» — wszystkie. Najpierw bot zapyta ponownie: «Usunąć wszystkie reguły?» i napisze, ile i jakich (przycisk «Usuń wszystkie»). Potem również появится powiadomienie «Usunięto reguł: {n}» z przyciskiem «Przywróć».

Wszystkie te działania zmieniają tylko stronę. Do plików trafią po kliknięciu «Zapisz ustawienia», przy czym zapisane zostaną **tylko żywioły, w которых coś się изменилось**. Jeśli opuścisz stronę без zapisania, okno zapyta «Zapisać изменения?».

> [!tip] Jeśli masz wątpliwości, czy usunąć regułę, lepiej wyłącz ją przełącznikiem. W przypadku reguł, które bot zapamiętał sam, istnieje jeszcze jeden powód (patrz niżej): wyłączonej bot nie dotyka i nie tworzy na nowo, a usunięta może pojawić się ponownie.

### Okno «Nowa reguła» krok po kroku

Kliknij «Nowa reguła» (lub przycisk «Warunek» na первой вкладке, на доле карты pokoju). Otworzy się okno. Jeśli wybrano jeden żywioł, od razu go zaproponuje. Ołówek w wierszu otwiera to samo okno z nagłówkiem «Zmień regułę».

![Okno «Nowa reguła»: żywioł i nazwa, trzy wyzwalacze, pola warunku, akcja i skład](images/rule_editor.png)

1. **Wybierz żywioł w polu «Żywioł komnaty».** Reguła będzie działać tylko tam. Od żywiołu zależy, których tytanów można wybrać: do pokoju «Ziemia» tylko ziemnych, do «Woda» tylko wodnych, a do «Mieszana» dowolnych. Jeśli zmienisz żywioł później — okno samo skoryguje wybór.
2. **Nazwij regułę (opcjonalnie).** Pole «Nazwa reguły» можно оставить пустым: тогда имя составится из условия, например «Araji: PŻ poniżej 50%». Tę nazwę bot zapisuje потом в дневник, когда правило сработало.
3. **Wybierz «Wyzwalacz»** — na co bot powinien zwracać uwagę: «Wg PŻ», «Wg энергии» lub «Wg wrogów».
   - «Wg PŻ» i «Wg энергии»: wybierz **«Tytan»** i wpisz liczbę w polu «PŻ poniżej, %» (lub «Energia poniżej, %») od 0 do 100. Domyślnie PŻ wynosi 35, energia — 100. Jeśli wpiszesz nie-liczby lub liczbę spoza zakresu, pole zaczerwieni się, a pod nim pojawi się «Liczba od 0 do 100».
   - «Wg wrogów»: zaznacz w siatce «Groźni wrogowie w komnacie» wszystkich, którzy muszą występować **razem**. Obok wyświetla się «· wybrano: N». Jeśli nie wybierzesz nikogo — nie można zapisać.
4. **Wybierz «Akcja po zadziałaniu».** Są dwa pola wyboru, wykluczające się nawzajem: „Zatrzymać się i zapytać mnie” oraz «Zakazać wejścia do komnaty (Skip)». Jeśli żadne nie jest zaznaczone — reguła **postawi skład**.
5. **Wymagać przetestowania tytanów (opcjonalnie).** Reguła zadziała tylko wtedy, gdy wybrani tytani (od 1 do 5, z dowolnych żywiołów) stoczyli już bitwę w tym uruchomieniu. Na przykład skład wymaga Sigurda, a ty nie chcesz go stawiać, dopóki w ogóle nie walczył. Krzyżyk obok usuwa przetestowanie. Przetestowanie mają tylko reguły, które stawiają skład. Po miękkiej pauzie i walce ręcznej bot zapomina stan tytanów i przetestowanie zaczyna się od nowa.
6. **Wybierz «Skład dla tej reguły».** Kliknij «Wybierz skład» i w oknie «Zbierz skład» ustaw **od 3 do 5 tytanów** (tak samo jak dla składu podstawowego). Dla opcji «Zapytać ciebie» i «Skip» skład nie jest potrzebny, napisane jest tam «Ta akcja nie wymaga składu».
7. **Kliknij «Zapisz regułę».** Dopóki przycisk jest szary, na dole okna napisane jest, czego brakuje: «Wybierz skład: od 3 do 5 tytanów», «Wybierz co najmniej jednego wroga» lub «Popraw liczbę: od 0 do 100». «Anuluj» zamyka okno bez zmian.

Nowa reguła trafia na **pierwsze место** swojego żywiołu, zmieniona pozostaje na swoim miejscu (jeśli zmieniłeś żywioł, idzie jako pierwsza w nowym). Do pliku trafi, jak cała reszta, po kliknięciu «Zapisz ustawienia». Jeśli otworzyłeś okno przyciskiem «Warunek» z первой вкладки, po zapisaniu pojawi się powiadomienie „Reguła «…» została dodana do zakładki «Reguły i przechwyty»”.

> [!note] Regułę, którą bot zapamiętał sam, można otworzyć ołówkiem i poprawić. Wszystko, czego nie widać w oknie (na przykład „tolerancja strat” lub dodatkowy warunek wg PŻ), **zostanie zachowane bez zmian**. Ten warunek okno pokaże szarym wierszem „Jeszcze w warunku (zostanie zachowane bez zmian): …”.

### Reguły, które bot zapamiętał sam

Jeśli włączony jest «Bot decyduje sam», na liście pojawiają się reguły, których nie napisałeś ty. Widać je po nazwie:

- :refresh-cw: **«Auto: Angus + Sylva w komnacie»** — bot wycofał złą bitwę, powtórzył innym składem i ten dał radę. Bot zapamiętał: „przeciwko tym wrogom stawiać ten skład”. Pod nazwą napisane jest «Zapamiętał bot po wycofaniu» (lub «Twój pak po wycofaniu, zapamiętał bot», jeśli skład wybrałeś ty w oknie SOS). Jeśli skład przegrał z powodu warunku (na przykład „Araji poniżej 50%”), zostaje on dodany do warunku. Taka reguła trafia na pierwsze miejsce.
- :star: **«Złota: Angus + Sylva w komnacie»** — «Pak często pokonywał tych wrogów». Podczas uruchomienia bot przegląda historię i wybiera skład, który przeciwko temu zestawowi wrogów stoczył **5 bitew i więcej** oraz wygrał **80% i więcej**. Podstawowy skład, składy reguł ratowania i twoje składy zapasowe nie trafiają do „złotych”.

W pliku te reguły nazywają się inaczej („Anti-pak przeciwko: …”, „Złota reguła przeciwko: …”) i właśnie tak są zapisywane w dzienniku: `[ОБУЧЕНИЕ] Новое правило '…': пак […]. Сохранено на 1-е место.`. Okno po prostu pokazuje je krótko i w przystępny sposób. Jeśli zmienisz nazwę reguły — zobaczysz swoją nazwę.

Co warto wiedzieć o tych regułach:

- **Bot nie tworzy duplikatów.** Reguła z tym samym warunkiem nie tworzy się po raz drugi: u starej zmienia się skład i przesuwa się ona na górę.
- **Nie każde udane wycofanie jest zapamiętywane.** Jeśli zła bitwa zdarzyła się tylko dlatego, że tytan wszedł do niej ranny, a ze 100% PŻ wszystko byłoby w porządku („wrogowie nie mają nic do rzeczy”), reguła nie powstaje.
- **Wyłączonych reguł bot nie dotyka:** nie włącza ich ani nie nadpisuje. Tego samego składu już więcej nie zapamięta, a wyłączona reguła „złota” nie powróci.
- **Usunięte reguły mogą powrócić.** „Złota reguła” przy następnym uruchomieniu utworzy się ponownie, dopóki przeciwko tym wrogom nie ma innej reguły. Jeśli ci się nie podoba — wyłącz ją przełącznikiem. Regułę „Auto” bot utworzy od nowa, jeśli wycofanie ponownie zakończy się tak samo.
- **Dopóki okno jest otwarte, bot może zapisać nową regułę do pliku.** Gdy klikniesz «Zapisz ustawienia», okno ponownie odczyta plik i umieści te nowe reguły na górze, niczego nie tracąc. Jeśli zajrzałeś na zakładkę, niczego nie zmieniając — zobaczysz świeżą listę z dysku.

> [!warning] Jeśli plik reguł żywiołu jest uszkodzony (na przykład modyfikowano go ręcznie i pomylono wcięcia), okno napisze, na przykład dla wody: «Plik reguł jest uszkodzony: bot_data/rules/water.yml — okno nie zmienia reguł tego żywiołu». Pozostałe żywioły działają. Nie trzeba edytować pliku ręcznie: kliknij «Wyślij log autorowi» na stronie głównej i napisz, co się stało.

> [!tip] Od czego zacząć? Nic nie pisz z góry. Pograj kilkadziesiąt komnat z włączonym «Bot decyduje sam» i zajrzyj tutaj: bot zdąży już zapamiętać kilka reguł. Nieudane wyłącz, dobre podnieś strzałkami wyżej. Dodawaj własne reguły, gdy widzisz powtarzający się problem: „Araji wiecznie chodzi ranny” — reguła ratowania; „ten zestaw wrogów zawsze zabija mój podstawowy skład” — reguła przeciwko wrogom.

> [!done] Teraz potrafisz nauczyć bota wyjątków i rozumiesz, dlaczego stawia właśnie ten skład. Dalej — Telegram i okna, które wzywają cię na pomoc. [Następna sekcja →](#10)

## Gdy walka poszła źle: okna SOS

Prawie всегда bot radzi sobie sam. Ale czasami natrafia na sytuację, w której bez człowieka ani rusz: walka wygrana, ale cena jest zbyt wysoka, albo reguły nie dają ani jednego pasującego paku. Wtedy bot **zatrzymuje się i wzywa cię** okienkiem na środku ekranu. SOS to sygnał alarmowy, jak na statku: „potrzebna pomoc”. Dopóki nie odpowiesz, bot niczego nie klika i czeka (ale nie wiecznie, o tym poniżej).

Są trzy okna, każde dla innego przypadku:

- :triangle-alert: **«Wymagana interwencja»** — walka się skończyła, ale wynik jest zły. To główne okno, pojawia się najczęściej.
- :users: **«Brak pasującego paku»** — bot ещё nie zaczął walki: reguły nie dają mu paku dla tej komnaty.
- :check: **«Pak dał radę»** — sam выбраłeś inny pak, wygrał on, a bot pyta, czy go zapamiętać.

![Okno «Wymagana interwencja»: powód, komnata, wrogowie, twój pak z paskami PŻ i trzy przyciski](images/sos_window.png)

> [!note] Kiedy pojawia się okno: jeśli opcja «Bot decyduje sam» jest **wyłączona** (tak jest domyślnie), okno otwiera się po **każdej** złej walce. Jeśli jest włączona, bot najpierw próbuje poradzić sobie bez ciebie i wzywa cię tylko тогда, gdy nie может: walka toczyła się ręcznie (Angus), okno wyniku nie zostało odczytane, pak wybrałeś ty, w komnacie bot cofał już tyle razy, ile dozwolone, albo brakuje drużyny zapasowej. Czym jest „zła walka” i jak to skonfigurować — w sekcjach o «Baza i pokoje» oraz «Autotaktyka i PŻ».

### Okno «Wymagana interwencja»

Na górze krótko: «Walka poszła źle. Co robimy?». Poniżej fakty, abyś mógł zdecydować bez spoglądania do dziennika:

- **Powód.** Co dokładnie nie spodobało się botowi. Na przykład: „Próg krytyczny! Araji ma 12% PŻ (próg: 40%)”, „Przekroczona Delta strat! Rigel stracił 45% PŻ (tolerancja: 30%)”, „FATALNIE! Iyari nie żyje…”, „Duże straty paku!…” lub „Nie удалось прочитать окно результата: не найдены…”. Imiona tytanów — w języku programu.
- **Komnata.** Żywioł drzwi i numer komnaty: „Ogień · komnata 54”.
- **Wrogowie.** Kafelki tytanów, przeciwko którym toczyła się walka. Jeśli bot nie rozpoznał wrogów — wiersz się не появится.
- **Twój pak.** Każdy tytan ze swoim paskiem zdrowia i napisem „PŻ przed walką → PŻ po”: „36% → 12%”. Jeśli PŻ tytana jest poniżej jego proгу paniki (ogólnego lub indywidualnego), pasek i liczba są **czerwone**. Wszedł do walki ranny i wyszedł prawie bez PŻ — widać to od razu.
- **Licznik czasu.** Na dole: «Bez odpowiedzi bot zdecyduje sam za 9:41». Ostatnia minuta jest żółta, потом «Bot decyduje sam…». Jeśli w sekcji «Autotaktyka и PŻ» ustawiono 0, ten wiersz nie występuje: bot czeka na ciebie zawsze.

Przyciski (od prawej do lewej, główny jest po prawej stronie):

1. **«Cofnij walkę»** (niebieski). Zagraj tę walkę ponownie innym pakiem. Okno ukryje się, otworzy się «Zbierz skład» z obecnym pakiem; zmień tytanów i kliknij «Cofnij z tym pakiem». Co stanie się дальше — w części «Odwrót» poniżej. Jeśli zamkniesz «Zbierz skład» bez wyboru — okno SOS powróci, nic nie zostało utracone.
2. **«Ignoruj»** (szary). Zaakceptuj walkę taką, jaka jest: komnata zostaje zaliczona, bot idzie dalej z tymi PŻ, które zostały. Odpowiednie, gdy straty ci odpowiadają (na przykład tytan i tak wszedł ranny i ogólnie wszystko jest w porządku).
3. **«Przejdź ręcznie»** (szary). Bot niczego nie klika, a ty sam przechodzisz tę komnatę w grze. Bot czeka, aż wrócisz do korytarza: chorągiewka drzwi musi być widoczna przez 2 sekundy z rzędu. Jeśli ostatnie было okno wyniku — komnata zostaje zaliczona; jeśli wycofałeś się bez zwycięstwa — nie. Jeśli zamkniesz okno wyniku bez ponownej gry — walka zostaje zaliczona taka, jaka była. Po ręcznej grze bot zapomina PŻ tytanów i składy w slotach (sam odczyta je ponownie z ekranu wyboru drużyny) i dalej gra sam.

> [!warning] Walki, w której użyto **ręчной superumiejętności Angusa**, nie można cofnąć: na jej oknie wyniku nie ma przycisku „Jeszcze raz”. Zamiast «Cofnij walkę» w oknie появится czerwony przycisk **«Zatrzymaj bota»**, a pozostaną tylko opcje «Ignoruj» lub «Przejdź ręcznie».

### Odwrót: co bot robi po twoim wyborze

Okno się zamknęło, polecenie trafiło do bota. Dalej robi wszystko sam, a w dzienniku widać to po znaczniku `[ОТКАТ]`:

1. Klika **„Jeszcze raz”** w oknie wyniku i czeka na wczytanie walki (czasami trwa to 20–30 sekund lub dłużej, dlatego czeka do minuty).
2. Wstrzymuje walkę **pauzą** (jeden raz) i klika **„Wycofaj się”**.
3. Wraca do korytarza, wchodzi do **tej samej komnaty** i ustawia twój nowy pak.

Jeśli walka znów poszła źle — okno powróci. Jeśli poszła dobrze — появится okno «Pak dał radę» (opisane poniżej).

Jeśli połączenie z grą zostało utracone (obrazek „ładowanie” nie znika), bot nie poddaje się: czeka na grę do 15 minut i pisze o tym w dzienniku. Tylko если wycofanie nie powiedzie się, bot zapisuje zrzut ekranu w `bot_data/debug/`, włącza miękką pauzę i wysyła ci wiadomość na Telegramie. Szczegóły — w sekcji o problemach.

### Okno «Brak pasującego paku»

Pojawia się, gdy bot выбраł już drzwi i spojrzał na wrogów, ale **nie ma co wystawić**. Zdarza się z dwóch powodów, obu wynikających z twoich reguł:

- zadziałała reguła „Zapytaj mnie” (została stworzona właśnie po to);
- główny pak komnaty содержит tytana, которого zabroniła reguła „Skip” (bot pisze coś w stylu „FATALNIE: Wszystkie paki odrzucone…”).

Okno pyta: «Reguły nie dają paku dla tej komnaty. Co robimy?». W nim znajdują się te same pola «Powód», «Komnata» i «Wrogowie», ale bez pasków PŻ: walka się ещё nie odbyła. Przyciski:

- **«Zbuduj nowy pak»** (niebieski) — otwiera «Zbierz skład», przycisk nazywa się tam «Zastosuj». Bot ustawi wybranych tytanów i **od razu zapamięta pak jako regułę** „przeciw tym wrogom” (nie ma tu weryfikacji przed zapamiętaniem, bądź uważny).
- **«Przejdź ręcznie»** — przechodzisz komnatę sam, bot czeka w korytarzu. Komnata zostaje zaliczona, jeśli wygrasz.
- **«Zatrzymaj bota»** (czerwony) — bot pisze podsumowanie sesji i wyłącza się.

Przycisku «Ignoruj» tu nie ma: nie ma czego akceptować, walka się nie odbyła.

### Okno «Pak dał radę»

To okno pojawia się, gdy walkę wygrał pak, который **wybrałeś ty** (poprzez «Cofnij walkę» lub «Spróbuj inny», w oknie lub na Telegramie). Jeśli drużynę zapasową выбраł sam bot i dała ona radę, bot sam ją zapamięta i o nic nie zapyta.

Wewnątrz — komnata, wrogowie (z ostatniego okna SOS, jeśli miało miejsce nie dawniej niż 15 minut temu) oraz twój pak z PŻ po walce. Pytanie: «Testowany pak wygrał. Zapamiętać go jako regułę przeciw tym wrogom?». Przyciski:

- **«Zapisz pak»** (zielony) — bot zapamięta regułę „przeciw tym wrogom” z tym pakiem. Na liście reguł pojawi się jako «Auto: …» lub «Twój pak po wycofaniu, zapamiętał bot».
- **«Spróbuj inny»** — znowu «Zbierz skład» i odwrót: bot zagra wygraną walkę ponownie innym pakiem.

Jeśli nie odpowiesz — po upływie czasu z licznika (napis „Bez odpowiedzi bot zapisze pak sam za…”) bot zapisze pak sam, tak jakbyś kliknął «Zapisz pak».

### Krzyżyk okna i «Zatrzymać bota?»

Okna nie mają opcji „po prostu zamknij”: jeśli zamkniesz okno, bot nadal będzie czekał na odpowiedź. Dlatego krzyżyk pyta: **«Zatrzymać bota?»**. Jeśli odpowiesz „Zatrzymaj bota” — bot zakończy pracę, napisze podsumowanie i wyśle je na Telegram. Jeśli nie odpowie w ciągu 10 sekund, program zatrzyma go sam. W oknie «Pak dał radę» pytanie jest inne: zatrzymanie działa tam tak samo, jak przy „STOP F10”, **podsumowanie сессии nie zostanie wysłane na Telegram**. Jeśli zmieniłeś zdanie — kliknij «Anuluj», okno pozostanie.

### Co się stanie, если не odpowiesz

Za каждым разом, gdy nie odpowiesz w czasie ustawionym w sekcji «Autotaktyka i PŻ» («Limit czasu okna SOS без ответа, мин»: domyślnie 10, do 60, 0 — czekaj всегда), bot pisze `[ТАКТИКА] Ответа нет 10 мин. Решаю сам.`, okno zamyka się i otrzymujesz wiadomość na Telegramie, że bot podjął decyzję sam. Działa to również при выłączonym trybie «Bot decyduje sam». Decyzja zależy od okna:

- **«Wymagana interwencja»:** если есть drużyna zapasowa i walkę можно cofnąć (nie Angus, próby w komnacie się nie skończyły) — **odwrót** i drużyna zapasowa; w przeciwnym razie, если wszyscy tytani żyją — walka zostaje **zaakceptowana** («Ignoruj»); w przeciwnym razie (ktoś zginął lub nie został znaleziony w oknie) — **miękka pauza**.
- **«Brak pasującego paku»:** если pasuje drużyna zapasowa без rannych и bez zabronionych tytanów — bot ustawia ją **i nie zapamiętuje reguły**; jeśli takiej nie ma — **miękka pauza**.
- **«Pak dał radę»:** pak zostaje zapisany.

Miękka pauza działa jak przycisk „Pauza F9”: bot czeka w korytarzu, aż klikniesz «Kontynuuj».

> [!tip] Odpowiedziałeś w tej samej chwili, gdy bot podjął już decyzję sam? Nic strasznego: bot pominie starą odpowiedź i napisze `[ЛОГИКА] Пропускаю ответ ...: он пришёл на прошлое окно.`

### Odpowiedź z Telegrama

Jeśli Telegram jest skonfigurowany, **to samo pytanie** trafia również na czat: zrzut ekranu z gry, podpis (komnata, wrogowie, powód, pak z PŻ) oraz przyciski. Możesz odpowiedzieć tam, gdzie ci wygodniej: jeśli odpowiesz na czacie — okno na komputerze zamknie się samo, i na odwrót.

- **«Cofnij (Złóż skład)»** (zielony) — bot poprosi o wpisanie na czacie imion **3–5 tytanów** po przecinku lub spacji, pokaże, kogo rozpoznał, i zapyta «Czy wszystko się zgadza?» («Zatwierdź skład» / «Wpisz inny»). Dla walki ręcznej Angusa oraz dla «Brak pasującego paku» zamiast niej pojawi się czerwony прициск «Zatrzymaj bota».
- **«Przejdź ręcznie»** oraz **«Ignoruj (Kontynuuj)»** — to samo, co w oknie. W oknie «Brak pasującego paku» przycisku «Kontynuuj» nie ma.
- Wiadomość «Pak dał radę» trafia na Telegram tylko wtedy, gdy pak wysłałeś również stamtąd: «Zatwierdź i Zapisz» lub «Cofnij i Spróbuj ponownie».

Jeśli połączenie z interเนtem zostanie utracone, wiadomość zostanie wysłana później (bot ponawia próby), a samo okno na komputerze pozostaje. Konfiguracja Telegrama znajduje się w poświęconej mu sekcji.

### Pasek miniaturowy i okna SOS

Jeśli okно programu jest zminimalizowane do paska miniaturowego, okno SOS pojawi się **na środku gry**. Pasek miniaturowy staje się w tym czasie czerwony, a jego przycisk «SOS» przywraca zagubione okno ponad grę.

> [!tip] Jak wybierać? Spójrz na «Twój pak». Jeden tytan wszedł ranny i osłabł, reszta w porządku — często wystarczy «Ignoruj». Wrogowie są ci znani i znacznie silniejsi — «Cofnij walkę» z innym pakiem. Nic nie jest jasne — «Przejdź ręcznie». Odwrót wymaga czasu (walkę trzeba wczytać na nowo, co trwa 20–30 sekund lub dłużej), a «Ignoruj» nie kosztuje nic.

> [!done] Teraz wiesz już, co oznacza każde okno SOS, co robi dany przycisk i co bot zrobi bez ciebie. Dalej — jak bot decyduje sam, gdy nie ma cię w pobliżu. [Następny rozdział →](#11)

## Jak bot decyduje sam

W sekcji o oknach SOS widziałeś, że bot wzywa cię po złej walce. Ale nie zawsze tak jest: если włączysz opcję «Bot decyduje sam» (zakładka «Baza i pokoje», rozdział 7), bot **najpierw próbuje poradzić sobie bez ciebie** i prosi o pomoc tylko wtedy, gdy mu się nie uda. Tutaj przeanalizujemy, jak myśli. Nie będzie tu wzorów: только pytania, które bot sobie zadaje, oraz przykłady.

Wyobraź sobie doświadczonego partnera, który siedzi obok ciebie przy telefonie. Walka poszła źle, a ty poszedłeś po herbatę. Nie będzie siedział i czekał. Przypomni sobie, co już pomagało przeciwko takim wrogom, zagra walkę ponownie innym składem i zapisze, co zadziałało. Mniej więcej tak zachowuje się bot. Tyle że ma reguły, aby nie narobić szkód.

> [!note] Opcja «Bot decyduje sam» jest domyślnie **wyłączona**, i wszystko, o czym mowa poniżej, w takim przypadku się nie dzieje: po każdej złej walce bot po prostu otwiera okno SOS. Jeśli włączyłeś przełącznik i kliknąłeś «Zapisz ustawienia» — zadziała to od następnego kliknięcia «Zacznij farmić». Co dokładnie można dostosować, omówiliśmy w rozdziale 8 («Autotaktyka i PŻ»), a tutaj mowa o tym, **co bot robi z tymi liczbami**.

### Zła walka: co bot robi po kolei

1. **Zauważa, że walka jest zła.** Ktoś zginął lub ma PŻ poniżej progu paniki, stracił więcej niż wynosi tolerancja albo aż trzech tytanów uległo osłabieniu (rozdział 7 i 8). W dzienniku pojawia się wiersz `[ТАКТИКА] Плохой бой: ...` z powodem.
2. **Sprawdza, czy może cofnąć sam.** Nie może w czterech przypadkach: walka toczyła się ręcznie (superumiejętność Angusa, na oknie wyniku nie ma прициску „Jeszcze raz”), okno wyniku nie zostało odczytane, pak ustawiłeś **ty** (wtedy decyzja należy do ciebie) lub bot wykorzystał już próбы w tej komnacie. Jeśli nie może — otwiera się okno SOS, a w dzienniku pojawia się `[ТАКТИКА] Сам не откатываю: ... Спрашиваю вас.` z powodem.
3. **Szuka drużyny zapasowej.** Jak — w następnym rozdziale. Jeśli nie ma pasującej — znowu okno SOS.
4. **Cofa i gra ponownie.** Te same kroki `[ОТКАТ]`, co po twoim wyborze („Jeszcze raz”, pauza, „Wycofaj się”), a w tej samej komnacie zostaje ustawiona drużyna zapasowa. W dzienniku pojawia się `[ТАКТИКА] Откатываю бой сам и переиграю паком ... (взят: ...)`.
5. **Sprawdza wynik.** Jeśli drużyna zapasowa dała radę — bot idzie dalej i zazwyczaj zapamiętuje pak (o tym poniżej). Jeśli walka znów jest zła — następuje druga próba, i tak dalej, aż skończą się próby («Ile składów zapasowych próbować w pokoju», domyślnie 2, nie więcej niż 3). Potem wzywa ciebie.

> [!tip] Bot za każdym razem cofa całą walkę, a nie „poprawia w trakcie”. Odwrót wymaga czasu (walkę trzeba wczytać na nowo, co trwa 20–30 sekund lub dłużej), dlatego nie lubi pustych prób: patrz poniżej, jak wybiera pak.

### Skąd bot bierze drużynę zapasową

Przegląda listę od góry do dołu i bierze **pierwszy pasujący**:

1. **Twoje «Drużyny zapasowe»** — zakładka «Baza i pokoje», karta komnaty. Pobierane są po kolei, tak jak je ustawiłeś. W dzienniku źródło nazywa się „twój pakiet drużyn zapasowych”.
2. **Paki z reguł danego żywiołu** — w dzienniku „reguły żywiołu”. Wewnątrz obowiązuje własna kolejność: najpierw reguły „przeciw tym wrogom”, potem paki, które już wygrywały z tymi konkretnymi wrogami (najlepsze pod względem pozostałych PŻ jako pierwsze), potem pozostałe „anty-paki”, a na końcu reszta, włącznie z głównym pakiem komnaty.
3. **Historia walk** — w dzienniku „historia walk”. To ostatnia kolejka i pobierane są tylko paki, które już wygrywały z tymi wrogami. Bot pamięta walki z ostatnich 20 uruchomień.

Czego bot **nigdy nie wstawi** jako drużyny zapasowej:

- paku, który już przegrał w tej komnacie (żeby nie powtarzać błędu);
- paku, który „przegrywa z tymi wrogami”: poprzednio przeciwko nim walka została cofnięta z winy wrogów, a liczba wygranych paku nie jest większa niż liczba porażek. Jedna nieudana próba **nie psuje dobrego paku**: jeśli wygrał przeciwko tym wrogom pięć razy i raz przegrał, bot nadal go użyje;
- paku z tytanem, którego zabroniła reguła „Skip”;
- paku z tytanem, którego PŻ jest już **poniżej progu paniki**: bot nie wyśle go do walki na pewną śmierć;
- z historii — paku, w którym znajduje się tytan, którego nigdzie nie wskazałeś (ani w pakach, ani w regułach). W historii pozostają paki dawno usuniętych reguł, a bot ich nie wskrzesza.

Istnieją również paki „niebezpieczne”: takie, w których ranny tytan, sądząc po poprzednich walkach, nie dożyje do końca starcia. Bot wybiera je **w ostatniej kolejności**, tylko jeśli nie ma nic lepszego. Jak to określa — w części „Ranny tytan” poniżej.

Dlaczego bot nie wziął danego paku, widać w dzienniku: `[ТАКТИКА] Не беру запасной пак ...` oraz powód. Jeśli opcje zapasowe się skończyły, a walka nadal jest zła — to nie awaria, ale szczere „nie wiem, co jeszcze wystawić”.

### Zapamiętać czy nie: reguła «Auto: …»

Drużyna zapasowa dała radę. Bot zapisuje to jako regułę „przeciw tym wrogom — ustaw ten pak”, i następnym razem, gdy spotka taki sam skład, ustawi go od razu. Na liście ta reguła to «Auto: {names} w komnacie», trafia na pierwsze miejsce (rozdział 9). W dzienniku: `[ТАКТИКА] Запасной пак ... справился. Запоминаю его против этих врагов.`

Ale bywa i tak, że **zapamiętywać nie wolno**. Przykład: Araji wszedł do walki z 36% zdrowia i spadł do 5%. Główny pak nie jest winny: gdyby Araji był zdrowy, walka poszłaby dobrze. Gdyбы bot zapisał regułę „przeciw tym wrogom ustawiaj pak zapasowy”, zacząłby wystawiać drużynę zapasową tam, где główna radzi sobie świetnie, marnując twoją siłę. Dlatego bot sprawdza: **„a czy ze 100% PŻ u wszystkich walka byłaby zła?”**. Jeśli nie — oznacza to, że wrogowie nie są winni, pomoc była jednorazowa, a reguła nie powstaje.

W dzienniku widać to od razu: `[ТАКТИКА] Враги ни при чём: в бой вошли раненые ...` a potem `Правило не запоминаю: это была разовая помощь раненым титанам`.

Zapamiętanie nie uda się również w trzech innych przypadkach:

- bot nie rozpoznał wrogów (`[ОБУЧЕНИЕ] Враги не распознаны — правило не сохраняю`): reguła „bez wrogów” zadziałałaby w każdej komnacie;
- wyłączyłeś regułę z takim samym pakiem przełącznikiem: wyłączonej reguły bot nie rusza;
- pak wybrałeś sam: wtedy decyduje twoje okno «Pak dał radę» (rozdział 10).

### Ranny tytan: pomoc z wyprzedzeniem, a nie po walce

Najcenniejsze, co potrafi bot, to **nie dopuszczać do złej walki**, a nie naprawiać jej skutki. Gdy znajduje się na ekranie wyboru drużyny, patrzy na zdrowie tytanów oraz historię: „jak kończyły się walki tym pakiem w tej komnacie?”. W tym celu bot przechowuje informację, ile PŻ tytan zazwyczaj **traci** w walce z tym pakiem (średnia z последних pięciu walk, potrzebne są co najmniej dwie walki). Jeśli ranny na wejściu tytan po odjęciu zwykłej straty PŻ **spadnie poniżej progu paniki** — bot nie będzie ryzykować i od razu ustawi drużynę zapasową, jeszcze przed walką.

Przykład: Araji z 36% PŻ idzie na ogień. W ostatnich walkach tutaj zazwyczaj tracił około 29%. Wychodzi: 36 − 29 = 7%, a próg paniki wynosi 40. Walka prawie na pewno skończy się źle, więc bot **od razu** ustawia pak zapasowy, na przykład z Molochem. To jednorazowa pomoc, reguła nie jest zapamiętywana.

Dwie niuanse, aby bot nie wydawał się dziwny:

- **Energia również jest ważna.** Jeśli tytan ma teraz mniej więcej tyle energii, co w poprzednich walkach (różnica nie większa niż 25%), bot przyjmuje do prognozy właśnie te walki. Araji z dobrą energią traci w ogniu mało, z pustą dużo, i prognoza to uwzględnia.
- **Jedna walka to nie statystyka.** Przy меньше niż dwóch walkach bot nie ufa prognozie i niczego nie zmienia.

Paków z reguł ratunkowych („jeśli Araji ma poniżej 50% — ustaw Sigurda”, rozdział 9) bot nie zastępuje z wyprzedzeniem: ustawiłeś je właśnie dla rannego, a twój zamysł jest ważniejszy niż jego prognoza.

### Drzwi według stanu zdrowia

Jeśli bot decyduje sam i w korytarzu widać **kilka dozwolonych drzwi**, wybiera nie tylko według kolejności (rozdział 8, «Kolejność drzwi»), ale uwzględniając rannych:

1. Najpierw idzie do drzwi, **za którym ranny zostanie uleczony**: zadziała twoja reguła ratunkowa lub bot sam złoży skład leczący.
2. Drzwi, za którym rannemu — sądząc po poprzednich walkach — grozi niebezpieczeństwo, bot **pomija**, jeśli są inne.
3. W przeciwnym razie wszystko odbywa się jak zwykle, według kolejności.

Widać to po wierszu `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...`. Drzwi zabronionych przez regułę „Skip” bot nadal nigdy nie otworzy. Wrogów za drzwiami bot jeszcze nie widzi, dlatego opiera się tutaj na podstawowym paku drzwi.

### Skład leczący w komnacie „Mieszanej”

Jeśli rannego można uleczyć, a twoja reguła leczenia nie zadziałała, bot **sam składa skład leczący**: ustawia w komnacie „Mieszanej” rannego oraz, jeśli trzeba, zdrowego, naładowanego uzdrowiciela. Leczą po jednym tytanie, głównych wcześniej niż zapasowych, a tych, którzy są poniżej progu paniki, nie leczą wcale. Wszystkie szczegóły (próg «Leczyć tytana, если PŻ poniżej, %», «Kogo usunąć ze składu dla rannego», ten sam Sigurd dla Rigela) — w rozdziale 8. Tutaj ważne jest jedno: to taka sama **jednorazowa pomoc**, jak pak zapasowy z prognozy. Reguła po niej nie powstaje, a w podsumowaniu jest liczona osobno („składy leczące (bot złożył sam)”).

### «Złote reguły»: bot uczy się na całej historii

Wszystkie te decyzje bot podejmuje w trakcie gry. A „złote reguły” podsumowuje **raz, przy uruchomieniu farmy**. Bot przegląda historię walk i szuka paku, który przeciwko takiemu samemu składu wrogów stoczył **5 walk lub więcej i wygrał 80% lub więcej**. Taki pak zapisuje jako regułę «Złota: {names} w komnacie» (rozdział 9). W dzienniku: `[ОБУЧЕНИЕ] ...: 'Золотое правило против: ...' — пак ... Сохранено на 1-е место.`

Złotą regułą nie stanie się:

- główny pak komnaty, paki reguł ratunkowych i twoje «Drużyny zapasowe» (służą do pomocy, a nie do każdej walki);
- składy leczące, które bot złożył sam: są potrzebne tylko wtedy, gdy tytan jest ranny;
- pak z tytanem, którego nie ma w twoich pakach ani regułach;
- pak przeciwko wrogom, dla których reguła już istnieje (twoja, «Auto» lub wyłączona).

Złotych reguł nie ma, dopóki opcja «Bot decyduje sam» jest wyłączona. Pojawiła się nieudana reguła? **Wyłącz ją przełącznikiem**, a nie usuwaj: usunięta powróci przy następnym uruchomieniu, wyłączonej bot nie ruszy.

### Jeśli nie odpowiedziałeś na okno SOS

To już nie jest „bot decyduje sam”, ale „bot decyduje za ciebie” (rozdział 10, „Co się stanie, jeśli nie odpowiesz”). Działa to również przy wyłączonym «Bot decyduje sam»: po upływie limitu czasu («Limit czasu okna SOS без ответа, мин») bot cofnie walkę pakiem zapasowym, zaakceptuje ją lub włączy miękką pauzę. Za każdym razem pisze `[ТАКТИКА] Ответа нет N мин. Решаю сам.`, zamyka okno i wysyła wiadomość na Telegramie.

### Jak zrozumieć, co bot robił bez ciebie

Na końcu сессии w bloku «Podsumowanie sesji» (przycisk «Szczegóły») oraz w wierszu `[ИТОГ]` znajdują się liczniki:

- **„cofnięcia”**: ile walk zagrało się ponownie w sumie;
- **„w tym bez ciebie”**: ile z tych cofnięć bot wykonał sam, nie pytając, zarówno z prognozy, jak i po upływie limitu czasu;
- **„składy leczące (bot złożył sam)”**: ile razy leczył rannego składem leczącym.

To samo podsumowanie trafi na Telegram: „Cofnięć: 6 (bot sam: 5)”. Jeśli „bez ciebie” to prawie wszystko, bot daje radę. Jeśli liczba rośnie, a «Złote reguły» się nie pojawiają, oznacza to, że ci sami wrogowie raz za razem niszczą główny pak. Zajrzyj do zakładki «Reguły i przechwyty», какие reguły zapamiętał, i zastanów się, czy nie czas zmienić główny pak.

> [!warning] Bot decyduje na podstawie **historii** oraz prognozy, a nie widzi walki z góry. Może się pomylić: w pierwsze dni, gdy historii jest mało, drużyna zapasowa jest dobierana po omacku. Nie strasz się, jeśli przez pierwsze kilkadziesiąt komnat przy opcji «Bot decyduje sam» cofa walki częściej, niżbyś chciał. Im więcej walk w historii, tym dokładniejszy wybór.

> [!tip] Od czego zacząć? Ustaw co najmniej po jednej lub dwóch «Drużynach zapasowych» w każdej komnacie (rozdział 7): wtedy bot nie będzie szukał po omacku. Włącz «Bot decyduje sam» i przez parę dni po prostu obserwuj wiersze `[ТАКТИКА]` oraz «Podsumowanie sesji». Jeśli nie podoba ci się, co bot robi — wyłącz przełącznik, a wszystko wróci do okien SOS.

> [!done] Teraz rozumiesz, kiedy i jak bot radzi sobie bez ciebie, co zapamiętuje i kiedy wzywa pomoc. Dalej — Telegram: jak otrzymywać wiadomości, gdy nie ma cię przy komputerze. [Następny rozdział →](#12)

## Telegram

Bot może pisać do ciebie w Telegramie, gdy jesteś z dala od komputera: poszedłeś do kuchni, poszedłeś spać, pojechałeś do pracy. Jeśli walka wymaga twojej pomocy, na czacie pojawi się zrzut ekranu i przyciski. Naciśniesz przycisk na telefonie — bot zrobi tak, jak powiesz. Jeśli wszystko idzie gładko, bot milczy: wiadomości przychodzą **tylko w przypadku problemów** i **raz na końcu sesji**.

Co będzie potrzebne: aplikacja Telegram i pięć minut. Konfigurację przeprowadza się tylko raz.

> [!note] Telegram jest opcjonalny. Bez niego bot działa tak samo, po prostu okna SOS widzisz tylko na ekranie komputera, a podsumowania sesji nie ma. Ale jeśli planujesz zostawiać bota na noc, skonfiguruj go: dzięki temu dowiesz się o problemie od razu, a nie rano.

### Co trzeba przygotować

Potrzebujesz dwóch rzeczy, obu uzyskanych w samym Telegramie:

- :send: **Token bota** (klucz, za pomocą którego program loguje się do twojego bota). Jest to długi ciąg cyfr i liter, np. `123456789:AAH…`. Token wydaje specjalny bot **@BotFather**.
- :user: **Chat ID** (numer czatu). Jest to liczba, po której Telegram wie, do kogo dostarczyć wiadomość: do ciebie, a nie do kogoś innego.

> [!warning] Token jest jak hasło do twojego bota. Nikomu go nie pokazuj, nie wysyłaj na zrzutach ekranu ani w wiadomościach (nawet autorowi programu). Zrzut ekranu okna «Ustawienia Telegrama» rób wtedy, gdy token jest ukryty kropkami.

### Krok po kroku

1. **Stwórz swojego bota.** W Telegramie znajdź **@BotFather** (prawdziwy ma obok niebieską parafkę) i naciśnij «Uruchom». Napisz do niego `/newbot`, wymyśl nazwę (dowolną, zobaczysz ją tylko ty) oraz login kończący się na `bot`, np. `moi_titan_bot`. W odpowiedzi BotFather wyśle wiadomość z tokenem: skopiuj go.
2. **Sprawdź swój Chat ID.** Znajdź bota **@getmyid_bot**, naciśnij «Uruchom» — odpowie linijką `Your user ID` i liczbą. To właśnie jest Chat ID, skopiuj tę liczbę. Jeśli ten bot nie odpowiada, jest alternatywna droga: napisz dowolne słowo do **swojego** bota z kroku 1, otwórz w przeglądarce adres `https://api.telegram.org/bot<твой токен>/getUpdates` (zamiast `<твой токен>` wstaw token) i znajdź w odpowiedzi `"chat":{"id":` — liczba zaraz po nim to właśnie Chat ID.
3. **Naciśnij «Uruchom» u swojego bota.** Znajdź bota utworzonego w kroku 1 i naciśnij «Uruchom» (lub napisz do niego `/start`). Bez tego Telegram **nie zezwoli** botowi pisać do ciebie jako pierwszemu. To najczęstsza przyczyna, dla której wiadomości nie przychodzą.
4. **Otwórz okno w programie.** Naciśnij kropkę Telegrama na pasku po lewej stronie lub przycisk **«Skonfiguruj Telegram»** w zakładce «Baza i pokoje» (sekcja 7). Otworzy się okno «Ustawienia Telegrama».
5. **Wypełnij je.** Włącz przełącznik «Wysyłać wiadomości do Telegrama». W polu «Token bota (od @BotFather)» wklej token, w polu «ID czatu» wklej liczbę. Najwygodniejszy jest przycisk **«Wklej»** obok pola: pobiera to, co skopiowałeś. Token jest ukryty kropkami; ikona oka pokazuje go, aby sprawdzić, czy został wklejony poprawnie. Prawy przycisk myszy na polu to również «Wklej».
6. **Sprawdź połączenie.** Naciśnij **«Sprawdź Telegram»**. Po kilku sekundach po prawej stronie pojawi się zielone «Wiadomość wysłana — sprawdź Telegram», a na czacie z twoim botem — wiadomość «Test połączenia: wszystko działa». Jeśli przyszła — wszystko gotowe.
7. **Zapisz.** Naciśnij **«Zastosuj»**, a następnie na dole strony **«Zapisz ustawienia»**.

![Okno «Ustawienia Telegrama»: przełącznik, pola tokena i ID czatu, przyciski «Wklej» i «Sprawdź Telegram»](images/telegram_window.png)

> [!warning] «Zastosuj» tylko przenosi wartości na stronę „Kreatora reguł”, do pliku **nie są zapisywane**. Dopóki nie naciśniesz «Zapisz ustawienia», na dole świeci się «Są niezapisane zmiany», a bot nic nie wie o Telegramie. Jeśli opuścisz stronę bez zapisu — program zapyta «Zapisać zmiany?».

> [!tip] «Sprawdź Telegram» sprawdza to, co jest obecnie wpisane w oknie, nawet jeśli jeszcze niczego nie zapisałeś. Dlatego sprawdzaj **przed** naciśnięciem «Zastosuj»: znalazłeś błąd — poprawiłeś — sprawdziłeś ponownie. Sprawdzanie odbywa się w tle, okno się nie zawiesza i nie trzeba czekać na odpowiedź dłużej niż 20 sekund.

### Jeśli test się nie powiódł

Pod przyciskiem pojawi się czerwony napis „Nie wysłano: …” z przyczyną. Najczęstsze z nich:

- **«Uzupełnij token i ID czatu»** — jedno z pól jest puste.
- `Unauthorized` — token jest nieprawidłowy: zgubiono znak, dodano zbędną spację lub skopiowano nie całość. Wklej go ponownie przyciskiem «Wklej».
- `chat not found` lub `Forbidden` — ID czatu jest nieprawidłowe lub nie nacisnąłeś «Uruchom» u **swojego** bota (krok 3). Sprawdź oba punkty.
- **«błąd połączenia z Telegramem»** — brak internetu lub Telegram z tego komputera się nie otwiera. Sprawdź, czy na tym samym komputerze działa Telegram (lub strona telegram.org).

Jeśli po poprawieniu wiadomość nadal nie przychodzi, stwórz nowego bota u @BotFather (krok 1) i zacznij od nowa: to szybsze niż szukanie literówki.

### Jak rozpoznać, że Telegram jest włączony

Na pasku po lewej stronie przy przycisku Telegrama znajduje się kropka: po najechaniu myszą pojawi się podpowiedź **«Telegram: włączony»** lub **«Telegram: nieskonfigurowany»**. Włączony — oznacza, że przełącznik jest ustawiony i oba pola są wypełnione. To **nie jest test połączenia**: czy token działa, pokaże tylko przycisk «Sprawdź Telegram». To samo widać w zakładce «Baza i pokoje»: obok przycisku «Skonfiguruj Telegram» świeci się zielone «Powiadomienia SOS włączone» lub szare «Telegram nieskonfigurowany». Kropka odświeża się sama po kilku sekundach od zapisania.

### Jakie wiadomości przychodzą

Język wiadomości jest taki sam, jaki wybrano w oknie programu.

- :swords: **Okno SOS** — nagłówek «Potrzebna twoja pomoc» (lub «Brak pasującego paku»), zrzut ekranu z gry i podpis: pokój, wrogowie (na kogo szli), przyczyna, twój skład z paskami HP i energii. Na dole przyciski. To samo pytanie, co w oknie na komputerze (sekcja 10).
- :triangle-alert: **Alerty** — krótka wiadomość bez przycisków, która mówi, co się stało i co zrobić. Oto one: «Nie udało się cofnąć walki» (bot jest w miękkiej pauzie, spójrz na ekran telefonu), «Bot chyba się zawiesił» (5 minut bez pokoju) i taka sama wiadomość, gdy nie udaje się rozpocząć walki (najprawdopodobniej brak połączenia z serwerem gry), «Ekran komputera jest zablokowany» (bot nie widzi gry dłużej niż minutę; odblokuj komputer, a sam kontynuuje) i «Nie odpowiedziałeś — bot zdecydował sam».
- :chart-no-axes-column: **Podsumowanie sesji** — gdy bot się zatrzymał: ile minęło czasu, pokoi, pięter i tytanitu, czy były cofnięcia i okna SOS («bot sam: N» — to cofnięcia, które wykonał bez ciebie), najdłuższe pokoje. Jeśli bot przerwał pracę z powodu błędu, w nagłówku pojawi się «Bot przerwał pracę z powodu błędu» oraz przyczyna.

Podsumowanie przychodzi przy każdym zatrzymaniu: osiągnięto cel, naciśnięto Ctrl+Q, Ctrl+Shift+Q, bot przerwał pracę z powodu błędu. **Nie przychodzi** po „STOP F10” i po «Zatrzymaj i zamknij» (sekcja 6), ponieważ natychmiast zamykają one bota.

### Przyciski pod wiadomością SOS

Naciskaj je w Telegramie tak samo jak w oknie na komputerze:

- **«Cofnij (Złóż skład)»** (zielony). Bot wyśle: „Napisz imiona 3-5 tytanów na czacie”. Napisz je na czacie po przecinku lub spacji, np. `гиперион, сигурд, нова` lub krótko, pierwszymi trzema literami: `гип сиг нов`. Bot odpowie, kogo rozpoznał, i zapyta „Czy wszystko się zgadza?”: **«Zatwierdź skład»** uruchomi cofnięcie, **«Wpisz inny»** pozwoli wprowadzić ponownie. Jeśli nie znalazł 3–5 tytanów — bot powie, ilu rozpoznał, i poprosi o ponowne napisanie.
- **«Przejdź ręcznie»** (niebieski). Bot niczego nie naciska i czeka, aż sam dokończysz pokój.
- **«Ignoruj (Kontynuuj)»** (szary). Zaakceptować walkę taką, jaka jest, i iść dalej.
- **«Zatrzymaj bota»** (czerwony). Zamiast «Cofnij» jest pokazywany wtedy, gdy walka toczyła się ręcznie (ult Angusa) lub brakuje odpowiedniego składu. W oknie «Brak pasującego paku» przycisku «Kontynuuj» nie ma.

Gdy skład wybrany przez ciebie dał radę, pytanie «Pak dał radę» przychodzi do Telegrama z dwoma przyciskami: **«Zatwierdź i Zapisz»** (zapamiętaj skład regułą) i **«Cofnij i Spróbuj ponownie»** (napisz inny). Przychodzi na czat tylko wtedy, gdy skład wysłałeś również z Telegrama.

Po naciśnięciu pod wiadomością pozostaje jeden zielony przycisk „Wybrano: …”, pozostałe znikają. Odpowiedzieć można **tylko raz**: naciśnięć na starą wiadomość bot nie słucha. Odpowiedziałeś na czacie — okno na komputerze zamknie się samo, odpowiedziałeś na komputerze — bot przestanie czekać na odpowiedź z Telegrama.

> [!tip] Bot zdecydował sam, gdy szukałeś telefonu? Nic strasznego. Przyjdzie wiadomość «Nie odpowiedziałeś — bot zdecydował sam», a przyciski na starym pytaniu nic już nie zrobią. Ile czasu bot na ciebie czeka, ustawia się w „Auto-taktyce” (sekcja 8, «Limit czasu okna SOS bez odpowiedzi, min»).

### Jeśli internet zaniknął

Bot nie zatrzymuje się i nie czeka na Telegram: wiadomość wychodzi w tle. Jeśli nie udało się z powodu połączenia, próbuje ponownie po **30 sekundach, 1, 2, 5 i 10 minutach** (łącznie około 18 minut), a w dzienniku widać linijki `Сообщение в Telegram не ушло (...). Пробую снова через N с.` i na końcu `Сообщение в Telegram: отправлено с N-й попытки`. To samo dotyczy okna SOS: pozostaje ono na ekranie komputera, a pytanie trafi do Telegrama, gdy połączenie powróci. Podsumowanie sesji bot powtarza krócej (po 10 i 30 sekundach), ponieważ po nim się wyłącza. Błędów samego Telegrama (nieprawidłowy token) bot nie powtarza: należy je poprawić w ustawieniach.

> [!note] Bot nie przyjmuje od ciebie poleceń „w dowolnym momencie” (zatrzymaj, wstrzymaj z poziomu czatu). Telegram odpowiada tylko na pytania, które bot sam zadał. Zatrzymanie bota z poziomu czatu nie jest możliwe, z wyjątkiem przycisku «Zatrzymaj bota» pod wiadomością SOS.

> [!done] Telegram jest skonfigurowany i teraz bot będzie mógł cię wezwać, gdziekolwiek jesteś. Dalej — statystyki: ile pokoi, pięter i tytanitu zebrano z podziałem na dni. [Następna sekcja →](#13)

## Statystyki

Strona «Statystyki» odpowiada na pytanie „ile nagrałem?”: ile tytanitu, pokoi, pięter i mikstury tytanów zebrało się w ciągu tygodnia, miesiąca i całego czasu. Otwiera się ją прициском **«Statystyki»** na pasku po lewej stronie, na górze napisane jest «Statystyki aktywności».

Te liczby bot **liczy sam**, a nie odczytuje z ekranu gry. Przeszedł pokój — zapisał: **6 tytanitu i 25 mikstury**, a jeśli w oknie wyniku była ikonka „x2” — **12 tytanitu i 50 mikstury**. Otrzymał nagrodę w punkcie kontrolnym — zapisał piętro. Pokój, który przeszedłeś ręcznie i który bot zaliczył (sekcja 10), również zapisuje. Podsumowania znajdują się w pliku `bot_data/stats.json` i są przechowywane według „dni gry”.

> [!note] **Dzień gry** nie rozpoczyna się o północy, lecz o godzinie resetu ustawionej w Kreatorze reguł (domyślnie 5:00, sekcja 7). Dlatego wszystko, co bot zebrał o 02:30 w nocy, jest zapisane jako dzień **wczorajszy**: w grze o tej porze wciąż trwa wczorajszy dzień. Jeśli rano «Tytanit (dziś)» wynosi zero, mimo że grałeś w nocy, dokładnie tak powinno быть.

### Co znajduje się na stronie

Po lewej stronie u góry znajduje się podpowiedź, po prawej wybór **«Okres»**, pod nimi pięć kafelków, wykres, a na dole «Ręczna korekta».

- :calendar: **Okres** — «7 dni», «14 dni», «30 dni» lub «Cały czas». Wybrany świeci się na niebiesko. Przy pierwszym otwarciu ustawione jest «14 dni».
- :gem: **«Tytanit»** — suma za dany okres.
- :calendar: **«Tytanit (dziś)»** — tylko za bieżący dzień gry. Niezależnie od okresu.
- :flask-conical: **«Mikstura tytanów»**, :door-open: **«Pokoje»** i :layers: **«Piętra»** — sumy за dany okres.

Liczby do 100 000 w kafelku są napisane w całości (`98 540`), a długie są skrócone: `105.5K` to sto pięć i pół tysiąca, `1.24M` — milion dwieście czterdzieści tysięcy. Pełna liczba pojawi się po najechaniu myszą na kafelek. «Cały czas» pobiera ogólne liczniki z pliku, a nie sumę słupków, dlatego kafelki zgadzają się z historią, nawet jeśli słupków jest wiele.

> [!tip] Strona odczytuje liczby **przy każdym otwarciu**, a nie w trakcie gry. Bot działa, a liczby się nie zmieniają? Przejdź na inną stronę i wróć.

![Strona «Statystyki»: kafelki, wykres według dni i wybrany słupek z etykietą](images/stats_page.png)

### Wykres: słupki i kliknięcia

Pod nagłówkiem «Aktywność tytanitu» znajduje się podpis informujący, jak są pogrupowane słupki: «dziennie», «tygodniowo» lub «miesięcznie». Słupków jest nie więcej niż piętnaście, aby wykres nie zamienił się w gęsty płot:

- **7 i 14 dni** — jeden dzień na słupek.
- **30 dni** — jeden tydzień (od poniedziałku do niedzieli; skrajne tygodnie są niepełne — zawierają tylko dni wchodzące w dany okres).
- **«Cały czas»** — dziennie, dopóki danych jest mniej niż dwa tygodnie; potem tygodniowo, a gdy tygodni jest więcej niż piętnaście — miesięcznie.

Po lewej stronie znajduje się skala z przerywaną siatką, liczby na skali są krótkie (`3.6K`, `140K`). Podpisy pod słupkami, jeśli się nie mieszczą, są pokazywane co drugi; ostatni (dzisiejszy) jest widoczny zawsze. Dzień bez gry — puste miejsce, brakuje słupka. Za okres bez danych wykres pokaże «Brak danych za ten okres».

1. **Najedź myszą na słupek.** Nad nim pojawi się dokładna liczba tytanitu. To tylko podpowiedź, nic się nie zmienia.
2. **Kliknij słupek.** Stanie się jaśniejszy, pozostałe zbledną, obok pojawi się etykieta z datą i liczbą. Dla tygodnia w etykiecie tytanit jest rozpisany **dziennie**, dla miesiąca — **tygodniowo**. W lewym górnym rogu zaświeci się niebieski napis, na przykład «Pokazany dzień: 19.10.2026 · dziś» (lub „Pokazany tydzień”, „Pokazany miesiąc”).
3. **Spójrz na kafelki.** Pokazują teraz liczby dla tego słupka: tytanit, miksturę, pokoje i piętra za dany dzień, tydzień lub miesiąc. «Tytanit (dziś)» pozostaje bieżący.
4. **Wróć do podsumowania.** Kliknij ten sam słupek ponownie lub niebieski napis z krzyżykiem (✕). Jeśli zmienisz okres — wybór również się zresetuje.

### Tabela

Przycisk **«Tabela»** po prawej stronie nad wykresem pokazuje te same słupki w formie listy: «Data», «Tytanit», «Pokoje», «Piętra», «Mikstura tytanów». Najnowsze daty są na górze, na dole znajduje się wiersz **«Razem»**. Wiersz można również wybrać kliknięciem, a kafelki pokażą jego liczby. Przycisk zamienia się przy tym w **«Wykres»** i przywraca widok graficzny. Tabela jest wygodna, gdy potrzebne są dokładne liczby dla всех dni naraz.

![Tabela: daty, tytanit, pokoje, piętra i mikstura, na dole «Razem»](images/stats_table.png)

### Ręczna korekta

Bot liczy według własnej arytmetyki (6 lub 12 tytanitu za pokój), a w grze liczba może być inna: grałeś sam, bot był wyłączony, program uruchomiono nie od samego rana. Aby statystyki zgadzały się z grą, służy karta **«Ręczna korekta»**.

1. **Wybierz dzień.** Na liście znajduje się — „Dzisiaj”, „Wczoraj” i jeszcze pięć poprzednich dni, łącznie siedem. Potrzebujesz starszego dnia? Wybierz okres «7 dni» lub «14 dni» i kliknij jego słupek: ten dzień wstawi się do listy sam (dla słupka tygodniowego i miesięcznego nie wstawi się — tylko dla dziennego).
2. **Wpisz ogólną liczbę z gry.** W polu «Tytanitu dziennie» — to, co w grze jest показане **za cały dzień**, a nie „ile dodać”. Dla wybranego dnia jest już wpisane to, co zapisano obecnie.
3. **Naciśnij «Zastosuj»** (lub Enter w polu).

Przykład. Bot w ciągu dnia zapisał 90 tytanitu, a w grze za ten sam dzień jest 150. Wpisujesz **150** — program dodaje różnicę 60 i sam przelicza resztę: około **+5 pokoi, +1 piętro i +250 mikstury**. To szacunek: przyjmuje się, że pierwsze 10 pokoi tego dnia dało po 6 tytanitu, a pozostałe po 12. Jeśli grałeś inaczej, pokoje i piętra mogą nieznacznie różnić się od rzeczywistych, ale tytanit będzie dokładnie taki, jak u ciebie.

Gdy wszystko się uda, na dole pojawi się powiadomienie «Tytanit za 19.10.2026: 150», a do dziennika na stronie głównej trafi wiersz `[СТАТИСТИКА] Данные за 2026-10-19 синхронизированы! Дельта: +60 тит., +5 комн., +250 зелий.`. Jeśli wpisałeś mniej niż zapisano, liczby się zmniejszą.

Co może pójść nie tak:

- **«Wpisz liczbę całkowitą od 0»** — w polu znajdują się litery, przecinek, minus lub jest puste. Pole stanie się czerwone.
- **«Bot sam zebrał tego dnia 90 — nie można podać mniej»** — nie można wpisać mniej niż to, co bot zebrał **sam**, ponieważ jest to zapisane uczciwie. Zmniejszyć liczbę można tylko do tej wartości.
- **«Ten dzień ma już dokładnie tyle»** — wpisałeś tę samą liczbę, nie ma co zmieniać.

> [!warning] «Zastosuj» zapisuje liczby **od razu** do `bot_data/stats.json`. Przycisk «Zapisz ustawienia» nie występuje tutaj i nie jest potrzebny, inaczej niż w Kreatorze reguł (sekcja 7). Cofnąć edycji przyciskiem nie można, ale nic nie stoi na przeszkodzie, by ponownie wpisać poprzednią liczbę.

> [!note] Korekta zmienia **tylko statystyki**. «Podsumowanie sesji» na stronie głównej oraz cel sesji (sekcja 4) są liczone oddzielnie, na podstawie tego, co bot zebrał podczas tego uruchomienia, i nie zależą od strony «Statystyki».

### «Resetuj»: wykasuj całą historię

Przycisk **«Resetuj»** (z ikoną kosza, po prawej stronie w karcie «Ręczna korekta») zeruje wszystkie statystyki: tytanit, pokoje, piętra i miksturę ze wszystkich dni. Nacisnąłeś przypadkowo? Nic się nie stanie: najpierw program zapyta «Zresetować statystyki?» i przypomni, że nie można tego cofnąć. Przyciskiem «Resetuj» w oknie potwierdzasz, a przyciskiem «Anuluj» — rezygnujesz. Po zresetowaniu pojawi się powiadomienie «Statystyki zresetowane», a w dzienniku wiersz `[СТАТИСТИКА] Вся история полностью сброшена!`.

Kasowane są только statystyki. Reguły, składy, ustawienia, `profile.yml` i logi walk pozostają. Jeśli bot w tym momencie działa, kontynuuje i liczy dalej od zera, a cel sesji nie zostaje zresetowany.

> [!tip] Chcesz zresetować „na próbę”? Najpierw zapisz kopię: zamknij program i skopiuj plik `bot_data/stats.json` w inne miejsce (folder programu otwiera przycisk «Folder bota» na stronie «O programie»). Przywrócić historię można, umieszczając plik z powrotem.

### Często zadawane pytania

- **Liczby nie zgadzają się z grą.** Bot liczy, a nie odczytuje ekranu: 6 lub 12 tytanitu za pokój. Jeśli pobierałeś tytanit z innych źródeł, gra pokaże więcej. Porównaj i popraw poprzez «Ręczna korekta».
- **Dzisiejszy dzień jest pusty, a ja grałem.** Sprawdź godzinę resetu: przed nią bot zapisuje we „wczoraj” (patrz „Dzień gry” powyżej). Zmieniłeś godzinę w Kreatorze reguł? Uruchom ponownie program, aby strona również to uwzględniła.
- **Słupków jest mało, a okres jest duży.** Dni, w których bot nie działał, są na wykresie puste. «Cały czas» i miesiące domyślnie kompresują wykres: aby zobaczyć konkretne dni, wybierz «7 dni» lub «14 dni».
- **W dzienniku widnieje `[СТАТИСТИКА] ВНИМАНИЕ: Файл stats.json поврежден`.** Plik z historią nie został odczytany (na przykład komputer został wyłączony w momencie zapisu). Bot rozpoczyna nową statystykę od zera i nadpisze plik. Skopiuj go wcześniej, jeśli stara historia jest dla ciebie ważna.

> [!done] Teraz wiesz, jak odczytywać liczby, przełączać okresy, porównywać statystyki z grą i je wymazywać. Dalej — co zrobić, jeśli coś pójdzie nie tak. [Następna sekcja →](#14)

## Jeśli coś poszło nie так

Dobra wiadomość: bot potrafi sam wykaraskać się z większości kłopotów. Zawiesił się — rozejrzy się i zacznie od nowa. Stracił internet — poczeka. Zablokowałeś komputer — poczeka i przejdzie dalej. Jesteś potrzebny tylko wtedy, gdy sam o to **poprosił** (wszedł w pauzę, napisał na Telegramie) albo gdy niczego nie klika, a z dziennika nie da się zrozumieć dlaczego. Ten rozdział dotyczy obu przypadków: co bot robi bez ciebie, jak zrozumieć, gdzie leży usterka, i co klikać.

Zasada na każdą okazję: **nie panikuj i nie śpiesz się**. Bota można bez obaw zatrzymać, uruchomić ponownie i włączyć jeszcze raz: statystyki, składy, reguły i ustawienia leżą w plikach i nigdzie nie znikną.

### Jak zrozumieć, że coś jest nie tak

- :triangle-alert: **Czerwona liczba na pigułce «Błędy»** w dzienniku na stronie głównej. Liczy ona nie tylko awarie: trafiają tu także ostrzeżenia (na przykład „okno gry jest przysłonięte”). Sama liczba nie jest powodem do strachu — trzeba otworzyć pigułkę i przeczytać wiersze.
- :pause: **Stan «Pauza» i zielony прициск «Kontynuuj», choć nie klikałeś pauзы.** Oznacza to, że bot zatrzymał się sam i czeka na ciebie. W dzienniku pojawia się wtedy wiersz `[ВНИМАНИЕ] Бот на мягкой паузе: ...` z powodem.
- :send: **Wiadomość na Telegramie** (jeśli jest skonfigurowany, rozdział 12): «Bot chyba się zawiesił», «Nie udało się cofnąć walki», «Ekran komputera jest zablokowany».
- :eye: **Cisza.** Wiersze w dzienniku nie pojawiają się przez minutę lub dłużej, a w grze nic się nie dzieje. To również objaw: zobacz rozdział „Częste przypadки” poniżej.

Etykiety w dzienniku świadczące o problemie:

- `[СТОРОЖ]` — bot uznał, że się zawiesił, i sam zaczął od nowa.
- `[СЕТЬ]` — wygląda na brak połączenia z serwerem gry.
- `[ЭКРАН]` — komputer nie pozwala zrobić zrzutu ekranu (jest zablokowany).
- `[ОТКАТ]` — kroki cofania walki i jej błędy (rozdział 10).
- `[ВНИМАНИЕ]` — bot prosi о uwagę: pauza, zamknięte okno gry.
- `[ОШИБКА]` — coś się zepsuło; obok napisano co.
- `[ADB]` i `[VISION]` — połączenie z telefonem i kliknięcia.

### Co bot robi sam

Tutaj niczego nie klikasz. Po prostu wiedz, że to normalne i nie psuje sesji.

- :gauge: **Zawieszenie: 5 минут bez ani jednego pokoju.** To „stróż” (tak nazywa się sprawdzanie, które pilnuje, czy bot nie utknął). Bot pisze `[СТОРОЖ] Бот 5 мин не прошёл ни одной комнаты ... Тревога 1 из 3.`, zapisuje zrzut ekranu, wysyła wiadomość na Telegramie (jeśli jest skonfigurowany) i wykonuje **„sprytny start”**: ponownie patrzy na ekran i decyduje, od czego kontynuować. Jeśli nie pomogło, po kolejnych 5 minutach znowu następuje alarm. **Trzeci alarm z rzędu** (czyli około 15 minut bez pokoi) — bot przechodzi w miękką pauzę i czeka na ciebie. Czasu, kiedy bot czekał na ciebie (okno SOS, pauza, cudze okno na wierzchu gry), stróż nie wlicza.
- :activity: **Utknął w jednym miejscu.** Ekran wyboru drużyny nie pojawił się w ciągu 30 sekund lub okno wyniku nie pojawiło się w ciągu 3 minut. Wtedy `[СТОРОЖ] Зависание: ...`, zrzut ekranu i taki sam sprytny start, ale już bez alarmu na Telegramie.
- :globe: **Walka się nie rozpoczyna (najprawdopodobniej brak połączenia z serwerem gry).** Przycisk „Auto” wciśnięty, a walki brak. Bot próbuje ещё два раза сразу, potem czeka и próbuje ponownie: po 30 sekundach, 1, 2, 4 i 8 minutach. Wszystko to w dzienniku jako `[СЕТЬ] Бой не начался N раз(а) подряд ... Жду N с и пробую снова.` Jeśli to również nie pomogło (około 15 minut): zrzut ekranu, wiadomość «Bot chyba się zawiesił» i miękka pauza.
- :rotate-ccw: **Utracono połączenie podczas cofania walki.** Bot nie poddaje się, lecz **czeka na grę do 15 minut**: pisze `[ОТКАТ] Бой не загрузился ... Не сдаюсь`, zapisuje zrzut ekranu i raz na minutę informuje `Всё ещё жду игру`. Połączenie wróciło — cofanie dokończy się samo (`Игра снова откликается`). Nie wróciło w ciągu 15 minut — «Nie udało się cofnąć walki», wiadomość na Telegramie i pauza.
- :monitor: **Komputer jest zablokowany (Win+L) lub ekran się wyłączył.** Windows nie pozwala robić zrzutów ekranu i bot nic nie widзи. On **nie wyłącza się**, lecz próbuje ponownie co 2 sekundy: `[ЭКРАН] Не удаётся сделать снимок экрана ... Похоже, ПК заблокирован`. Dłużej niż minutę — jedna wiadomość «Ekran komputera jest zablokowany». Odblokowałeś — `[ЭКРАН] Снимок экрана снова работает`, bot kontynuuje sam.
- :layers: **Okno gry zasłonięte innym oknem.** Bot czeka, aż znowu stanie się główne (`[ВНИМАНИЕ] Окно игры перекрыто ... Бот ждет фокуса`). Kliknij w okно gry, a on posunie się dalej. Dlaczego tak jest — w rozdziale 5.
- :target: **Kliknięcie nie dotarło.** Jeśli po 4 sekundach od kliknięcia ekran się nie zmienił, bot klika jeszcze raz: `[VISION] Клик по '...' не зарегистрирован сервером ... Повторяю...`. Rzadkie takie wiersze to norma: telefon czasami „myśli”.
- :smartphone: **Połączenie z telefonem przez kabel mignęło.** Bot pisze `[ADB] Постоянное соединение с телефоном оборвалось ... Переподключусь при следующем нажатии` i łączy się ponownie.
- :send: **Wiadomość na Telegramie nie wyszła z powodu internetu.** Bot powtórzy ją później (rozdział 12) i pracuje dalej.

> [!note] Ile razy bot zawiesił się podczas sesji, widać w bloku `[ИТОГ]` w dzienniku (wiersz ze słowem „зависания”). Rzadkie przypadki to nie problem. Jeśli jest ich dużo, poszukaj przyczyny w rozdziale „Częste przypadki” poniżej.

### Bot wszedł w pauzę sam: co robić

Zatrzymał się, ponieważ dalej bez ciebie się nie da. Działaj po kolei:

1. **Spójrz na ekran gry.** Okno `HeroWarsBot_Arena` pokazuje, gdzie bot utknął: okno wyniku, walka, menu pauzy, „grzybek” ładowania lub coś niespodziewanego (cudze okno, reklama, zapytanie z gry).
2. **Przeczytaj ostatnie wiersze dziennika.** Otwórz pigułkę «Błędy» i spójrz na dół: tam powiedziano, dlaczego bot się zatrzymał (`[СТОРОЖ]`, `[ОТКАТ] ОШИБКА`, `[СЕТЬ]`).
3. **Przywróć grę do korytarza Lochów.** Zamknij zbędne rzeczy, poczekaj, aż walka się zakończy lub załaduje, i przejdź do ekranu z drzwiami i chorągiewką.
4. **Kliknij «Kontynuuj».** Bot ponownie się rozejrzy (sprytny start) i pójdzie dalej.

> [!note] Pauza po nieudanym cofnięciu bywa też taka: ręczna walka zdążyła się zakończyć, przycisku „Jeszcze raz” na oknie wyniku już nie ma i nie da się jej cofnąć. Okno wyniku zostaje na ekranie — niczego nie trzeba zamykać, po kliknięciu «Kontynuuj» bot sam kliknie „OK”. Spójrz na tym oknie, kto przeżył.

> [!tip] Bot wchodzi w pauzę nie z powodu każdego drobiazgu, lecz gdy próbował i nie wyszło. Dlatego zanim klikniesz «Kontynuuj», ustal, **co dokładnie** poszło nie tak. Jeśli przyczyna pozostała (brak internetu, zamknięta gra), bot znowu zatrzyma się po kilku minutach.

### Częste przypadki: na co patrzeć i co robić

**Bot niczego не klika, а w dzienniku jest cicho.** Najprawdopodobniej nie widzi gry lub nie może w niej niczego znaleźć. Sprawdź po kolei:

1. **Okno gry jest na swoim miejscu.** Nazywa się `HeroWarsBot_Arena`, nie jest zminimalizowane ani zamknięte. Jeśli okna nie ma, bot o tym nie pisze, lecz po cichu sprawdza je co pół sekundy. Dlatego cisza w dzienniku przy znikniętym oknie to zwykła rzecz. Kliknij «Podłącz телефон»: okno otworzy się na nowo.
2. **Rozmiar okna nie zmieniał się.** Bot mierzy okno jeden raz przy uruchomieniu i dalej korzysta z tej miary. Rozciągnąłeś, powiększyłeś lub przesunąłeś okno po starcie — zatrzymaj bota (F10), kliknij «Resetuj rozmiar okna gry» i znowu «Zacznij farmić». Szczegóły — w rozdziale 3.
3. **W grze — korytarz Lochów**, a nie menu, sklep, wydarzenie kogoś innego czy okno z reklamą.
4. **Język programu zgadza się z językiem gry** (dwie litery na dole lewego paska). W przeciwnym razie bot nie rozpozna przycisków.
5. **Nic nie zasłania okna gry.** Dowolne okno na wierzchu gry — i bot czeka na fokus.

**Bot „widzi” i klika, a w grze nic się nie dzieje.** W dzienniku pojawiają się wiersze po wierszu „Клик по ... не зарегистрирован сервером ... Повторяю...”. Oznacza to, że polecenie kliknięcia nie dociera do telefonu. Sprawdź:

- Włączone są **oba** ustawienia debugowania w telefonie: „Debugowanie USB” i „Debugowanie USB (ustawienia bezpieczeństwa)”. Bez drugiego obraz jest, ale kliknięcia nie działają (rozdział 2).
- Telefon jest odblokowany, kabel włożony ściśle. Spróbuj innego gniazda USB.
- W wierszu poleceń `adb devices` pokazuje obok telefonu `device`, a nie `unauthorized` i nie pustą listę.
- Jeśli nie pomogło: zatrzymaj bota, kliknij «Uruchom ponownie scrcpy», a potem «Zacznij farmić».

**Bot klika nie tam, gdzie trzeba, lub myli tytanów.** Najczęściej okno gry nie ma właściwego rozmiaru lub było ruszane po starcie (reset rozmiaru, jak wyżej). Rozmiar jest prawidłowy, a bot i tak się myli — zapisz zrzut ekranu z tego momentu i wyślij autorowi razem z logiem (poniżej).

**Okno programu „nie odpowiada”.** Program sam pilnuje siebie: jeśli okno nie odpowiada przez 5 sekund, zapisuje w pliku, w którym wierszu kodu utknął. Plik znajduje się w `bot_data/debug/` i nazywa się `ui_freeze_<дата>_<время>.txt`. Co robić:

1. **Poczekaj minutę.** Często okno ożywa samo: jest zajęte ciężką pracą.
2. **Bot działa niezależnie od okna.** Trzeba go zatrzymać, a przyciski nie odpowiadają? Naciśnij Ctrl+Shift+Q: tego skrótu słucha sam bot, a nie okno programu (rozdział 6).
3. **Nie ożyło — zamknij okno krzyżykiem.** Nie zamyka się — przez menedżer zadań (Ctrl+Shift+Esc). Potem sprawdź tam samo, czy na liście nie został `HeroWarsBot.exe` lub `python`: jeśli tak, zamknij go również, inaczej bot będzie kontynuować klikanie w grze bez okna.
4. **Wyślij plik `ui_freeze_...txt` autorowi.** Są tam tylko nazwy plików i wierszy kodu programu, nic osobistego.

**Bot zatrzymał się, a ty go nie zatrzymywałeś.** Otwórz kartę «Podsumowanie sesji» na stronie głównej (przycisk «Szczegóły») i spójrz na powód:

- «okno scrcpy zamknięte» — okno gry zostało zamknięte lub zniknęło (wyciągnięto kabel, telefon się zablokował). Podłącz телефон na nowo.
- «bot zakończył pracę» — proces zakończył się bez powodu. Jeśli masz Telegram, podsumowanie przyszło tam; jeśli nie, poszukaj w dzienniku wiersza `[ОШИБКА] Бот остановился из-за ошибки:` i tekstu pod nim.
- «Пак не найден в правилах» — dla pokoju nie ustawiono głównego składu. Otwórz «Kreator reguł» → «Baza i pokoje» i ustaw go we wszystkich czterech pokojach (rozdział 7).
- «Ошибка: ...» — program wykręcił błąd. Wyślij log autorowi (poniżej).

> [!warning] Po wciśnięciu «STOP» (F10) bot nie zdąży napisać bloku `[ИТОГ]` i nie wyśle podsumowania na Telegramie: został zabity w locie (rozdział 6). To nie jest awaria.

**Telefon „zasnął” lub экран zgasł.** Program uruchamia scrcpy z trybem „nie pozwalaj telefonowi zasypiać” (`--stay-awake`). Przycisk «Wyłącz экран телефона» gasi tylko **ekran**: gra toczy się dalej, a bot wszystko widzi. Ale jeśli telefon się zablokował lub odłączył od kabla, w oknie gry będzie ekran blokady lub pustka i bot niczego nie znajdzie. Odblokuj telefon, sprawdź kabel i kliknij «Uruchom ponownie scrcpy».

**Nie przychodzą wiadomości na Telegramie.** Najprawdopodobniej nie wciśnięto „Uruchom” u swojego bota lub jest błędny token/Chat ID — omówienie w rozdziale 12. Bot działa przy tym normalnie.

**Bot wystawia nie tych tytanów lub decyduje inaczej, niż chciałeś.** To nie usterka, lecz reguły: przeanalizuj rozdziały 7–11 (składy, progi, reguły, «Bot decyduje sam»). Decyzję bota zawsze można znaleźć w dzienniku po wierszach `[ТАКТИКА]`.

### Gdzie leżą logi i zrzuty ekranu

Przycisk **«Folder bota»** na stronie «O programie» otwiera folder, z którego uruchomiono program. Znajdują się w nim pliki, które bot tworzy sam. Potrzebne вещи są wewnątrz folderu `bot_data`:

- :file-text: `bot_data/logs/bot_log_<дата>_<время>.txt` — **pełny log każdego uruchomienia bota.** Bot pisze go sam, wiersz po wierszu, dlatego zostaje on nawet po awarii i zamknięciu programu. To główny plik do analizy.
- :gauge: `bot_data/logs/timings_<дата>_<время>.csv` — ile zajął każdy pokój (korytarz, kompletowanie, walka, wynik).
- :swords: `bot_data/logs/battle_log_<дата>_<время>.jsonl` i `battle_log.csv` — historia walk: pokój, wrogowie, skład, wynik, HP i energia tytanów.
- :image: `bot_data/debug/` — **zrzuty ekranu do analizy.** Nazwa mówi, co się stało: `stuck_...` — zawiesił się, `sos_...` — okno SOS, `rollback_wait_...` — czekał na grę podczas cofania, `rollback_fail_...` — cofanie nie powiodło się, `start_fail_...` — walka się nie rozpoczęła, `result_unreadable_...` — nie odczytano okna wyniku. Dalej numer pokoju, żywioł i czas (`stuck_комната12_water_2026-10-19_14-03-21.png`). Tam znajduje się również `ui_freeze_...txt`, jeśli okno programu zawieszało się.

> [!warning] Bot sam usuwa stare pliki: przy uruchomieniu w `bot_data/logs/` zostaje 20 najnowszych plików każdego rodzaju (`.txt`, `.jsonl`, `timings_*.csv`), a w `bot_data/debug/` — 50 najnowszych zrzutów ekranu. Jeśli chcesz zachować logi po problematycznej nocy, **skopiuj je w inne miejsce przed następnym uruchomieniem bota**. W ten sam sposób kasuje się log zachowany przyciskiem «Zapisz log» do folderu domyślnego: zapisuj go w inne miejsce, na przykład na pulpit.

> [!warning] Nie usuwaj ani nie zmieniaj nazwy `profile.yml` (twoje ustawienia i Telegram) oraz folderu `bot_data`: znajdują się w nim statystyki, reguły zapamiętane przez bota i historia walk. Usunąć można tylko `bot_data/debug` oraz stare logi, i to tylko wtedy, gdy nie są potrzebne.

### Jak wysłać log autorowi

Gdy problemu nie udało się rozwiązać, najszybszą drogą jest przesłanie autorowi informacji o tym, co się stało.

1. **Zapamiętaj, kiedy to było.** Czas i przybliżona liczba pokoi (`[СТАТИСТИКА] Комнат: N`) pomagają znaleźć właściwe miejsce w długim logu.
2. **Znajdź pliki.** Log — `bot_data/logs/bot_log_...` z danej nocy, zrzuty ekranu — z `bot_data/debug/` z podobnym czasem w nazwie, a w przypadku zawieszenia okna także `ui_freeze_...txt`.
3. **Kliknij «Wyślij log autorowi»** pod dziennikiem na stronie głównej. Program zaproponuje zapisanie tego, co znajduje się obecnie w dzienniku (jest to plik `gui_log_...txt`), a następnie otworzy twój program pocztowy z gotową wiadomością na adres autora.
4. **Załącz pliki do wiadomości sam.** Program nie potrafi dołączać plików do wiadomości: tylko ją otwiera. Dołącz `gui_log_...txt` lub `bot_log_...txt`, zrzuty ekranu oraz (jeśli wystąpił) `ui_freeze_...txt`.
5. **Opisz słowami:** co robiłeś, czego oczekiwałeś, co zobaczyłeś i kiedy to było. Jedno zdanie „nie działa” prawie wcale nie pomaga autorowi.

> [!warning] **Nigdy nie dołączaj** `profile.yml` i `bot_data/profile.yml.bak`: zawierają one token twojego bota Telegram. Zrzut ekranu okna «Ustawienia Telegrama» również przesyłaj tylko z ukrytym tokenem (kropkami).

> [!note] Poczta się nie otworzyła (program pocztowy nie jest skonfigurowany)? Na stronie «O programie» znajduje się przycisk «Napisz do autora»: jeśli wiadomości nie udało się otworzyć, kopiuje on adres do schowka, dzięki czemu możesz napisać z dowolnej poczty.

### Jeśli nic nie pomaga

Idź od rzeczy najprostszych do bardziej skomplikowanych, sprawdzając po każdym kroku, czy bot ożył:

1. **«Pauza» → przywróć grę do korytarza → «Kontynuuj».**
2. **«STOP» (F10) → «Zacznij farmić».** Bot zacznie od sprytnego startu i sam zorientuje się, gdzie jest.
3. **Zatrzymaj bota i kliknij «Uruchom ponownie scrcpy».** Potem znowu «Zacznij farmić».
4. **Zamknij program i otwórz go ponownie.** Jeśli telefon „zawisł”, wyciągnij i włóż kabel.
5. **Uruchom ponownie komputer i telefon.** Brzmi jak żart, ale rozwiązuje połowę dziwnych problemów.

Cele sesji (czas, pokoje, piętra, tytanit) po ponownym uruchomieniu są liczone od nowa, a statystyki, składy i reguły pozostają: znajdują się w plikach.

> [!done] Teraz wiesz, jak bot ratuje się sam, co robić, gdy zatrzymał się, oraz jak zebrać i wysłać log. Został ostatni rozdział: o programie i jak wesprzeć projekt. [Następny rozdział →](#15)

## O programie i wsparcie

Ostatnia strona w lewym menu to «O programie». Dotyczy ona samego programu: jaką masz wersję, czy wszystko jest na miejscu, gdzie napisać do autora i jak powiedzieć „dziękuję”. Nic nie musisz na niej konfigurować, za to znajdują się tu dwa przydatne przyciski: «Sprawdź aktualizacje» oraz «Folder bota».

### Co znajduje się na stronie

- :shield-check: **Karta programu** na górze. Nazwa «Hero Wars: Knowledge Engine Bot», obok — **numer wersji** (na przykład `v1.6.1`) i etykieta `Beta`. „Beta” oznacza „testowane w boju”: program działa, ale autor wciąż go dopracowuje i błędy są możliwe. Pod nazwą — krótki opis. Po prawej cztery przyciski, o nich poniżej.
- :user: **«Autor i licencja»**: imię i nazwisko autora, jego e-mail oraz licencja. Kliknij adres e-mail — otworzy się wiadomość.
- :monitor: **«Stan komponentów»**: sprawdzanie, czy na komputerze znajduje się wszystko, co potrzebne do pracy. Szczegóły — poniżej.
- :heart: **«Wesprzyj projekt»**: sposoby podziękowania autorowi. To nie jest obowiązkowe.

> [!tip] Podawaj wersję autorowi, gdy piszesz o problemie: od razu pokazuje ona, z jakiego dokładnie programu korzystasz. Wersja znajduje się w karcie na górze, obok nazwy.

### Cztery przyciski na kartce

1. **«Sprawdź aktualizacje».** Otwiera w przeglądarce stronę wydań projektu na GitHubie (GitHub to strona, na której autor przechowuje program; „wydanie” to gotowa wersja do pobrania). Porównaj tam najnowszy numer ze swoim. Nowszy — możesz aktualizować, taki sam — masz najnowszą wersję.
2. **«Folder bota».** Otwiera w Eksploratorze Windows folder, z którego uruchomiono program: ten sam, w którym leżą twoje ustawienia i dane. Przydaje się, gdy trzeba skopiować pliki lub znaleźć log.
3. **«Napisz do autora».** Otwiera wiadomość na adres autora w twoim programie pocztowym. Jeśli na komputerze nie ma programu pocztowego, wiadomość się nie otworzy. Wtedy program sam umieści adres w schowku (pamięci podręcznej, skąd wkleja się przez Ctrl+V) i poinformuje o tym na dole okna: «Nie udało się otworzyć — skopiowano do schowka». Wklej adres do wiadomości z dowolnej poczty.
4. **«GitHub projektu».** Otwiera główną stronę projektu na GitHubie: tam znajduje się kod źródłowy i opis.

> [!note] Program **sam nie łączy się z internetem po aktualizacje**: «Sprawdź aktualizacje» tylko otwiera stronę, a decyzję podejmujesz ty. Tak to zaprojektowano, aby nic nie zmieniało się bez twojej wiedzy.

### Jak zaktualizować program

Aktualizacja nie „instaluje się na wierzch” — pobierasz nową wersję i przenosisz do niej swoje dane. Dzięki temu twoje składy i statystyki nie znikną.

1. **Zatrzymaj bota i zamknij program.** Krzyżyk okna, jeśli bot działa, zapyta, czy go zatrzymać.
2. **Pobierz nową wersję** na stronie wydań (przycisk «Sprawdź aktualizacje») i rozpakuj do nowego folderu, a nie na stary.
3. **Przenieś swoje dane.** Ze starego folderu do nowego skopiuj plik `profile.yml` oraz cały folder `bot_data`. Nowy program bez nich zaczyna „od zera”: puste ustawienia i puste statystyki.
4. **Uruchom nowy program** i zajrzyj do «O programie»: numer wersji powinien być nowy, a wszystkie trzy komponenty — w porządku.
5. **Starego folderu na razie nie usuwaj.** Popracuj parę dni na nowej wersji. Jeśli wszystko jest dobrze — wtedy go usuń.

> [!warning] Nie kopiuj plików z `bot_data` po jednym „co potrzebne”, lecz przenieś cały folder: reguły zapamiętane przez bota, historia walk i statystyki są ze sobą powiązane, a zebranie ich na nowo nie jest możliwe.

### «Stan komponentów»

Program sam sprawdza, czy obecne jest wszystko, bez czego bot nie działa. Sprawdzanie odbyва się w tle przy każdym wejściu na stronę. Dopóki trwa, widać «sprawdzam…».

- :smartphone: **ADB** — usługa, przez którą komputer klika na telefonie. Powinno być «znaleziono».
- :monitor: **scrcpy** — program, który pokazuje ekran telefonu w oknie na komputerze. Powinno być «znaleziono».
- :image: **Baza szablonów** — „obrazki-wzorce” przycisków i tytanów, po których bot rozpoznaje, co ma na ekranie. Powinno być «załadowana».

Co robić, jeśli coś jest na czerwono:

- **ADB lub scrcpy «nie znaleziono».** Oznacza to, że folder z nimi nie został dodany do `PATH` (listy miejsc, w których Windows szuka programów). Jak to zrobić — w rozdziale [«Co będzie potrzebne i instalacja»](#2). Po edycji `PATH` zamknij program i otwórz go ponownie: już uruchomiony program nowego `PATH` nie widzi.
- **Baza szablonów «nie znaleziona».** Z folderu programu zniknęły pliki. Najczęściej archiwum nie zostało rozpakowane do końca lub antywirus coś usunął. Rozpakuj archiwum ponownie do nowego folderu i przenieś `profile.yml` oraz `bot_data`, tak jak przy aktualizacji.

### Co znajduje się w folderze bota i czego nie wolno usuwać

Otwórz go przyciskiem «Folder bota». Plików jest tam sporo, ale ty potrzebujesz tylko kilku. Reszta to pliki systemowe, potrzebne programowi do pracy.

- :file-text: `HeroWarsBot.exe` — sam program. Bot działa również z niego, nie ma osobnego pliku. Wszystkie pozostałe pliki i foldery obok niego (`guide`, `ui`, biblioteki, pliki z rozszerzeniem `.dll` i inne) są częścią programu. **Niczego z nich nie usuwaj ani nie zmieniaj nazw**, inaczej przestanie się uruchamiać.
- :file-text: `profile.yml` — twoje ustawienia: cel sesji, progi, Telegram. **Zawiera token twojego bota Telegram, więc nikomu go nie wysyłaj.** Pojawia się po pierwszym kliknięciu «Zapisz ustawienia».
- :folder: `bot_data` — wszystko, co program i bot zapisały same. To **najcenniejsze**, co masz. Wewnątrz:
  - `stats.json` — statystyki (strona «Statystyki»);
  - folder `rules` — twoje składy i reguły, w tym te zapamiętane przez bota;
  - folder `logs` — historia walk i log bota (`bot_log_...txt`);
  - folder `debug` — zrzuty ekranu do analizy (okna SOS, zawieszenia, nieudane cofania);
  - `titan_state.json` — zdrowie i energia tytanów na dany dzień gry;
  - `profile.yml.bak` — kopia zapasowa ustawień. Na jej podstawie działa «Przywróć / Resetuj» w «Kreatorze reguł». **Ona również zawiera token Telegrama**;
  - `ui_settings.json` — wybrany język okna;
  - `sos_info.json`, `temp_sos.png`, `temp_test.png` — drobne pliki robocze do wiadomości na Telegramie.
- :pause: `pause.flag` — „flaga pauzy”. Pojawia się, gdy bot jest w stanie miękkiej pauzy. Jeśli została z poprzedniego razu, program sam ją usunie przy uruchomieniu.

> [!warning] **Nie usuwaj ani nie zmieniaj nazw** `profile.yml` oraz `bot_data`. Jeśli usuniesz `bot_data` — znikną statystyki, składy, reguły i wszystko, czego bot się nauczył. Jeśli naprawdę musisz zwolnić miejsce, możesz wyczyścić zawartość `bot_data/debug` oraz stare logi w `bot_data/logs`. Ale bot sam zostawia tylko 20 ostatnich logów i 50 ostatnich zrzutów ekranu, więc miejsce zazwyczaj nie stanowi problemu.

> [!tip] **Rób kopię raz w tygodniu.** Skopiuj `profile.yml` i folder `bot_data` na pendrive'a lub do chmury. Jeśli komputer się zepsuje lub przeinstalujesz Windowsa, program pobierzesz na nowo, a składy i statystyки przywrócisz z kopii. Token Telegrama w kopii istnieje — przechowuj ją u siebie, a nie w folderze udostępnionym.

### Autor i licencja

Program napisał i utrzymuje **Platon Petrunin**. Pytania, błędy i pomysły — przycisk «Napisz do автора» lub adres na karcie «Autor i licencja».

Licencja nazywa się **PolyForm Noncommercial 1.0.0**. Mówiąc prosto:

- :check: korzystać dla siebie, do swojej gry można za darmo — ile tylko chcesz;
- :check: analizować kod i zmieniać go dla siebie również można;
- :x: **nie wolno zarabiać**: sprzedawać programu ani jego pliku `.exe`, podawać się za autora pod inną nazwą, wbudowywać w płatne usługi. Do tego wymagana jest pisemna zgoda autora.

> [!note] To jest krótkie streszczenie, a nie tekst prawny. Jeśli twój przypadek jest nietypowy (na przykład chcesz rozdać program znajomym lub społeczności), najpierw napisz do autora. Pełny tekst licencji znajduje się w pliku `LICENSE` w projekcie na GitHubie.

### Jak wesprzeć projekt

Program jest darmowy, a autor tworzy go w wolnym czasie. Jeśli oszczędza ci czas i nerwy, możesz powiedzieć „dziękuję” finansowo. Jest to **dobrowolne**: bot działa tak samo, niezależnie od tego, czy zapłaciłeś, czy nie, i nie ma żadnych „płatnych funkcji”.

Na dole strony «O programie» znajdują się trzy bloki:

1. **«Kryptowaluta».** Trzy portfele: `USDT · TRC20`, `Bitcoin · BTC` oraz `Ethereum · ETH`. Pełny adres jest widoczny w polu. Skopiować go można przyciskiem «Kopiuj» po prawej stronie (na dole pojawi się «Adres skopiowany»), podwójnym kliknięciem w pole (zaznaczy się całość) lub prawym przyciskiem myszy — «Kopiuj».
2. **«Wpłata przez Telegram».** Trzy wiersze — ruble (`RUB`), euro (`EUR`) i dolary (`USD`). W każdym są dwa przyciski: **«Aplikacja»** otwiera płatność w aplikacji Telegram, **«Przeglądarka»** — w przeglądarce, jeśli Telegram nie jest zainstalowany. Wybierz walutę, w której wygodniej.
3. **«Przelewy bezpośrednie».** Przyciski «Wesprzyj na Boosty» oraz «YooMoney (RUB)»: otwierają strony tych serwisów, dalej jak przy zwykłej płatności.

> [!warning] **Ostrożnie z kryptowalutami.** Przelewaj tylko w tej sieci, która jest napisana obok portfela: dla `USDT` jest to `TRC20`, a nie inna. Pieniądze wysłane do złej sieci **nie są do odzyskania**. Adres bierz tylko z programu, przyciskiem «Kopiuj»: na stronach internetowych i w cudzych wiadomościach mogą go podmienić. Za pierwszym razem wyślij niewielką kwotę.

### Często zadawane pytania

- **Mam starą wersję — czy to straszne?** Nie. Program nie przestaje działać z powodu wyjścia nowej wersji. Jednak w nowych wersjach zazwyczaj naprawiane są błędy, więc raz na kilka tygodni zaglądaj na stronę wydań.
- **«Folder bota» się nie otworzył.** Pojawi się napis «Nie udało się otworzyć folderu». Otwórz go sam: Eksplorator plików, folder, do którego rozpakowałeś program.
- **Dlaczego nie ma przycisku «Aktualizuj»?** Program sam niczego nie pobiera, aby nie popsuć twoich ustawień bez pytania. Aktualizację wykonujesz sam, krok po kroku jak wyżej.
- **Jeśli nie wesprę, czy coś się zmieni?** Nic. Bot działa dla wszystkich tak samo.

> [!done] To jest ostatni rozdział. Teraz wiesz już wszystko, aby uruchomić bota, skonfigurować go pod siebie, zrozumieć jego decyzje i skorygować, jeśli coś poszło nie tak. Udanej gry! Jeśli masz jeszcze pytania, przycisk «Napisz do autora» znajduje się poniżej.
