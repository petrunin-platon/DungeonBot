# Hero Wars: Knowledge Engine Bot

Hallo! Das ist ein Programm, das für dich automatisch den Titanen-Dungeon im Spiel Hero Wars durchspielt. Du schaltest es ein, kümmerst dich um deine Dinge — und es öffnet Türen, stellt Teams zusammen und holt Belohnungen ab.

Dieses Handbuch ist so geschrieben, dass sich jeder zurechtfinden kann. Unbekannte Wörter erklären wir sofort und am Ende jedes Abschnitts geben wir einen Hinweis, wie es weitergeht.

## Was der Bot kann

Der Bot ist kein geistloser „Clicker“. Er sieht sich den Spielbildschirm genauso an wie du und entscheidet selbst, was als Nächstes zu tun ist. Das kann er:

- :eye: **Sieht den Bildschirm.** Macht alle Bruchteile einer Sekunde einen Screenshot des Spielfensters und erkennt darauf Schaltflächen, Türen und Gegner.
- :door-open: **Wählt die Tür.** Betritt Räume in der von dir festgelegten Reihenfolge und umgeht jene, wo es gerade gefährlich ist.
- :users: **Stellt das Team auf.** Für jeden Raum hat er ein „Pack“ (so nennen wir ein Team aus fünf Titanen). Der Bot platziert die Titanen selbst an ihren Stellen.
- :heart-pulse: **Überwacht die Gesundheit.** Liest nach jedem Kampf die LP (Lebenspunkte) und Energie der Titanen ab und entscheidet, ob das Pack bereit für den nächsten Kampf ist.
- :swords: **Ruft dich, wenn der Kampf schlecht gelaufen ist.** Es erscheint das Fenster «Eingriff erforderlich»: Du kannst den Kampf mit einem anderen Pack wiederholen, ihn akzeptieren oder manuell spielen. Wenn du nicht am Computer bist, kann der Bot selbst entscheiden.
- :chart-no-axes-column: **Lernt aus seinen Kämpfen.** Merkt sich, welches Pack welche Gegner besiegt hat, und setzt es beim nächsten Mal direkt ein.
- :send: **Schreibt auf Telegram.** Wenn du möchtest, sendet er eine Sitzungsbilanz und einen Alarm, wenn etwas schiefgelaufen ist.

> [!note] Beispiel: «Araji» ging mit 36% Lebenspunkten in den Kampf und fiel danach auf 8%. Der Bot sieht das, erkennt, dass der Kampf schlecht gelaufen ist, und fragt dich entweder oder macht den Kampf selbst rückgängig und wiederholt ihn mit einem anderen Pack.

### Was der Bot не tut

- Er spielt **nur den Titanen-Dungeon** durch. Andere Spielmodi kennt er nicht.
- Er **spielt nicht „in der Cloud“**. Das Spiel läuft auf deinem Android-Handy, und der Windows-PC sieht auf den Handybildschirm und klickt über ein USB-Kabel darauf. Es werden sowohl das Handy als auch der Computer benötigt.
- Er ist kein Zauberer: Wenn keine Verbindung zum Spiel besteht, wartet er ehrlich, bis sie wieder da ist, und schreibt dir darüber.

### Ist das sicher für den Account?

Der Bot versucht sich wie ein menschlicher Spieler zu verhalten, nicht wie ein Roboter:

- jeder Klick trifft einen **zufälligen Punkt** der Schaltfläche und nicht immer dieselbe Stelle;
- vor dem Klick hält er eine **Reaktionspause** ein — von 0,3 bis 0,8 Sekunden, nachdem die Schaltfläche erschienen ist;
- er klickt **nicht öfter als zweimal pro Sekunde**.

> [!warning] Kein Programm kann eine vollständige Garantie geben: Die Spielregeln werden vom Publisher festgelegt. Der Bot tut nichts „unmenschlich Schnelles“, aber die Entscheidung, ob du ihn nutzt, liegt bei dir.

### Wie es im Handbuch weitergeht

- **Was du brauchst und Installation** — was du einmalig besorgen und einrichten musst.
- **Handy verbinden** — das erste Starten des Farmens.
- **Hauptseite und Mini-Leiste** — wie man das Fenster und die kleine Leiste unter dem Spiel liest.
- **Pause und Stopp** — Schaltflächen und Tastenkombinationen.
- **Regelmeister** — wie du dem Bot deine Packs und die Reihenfolge der Türen beibringst.
- **Wenn ein Kampf schlecht lief** — Eingriffsfenster und wie der Bot selbst entscheidet.
- **Telegram, Statistik, если что-то пошло не так** — alles Weitere.

> [!done] Jetzt weißt du, was der Bot kann. Als Nächstes — was du einmalig einrichten musst. [Nächster Abschnitt →](#2)

## Was du brauchst und Installation

Das wird **einmalig** erledigt. Danach startest du das Programm einfach per Doppelklick. Nimm dir etwa fünfzehn Minuten dafür Zeit — danach wird es ganz einfach.

### Was du benötigst

- :monitor: **Einen Windows-Computer.** Darauf laufen das Programm und der Bot.
- :smartphone: **Ein Android-Handy mit Hero Wars.** Das Spiel läuft auf dem Handy, und der Computer sieht auf dessen Bildschirm und klickt darauf.
- :terminal: **Ein USB-Kabel.** Am besten das, mit dem das Handy geladen wird und Dateien überträgt: Es gibt „Nur-Lade-Kabel“, über die der Computer das Handy nicht erkennt.
- :folder: **Das Programmarchiv** (Datei `.zip`, darin liegt `HeroWarsBot.exe`).

> [!note] Das Spiel bleibt auf dem Handy. Der Bot installiert dort nichts Zusätzliches und greift nicht auf Spieldateien zu: Er sieht nur auf den Bildschirm und klickt darauf, wie du es mit dem Finger tun würdest.

### Schritt A. Entpacke das Programm

1. **Entpacke das Archiv** — klicke mit der rechten Maustaste darauf und wähle „Alle extrahieren…“. Wähle einen einfachen Ordner ohne Sonderzeichen, z. B. `C:\HeroWarsBot`.
2. **Prüfe, ob die Dateien vorhanden sind** — im Ordner muss `HeroWarsBot.exe` neben den anderen Dateien und Ordnern liegen.

> [!warning] Entpacke zuerst das Archiv und starte erst dann das Programm. Wenn du die `.exe` direkt aus dem Archiv öffnest, sind die restlichen Programmdateien nicht verfügbar und es funktioniert nicht ordnungsgemäß.

> [!tip] Dieser Ordner ist das „Zuhause“ des Bots. Neben `HeroWarsBot.exe` legt er selbst seine Dateien an: Einstellungen, Statistiken, Kampfverlauf. Verschiebe die `.exe` daher nicht getrennt von den restlichen Dateien; wenn du umziehst, verschiebe den gesamten Ordner.

### Schritt B. Installiere scrcpy

scrcpy ist ein kleines Programm, das den Handybildschirm in einem Fenster auf dem Computer anzeigt. Der Bot „sieht“ genau auf dieses Fenster. Zusammen damit wird auch **adb** installiert — ein Helfer, über den der Bot auf den Handybildschirm klickt.

1. **Lade scrcpy herunter** — wähle auf der [Projektseite](https://github.com/Genymobile/scrcpy/releases) die neueste Version für Windows (`.zip`-Archiv mit „win64“ im Namen).
2. **Entpacke das Archiv** — am besten in einen einfachen Ordner ohne Leerzeichen und Sonderzeichen, z. B. `C:\scrcpy`. Darin müssen die Dateien `scrcpy.exe` und `adb.exe` liegen.
3. **Füge den Ordner zu PATH hinzu** — so weiß Windows, wo diese Programme zu finden sind. Wie das geht, siehst du unten.

**So fügst du den Ordner zu PATH hinzu:**

1. **Öffne die Einstellungen** — drücke die Windows-Taste, gib „Umgebungsvariablen“ ein und wähle „Systemumgebungsvariablen bearbeiten“.
2. **Finde „Path“** — klicke im geöffneten Fenster auf „Umgebungsvariablen“, wähle in der oberen Liste die Zeile `Path` und klicke auf „Bearbeiten“.
3. **Füge den Ordner hinzu** — klicke auf „Neu“, gib `C:\scrcpy` ein (deinen Ordner, falls er anders heißt) und schließe alle Fenster mit „OK“.

> [!note] PATH ist eine Liste von Ordnern, in denen Windows nach Programmen sucht, wenn du sie beim Namen rufst. Wenn du den Ordner zur Liste hinzugefügt hast, werden `scrcpy` und `adb` von überall gefunden.

### Schritt C. Überprüfe, ob scrcpy installiert ist

1. **Öffne die „Eingabeaufforderung“** — Windows-Taste, gib `cmd` ein, drücke Enter. Wenn das Fenster vor der Installation bereits geöffnet war, schließe es und öffne es erneut: Das alte Fenster weiß nichts von neuen Ordnern.
2. **Überprüfe scrcpy** — gib `scrcpy --version` ein und drücke Enter. Es sollte die Programmversion erscheinen.

Wenn Windows statt der Version „ist entweder falsch geschrieben oder konnte nicht gefunden werden“ anzeigt, bedeutet das, dass der Ordner nicht in PATH aufgenommen wurde. Kehre zu Schritt B zurück und stelle sicher, dass der Ordner mit der `scrcpy.exe` in PATH eingetragen ist.

### Schritt D. Richte das Handy ein

Das Handy muss dem Computer erlauben, es zu steuern. Das nennt sich „USB-Debugging“ (ein Modus, der für App-Entwickler gedacht ist). Der Bot nutzt ihn, um auf den Bildschirm zu klicken.

1. **Aktiviere den Entwicklermodus** — gehe zu „Einstellungen“ → „Über das Telefon“ und tippe **7-mal hintereinander** auf „Build-Nummer“. Das Handy meldet, dass du jetzt Entwickler bist.
2. **Finde „Entwickleroptionen“** — dieser Punkt erscheint in den Einstellungen (manchmal unter «System» oder „Zusätzliche Einstellungen“).
3. **Aktiviere zwei Einstellungen** — „USB-Debugging“ **und** „USB-Debugging (Sicherheitseinstellungen)“.
4. **Schließe das Kabel an** — wenn das Handy fragt „USB-Debugging von diesem Computer zulassen?“, markiere „Immer zulassen“ und tippe auf „OK“.

![Bereich „Entwickleroptionen“ mit zwei aktivierten Debugging-Einstellungen](images/usb_debug.png)

> [!warning] Aktiviere **beide** Einstellungen. Wenn nur die erste aktiviert ist, wird das Bild vom Handy auf den Computer übertragen, aber Klicks gelangen nicht ins Spiel: Der Bot wird „tippen“, aber das Spiel bemerkt nichts.

Jetzt prüfen wir die Verbindung. Schließe das Handy per Kabel an, öffne die „Eingabeaufforderung“ und gib `adb devices` ein. In der Liste muss eine Zeile mit dem Wort `device` neben der Telefonnummer stehen.

- :check: `device` — alles bestens, das Handy ist bereit.
- :triangle-alert: `unauthorized` — das Handy wartet auf deine Erlaubnis. Sieh auf seinen Bildschirm und tippe auf „Zulassen“.
- :triangle-alert: Liste ist leer — der Computer sieht das Handy nicht. Versuche ein anderes Kabel oder einen anderen USB-Anschluss.

### Schritt E. Erster Start des Programms

1. **Öffne den Programmordner** — den Ordner, in den du das Archiv entpackt hast.
2. **Mache einen Doppelklick auf `HeroWarsBot.exe`** — das Programmfenster öffnet sich.
3. **Sieh dich um** — links ist die Leiste mit den Abschnitten, in der Mitte die Hauptseite. Solange das Handy nicht verbunden ist, steht in der Kopfzeile «Warte auf Telefon» — das ist normal.

> [!tip] Starte das Programm immer aus seinem Ordner heraus (oder erstelle eine Verknüpfung zu `HeroWarsBot.exe`: rechte Maustaste → „Senden an“ → „Desktop“). Dann findet es seine Einstellungen und Dateien.

> [!done] Alles bereit: Das Programm ist entpackt, scrcpy und das Handy sind eingerichtet. Jetzt verbinden wir das Handy und starten das erste Farmen. [Nächster Abschnitt →](#3)

## Handy verbinden und erstes Farmen

Jetzt verbinden wir das Handy und starten den Bot zum ersten Mal — das dauert etwa fünf Minuten. Merke dir zuerst: Auf dem Monitor wird es **zwei Fenster** geben.

- :monitor: **Das Programmfenster** — das Fenster, in dem du dieses Handbuch liest. Darin befinden sich Schaltflächen, Einstellungen und das Protokoll (so heißt der Nachrichten-Feed, in den der Bot schreibt, was er tut).
- :smartphone: **Das Spielfenster** — das „Spiegelbild“ des Handybildschirms auf dem Monitor, es heißt `HeroWarsBot_Arena`. Der Bot „sieht“ genau in dieses Fenster.

### Was beim ersten Start auf der Hauptseite zu sehen ist

Solange du noch nie Einstellungen gespeichert hast, befindet sich auf der Hauptseite (erste Schaltfläche in der linken Leiste) die Karte «Erste Schritte» mit der Aufschrift «3 Schritte · etwa 5 Minuten».

![Erster Start: Karte «Erste Schritte», rote Aufschrift «Warte auf Telefon…» und blaue Schaltfläche «Handy verbinden»](images/connect_phone.png)

- :smartphone: **«Handy verbinden»** — mit dem Wort «jetzt» markiert. Wenn das Handy verbunden ist, wird die Schrittnummer durch ein grünes Häkchen ersetzt. Damit beschäftigen wir uns jetzt.
- :sliders-vertical: **«Packs pro Raum prüfen»** — der Link «Öffnen →» führt zum «Regelmeister» (zweite Schaltfläche in der linken Leiste, Regler-Symbol). Dort sagst du dem Bot, mit welchen Titanen er jeden Raum betreten soll.
- :send: **«Telegram für SOS einrichten»** — optional. Der Bot schreibt dir auf Telegram, wenn er Hilfe braucht.

> [!warning] Die Packs sind das Wichtigste vor dem ersten Farmen. Der Bot setzt in jeden der vier Räume (Wasser, Erde, Feuer und gemischt) das Pack ein, das im «Regelmeister» eingetragen ist, und kann deine Titanen nicht erraten. Wie das eingerichtet wird — im Abschnitt über den «Regelmeister» weiter hinten im Handbuch. Die Karte «Erste Schritte» verschwindet, wenn du die Einstellungen zum ersten Mal im «Regelmeister» speicherst.

### Schritt A. Verbinde das Handy

1. **Bereite das Handy vor** — schließe es per Kabel an und entsperre den Bildschirm. Beide USB-Debugging-Einstellungen müssen aktiviert sein, wie in [Abschnitt 2](#2).
2. **Klicke auf «Handy verbinden»** — das ist die große blaue Schaltfläche oben rechts. Während das Programm nach dem Handy sucht, steht darauf «Verbinde…». Das Warten kann bis zu 20 Sekunden dauern.
3. **Finde das Spielfenster** — es erscheint ein neues Fenster `HeroWarsBot_Arena` mit dem Handybildschirm. Nicht zu sehen? Es könnte sich hinter dem Programmfenster versteckt haben: Suche danach in der Taskleiste unten auf dem Bildschirm.
4. **Prüfe die Plakette in der Kopfzeile** — die rote «Warte auf Telefon…» sollte grün werden: «verbunden». Und die blaue Schaltfläche verwandelt sich in das grüne «Farmen starten». (Kopfzeile — die obere Leiste des Fensters, Plakette — das Rechteck mit der Aufschrift.)

![Handy verbunden: grüne Aufschrift «verbunden», Schaltfläche «Farmen starten» und daneben das Spielfenster](images/phone_connected.png)

Das Fenster ist nicht erschienen und im Protokoll steht „scrcpy-Fenster nicht erschienen oder Dienstprogramm nicht gefunden!“? Überprüfe der Reihe nach:

- :smartphone: Der Handybildschirm ist entsperrt, das Kabel steckt fest. Versuche einen anderen USB-Anschluss.
- :terminal: In der Eingabeaufforderung zeigt `adb devices` das Wort `device` neben deinem Handy an. Wenn dort `unauthorized` steht — erlaube das Debugging auf dem Handybildschirm.
- :terminal: In der Eingabeaufforderung antwortet `scrcpy --version` mit der Version. Antwortet sie nicht? Der Ordner mit scrcpy ist nicht in PATH gelandet — kehre zu [Abschnitt 2](#2) zurück. Nach dem Bearbeiten von PATH muss das Programm geschlossen und erneut geöffnet werden.

### Schritt B. Begib dich in den Dungeon-Korridor

Der Titanen-Dungeon ist ein Spielmodus, bei dem du Etagen hinabsteigst und in jedem Raum gegen Gegner kämpfst. Der **Korridor** ist der Bildschirm zwischen den Kämpfen: Darauf ist eine Tür mit einer Flagge zu sehen, und sonst ist nichts geöffnet. Vom Korridor aus startet der Bot.

1. **Öffne das Spiel** — starte Hero Wars auf dem Handy und gehe in den Titanen-Dungeon.
2. **Stelle dich in den Korridor** — если идёт бой, доиграй его сам и закрой окно результата. Нужен спокойный экран с дверью и флажком.

![Dungeon-Korridor der Titanen: an der Tür ist eine Flagge zu sehen](images/dungeon_corridor.png)

> [!warning] Starte das Farmen nicht mitten im Kampf. Zuerst scannt der Bot den Bildschirm und schafft Ordnung: Sieht er einen Kampf, zieht er sich daraus zurück; sieht er das Ergebnisfenster mit der Schaltfläche „Erneut“, bricht er diesen Kampf ab und wiederholt den Raum; sieht er die Teamauswahl, führt er den Kampf durch und bricht ihn sofort ab. Er wird danach weiterarbeiten, aber dein Sieg geht verloren.

### Schritt C. Starte das Farmen

> [!warning] **Die Sprache des Programms muss mit der Sprache des Spiels übereinstimmen.** Schaltflächen mit Aufschriften („Angreifen“, „OK“, „Erneut“) und die Flagge an der Tür erkennt der Bot anhand von Bildern in der Sprache, die im Programm ausgewählt ist. Das ist die Schaltfläche mit zwei Buchstaben („DE“ bzw. „RU“) unten in der linken Leiste. Wenn das Spiel auf Deutsch ist, muss im Programm „DE“ eingestellt sein. Wenn die Sprachen unterschiedlich sind, findet der Bot die Schaltflächen einfach nicht.

1. **Klicke auf «Farmen starten»** — die grüne Schaltfläche anstelle von «Handy verbinden». Das Programm passt das Spielfenster automatisch an die richtige Größe an und platziert es in der oberen linken Ecke des Bildschirms.
2. **Erschrecke nicht, dass das Programmfenster verschwunden ist** — es hat sich in die Taskleiste minimiert, und unter dem Spiel ist eine schmale Leiste erschienen — die **Mini-Leiste**. Darauf ist zu sehen, was der Bot tut. Das Fenster wiederherstellen: Das Symbol «Programmfenster öffnen» auf der Mini-Leiste (fahre mit der Maus darüber — es erscheint ein Hinweis) oder die Schaltfläche in der Taskleiste.
3. **Beobachte das Spiel** — nach einigen Sekunden klickt der Bot auf die Tür und der erste Raum beginnt. Ein Raum dauert etwa eine halbe bis eine Minute.
4. **Merke dir, wie du den Bot stoppst** — die Taste F10 stoppt ihn sofort, F9 pausiert ihn (der Bot spielt den Raum zu Ende und wartet). Die Tasten funktionieren, wenn das Spielfenster oder das Programmfenster aktiv ist.

Wenn du das Programmfenster maximiert hast, wirf einen Blick in das Protokoll. Vor jeder Zeile steht dort die Zeit — wir haben sie weggelassen. Folgendes sollte erscheinen:

- `[УМНЫЙ СТАРТ] Сканирую экран для восстановления контекста...` — der Bot sieht sich um.
- `[УМНЫЙ СТАРТ] Контекст не требует экстренных действий. Начинаю с HALLWAY.` — alles in Ordnung, er beginnt im Korridor („HALLWAY“ heißt auf Englisch „Flur“ oder „Korridor“).
- `[СТАТИСТИКА] Комнат: 1` — der erste Raum ist geschafft. Alles funktioniert!
- :triangle-alert: `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` — der Bot wartet, bis das Spielfenster wieder im Vordergrund ist. Klicke mit der Maus darauf, und die Arbeit wird fortgesetzt.

Eine Minute ist vergangen und der Bot klickt nichts? Überprüfe:

- :gamepad-2: Im Spiel ist gerade der Titanen-Dungeon-Korridor und nicht das Menü, der Shop oder ein Kampf.
- :globe: Die Sprache des Programms stimmt mit der Sprache des Spiels überein (Warnung oben).
- :maximize-2: Das Spielfenster ist vollständig auf dem Bildschirm: nicht gestreckt, nicht maximiert, nicht über den Rand hinausgeschoben. Andernfalls stoppe den Bot (F10), klicke auf «Größe des Spielfensters zurücksetzen» und starte erneut.
- :terminal: Im Protokoll gibt es keine Zeilen mit „[ОШИБКА]“. Falls doch — behandeln wir diese im Abschnitt „Wenn etwas schiefgeht“.

### Während der Bot arbeitet

- :monitor: Das Spielfenster muss sichtbar sein: Verdecke es nicht mit anderen Fenstern und minimiere es nicht. Klickst du auf ein anderes Fenster, hält der Bot an und wartet.
- :smartphone: Schließe das Spielfenster nicht und ziehe nicht am Kabel. Ist das Fenster verschwunden, stoppt das Programm den Bot von selbst („scrcpy-Fenster geschlossen — stoppe Bot“).
- :maximize-2: Strecke und maximiere das Spielfenster nicht: Der Bot misst es beim Start aus und verwendet diese Messung im Weiteren.
- :gamepad-2: Klicke nicht selbst auf den Handybildschirm: Der Bot klickt über ADB, und ihr werdet euch gegenseitig stören. Möchtest du manuell spielen — pausiere den Bot (F9) und warte, bis er im Korridor steht.
- :triangle-alert: Sperre den Computer nicht (Win+L): Auf einem gesperrten PC sieht der Bot den Bildschirm nicht und wartet, bis du zurückkehrst.
- :moon: Schalte für das nächtliche Farmen den Energiesparmodus des Computers aus: Öffne in den Windows-„Einstellungen“ den Bereich „System“ → „Netzbetrieb und Energiesparen“ und wähle für Bildschirm und Energiesparmodus „Niemals“. Ein eingeschlafener oder ausgeschalteter Monitor ist dasselbe wie ein gesperrter Computer: Der Bot stoppt und wartet. Die Namen der Punkte hängen von der Windows-Version ab.

### Schaltflächen in der Kopfzeile

Oben rechts, neben der Plakette, befinden sich drei Symbole. Fahre mit der Maus über ein beliebiges Symbol — es erscheint eine Beschriftung.

![Kopfzeile des Fensters: Handy-Plakette, drei Schaltflächen und Fenster-Schaltflächen](images/header_buttons.png)

- :moon: **«Telefonbildschirm ausschalten»** — schaltet den Handybildschirm aus, aber das Spiel läuft weiter und der Bot sieht alles. Praktisch für die Nacht: weniger Belastung für Bildschirm und Akku. Das Programm bringt das Spielfenster in den Vordergrund und drückt darin Alt+O (so schaltet scrcpy den Bildschirm aus). Den Bildschirm wieder einschalten — mit der Einschalttaste am Handy. Eine identische Schaltfläche gibt es auf der Mini-Leiste.
- :refresh-cw: **«scrcpy neu starten»** — schließt das Spielfenster und öffnet es erneut. Nützlich, wenn das Bild vom Handy eingefroren ist. Funktioniert nur mit dem Fenster, das das Programm selbst gestartet hat. Klicke nicht darauf, während der Bot arbeitet: Ein verschwundenes Fenster betrachtet das Programm als Verbindungsabbruch und stoppt den Bot.
- :maximize-2: **«Größe des Spielfensters zurücksetzen»** — setzt das Fenster `HeroWarsBot_Arena` auf die Größe 1606 × 748 zurück und platziert es in der oberen linken Ecke. Das ist die Standardgröße: Auf sie ist die Schaltflächensuche abgestimmt. Hast du das Fenster gestreckt oder maximiert — klicke auf die Schaltfläche vor «Farmen starten» (obwohl «Farmen starten» dasselbe von selbst erledigt). Das Fenster ist breit: Auf einem Full-HD-Monitor (1920 × 1080) passt es vollständig, und der Bot sieht nur das, was sich auf dem Bildschirm befindet.

### Das Programmfenster ohne Windows-Rahmen

Das Programmfenster hat keinen gewöhnlichen Windows-Rahmen, daher besitzt es eigene Schaltflächen oben rechts hinter einer dünnen Linie:

- :minus: **«Minimieren»** — minimiert das Fenster in die Taskleiste.
- :square: **«Maximieren»** — Fenster im Vollbild; danach heißt die Schaltfläche «Größe wiederherstellen». Ein Doppelklick auf die Kopfzeile tut dasselbe.
- :x: **«Schließen»** — schließt das Programm und damit auch das Spielfenster, falls es vom Programm geöffnet wurde. Wenn der Bot arbeitet, fragt er zuerst «Bot stoppen?»; die Schaltfläche «Stoppen und schließen» stoppt ihn sofort, und die Sitzungsbilanz wird nicht an Telegram gesendet.
- :grip-vertical: **Fenster verschieben** — an der Kopfzeile: an einer leeren Stelle oben oder am Titel.
- **Größe ändern** — an der Ecke unten rechts (drei schräge Striche). Ganz klein wird das Fenster nicht werden.

> [!note] Verwechsle nicht «Minimieren» und «In Mini-Leiste verkleinern». «Minimieren» blendet das Fenster einfach in der Taskleiste aus. «In Mini-Leiste verkleinern» ist eine Schaltfläche auf der Hauptseite, während der Bot arbeitet: Sie zeigt zusätzlich die Mini-Leiste unter dem Spiel an.

> [!done] Das Handy ist verbunden, der Bot hat den ersten Raum geschafft — die Grundlage steht. Als Nächstes finden wir heraus, was die Hauptseite anzeigt und wie man das Protokoll liest. [Nächster Abschnitt →](#4)

## Hauptseite und Protokoll

Die Hauptseite ist die erste Schaltfläche in der linken Leiste und genau die siehst du am häufigsten. Sie ähnelt einem Armaturenbrett im Auto: oben Zahlen („wohin wir fahren“ und „wie wir fahren“), unten das Protokoll, in das der Bot selbst schreibt, was er tut. Wir erklären, was wo liegt und wie man sich nicht in den Protokollzeilen verliert.

### Die Karte oben: Sie ändert ihr Aussehen selbstständig

Im oberen Teil der Hauptseite befindet sich eine große Karte, aber sie zeigt Verschiedenes an — je nachdem, was gerade mit dem Bot los ist:

- :sliders-vertical: **«Starteinstellungen»** — der Bot steht still, aber die Einstellungen sind bereits gespeichert. Das ist das, „womit der Bot in den Kampf zieht“: Ziel, Modus und Schwellenwerte.
- :activity: **«Aktuelle Sitzung»** — der Bot arbeitet. Live-Zahlen: wie viel gesammelt, wie viel geschafft, wie viel Zeit vergangen ist.
- :file-text: **«Sitzungsbilanz»** — der Bot hat angehalten. Die Karte zeigt, was erreicht wurde und warum er angehalten hat.
- :list: **«Erste Schritte»** — nur solange du noch nie Einstellungen gespeichert hast (sie wird in [Abschnitt 3](#3) beschrieben).

Eine Sitzung ist ein einziger Bot-Start: von «Farmen starten» bis zum Stopp.

### Starteinstellungen

Vier Plaketten, und jede beantwortet eine Frage. Die Zahlen stammen aus deinen Einstellungen. Wenn dir also etwas nicht gefällt, klicke oben rechts auf der Karte auf «Im Regel-Assistenten ändern →»: Der «Regelmeister» öffnet sich.

![Hauptseite vor dem Start: Karte «Starteinstellungen» und leeres Protokoll](images/main_config.png)

- :target: **«Sitzungsziel»** — wann der Bot anhalten soll. Es gibt **ein** Ziel: Titanit, Räume, Etagen oder Zeit. Wenn in den Einstellungen mehrere festgelegt sind, wird das erste in der Reihenfolge „Titanit → Räume → Etagen → Zeit“ genommen. Hast du nichts geändert — ist das Ziel 120 Titanit, das sind 10–20 Räume. «Ohne Limit» bedeutet, dass alle Ziele null sind und der Bot läuft, bis du ihn stoppst.
- :shield-check: **«Modus»** — Plakette «Bot entscheidet selbst» mit dem Vermerk «AN» oder «AUS». Aktiviert: Bei einem schlechten Kampf wiederholt der Bot den Kampf selbst mit einem anderen Pack. Deaktiviert: Er ruft dich. Details — in den Abschnitten über den «Regelmeister».
- :heart-pulse: **«LP-Panikschwelle»** — zum Beispiel 40%. Wenn nach dem Kampf bei einem der Titanen weniger Lebenspunkte übrig sind, gilt der Kampf als schlecht. Ein Pack ist ein Team aus fünf Titanen; LP sind Lebenspunkte.
- :calendar: **«Tagesreset»** — zum Beispiel 05:00. Ab dieser Stunde beginnt im Spiel ein neuer Tag: Der Bot berechnet die Tagesstatistik und vergisst, wie viele Lebenspunkte die Titanen gestern hatten.

> [!note] Der Bot liest die Einstellungen **einmalig, wenn du auf «Farmen starten» klickst**. Wenn du während des Betriebs etwas änderst, erfährt der Bot erst beim nächsten Start davon. Daher werden auf der Karte während der Arbeit des Bots genau die Einstellungen angezeigt, mit denen er gestartet ist.

### Aktuelle Sitzung

Wenn der Bot gestartet ist, verwandelt sich die Karte in die «Aktuelle Sitzung». Oben rechts leuchtet der Status:

- :activity: **«Farmen läuft»** — alles in Ordnung, der Bot arbeitet.
- :pause: **«Pause»** — du hast auf «Pause» geklickt (oder der Bot hat selbst eine sanfte Pause eingelegt). Die Schaltfläche wurde dabei zu «Fortsetzen».
- :triangle-alert: **«Wartet auf deine Entscheidung»** — auf dem Bildschirm ist das Fenster «Eingriff erforderlich», der Bot wartet auf deine Antwort.
- :refresh-cw: **«Bot wird gestartet»** — die ersten Sekunden nach «Farmen starten».

![Farmen läuft: Sitzungs-Plaketten mit Fortschrittsbalken zum Ziel](images/main_session.png)

Es gibt vier Plaketten:

1. **«Titanit in dieser Sitzung»** — wie viel Titanit der Bot gesammelt hat. Das ist eine **Berechnung, kein Ablesen vom Bildschirm**: 6 pro Raum und 12, wenn im Spiel das Symbol „x2“ leuchtet. Wenn das Ziel Titanit ist, erscheinen daneben „gesammelt / benötigt“, Prozentangaben und ein Balken.
2. **«Etagen geschafft»** — eine Etage wird gezählt, wenn der Bot die Belohnung am Speicherpunkt abgeholt hat (so heißt die Stelle am Ende einer Etage, an der man auf „Aktivieren“ und „Abholen“ klickt). Daneben steht, welche Tür er zuletzt betreten hat: Wasser, Erde, Feuer oder gemischt.
3. **«Kämpfe in dieser Sitzung»** — zum Beispiel «{wins} Siege von {total}». Ein Sieg ist ein gezählter Raum. Ein Rücksetzer ist ein Kampf, den der Bot wiederholt hat: Er zählt ebenfalls als Kampf, daher ist „insgesamt“ manchmal höher als „Siege“.
4. **«Sitzungsdauer»** — Stunden:Minuten:Sekunden und klein «Raum im Schnitt {s} s». Der Durchschnitt wird nach Räumen berechnet, ohne Wartezeit am Speicherpunkt.

> [!tip] Wenn das Ziel Räume oder Zeit ist, stehen die Prozentangaben rechts als „35% von 100“ oder „35% von 120 Min.“ — in die Zahl selbst passt das Ziel nicht. Der Balken unter der Plakette ist derselbe.

> [!note] Wenn das Ziel erreicht ist, bricht der Bot die Etage nicht mittendrin ab. Er schreibt im Protokoll `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.`, spielt die verbleibenden Räume zu Ende und hält vor dem Speicherpunkt an, ohne auf „Aktivieren“ zu klicken: Die Belohnung für die Etage holt er als Allererstes beim nächsten Start ab. Eine Ausnahme ist das Etagenziel: Dann stoppt der Bot direkt nach der Belohnung.

### Sitzungsbilanz

Der Bot hat angehalten — die Karte zeigt das Ergebnis und das Fenster wird automatisch aus der Mini-Leiste wiederhergestellt. Oben steht der Grund für den Stopp: die Schaltfläche «STOPP», ein geschlossenes scrcpy-Fenster, normales Beenden oder das, was der Bot selbst geschrieben hat (z. B., dass das Ziel erreicht wurde).

![Sitzungsbilanz: Stoppgrund, Zahlen und Schaltfläche «Details»](images/main_summary.png)

Dieselben vier Plaketten wie in der Sitzung, aber jetzt sind es die endgültigen Zahlen; bei den „Kämpfen“ wird „SOS-Fenster: N“ hinzugefügt (wie oft der Bot dich gerufen hat). Die Schaltfläche **«Details»** öffnet ein Fenster mit dem gesamten Bericht des Bots: durchschnittliche Zeiten nach Etappen, die längsten Räume, wie viele Rücksetzer es gab und wie viele davon der Bot **ohne dich** durchgeführt hat. Das Symbol ✕ rechts blendet das Ergebnis aus und anstelle dessen ist wieder die «Starteinstellungen» zu sehen. Klickst du auf «Farmen starten» — verschwindet das Ergebnis von selbst.

> [!note] Wenn Telegram eingerichtet ist, wird das Ergebnis bei jedem normalen Stopp automatisch dorthin gesendet. Die Schaltfläche «STOPP» (F10) beendet den Bot sofort, daher wird das Ergebnis in diesem Fall nicht an Telegram gesendet.

### Protokoll: Was drin steht und wie man es liest

Der untere Teil der Hauptseite ist das **«Arbeitsprotokoll»**. Der Bot schreibt jeden seiner Schritte hinein und das Programm zeigt dies im Fenster an. Erschrecke nicht vor der Anzahl der Zeilen: Du musst nicht alles lesen, das Protokoll wird benötigt, wenn etwas schiefgegangen ist oder wenn du neugierig bist.

Jede Zeile ist gleich aufgebaut:

`10:26:17.486 [НАВИГАЦИЯ] Двери (слева направо): EARTH (0.98), FIRE (0.97)`

1. **Zeit** — in Grau. Stunden:Minuten:Sekunden und Tausendstelsekunden.
2. **Tag in eckigen Klammern** — „wer spricht“ und worum es geht. Er ist farbig markiert: Die Farbe deutet darauf hin, zu welchem Protokollbereich die Zeile gehört.
3. **Text** — was genau passiert ist. Eine lange Zeile wird umgebrochen, und die Fortsetzung steht unter dem Text, nicht unter der Zeit.

Eine Zeile ohne Tag (zum Beispiel ` ---> HYPERION: ХП 100%, Энергия 79%`) — ist die Fortsetzung der Zeile darüber und gehört zum selben Bereich.

### „Pillen“-Filter

Über dem Protokoll befinden sich fünf „Pillen“-Schaltflächen. Klicke auf eine — und im Protokoll bleiben nur die Zeilen dieses Bereichs. Die Auswahl wird gespeichert: Öffnest du das Programm morgen wieder, ist dieselbe Pille ausgewählt.

![Protokoll mit den Pillen «Alle», «Kämpfe», «Regeln», «System» und «Fehler»](images/journal_pills.png)

- **«Alle»** — alles nacheinander.
- **«Kämpfe»** (grüne Tags) — der Verlauf des Durchspielens: Räume, Zeit, Gesundheit der Titanen, Rücksetzer. Tags `[КОМБАТ]`, `[СТАТИСТИКА]`, `[ВРЕМЯ]`, `[СОСТОЯНИЕ]`, `[АНАЛИЗАТОР]`, `[ОТКАТ]`, `[ЛИМИТ]`, `[ИТОГ]`.
- **«Regeln»** (gelbe Tags) — Entscheidungen des Bots: welches Pack eingesetzt werden soll, warum ein Kampf zurückgesetzt wurde, was er sich gemerkt hat. Tags `[ТАКТИКА]`, `[КОМАНДА]`, `[ПРАВИЛА]`, `[ОБУЧЕНИЕ]`, `[SOS_CLOSE]`.
- **«System»** (hellblaue Tags) — alles Weitere: Korridor und Türen (`[НАВИГАЦИЯ]`), Start (`[УМНЫЙ СТАРТ]`), Verbindung. Die Zeilen des Programms selbst mit dem Tag `[GUI]` sind grau, liegen aber auch hier.
- **«Fehler»** (rote Tags) — alles, was Aufmerksamkeit erfordert: `[ОШИБКА]`, `[ВНИМАНИЕ]`, `[СТОРОЖ]`, `[SOS]`. Neben dem Namen steht eine Zahl — wie viele solcher Zeilen zusammengekommen sind.

> [!warning] Eine rote Zahl bei «Fehler» ist nicht immer ein Defekt. Dort landet auch `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` — der Bot wartet einfach, bis du das Spielfenster wieder in den Vordergrund holst. Lies den Text der Zeile und erschrecke nicht vor der Farbe.

### Beispiele echter Zeilen

Das sind Zeilen aus einer echten Sitzung des Bots (die Zeit wurde der Kürze halber weggelassen). Lerne diese fünf zu lesen — und du verstehst jedes Protokoll.

- `[НАВИГАЦИЯ] Выбрана комната EARTH (порядок: water → mix → earth → fire)` — der Bot hat die Erdtür gewählt. In den Klammern — deine Reihenfolge der Türen. Die Zahl in der Zeile „Türen (von links nach rechts)“ weiter oben gibt an, wie sicher sich der Bot ist, die Tür erkannt zu haben (1 — absolut).
- `[ВРЕМЯ] Комната 2 (earth): коридор 12.8 с | сборка 3.3 с | бой 8.0 с | результат 9.1 с | всего 33.2 с` — Bericht über den Raum: wie viel Zeit für den Weg zur Tür, die Zusammenstellung des Teams, den Kampf und das Schließen des Ergebnisfensters benötigt wurde.
- `[СТАТИСТИКА] Комнат: 3 | Титанит: 36` — der dritte Raum ist geschafft, 36 Titanit gesammelt. Diese Zahlen landen auf den Sitzungs-Plaketten.
- `[ТАКТИКА] Откатываю бой сам и переиграю паком [...] (взят: ваш список запасных паков).` — der Kampf lief schlecht und der Bot (Modus «Bot entscheidet selbst») wiederholt ihn mit einem Reserve-Pack. Wenn das Reserve-Pack es schafft: `[ТАКТИКА] Запасной пак [...] справился. Запоминаю его против этих врагов.`
- `[ОТКАТ] Запускаю протокол отката боя...` — Beginn des Rücksetzens: „Erneut“ → Pause → „Rückzug“. Jede solche Zeile fügt einen Kampf auf der Plakette «Kämpfe in dieser Sitzung» hinzu.

> [!tip] Zu Beginn jeder Sitzung schreibt der Bot `[ТАКТИКА] Плохой бой: ХП ниже 30% | потеря больше 60% | ...` — die Schwellenwerte, nach denen er die Kämpfe beurteilen wird. Wenn etwas „nicht so gelaufen ist, wie du es erwartet hast“, vergleiche zuerst diese Zeile mit deinen Einstellungen.

### Schaltflächen unter dem Protokoll

![Schaltflächen unter dem Protokoll: «Log speichern», «Log an den Autor senden», «Leeren»](images/journal_buttons.png)

- :save: **«Log speichern»** — speichert das gesamte Protokoll in einer Textdatei. Das Programm schlägt selbst den Namen `gui_log_...txt` und den Ordner `bot_data/logs` vor; du kannst einen anderen wählen.
- :mail: **«Log an den Autor senden»** — zuerst dieselbe Speicherung, danach öffnet sich dein E-Mail-Programm mit einer vorgefertigten E-Mail. **Füge die Datei selbst als Anhang bei** (und `battle_log.csv` aus demselben Ordner): Das Programm kann das nicht tun. Kein E-Mail-Programm vorhanden? Schreibe dem Autor über die Adresse aus dem Abschnitt «Über das Programm».
- :x: **«Leeren»** — entfernt Zeilen aus dem Fenster, fragt aber zuerst «Protokoll leeren?». Das ist sicher: Das vollständige Log speichert der Bot selbst im Ordner `bot_data/logs`, und die Sitzungszahlen werden nicht zurückgesetzt.

Du kannst Text im Protokoll mit der Maus markieren und kopieren — mit Ctrl+C oder der rechten Maustaste («Kopieren»). Das Protokoll kann nicht bearbeitet werden — es ist schreibgeschützt. Wenn du im Protokoll nach oben gescrollt hast, um zu lesen, „entwischt“ es mit neuen Zeilen nicht nach unten; scrolle ganz nach unten — und es bewegt sich wieder zusammen mit dem Bot.

> [!note] Das Fenster merkt sich die letzten 50.000 Zeilen und zeigt die letzten 4.000 an — andernfalls würde es bei langem Farmen langsamer werden. Alles Weitere befindet sich in der Datei `bot_data/logs/bot_log_...txt`: Der Bot führt sie selbst, und das manuelle Speichern des Protokolls ist normalerweise nicht erforderlich.

Solange das Protokoll leer ist, steht an seiner Stelle die Aufschrift «Das Protokoll ist leer». Zeilen erscheinen nach dem Verbinden des Handys. Eine leere Pille zeigt «Hier ist noch nichts» und «Solche Zeilen gab es noch nicht» an — für «Fehler» sind das gute Nachrichten.

> [!done] Jetzt liest du die Hauptseite wie ein Armaturenbrett: Du weißt, was die Plaketten und die Farben der Protokoll-Tags bedeuten. Als Nächstes — die Mini-Leiste, eine kleine Leiste unter dem Spiel. [Nächster Abschnitt →](#5)

## Mini-Leiste unter dem Spiel

Solange der Bot läuft, brauchst du das Hauptfenster des Programms normalerweise nicht. Deshalb wird es automatisch in die Taskleiste minimiert und unter dem Spielbildschirm erscheint eine schmale Leiste — die **Mini-Leiste**. Das ist wie ein Armaturenbrett im Auto: Mit einem Blick siehst du, ob der Bot fährt, was er gerade tut, wie viel er schon geschafft hat und ob er nach dir ruft.

![Mini-Leiste unter dem Spielfenster während des Farmens](images/mini_bar.png)

### Wann sie erscheint und wo sie steht

- :monitor: **Erscheint automatisch.** Sobald der Bot startet („Farmen starten“), wird das Programmfenster minimiert und die Mini-Leiste platziert sich direkt unter dem Spiel. Wenn du das Programmfenster geöffnet hast und es wieder ausblenden willst, während der Bot arbeitet, klicke auf der Hauptseite auf „In Mini-Leiste verkleinern“.
- :smartphone: **Sitzt direkt unter dem Spiel** und hat genau dieselbe Breite wie das Spielbildschirm-Fenster. Wenn du das Spielfenster verschiebst, folgt die Mini-Leiste (das Programm prüft dies zweimal pro Sekunde).
- :eye: **Verdeckt das Spiel um keinen einzigen Pixel.** Das ist wichtig: Der Bot „schaut“ auf den Bildschirm, indem er Screenshots des Fensters macht. Wenn die Leiste auf dem Spiel liegen würde, würde der Bot sie anstelle der Schaltflächen sehen.
- :maximize-2: **Kein Platz unten** (Spielfenster befindet sich am unteren Bildschirmrand) — die Leiste platziert sich über der Titelleiste des Fensters. Ist auch dort kein Platz, wird sie nicht angezeigt und das Programmfenster bleibt in der Taskleiste. Wenn du das Spielfenster minimierst, blendet sich die Leiste aus und kehrt zusammen mit ihm zurück.

> [!tip] Siehst du die Mini-Leiste nicht, obwohl der Bot arbeitet? Schiebe das Spielfenster weiter nach oben: Darunter werden etwa 100 Pixel freier Platz benötigt. Das Fenster darf verschoben werden, die Größe darfst du aber nicht verändern (das haben wir in Abschnitt 3 besprochen).

### Was auf der Leiste zu sehen ist: fünf Spalten von links nach rechts

- :activity: **Status.** Ein Wort und ein farbiger Punkt, der „atmet“, solange alles in Ordnung ist: „START“, „FARMEN LÄUFT“, „PAUSE“, „DEBUG-PAUSE“ oder ein rotes „SOS“. Darunter — **was der Bot gerade tut** und seit wie vielen Sekunden: zum Beispiel „Kampf · Feuer · 12 s“. Danach „Räume: 12 · Etagen: 2“ und die Sitzungszeit, zum Beispiel „Zeit 00:42:17“.
- :target: **Ziel.** Name des Ziels, wie viel erledigt ist, wie viel benötigt wird und ein Fortschrittsbalken. Darunter — „~28 s pro Raum“ (Durchschnittszeit; vor dem ersten Raum steht dort „Raumzeit — nach dem ersten“) und die Prognose „Ziel in ≈ 1 Std. 10 Min.“. Die Prognose berechnet der Bot anhand der Geschwindigkeit **dieser** Sitzung, weshalb sie am Anfang schwankt und sich später einpendelt. Gibt es kein Ziel („Ohne Limit“), gibt es keinen Balken und stattdessen die Anzeige „≈ N Titanit pro Stunde“.
- :heart-pulse: **Gesundheit des Teams.** Die Quadrate der Titanen aus dem letzten Kampf und ihre HP danach — in der Reihenfolge, wie sie auf dem Spielbildschirm stehen. Vor dem ersten Kampf steht dort „noch keine Kämpfe“. Die Farbe der Zahl gibt Hinweise: Rot — HP unter der Panikschwelle (global oder individuell), Gelb — unter der Schwelle, ab der der Bot den Titanen heilt, normale Farbe — alles in Ordnung. Ein Gedankenstrich „—“ bedeutet, dass das Titanen-Icon im Ergebnisfenster nicht gefunden werden konnte.
- :list: **Ereignisse.** Die letzten vier Zeilen, die aktuellste oben und etwas größer. Links eine farbige Markierung, rechts die Uhrzeit.
- :gamepad-2: **Schaltflächen.** Vier Schaltflächen in einem 2×2-Quadrat.

### Was der Bot „gerade tun“ kann

In der ersten Spalte nennt der Bot selbst seine Phase. Das bedeuten diese Wörter:

- **„Korridor“**, **„Türwahl“**, **„Team wird gestellt“**, **„Kampf“**, **„Ergebnisfenster“** — der normale Ablauf eines Raums. Den Phasen „Team wird gestellt“, „Kampf“, „Ergebnisfenster“ und „Rückzug“ wird das Element des Raums angehängt: „Kampf · Wasser · 12 s“.
- **„Speicherpunkt“** — die Etage ist geschafft, der Bot holt die Belohnung ab.
- **„Rückzug“** — der Kampf lief schlecht, der Bot zieht sich zurück und bereitet die Wiederholung vor.
- **„Prüft den Bildschirm“** — nach dem Start sieht sich der Bot um und entscheidet, womit er beginnen soll (das ist der „intelligente Start“).
- **„Pause im Korridor“**, **„Wartet auf deine Entscheidung“**, **„Du spielst selbst“** — der Bot steht still, weil du Pause gedrückt hast, weil er dich etwas gefragt hat oder weil du „Manuell spielen“ gewählt hast.
- **„Wartet auf das Spielfenster“** und **„Wartet auf Verbindung“** — der Bot wartet: Entweder ist das Spiel nicht im Vordergrund (siehe unten) oder es besteht keine Verbindung zum Spielserver.

Wenn dieselbe Anzeige länger als üblich bestehen bleibt, steigt die Sekundenzahl rechts und zeigt dir, dass der Bot in Wirklichkeit stillsteht.

### Ereignisse: Markierungen und ihre Bedeutung

Die Markierung links zeigt, worum es bei dem Ereignis geht:

- **Name des Elements** („Wasser“, „Erde“, „Feuer“, „Gemischt“) — Raum geschafft. Eine Zeile wie „Raum 45 geschafft · 28 s · meiste geschwächte HP: Araji 36%“ zeigt an, wie viele Sekunden der Raum gedauert hat und wer mit den niedrigsten HP übrig geblieben ist.
- **„Etage“** — Etage geschafft („Etage geschafft, insgesamt 3“).
- **„Rückzug“** — der Kampf wird wiederholt. **„SOS“** — der Grund für den Aufruf in einfachen Worten.
- **„Pause“** — „Pause: der Bot beendet den Kampf und wartet“, danach „Der Bot wartet im Korridor“.
- **„Bot“** — „Bot gestartet“, „Pause aufgehoben, der Bot macht weiter“, „Keine Antwort seit 10 Min. — der Bot hat selbst entschieden“.
- **„Limit“** — die Sitzung hat das Ziel erreicht, der Bot spielt noch bis zum Speicherpunkt weiter.
- **„Achtung“** — „Spielfenster nicht aktiv — der Bot wartet. Klicke ins Spiel“.
- **„Fehler“** — der Fehlertext so, wie ihn der Bot geschrieben hat.

Lange Zeilen werden mit Auslassungspunkten gekürzt. Der vollständige Text ist immer im Protokoll auf der Hauptseite verfügbar.

### Schaltflächen

Fahre mit der Maus darüber — es erscheint eine Beschriftung. Alle Schaltflächen tun dasselbe wie ihre „großen Geschwister“ auf der Hauptseite und in der Kopfzeile.

- :pause: **Pause / Fortsetzen** — „Sanfte Pause: der Bot beendet den Kampf und wartet (F9)“. Während der Pause verwandelt sich das Symbol in ein grünes Dreieck, und dieselbe Schaltfläche hebt die Pause wieder auf. Während der Bot noch startet, ist die Schaltfläche nicht verfügbar.
- :square-filled: **STOPP** — „Notstopp: der Bot stoppt sofort, keine Bilanz in Telegram (F10)“.
- :moon: **Telefonbildschirm** — „Telefonbildschirm ausschalten“, das Spiel läuft dabei weiter.
- :maximize-2: **Maximieren** — „Programmfenster öffnen“. Die Mini-Leiste verschwindet. Dasselbe Ergebnis liefert die Schaltfläche des Programmfensters in der Taskleiste. Wenn du die Leiste zurückhaben willst, klicke auf der Hauptseite auf „In Mini-Leiste verkleinern“.

> [!note] Wenn der Bot nach dir ruft, färbt sich die Mini-Leiste rot und das Fenster „Eingriff erforderlich“ erscheint automatisch in der Mitte des Spielbildschirms — du musst das Programmfenster nicht maximieren. Die erste Schaltfläche setzt in diesem Moment nicht auf Pause und klickt nicht auf „Fortsetzen“: Sie zeigt das SOS-Fenster an, falls es unter andere Fenster geraten ist (Beschriftung — „SOS-Fenster zeigen: der Bot wartet auf deine Entscheidung“). Sobald du im Fenster geantwortet hast, wird die Mini-Leiste wieder normal. Wie man antwortet, besprechen wir im Abschnitt über SOS-Fenster.

![Mini-Leiste während SOS](images/mini_bar_sos.png)

### Die wichtigste Regel: Der Bot arbeitet nur, solange das Spiel im Vordergrund ist

Der Bot macht Screenshots vom Bildschirm und sucht darauf nach Schaltflächen. Wenn sich ein anderer Browser, Messenger oder Dateiexplorer über das Spiel legt, erscheinen diese auf dem Screenshot und nicht das Spiel: Der Bot könnte an die „falsche Stelle“ klicken. Sobald daher ein anderes Fenster aktiv wird, stoppt er und wartet. Im Protokoll erscheint die Zeile „[ВНИМАНИЕ] Окно игры перекрыто … Бот ждет фокуса…“, in der Mini-Leiste die Markierung „Achtung“ und die Phase „Wartet auf das Spielfenster“. Klickst du ins Spiel — „[ИНФО] Окно снова активно. Продолжаем работу.“

- :monitor: **Klicks auf die Mini-Leiste stoppen den Bot nicht.** Die Mini-Leiste ist so gebaut, dass sie nicht zum aktiven Fenster wird: Das Spiel bleibt „hauptsächlich“, während du Schaltflächen auf der Leiste drückst.
- :triangle-alert: **„Maximieren“ stoppt den Bot vorübergehend.** Das Programmfenster ist aktiv geworden, das Spiel jedoch nicht, sodass der Bot beim nächsten Schritt anhält. Wenn du fertig bist, klicke auf das Spielfenster, und der Bot macht weiter. Der Wächter zählt diese Wartezeit nicht als „Aufhängen“.
- :gamepad-2: Du möchtest am Computer arbeiten, während der Bot farmt? Öffne andere Fenster **nebeneinander** und nicht über dem Spiel, und klicke nicht darauf. Oder verschiebe die Aufgabe bis zur Pause (F9).

> [!warning] Die Tastenkombinationen F9 und F10 funktionieren nur, wenn das Spielfenster oder das Programmfenster aktiv ist. Drückst du F10 im Browser, stoppt der Bot nicht: Die Tasten reagieren nicht, wenn du mit etwas anderem beschäftigt bist. Mehr dazu findest du im Abschnitt über Pause und Stoppen.

> [!done] Jetzt liest du die Mini-Leiste wie ein Armaturenbrett und weißt, warum du das Spiel nicht unter anderen Fenstern verstecken darfst. Als Nächstes — Pause, Stoppen und Tastenkombinationen. [Nächster Abschnitt →](#6)

## Pause, Stoppen und Tastenkombinationen

Der Bot läuft von selbst durch das Dungeon, aber manchmal musst du ihn abbremsen: Du möchtest manuell spielen, kurz weggehen или просто закончить. Dafür gibt es **vier Möglichkeiten**, und sie unterscheiden sich darin, **wie sanft** der Bot anhält. Stell dir ein Auto vor: „Pause“ bedeutet, am Straßenrand anzuhalten und den Motor abzustellen, während „Notstopp“ dem Herausziehen des Schlüssels während der Fahrt entspricht. Beide funktionieren, aber auf unterschiedliche Weise.

### Sanfte Pause: „Pause F9“

Die schonendste Methode. Klicke auf die Schaltfläche „Pause“ auf der Hauptseite, in der Mini-Leiste oder drücke die Taste **F9**.

1. **Drücke „Pause“ или F9.** Im Protokoll erscheint die Zeile `[GUI] Сигнал 'Мягкая пауза' отправлен. Бот остановится перед следующей дверью.`
2. **Warte, bis der Bot den Raum beendet hat.** Einen bereits laufenden Kampf bricht er nicht ab: Er spielt ihn zu Ende, schließt das Ergebnisfenster und zeichnet das Raumergebnis auf.
3. **Der Bot hält im Korridor an.** Im Protokoll: `[МЯГКАЯ ПАУЗА] Бот ждет в коридоре...`. Status auf der Hauptseite — „Pause“, in der Mini-Leiste — „PAUSE“, die Schaltfläche ist grün geworden („Fortsetzen“).
4. **Erledige deine Dinge und klicke auf „Fortsetzen“ (oder drücke erneut F9).** Der Bot schreibt `[ИНФО] Пауза снята. Кэш составов и здоровья очищен. Включаю механизм Умного Старта.` und macht weiter.

> [!note] „Cache geleert“ bedeutet, dass der Bot **vergessen hat**, welche Teams aufgestellt waren und wie viel Gesundheit die Titanen hatten: Während du mit dem Spiel beschäftigt warst, könnte sich alles geändert haben. Vor dem nächsten Kampf sieht er sich den Teamauswahl-Bildschirm erneut an und liest die Gesundheit davon ab. Der „intelligente Start“ bedeutet, dass der Bot zuerst prüft, was sich gerade auf dem Bildschirm befindet, und erst dann entscheidet, was zu tun ist (zum Beispiel ein vergessenes Ergebnisfenster schließt).

- :eye: **Während der Pause kannst du auf das Telefon schauen und Einstellungen im Programmfenster ändern.** Die Einstellungen übernimmt der Bot jedoch erst beim nächsten „Farmen starten“ (mehr dazu im Abschnitt über die Hauptseite).
- :door-open: **Wenn du im Spiel etwas gedrückt hast, kehre in den Korridor des Dungeons zurück** (wo die Fahne an der Tür zu sehen ist) und klicke erst dann auf „Fortsetzen“. So versteht der Bot genau, wo er sich befindet.
- :gauge: **Die Zeit läuft auch während der Pause weiter.** Wenn das Sitzungsziel Zeit ist („120 Minuten“), frisst die Pause einen Teil dieser Zeit. Dafür zählt der „Wächter“ (der prüft, ob sich der Bot aufgehängt hat) die Pausenzeit nicht mit und schlägt keinen Alarm.

> [!tip] Möchtest du über Nacht oder für längere Zeit weggehen? Eine sanfte Pause brauchst du dafür nicht: Lege auf der Hauptseite ein Ziel fest (Titanit, Räume, Etagen oder Zeit), und der Bot läuft selbstständig bis zum Speicherpunkt, stoppt und sendet die Bilanz.

### Wann der Bot selbst eine Pause einlegt

Manchmal bittet der Bot um Hilfe und geht von selbst in eine sanfte Pause. Dann zeigt die Schaltfläche ebenfalls „Fortsetzen“ an und im Protokoll steht `[ВНИМАНИЕ] Бот на мягкой паузе: ...` mit dem Grund. Das passiert, wenn:

- der Bot dreimal hintereinander innerhalb von 5 Minuten keinen einzigen Raum geschafft hat (der Wächter hat entschieden, dass er sich aufgehängt hat);
- der Rückzug des Kampfes fehlgeschlagen ist (Bildschirm wurde nicht erkannt, Schaltflächen wurden nicht gedrückt);
- der Kampf selbst nach langem Warten gar nicht erst begonnen hat;
- du nicht auf das Fenster „Kein passendes Pack“ geantwortet hast und kein Ersatzteam vorhanden ist.

Schaue in solchen Fällen zuerst **auf den Telefonbildschirm**, behebe das Problem (schließe ein überflüssiges Fenster, kehre in den Korridor zurück) und klicke erst danach auf „Fortsetzen“. Wenn Telegram eingerichtet ist, sendet der Bot eine Nachricht mit einem Screenshot.

### Notstopp: „STOPP F10“

Die rote Schaltfläche „STOPP“ (oder die Taste **F10**) stoppt den Bot **sofort**: Das Programm beendet den Bot-Prozess gewaltsam. Im Protokoll steht `[GUI] ЭКСТРЕННЫЙ СТОП. Процесс убит.`, auf der Bilanzkarte der Grund „vom Benutzer gestoppt (STOPP)“.

> [!warning] Was bei F10 verloren geht: Der Bot schafft es nicht mehr, den Block `[ИТОГ]` ins Protokoll zu schreiben und **sendet keine Sitzungsbilanz an Telegram**. Wenn er sich in diesem Moment in einem Kampf befand, läuft der Kampf im Spiel weiter (oder bleibt auf dem Bildschirm stehen) — das siehst du auf dem Telefon. Bereits geschaffte Räume sind in der Statistik gespeichert: Der Bot zeichnet sie sofort nach jedem Raum auf.

Wann genau diese Schaltfläche benötigt wird: Der Bot verhält sich merkwürdig (klickt an die falsche Stelle, reagiert nicht auf „Pause“) oder du musst sofort alles beenden. In allen anderen Fällen ist eine Pause oder Ctrl+Q besser.

### Tastenkombinationen: Was wo funktioniert

- :pause: **F9** — Pause / „Fortsetzen“ (dasselbe wie die Schaltfläche „Pause“ auf der Hauptseite).
- :square-filled: **F10** — „STOPP“.
- :gamepad-2: **Ctrl+Q** — stoppen **mit Bilanz**: Der Bot spielt den angefangenen Raum zu Ende, hält im Korridor an, stoppt und sendet die Sitzungsbilanz. Im Protokoll: `[ИНФО] Команда 'Ctrl+Q' принята! Бот завершит бой и остановится.`, der Stoppgrund ist „Manuelles Stoppen durch Benutzer (Ctrl+Q)“.
- :triangle-alert: **Ctrl+Shift+Q** — **sofort stoppen, aber mit Bilanz**: Der Bot druckt `[ЭКСТРЕННАЯ ОСТАНОВКА]`, zeichnet `[ИТОГ]` auf und unternimmt **einen** Versuch, die Bilanz an Telegram zu senden (ohne Wiederholungen, um keine Zeit zu verlieren).

Wichtige Feinheiten, wegen derer Tasten manchmal „nicht funktionieren“:

- **F9 und F10 werden vom Programmfenster registriert** und zwar nur dann, wenn **das Spielfenster oder das Programmfenster aktiv ist**. Drückst du F10 im Browser oder Messenger, passiert nichts. Wenn das Spiel minimiert oder von einem anderen Fenster verdeckt ist, nutze die Schaltflächen in der Mini-Leiste: Sie funktionieren immer, weil die Mini-Leiste dem Spiel den Fokus nicht entzieht.
- **Ctrl+Q und Ctrl+Shift+Q werden vom Bot selbst registriert** und nicht vom Programmfenster, daher funktionieren sie, solange der Bot läuft, selbst wenn ein anderes Fenster aktiv ist.
- **Diese Tastenkombinationen sind auch anderen Programmen bekannt.** Ctrl+Q schließt viele Programme (Word, Telegram Desktop), und Ctrl+Shift+Q schließt Browser. Drücke sie während der Bot arbeitet nicht in anderen Fenstern: Der Bot wird dies ebenfalls „hören“ und stoppen.
- **Ctrl+Q prüft der Bot, wenn er sich im Korridor befindet** vor der nächsten Tür. Während einer sanften Pause steht er still und prüft nichts, daher funktioniert Ctrl+Q erst nach „Fortsetzen“. Wenn der Bot jedoch im SOS-Fenster auf deine Antwort wartet, stoppt ihn Ctrl+Q sofort.
- **Gedrückthalten der Taste wiederholt nichts:** Ein Druck — ein Befehl.
- Drückst du F9 oder F10, wenn der Bot nicht gestartet ist, erscheint im Protokoll `[GUI] Нажата F9, но бот не запущен.`

### Das Schließkreuz des Fensters und das Schließen von scrcpy

- :x: **Das Schließkreuz des Programmfensters, während der Bot arbeitet.** Es öffnet sich die Frage „Bot stoppen?“. Die Schaltfläche „Stoppen und schließen“ schließt das Programm und den Bot sowie das Spielfenster (scrcpy) — falls es vom Programm selbst geöffnet wurde, sofort — und die Bilanz wird nicht an Telegram gesendet. Wenn du das nicht willst, schließe das Fragefenster und stoppe den Bot zuerst sanft.
- :smartphone: **Hast du das Spielfenster (`HeroWarsBot_Arena`) selbst geschlossen.** Das Programm schreibt `[GUI] Окно scrcpy закрыто — останавливаю бота (он напишет итог и пришлёт его в Telegram).` Der Bot verfasst selbst die Sitzungsbilanz und sendet sie an Telegram; antwortet er nicht innerhalb von 10 Sekunden, stoppt das Programm ihn wie bei F10.
- :pencil: Wenn im „Regelmeister“ ungespeicherte Änderungen vorhanden sind, fragt das Schließkreuz zuerst „Änderungen speichern?“.

### Was wählen

- **Ich möchte eine Pause machen und zurückkehren** — „Pause“ (F9). Klicke auf „Fortsetzen“, wenn du bereit bist.
- **Ich möchte beenden und die Bilanz erhalten** — Ctrl+Q (der Bot spielt den Raum zu Ende, stoppt und sendet die Bilanz an Telegram).
- **Ich muss sofort stoppen, brauche aber die Bilanz** — Ctrl+Shift+Q.
- **Der Bot ist defekt oder verhält sich merkwürdig** — „STOPP“ (F10), danach anhand des Protokolls analysieren.
- **Der Bot hat dich über ein SOS-Fenster gerufen und du möchtest beenden** — die Schaltfläche „Bot stoppen“ in diesem Fenster: Der Bot stoppt selbstständig und sendet die Bilanz. Das SOS-Fenster besprechen wir separat.

### Sitzungsbilanz in Telegram

Wenn Telegram eingerichtet ist, kommt die Bilanz bei jedem Stopp an, **außer bei der Schaltfläche „STOPP“** und dem Schließen des Programmfensters: Der Bot schreibt, ob du ihn selbst gestoppt hast („Bot von dir gestoppt“), ob er das Ziel erreicht hat („Farmen beendet“) oder wegen eines Fehlers abgestürzt ist, wie viel Zeit vergangen ist, wie viele Räume, Etagen und Titanit erreicht wurden, ob es Rückzüge und SOS-Fenster gab. Wenn keine Internetverbindung besteht, versucht der Bot noch zweimal, die Bilanz zu senden (nach 10 und 30 Sekunden) und schaltet sich dann aus. Wie man Telegram verbindet — in einem separaten Abschnitt.

> [!done] Jetzt weißt du, wie du den Bot sanft abbremst, wie du ihn dauerhaft stoppst und welche Taste was tut. Als Nächstes — das Einrichten von Regeln: Wie du dem Bot beibringst, die richtigen Teams aufzustellen. [Nächster Abschnitt →](#7)

## Regelmeister: „Basis und Räume“

„Regelmeister“ ist die zweite Schaltfläche in der linken Leiste (Symbol mit Reglern). Hier erklärst du dem Bot drei Dinge: **wann er stoppen soll**, **was als schlechter Kampf gilt** und **mit welchem Team er jeden Raum betreten soll**. Ein Pack (Team) ist eine Gruppe aus 3–5 Titanen. Die Seite ist oben in drei Registerkarten unterteilt: „Basis und Räume“, „Auto-Taktik und HP“ und „Regeln und Eingriffe“. In diesem Abschnitt geht es um die erste, wichtigste Registerkarte: Ohne sie weiß der Bot nicht einmal, wen er aufstellen soll.

![Registerkarte „Basis und Räume“: oben zwei Karten mit Einstellungen, unten vier Zeilen mit Teams](images/rules_base.png)

Oben — „Sitzungsparameter“ (zwei Karten), darunter — „Teams nach Räumen“. Unten auf der Seite befindet sich auf jeder Registerkarte gleichermaßen eine graue Leiste mit Schaltflächen: „Einstellungen speichern“ und „Wiederherstellen / Zurücksetzen“. Darüber mehr am Ende des Abschnitts. Das Wichtigste, das du dir sofort merken musst: **Solange du nicht auf „Einstellungen speichern“ klickst, ist nichts gespeichert** — keine einzige Änderung erreicht den Bot.

### Karte „Ziele und Limits“

- :target: **„Sitzungsziel“** — wann der Bot beenden soll. Es gibt immer nur **ein** Ziel aus vier Optionen: „Titanit“, „Räume“, „Etagen“ oder „Zeit“ (Zeit in Minuten). Wähle den Typ aus der Liste und trage eine Zahl in das Feld ein. Das Feld akzeptiert nur Ziffern. Die Beschriftung „0 — Ohne Limit“ bedeutet: Null deaktiviert das Ziel und der Bot läuft so lange, bis du ihn stoppst. Der runde Pfeil rechts („Ziel zurücksetzen“) setzt den Wert auf 0.
- :gem: **Titanit zählt der Bot selbst** und liest ihn nicht vom Bildschirm ab: 6 für einen normalen Raum und 12, wenn im Ergebnisfenster ein Symbol „x2“ zu sehen ist. Daher sind „120 Titanit“ etwa 20 Räume ohne „x2“. Solange du die Einstellungen noch nie gespeichert hast, nimmt der Bot automatisch das Ziel „120 Titanit“.
- :layers: **Der Bot bricht eine Etage nicht mittendrin ab.** Wenn er das Ziel „Titanit“, „Räume“ oder „Zeit“ erreicht hat, stoppt er nicht auf der Stelle: Er schreibt ins Protokoll `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.`, absolviert die verbleibenden Räume der Etage und stellt sich vor den Speicherpunkt, ohne auf „Aktivieren“ zu klicken. So bleibt die Etage nicht unvollständig und der Bot holt die Belohnung ab und rechnet die Etage als Erstes beim nächsten Start an. Wird der Speicherpunkt nach 6 Räumen nicht gefunden (auf einer Etage gibt es 5), stoppt der Bot so wie er ist. Das Ziel „Etagen“ wird sofort ausgelöst, sobald der Speicherpunkt passiert wurde.
- :gauge: **Die Zeit läuft auch während der Pause weiter.** Das Ziel „Zeit — 120“ bedeutet 120 Minuten ab dem Klick auf „Farmen starten“, einschließlich aller Pausen.
- :calendar: **„Tageswechsel-Stunde (Ortszeit)“** — wann bei dir ein neuer Spieltag beginnt. Standardmäßig 05:00. Davon hängt ab, welchem Tag die Kämpfe in der Statistik zugeordnet werden, sowie das Gedächtnis des Bots für die Gesundheit der Titanen: Es bleibt innerhalb eines Spieltages erhalten, und an einem neuen Tag beginnt der Bot von vorne. Trage die Stunde ein, nach der du den Tag als neu betrachtest (zum Beispiel, wenn du schlafen gehst).
- :send: **„Telegram einrichten“** — öffnet ein separates Fenster, in dem die Verbindung zum Messenger aktiviert wird. Neben der Schaltfläche befinden sich ein Punkt und eine Beschriftung: grün „SOS-Benachrichtigungen an“ oder grau „Telegram nicht eingerichtet“. Wie man es verbindet, besprechen wir im Abschnitt über Telegram. Hier ist eines wichtig: Die Schaltfläche „Übernehmen“ in diesem Fenster ändert nur diese Seite. Damit die Einstellung in die Datei gelangt, musst du zusätzlich auf „Einstellungen speichern“ klicken.

> [!tip] Welches Ziel sollst du wählen? „Zeit“ ist praktisch, wenn du ein Zeitfenster hast („Lass den Bot eine Stunde arbeiten, während ich das Abendessen koche“). „Titanit“ — wenn du eine bestimmte Menge an Belohnung sammeln musst. „Räume“ und „Etagen“ — wenn du genau eine bestimmte Anzahl schaffen möchtest. Bist du unsicher — lass „Titanit“ und 120 stehen: Das ist ein kurzer Testlauf.

### Karte „Sicherheit und Modus“

Hier wird entschieden, **was ein schlechter Kampf ist**. Der Bot liest die Gesundheit der Titanen im Ergebnisfenster ab und vergleicht zwei Zahlen mit deinen.

- :heart-pulse: **„HP-Panikschwelle, %“** — unter welchem Gesundheitsprozentwert nach dem Kampf der Kampf als schlecht gilt. Standardmäßig 40.
- :swords: **„HP-Verlust-Delta, %“** — wie viel Gesundheit ein einziger Titan in einem Kampf verlieren darf. Standardmäßig 30.

Beide Felder akzeptieren ganze Zahlen von 0 bis 100; wenn du etwas anderes eingibst, färbt sich das Feld rot mit der Beschriftung „Gib eine Zahl von 0 bis 100 ein“, und das Speichern der Einstellungen ist erst möglich, wenn du es korrigierst.

Ein anschauliches Beispiel mit einer Schwelle von 40 und einem Delta von 30:

- Araji ging mit 100 % in den Kampf und kam mit 80 % heraus — **alles gut**: 20 verloren, bleibt über 40.
- Araji ging mit 100 % hinein und kam mit 55 % heraus — **schlechter Kampf**. 55 liegt zwar über der Schwelle, aber es wurden 45 verloren, während 30 zulässig sind.
- Araji ging mit 50 % hinein und kam mit 35 % heraus — **schlechter Kampf**. Nur 15 verloren, aber 35 liegt unter der Panikschwelle.
- Wenn ein Titan stirbt oder im Ergebnisfenster nicht gefunden wurde — immer ein **schlechter Kampf**, egal was du eingestellt hast.

Verluste werden von der Gesundheit aus berechnet, mit der der Titan in den Kampf **eingetreten** ist, und nicht von 100 %. Daher stößt ein verwundeter Titan früher an die Schwelle als ein gesunder. Je höher die Schwelle und je kleiner das Delta, desto strenger ist der Bot und desto öfter ruft er dich; eine Null bei der Schwelle deaktiviert die Prüfung „unter der Schwelle“ (außer für Gefallene), und 100 beim Delta deaktiviert die Verlustprüfung.

> [!note] Schwelle und Delta gelten global für alle Titanen. Für einen einzelnen Titanen kannst du eine eigene Schwelle festlegen und zusätzlich die Regel „wenn drei viel verloren haben — schlechter Kampf“ aktivieren. Dies geschieht auf der benachbarten Registerkarte „Auto-Taktik und HP“.

Darunter befinden sich zwei Schalter:

- :shield-check: **„Bot entscheidet selbst“** („Setzt schlechte Kämpfe zurück und wählt ein Team“) — standardmäßig **ausgeschaltet**. Ausgeschaltet: schlechter Kampf → Fenster „Eingriff erforderlich“, der Bot wartet auf dich. Eingeschaltet: Der Bot setzt den Kampf ohne Nachfragen zurück, spielt ihn mit einem Ersatzteam erneut und wählt auch selbst ein Team basierend auf der Gesundheit der Titanen aus. Ausführlich — im Abschnitt über das autonome Arbeiten des Bots. Aktiviere es, wenn du dem Bot bereits bei der Arbeit zugesehen hast und den Ersatzteams vertraust.
- :swords: **„Manuelle Steuerung von Angus' Ulti“** („Global, in allen Räumen“) — standardmäßig **ausgeschaltet**, sodass jeder Kampf, auch mit Angus, im Auto-Kampf abläuft. Wenn eingeschaltet — drückt der Bot bei Teams mit Angus auf „Kampf“, aktiviert für ein paar Sekunden den Auto-Kampf wegen Angus' Ulti und schaltet ihn wieder aus. Einen solchen Kampf setzt der Bot nicht selbst zurück, sondern ruft dich. Beim Start ist im Protokoll zu sehen, was gewählt wurde: `[ТАКТИКА] Ангус: ...`.

### Teams nach Räumen

Unter der Beschriftung „Das Hauptteam kommt zuerst, Ersatzteams der Reihe nach, wenn ein Kampf schlecht läuft“ befinden sich vier Zeilen — nach Räumen: „Erde“, „Wasser“, „Feuer“ und „Gemischt“. Jede davon ist eine eigene Karte.

- :users: **Hauptteam** — Quadrate der Titanen unter dem Raumnamen. Der Bot stellt dieses auf, sofern kein Grund für ein anderes Vorgehen vorliegt (z. B. eine Regel von der Registerkarte „Regeln und Eingriffe“ wurde ausgelöst). Die Titanen werden von links nach rechts angezeigt, **wie sie auf dem Spielbildschirm stehen**. Gibt es kein Team, steht anstelle der Quadrate die Aufschrift „Pack nicht festgelegt“.
- :pencil: **Bleistift („Team ändern“)** — öffnet das Fenster „Team zusammenstellen“.
- :list: **„Ersatzteams“** mit der Anzahl „N Stk.“ — eine Dropdown-Liste (Pfeil nach unten/oben). Ersatzteams probiert der Bot der Reihe nach aus, wenn der Kampf schlecht verläuft und er selbst entscheidet („Bot entscheidet selbst“ ist aktiviert oder du hast nicht rechtzeitig auf das Fenster geantwortet). In jedem Raum gibt es bis zu 5 davon. Innerhalb ist jedes Ersatzteam eine Zeile `#1`, `#2` und so weiter, und rechts ein Schließkreuz („Team entfernen“). Die Schaltfläche „Team hinzufügen“ öffnet dasselbe Fenster „Team zusammenstellen“.
- :plus: **„Bedingung“** — „+ Bedingung“: ein schneller Weg zu einer Regel für diesen Raum, zum Beispiel „wenn gegen Angus — stelle dieses Team auf“. Es öffnet sich das Fenster „Neue Regel“ mit dem bereits ausgewählten Raum. Wie man es ausfüllt, besprechen wir im Abschnitt über Regeln.

Lege das Hauptteam in allen vier Räumen **vor dem ersten Farmen** fest: Der Bot kennt deine Titanen selbst nicht und verfügt von Haus aus über keine Teams.

So stellst du ein Team zusammen:

1. **Klicke auf den Bleistift** im gewünschten Raum. Es öffnet sich das Fenster „Team zusammenstellen“.
2. **Klicke auf die Titanen**, die du aufstellen möchtest. Erneutes Klicken entfernt sie wieder. Oben steht die Anzahl: „Gewählt: 3 / 5“ und der Hinweis „Bereit“ (bei zwei steht dort „Mindestens 3 · noch 1 nötig“).
3. **Beachte das Element des Raums.** In „Erde“, „Wasser“ und „Feuer“ passen nur Titanen dieses Elements, in „Gemischt“ hingegen alle, zusammen mit Metis (sie ist „Elarith“ und betritt keine anderen Räume: „Metis — nur im gemischten Raum“). Wenn 5 gewählt wurden, werden die restlichen Titanen gesperrt.
4. **Klicke auf „Übernehmen“** (oder „Abbrechen“, wenn du es dir anders überlegt hast; „Leeren“ entfernt alle Titanen auf einmal).

![Fenster „Team zusammenstellen“ für den Raum „Wasser“: drei Titanen ausgewählt, unten „Übernehmen“](images/rules_picker.png)

> [!warning] „Übernehmen“ im Fenster „Team zusammenstellen“ ändert nur die Seite: Das Team ist vorerst **nicht** in der Datei gespeichert. Es wird erst gespeichert, wenn du auf „Einstellungen speichern“ klickst. Das Hauptteam jedes Raums befindet sich in der Datei `bot_data/rules/<стихия>.yml`, Ersatzteams und alle Zahlen in `profile.yml`. Diese Dateien musst du nicht manuell bearbeiten.

Ein Ersatzteam, das bereits in der Liste vorhanden ist (in beliebiger Titanenreihenfolge), kann kein zweites Mal hinzugefügt werden: Es erscheint der Hinweis „Dieses Ersatzteam gibt es schon“.

> [!tip] Welche Teams sollst du als Ersatz aufstellen? Gib dem Bot die Wahl: Das Ersatzteam sollte sich vom Hauptteam um mindestens ein paar Titanen unterscheiden. Wenn Araji bei dir den Kampf oft verwundet verlässt, stelle im Ersatzteam diejenigen auf, die mehr Einsteckvermögen haben.

### Speichern und „Wiederherstellen / Zurücksetzen“

Die untere Leiste zeigt den Status an: „Alle Änderungen gespeichert“ (grünes Häkchen) oder „Ungespeicherte Änderungen“ (gelbes Symbol). Während der Bot arbeitet, steht daneben „Der Bot übernimmt die neuen Einstellungen beim nächsten Start“.

- :save: **„Einstellungen speichern“** speichert nur das, was du geändert hast, und zeigt den Hinweis „Einstellungen gespeichert“. Solange die Schaltfläche nicht gedrückt wurde, weiß der Bot nichts von deinen Änderungen. Im Protokoll erscheint `[GUI] Профиль настроек сохранен!`.
- :rotate-ccw: **„Wiederherstellen / Zurücksetzen“** — eine rote Schaltfläche; sie fragt zuerst „Einstellungen wiederherstellen?“. Die Einstellungen werden auf die **zuletzt gespeicherten** zurückgesetzt (Kopie `bot_data/profile.yml.bak`). Wenn keine Kopie vorhanden ist, wird `profile.yml` gelöscht und der Bot übernimmt die Standardwerte. Ungespeicherte Änderungen gehen verloren. Die Hauptteams und Regeln in den Dateien `bot_data/rules` rührt diese Schaltfläche nicht an, das Formular der Seite liest sie jedoch erneut von der Festplatte ab.
- :triangle-alert: **Wenn du die Seite mit ungespeicherten Änderungen verlässt** (in einen anderen Abschnitt oder über das Schließkreuz des Fensters), erscheint „Änderungen speichern?“ mit den Schaltflächen „Speichern“, „Nicht speichern“ und „Abbrechen“.

Der Bot liest die Einstellungen **ein einziges Mal, wenn du auf „Farmen starten“ klickst**. Du kannst sie während des Betriebs ändern, sie werden jedoch erst nach einem Stopp und einem erneuten Start wirksam. Selbst „Pause“ und „Fortsetzen“ aktualisieren sie nicht. Die Karte „Starteinstellungen“ auf der Hauptseite zeigt genau die Einstellungen an, mit denen der Bot gerade arbeitet.

> [!warning] Wenn die Datei `profile.yml` beschädigt ist, erscheint oben im Protokoll der Hauptseite `[ОШИБКА] Файл profile.yml поврежден!`, auf der Seite werden Standardwerte angezeigt und „Einstellungen speichern“ verweigert das Schreiben („profile.yml ist beschädigt — Einstellungen nicht gespeichert“). Klicke auf „Wiederherstellen / Zurücksetzen“.

> [!done] Jetzt weißt du, wie du das Ziel, die Schwellenwerte und die Teams für jeden Raum festlegst. Als Nächstes — die Registerkarte „Auto-Taktik und HP“: die Reihenfolge der Türen und wie der Bot Titanen heilt und wechselt. [Nächster Abschnitt →](#8)

## Regel-Assistent: „Auto-Taktik und HP“

Der zweite Reiter des „Regel-Assistenten“. Auf dem ersten („Basis und Räume“) hast du die Teams und allgemeinen Schwellen festgelegt. Hier erklärst du dem Bot, **wie er sich verhalten soll, wenn etwas schiefgeht**: welche Tür er zuerst betreten soll, was als schlechter Kampf gilt, wie oft er ein Ersatzteam versuchen soll, wie lange er auf dich warten soll und wie verletzte Titanen geheilt werden. Alle Felder sind bereits mit vernünftigen Werten vorausgefüllt, sodass der Bot auch ohne deine Änderungen funktioniert. Ändere sie, wenn du merkst, dass er sich nicht so verhält, wie du es möchtest.

![Reiter „Auto-Taktik und HP“: Info-Leiste oben, vier Türen, zwei Karten nebeneinander und persönliche Schwellen unten](images/tactics_tab.png)

Wie auf dem ersten Reiter **wird nichts gespeichert, bis du auf „Einstellungen speichern“ klickst**, und der Bot liest die Einstellungen einmalig beim Klick auf „Farmen starten“ ein. Wenn du während des Farmens etwas änderst, wird es erst nach einem Stopp und Neustart wirksam.

### Blaue Info-Leiste oben

Sie fasst kurz zusammen, was der Bot bei einem schlechten Kampf tut: Er bricht ihn ab, wiederholt ihn mit einem Ersatzteam und merkt sich ein erfolgreiches Team in einer Regel.

Wenn auf dem ersten Reiter der Schalter „Der Bot entscheidet“ ausgeschaltet ist, wird der Leiste ein weiterer Satz hinzugefügt. Er ist wichtig, deshalb gehen wir separat darauf ein. **Ohne „Der Bot entscheidet“ funktionieren zwei Dinge nicht: Ersatzteams und das Heilteam.** Alles andere auf diesem Reiter funktioniert immer:

- :door-open: Türreihenfolge;
- :gauge: Warten auf deine Antwort im SOS-Fenster (das Fenster, in dem dich der Bot ruft, wenn ein Kampf schlecht ist);
- :triangle-alert: Kriterien für schlechte Kämpfe;
- :heart-pulse: persönliche Panikschwellen.

### „Türreihenfolge“

Im Korridor sieht der Bot oft mehrere Türen auf einmal: eine pro Element („Wasser“, „Erde“, „Feuer“) oder „Gemischt“. Im Raum warten Feinde auf dich, und für jedes Element gibt es ein eigenes Team. Die Reihenfolge bestimmt, **welche Tür der Bot zuerst öffnet**. Standardmäßig ist das: „Wasser“, „Gemischt“, „Erde“, „Feuer“.

Vier Plätze verlaufen von links nach rechts, dazwischen Pfeile; jeder Platz trägt eine Nummer von 1 bis 4. Klicke auf einen Platz und wähle ein Element. Es gibt keine Duplikate: Wenn du ein Element wählst, das bereits an einem anderen Platz steht, **tauschen sie einfach die Plätze**. Beispiel: Es war „Wasser, Gemischt, Erde, Feuer“, du wählst an erster Stelle „Feuer“ — es wird zu „Feuer, Gemischt, Erde, Wasser“.

Zwei Vorbehalte, damit du dich im Spiel nicht wunderst:

- Wenn eine Tür **durch eine „Skip“-Regel verboten ist** (mehr dazu im Abschnitt „Regeln und Eingriffe“), überspringt der Bot sie, selbst wenn sie in der Reihenfolge an erster Stelle steht. Sind alle Türen verboten, nimmt er die erste laut Reihenfolge.
- Wenn „Der Bot entscheidet“ aktiviert ist, wählt der Bot manchmal **von selbst eine andere Tür**, nicht nach der Reihenfolge: dorthin, wo die Heilung für einen verletzten Titanen greift, oder um eine für Verletzte gefährliche Tür zu umgehen. Eine solche Wahl wird im Protokoll mit der Zeile `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...` angezeigt.

### Karte „Kriterien für schlechte Kämpfe und SOS“

- :swords: **„Ersatzteams pro Raum probieren“** — wie oft der Bot pro Raum selbst einen Kampf abbrechen und mit einem anderen Team neu spielen darf. Von 1 bis 3, Standard ist 2. Wenn alle Versuche aufgebraucht sind und der Kampf immer noch schlecht ist, ruft dich der Bot. Aufrufe funktionieren nur bei „Der Bot entscheidet“. Mehr als drei sind nicht möglich: Es macht keinen Sinn, denselben Kampf zehnmal zu wiederholen, und jeder Versuch kostet Zeit.
- :gauge: **„SOS-Fenster ohne Antwort, Zeitlimit in Min“** — wie viele Minuten der Bot wartet, bis du auf das Fenster „Eingriff erforderlich“ antwortest, bevor er selbst entscheidet. Von 0 bis 60, Standard ist 10. Der Hinweis unter dem Feld lautet „0 — immer warten“: **Null bedeutet „immer warten“**, der Bot bleibt stehen und wartet auf dich, wenn nötig bis zum Morgen. Das funktioniert auch **ohne** „Der Bot entscheidet“. Was genau der Bot selbst entscheidet (Kampf abbrechen, annehmen oder pausieren), steht im Abschnitt über SOS-Fenster.
- :users: **„Kampf gilt als schlecht, wenn“** — Gesamtverluste des Teams: „Titanen ≥ 3“ und „verloren ≥ 40“ „% HP je Titan“. Diese Prüfung erfasst den Fall, dass **jeder Einzelne sich zwar hält**, das Team insgesamt aber „einbricht“. Haben drei Titanen jeweils 40 % oder mehr verloren, ist der Kampf schlecht, selbst wenn keiner unter die Panikschwelle gefallen ist. Der Hinweis „0 Titanen — nicht prüfen“ bedeutet: Trage in das erste Feld 0 ein, um die Prüfung zu deaktivieren. Das erste Feld geht von 0 bis 5, das zweite von 0 bis 100.

Anschauliches Beispiel. Team: Araji, Hyperion, Rigel, Iyari, Lumira. Nach dem Kampf hat Araji 45 %, Rigel 42 %, Iyari 40 % und die restlichen jeweils 10 % verloren. Drei haben „40 und mehr“ verloren — der Kampf ist schlecht, selbst wenn jeder einzelne noch über seiner Panikschwelle liegt. Hätte Iyari nur 35 % verloren, wären es nur zwei gewesen, und die Gesamtprüfung hätte nichts zu beanstanden.

> [!note] Die übrigen Merkmale eines schlechten Kampfes — Panikschwelle und Verlusttoleranz — befinden sich auf dem ersten Reiter „Basis und Räume“. Ein Kampf ist schlecht, wenn **mindestens ein** Merkmal zutrifft: Jemand ist gestorben oder im Fenster nicht gefunden worden, jemand hat HP unter der Schwelle, jemand hat mehr als erlaubt verloren oder die Gesamtverlustprüfung hat angesprochen.

Wenn du eine falsche Zahl eingegeben hast (Buchstabe oder Zahl außerhalb der Grenzen), wird das Feld rot hervorgehoben, darunter erscheint „Zahl von … bis …“ und das Speichern der Einstellungen ist erst möglich, wenn du es korrigierst.

### Karte „Auto-Heilteam im gemischten Raum“

Oft passiert Folgendes: Ein Titan steckt ein paar Kämpfe hintereinander Treffer ein und läuft mit halber Gesundheit herum. Früher oder später fällt er unter die Schwelle und der Kampf wird schlecht. „Heilung“ bedeutet, dass der Bot **selbst ein spezielles Team zusammenstellt**, damit der Verletzte geheilt wird (ein Heiler wird hineingesetzt, der die Gesundheit des Verletzten wieder anhebt). Ein solches Team stellt der Bot nur für den „Gemischt“-Raum zusammen, da dort beliebige Titanen eingesetzt werden können.

Das funktioniert nur bei „Der Bot entscheidet“ und nur, wenn deine eigene Heilregel nicht gegriffen hat (eine Regel ist stärker).

- :heart-pulse: **„Titan heilen, wenn HP unter, %“** — Standard ist 60. Ein Titan, der gesünder als diese Zahl ist, gilt als gesund. **0 deaktiviert** das Heilteam komplett. Es gibt jedoch eine Untergrenze: Liegt die HP eines Titans bereits **unter der Panikschwelle**, kann er im „Gemischt“-Raum nicht geheilt werden und der Bot rührt ihn nicht an.
- :users: **„Wen für den Verletzten aus dem Team nehmen“** — drei Plätze mit Pfeilen. Wenn ein Verletzter eingesetzt werden muss und kein Platz im Team frei ist, muss jemand weichen. Klicke auf den Platz und wähle einen Titanen: Die Liste ist nach Elementen in Spalten unterteilt. **„— automatisch —“** (so ist es standardmäßig eingestellt) bedeutet: Der Bot entfernt vom Ende des Teams, lässt aber **Heiler unangetastet**. Für das Team „Hyperion, Rigel, Iyari, Lumira, Amon“ wären das Amon, dann Lumira. Wählst du einen Titanen, der bereits an einem anderen Platz steht, tauschen sie die Plätze.

Wie der Bot heilt, kurz und einfach erklärt:

1. Er prüft, wer HP unter 60 %, aber über der Panikschwelle hat und wer von ihnen nicht durch „Skip“-Regeln verboten ist.
2. Er heilt **einen nach dem anderen**, beginnend mit demjenigen, der seiner Schwelle am nächsten ist. Zuerst die Haupttitanen (aus den Basisteams), dann die Ersatztitanen.
3. Ist der Verletzte noch nicht im Team, nimmt er den Platz des entfernten Titans ein. Titanen, die ohnehin in ihrem „eigenen“ Raum geheilt werden (Wasser- und Erdtitanen: in ihrem Basisteam gibt es einen Heiler), zieht der Bot jedoch nicht in den „Gemischt“-Raum, es sei denn, sie steigen dort zwei Kämpfe hintereinander nicht über die Schwelle. Feuer-Titanen können in ihrem „eigenen“ Raum nicht geheilt werden, daher wird für sie die Heilung sofort aktiviert.
4. Ist der Verletzte bereits im Team, steigt aber zwei Kämpfe hintereinander nicht auf, tritt an die Stelle des entfernten Titans ein **gesunder und aufgeladener Heiler** (HP ab 80 %, Energie ab 60 %).
5. Ein Team wird nicht genommen, wenn kein Heiler mehr darin ist, es gegen diese Gegner verliert, für Verletzte gefährlich ist oder einen manuellen Kampf erfordert (Angus).

Warum ist der Bot so vorsichtig? Er wird niemanden heilen, den du nirgendwo angegeben hast: Einen Titanen, der nicht in deinen Teams und Regeln vorkommt, setzt der Bot nicht von selbst ein. Wenn das Zusammenstellen des Teams fehlschlägt (der Titan konnte nicht in den Slot gesetzt werden), hält der Bot nicht an, sondern setzt ein normales Team ein und **heilt diesen Titanen bis zum Ende des Durchlaufs nicht mehr**.

Im Protokoll ist dies an den Zeilen `[ТАКТИКА] Пак отхила (бот собрал сам): ...` und `[ТАКТИКА] Отхил: ...` zu erkennen (warum der Verletzte nicht geheilt wird).

### Karte „Persönliche Panikschwellen der Titanen, % HP“

Die allgemeine Panikschwelle (standardmäßig 40) gilt für alle. Es gibt jedoch Titanen, bei denen ein früher Verlust besonders schmerzhaft ist, und solche, die eine niedrige HP problemlos verkraften. Für sie kannst du eine **eigene Schwelle** festlegen.

- Unten steht der Hinweis „Andere Titanen: gemeinsame Schwelle 40%“ (die Zahl stammt vom ersten Reiter). Solange keine persönlichen Schwellen vorhanden sind, steht dort „Keine persönlichen Schwellen — alle Titanen nutzen die gemeinsame“.
- Klicke auf „Persönliche Schwelle für einen Titan festlegen“. Es öffnet sich ein kleines Fenster „Persönliche Panikschwelle“: Wähle einen Titanen aus der Liste und trage eine Zahl von 0 bis 100 ein. Klicke auf „Übernehmen“. Das Fenster zeigt „Gemeinsame Schwelle — 40%“, damit du einen Vergleichswert hast. In der Liste stehen nur Titanen, die noch keine persönliche Schwelle haben.
- Jede festgelegte Schwelle ist eine Kachel mit dem Titanen und einer gelben Zahl. Klicke auf die Kachel, um die Schwelle zu ändern (der Titan kann nicht geändert werden; er müsste entfernt und neu hinzugefügt werden). Das **Kreuzchen** auf der Kachel entfernt die Schwelle, und der Titan nutzt wieder die gemeinsame Schwelle.

Ein Kampf ist schlecht, wenn die HP dieses Titans nach dem Kampf **unter seiner persönlichen Schwelle** liegt. Beispiel: Die allgemeine Schwelle ist 40, für Rigel ist jedoch 60 eingestellt. Rigel beendet den Kampf mit 55 % — der Kampf ist schlecht, obwohl 55 % für die anderen normal wären.

> [!tip] Womit anfangen? Ändere nichts, bis du ein paar Dutzend Räume gesehen hast. Wenn du bemerkst, dass dich der Bot wegen desselben Titans ruft, stelle seine persönliche Schwelle etwas niedriger ein. Wenn der Bot zu oft das Team wechselt, um zu heilen, **verringere** die Zahl bei „Titan heilen, wenn HP unter, %“. Wenn du überhaupt nicht möchtest, dass er heilt, trage 0 ein.

> [!warning] Wenn du das „SOS-Fenster ohne Antwort, Zeitlimit in Min“ auf 0 gestellt hast und schlafen gehst, und der Bot dich am Fenster ruft, wird er bis zum Morgen warten. Lass besser 10–15 Minuten eingestellt und richte Telegram ein: So erfährst du sofort von dem Problem, und falls du es nicht rechtzeitig schaffst, entscheidet der Bot selbst.

> [!done] Jetzt weißt du, wie du die Türreihenfolge festlegst, was als schlechter Kampf gilt und wie der Bot verletzte Titanen heilt. Als Nächstes folgen Telegram und die Fenster, die dich um Hilfe rufen. [Nächster Abschnitt →](#9)

## Regel-Assistent: «Regeln und Eingriffe»

Der dritte Reiter des Regel-Assistenten. Auf dem ersten hast du das **Hauptteam** für jeden Raum festgelegt, auf dem zweiten — wie sich der Bot im Notfall verhält. Hier bringst du ihm **Ausnahmen** bei: „Setze normalerweise das Hauptteam ein, aber wenn das hier passiert — mach es anders“. Jede solche Ausnahme wird als **Regel** bezeichnet. Und ein „Eingriff“ bedeutet, dass eine Regel die Teamauswahl vom Hauptteam übernimmt und ihr eigenes Team einsetzt.

Eine Regel liest sich immer gleich: **„wenn [Bedingung] — dann [Aktion]“**. Zum Beispiel:

- :heart-pulse: „Wenn Arajis HP unter 50 % liegen — setze ein Team mit dem Heiler Sigurd ein“.
- :swords: „Wenn im Raum Angus, Sylva und Verdok sind — setze dieses Team ein“.
- :door-open: „Wenn Arajis HP unter 30 % liegen — betritt nicht ‚Feuer‘“.
- :users: „Wenn im Raum Angus, Avalon und Eden sind — halte an und frage mich“.

![Reiter «Regeln und Eingriffe»: Elementfilter, Regelliste mit Symbolen, Teams und Schaltern](images/rules_intercepts.png)

Jedes Element hat seine eigenen Regeln: „Erde“, „Wasser“, „Feuer“ und „Gemischt“ haben getrennte Listen. Wenn der Bot eine „Feuer“-Tür betritt, prüft er nur die „Feuer“-Regeln. Wie auf den anderen Reitern gilt: **Nichts ist gespeichert, bis du auf „Einstellungen speichern“ klickst**, und der Bot liest die Regeln nur einmal beim Klick auf „Farmen starten“.

> [!note] Viele Regeln musst du gar nicht selbst schreiben. Wenn „Der Bot entscheidet“ aktiviert ist, merkt sich der Bot **selbst** erfolgreiche Teams nach einem Rückzug und fügt selbst „Goldene Regeln“ hinzu. Sie erscheinen in derselben Liste (mehr dazu unten). Eigene Regeln sind nötig, wenn du bereits weißt, dass „man das so nicht machen sollte“ oder „in so einer Situation genau dieses Team benötigt wird“.

### Welche Arten von Regeln gibt es

Eine Regel hat eine von drei Bedingungen und eine von drei Aktionen. Zusammen ergeben sie die gewohnten Arten:

- :heart-pulse: **Rettung nach HP oder Energie.** Bedingung — „HP (oder Energie) dieses Titanen unter N%“, Aktion — ein anderes Team einsetzen. In der Liste ist das Symbol **«HEILUNG»** (nach HP) oder **«ENERGIE»**. So funktioniert die Heilung: Wenn ein Titan verletzt ist, wird ein Team mit einem Heiler eingesetzt.
- :swords: **Gegen diese Gegner.** Bedingung — „im Raum befinden sich alle diese Gegner“, Aktion — ein eigenes Team einsetzen. Symbol **«GEGNER»**. Man kann aus 13 Gegnern wählen, die der Bot im Titanendungeon erkennt.
- :door-open: **«Skip» — Verbot.** Bedingung — „HP oder Energie des Titanen unter N%“, Aktion — diesen Titanen nicht einsetzen und diesen Raum nicht betreten. Symbol **«SKIP»**, rechts der Hinweis „Raum überspringen“.
- :users: **«Dich fragen».** Beliebige Bedingung, die Aktion ist jedoch, nicht selbst zu entscheiden, sondern dich zu rufen. Rechts steht der Hinweis **«Dich fragen»**, und das Symbol hängt von der Bedingung ab („HP“, „ENERGIE“, „GEGNER“). Wenn sie auslöst, öffnet der Bot das Fenster „Kein passendes Pack“ und wartet auf deine Antwort. Wenn du nicht innerhalb der in „Auto-Taktik“ festgelegten Zeit antwortest, entscheidet er selbst.

Das Symbol „HP“ (und nicht „HEILUNG“) bedeutet, dass die Bedingung nach HP ist, die Aktion jedoch „Dich fragen“ lautet. Wenn gar keine Bedingung vorhanden ist, gibt es kein Symbol und unter dem Namen steht „Keine Bedingung — die Regel greift nie“.

Nun zu „Skip“, da es zwei Aufgaben gleichzeitig hat. Beispiel: In „Feuer“ existiert die Regel „Araji, HP unter 30%“.

1. **Tür.** Solange Araji weniger als 30 % hat, geht der Bot nicht in „Feuer“ und wählt eine andere Tür. Sind alle Türen verboten, nimmt der Bot die erste in der Reihenfolge.
2. **«Schwarze Liste».** In diesem Raum wird Araji nicht eingesetzt: Jedes Team, in dem er enthalten ist, verwirft der Bot und nimmt das nächste. Wenn auch das **Hauptteam** den verbotenen Titanen enthält, gibt es nichts einzusetzen — der Bot hält an und öffnet das Fenster „Kein passendes Pack“.

> [!warning] „Skip“ kann nicht nach Gegnern erstellt werden. Der Bot erfährt erst von den Gegnern, **nachdem** er die Tür betreten hat, daher kann er die Tür nicht anhand der Gegner auswählen. Im Regel-Fenster für „Nach Gegnern“ ist das Kontrollkästchen „Skip“ nicht verfügbar. Möchtest du einen Raum mit bestimmten Gegnern umgehen, erstelle eine Regel „Dich fragen“, damit die Entscheidung bei dir liegt.

### In welcher Reihenfolge der Bot die Regeln prüft

Wenn ein Kampf beginnt, geht der Bot die Regeln des Raums **in dieser Reihenfolge** durch:

1. **«Skip».** Zuerst erstellt der Bot eine „schwarze Liste“ von Titanen: wer durch eine ausgelöste „Skip“-Regel verboten wurde. Ein Team mit einem solchen Titanen passt nicht, selbst wenn eine andere Regel es selbst anfordert (das nennt man Veto: Das Verbot ist stärker als jede Regel).
2. **Rettung.** Regeln, bei denen die Bedingung die HP oder Energie eines Titanen enthält. Dazu gehören auch Regeln wie „gegen Gegner bei Araji < 50% HP“ (Gegner plus HP): Sie werden sofort hier geprüft, **vor** den normalen Regeln bezüglich Gegnern.
3. **Gegen Gegner.** Regeln, bei denen in der Bedingung nur Gegner stehen.
4. **Hauptteam** des Raums — wenn nichts gepasst hat.

Innerhalb jeder Gruppe geht der Bot von **oben nach unten** vor und nimmt die erste Regel, die auslöst. Deshalb werden die Pfeile benötigt: Wenn zwei Regeln für Gegner gleichzeitig passen, gewinnt diejenige, die weiter oben steht. Eine „Rettung“-Regel ist jedoch immer stärker als „Gegen Gegner“, egal wo sie in der Liste stehen. **Deaktivierte** Regeln nehmen an der Prüfung nicht teil.

Die Bedingungen werden mit dem verglichen, was der Bot über deine Titanen weiß (HP und Energie übernimmt er vom Teamauswahl-Bildschirm und nach den Kämpfen). Wenn der Bot die Gesundheit eines Titanen noch nicht gesehen hat, nimmt er an, dass sie voll ist, und die Regel „unter N%“ löst nicht aus. Wenn eine Bedingung mehrere Titanen enthält (was bei Regeln vorkommt, die sich der Bot selbst gemerkt hat), müssen **alle** Bedingungen gleichzeitig erfüllt sein. Bei Gegnern ist es genauso: Die Regel löst nur aus, wenn **alle** aufgeführten Gegner im Raum vorhanden sind.

### Die Regelliste: Was in einer Zeile steht

Oben — „Aktive Regeln“ und ein grauer Hinweis mit der Anzahl der Regeln, rechts der Hinweis: „Wähle ein Element, um die Reihenfolge zu ändern“ (wenn alle angezeigt werden) oder „Die Regel weiter oben wird zuerst geprüft“ (wenn ein Element gewählt ist). Darunter die Filter-Schaltflächen „Alle“, „Erde“, „Wasser“, „Feuer“, „Gemischt“ und die Schaltfläche „Neue Regel“. Darunter die Spaltenüberschriften „Nr.“, „Bedingung“, „Aktion“, „An“.

In jeder Zeile von links nach rechts:

- **Nummer** — der Platz in der Liste des jeweiligen Elements. Je kleiner die Nummer, desto früher wird die Regel geprüft. Wenn **ein** Element ausgewählt ist, erscheinen neben der Nummer die Pfeile „Nach oben“ und „Nach unten“. Ist „Alle“ gewählt, gibt es keine Pfeile: Die Elemente werden nacheinander angezeigt und konkurrieren nicht miteinander.
- **Symbole** — das Element des Raums und der Regeltyp („HEILUNG“, „HP“, „ENERGIE“, „GEGNER“, „SKIP“).
- **Name** und die graue Zeile darunter — die Bedingung in Worten, zum Beispiel „Araji: HP unter 50%“ oder „Gegner im Raum: Angus, Sylva“.
- **Aktion** — Pfeil und Quadrate der Team-Titanen (von links nach rechts, wie im Spiel) mit der Beschriftung „Packwechsel“. Oder der Hinweis „Dich fragen“ / „Raum überspringen“.
- **Schalter «An»** — Regel ein- oder ausschalten.
- **Stift** „Bearbeiten“ und **Kreuzchen** „Löschen“.

Wenn keine Regeln vorhanden sind, steht anstelle der Liste: „Keine Regeln vorhanden. Klicke auf ‚Neue Regel‘ — oder der Bot merkt sich nach einem Rückzug selbst eine Regel.“

### Schalter, Pfeile, Kreuzchen und «Leeren»

- :check: **Schalter.** Eine ausgeschaltete Regel wird ausgegraut, **bleibt aber in der Liste**, und der Bot überspringt sie einfach. Das ist der beste Weg, um „eine Regel vorübergehend zu entfernen“: Du musst das Team nicht neu zusammenstellen. Beim Start erscheint im Log die Zeile `[ПРАВИЛА] Выключено правил: N, бот их пропускает.`
- :chevron-up: **Die Pfeile „Nach oben“ und „Nach unten“** tauschen die Plätze der Regel mit der benachbarten. Sie werden benötigt, wenn zwei Regeln derselben Gruppe gleichzeitig passen könnten und es wichtig ist, welche zuerst geprüft wird.
- :x: **Kreuzchen „Löschen“.** Unten erscheint der Hinweis „Regel ‚…‘ gelöscht“ mit der Schaltfläche **«Rückgängig»**. Solange der Hinweis auf dem Bildschirm zu sehen ist, kann die Regel an derselben Stelle wiederhergestellt werden.
- :trash-2: **«Alle Regeln löschen»** löscht nur das, was **aktuell sichtbar ist**. Ist „Wasser“ ausgewählt, werden die Wasser-Regeln gelöscht; ist „Alle“ ausgewählt, werden alle gelöscht. Zuerst fragt der Bot nach: „Alle Regeln löschen?“ und gibt an, wie viele und welche (Schaltfläche „Alle löschen“). Danach erscheint ebenfalls der Hinweis „Gelöschte Regeln: N“ mit der Schaltfläche „Rückgängig“.

Alle diese Aktionen ändern nur die Seite. In die Dateien gelangen sie erst nach „Einstellungen speichern“, wobei **nur die Elemente gespeichert werden, bei denen sich etwas geändert hat**. Wenn du die Seite verlässt, ohne zu speichern, fragt das Fenster „Änderungen speichern?“.

> [!tip] Wenn du dir unsicher bist, ob du eine Regel löschen sollst oder nicht, schalte sie lieber mit dem Schalter aus. Bei Regeln, die sich der Bot selbst gemerkt hat, gibt es noch einen Grund (siehe unten): Eine ausgeschaltete Regel fasst der Bot nicht an und erstellt sie nicht neu, eine gelöschte kann jedoch wieder erscheinen.

### Das Fenster «Neue Regel» Schritt für Schritt

Klicke auf „Neue Regel“ (oder die Schaltfläche „Bedingung“ auf dem ersten Reiter unten auf der Raum-Karte). Ein Fenster öffnet sich. Wenn ein Element ausgewählt ist, wird dieses sofort vorgeschlagen. Der Stift in der Zeile öffnet dasselbe Fenster mit dem Titel „Regel bearbeiten“.

![Fenster «Neue Regel»: Element und Name, drei Auslöser, Bedingungsfelder, Aktion und Team](images/rule_editor.png)

1. **Wähle das Element im Feld «Element des Raums».** Die Regel wird nur dort funktionieren. Vom Element hängt ab, welche Titanen ausgewählt werden können: in „Erde“ nur Erd-Titanen, in „Wasser“ nur Wasser-Titanen und in „Gemischt“ alle. Wenn du das Element später änderst, passt das Fenster die Auswahl selbstständig an.
2. **Benenne die Regel (optional).** Das Feld „Name der Regel“ kann leer gelassen werden: Dann wird der Name aus der Bedingung zusammengestellt, zum Beispiel „Araji: HP unter 50%“. Diesen Namen schreibt der Bot später ins Log, wenn die Regel ausgelöst hat.
3. **Wähle den «Auslöser»** — worauf der Bot achten soll: „Nach HP“, „Nach Energie“ oder „Nach Gegnern“.
   - „Nach HP“ und „Nach Energie“: Wähle **«Titan»** und trage eine Zahl in das Feld „HP unter, %“ (oder „Energie unter, %“) von 0 bis 100 ein. Standardmäßig gilt für HP 35, für Energie 100. Wenn keine Zahl oder eine Zahl außerhalb der Grenzen eingegeben wird, wird das Feld rot und darunter erscheint „Eine Zahl von 0 bis 100“.
   - „Nach Gegnern“: Markiere im Raster „Gefährliche Gegner im Raum“ alle, die **zusammen** auftreten müssen. Daneben steht „· gewählt: N“. Wenn niemand ausgewählt ist, kann nicht gespeichert werden.
4. **Wähle die «Aktion beim Auslösen».** Es gibt zwei Kontrollkästchen, die sich gegenseitig ausschließen: „Anhalten und mich fragen“ und „Betreten des Raums verbieten (Skip)“. Wenn keines aktiviert ist, wird die Regel **ein Team einsetzen**.
5. **Einlaufzeit für Titanen verlangen (optional).** Die Regel löst nur aus, wenn die ausgewählten Titanen (1 bis 5, aus beliebigen Elementen) in diesem Durchlauf bereits gekämpft haben. Zum Beispiel verlangt das Team nach Sigurd, du möchtest ihn aber erst einsetzen, wenn er überhaupt schon gekämpft hat. Das Kreuzchen daneben entfernt die Einlaufzeit. Eine Einlaufzeit gibt es nur bei Regeln, die ein Team einsetzen. Nach einer weichen Pause und einem manuellen Kampf vergisst der Bot den Status der Titanen und die Einlaufzeit beginnt von vorn.
6. **Wähle das «Team für diese Regel».** Klicke auf „Team wählen“ und wähle im Fenster „Team zusammenstellen“ **3 bis 5 Titanen** (genauso wie für das Hauptteam). Für „Dich fragen“ und „Skip“ ist kein Team erforderlich; dort steht „Für diese Aktion ist kein Team nötig“.
7. **Klicke auf «Regel speichern».** Solange die Schaltfläche grau ist, steht unten im Fenster, was fehlt: „Wähle ein Team: 3 bis 5 Titanen“, „Wähle mindestens einen Gegner“ oder „Korrigiere die Zahl: 0 bis 100“. „Abbrechen“ schließt das Fenster ohne Änderungen.

Eine neue Regel wird an der **ersten Stelle** ihres Elements platziert; eine geänderte Regel bleibt an ihrer bisherigen Stelle (wenn du das Element geändert hast, geht sie an die erste Stelle im neuen Element). In die Datei gelangt sie wie alles andere erst nach „Einstellungen speichern“. Wenn du das Fenster mit der Schaltfläche „Bedingung“ vom ersten Reiter geöffnet hast, erscheint nach dem Speichern der Hinweis „Regel ‚…‘ wurde zum Reiter ‚Regeln und Eingriffe‘ hinzugefügt“.

> [!note] Eine Regel, die sich der Bot selbst gemerkt hat, kann mit dem Stift geöffnet und bearbeitet werden. Alles, was im Fenster nicht sichtbar ist (zum Beispiel die „Verlusttoleranz“ oder eine zusätzliche HP-Bedingung), **bleibt unverändert erhalten**. Diese Bedingung zeigt das Fenster als graue Zeile „Weiterhin in der Bedingung (bleibt unverändert): …“.

### Regeln, die sich der Bot selbst gemerkt hat

Wenn „Der Bot entscheidet“ aktiviert ist, erscheinen in der Liste Regeln, die nicht von dir verfasst wurden. Du erkennst sie am Namen:

- :refresh-cw: **«Auto: Angus + Sylva im Raum»** — der Bot hat einen schlechten Kampf zurückgesetzt, mit einem anderen Team erneut gespielt und dieses hat es geschafft. Der Bot hat sich gemerkt: „gegen diese Gegner dieses Team einsetzen“. Unter dem Namen steht „Vom Bot nach einem Rückzug gemerkt“ (oder „Dein Pack nach einem Rückzug, vom Bot gemerkt“, wenn du das Team im SOS-Fenster ausgewählt hast). Wenn das Team laut Bedingung verloren hat (zum Beispiel „Araji unter 50%“), wird dies der Bedingung hinzugefügt. Eine solche Regel wird an erster Stelle platziert.
- :star: **«Gold: Angus + Sylva im Raum»** — „Das Pack hat diese Gegner oft besiegt“. Beim Start sieht sich der Bot den Verlauf an und nimmt ein Team, das gegen diese Gegneraufstellung **5 Kämpfe oder mehr** bestritten und **80 % oder mehr** gewonnen hat. Das Hauptteam, die Teams von Rettungsregeln und deine Ersatzteams fallen nicht unter die „Goldenen“.

In der Datei heißen diese Regeln anders („Anti-Team gegen: …“, „Goldene Regel gegen: …“), und genau so werden sie im Log geschrieben: `[ОБУЧЕНИЕ] Новое правило '…': пак […]. Сохранено на 1-е место.` Das Fenster zeigt sie einfach kurz und verständlich an. Wenn du die Regel umbenennst, siehst du deinen eingegebenen Namen.

Was gut über diese Regeln zu wissen ist:

- **Der Bot erzeugt keine Duplikate.** Eine Regel mit derselben Bedingung wird kein zweites Mal erstellt: Bei der alten ändert sich das Team und sie rückt nach oben.
- **Nicht jeder erfolgreiche Rückzug wird gespeichert.** Wenn ein schlechter Kampf nur deshalb stattgefunden hat, weil der Titan ihn verletzt betreten hat, bei 100 % HP aber alles in Ordnung gewesen wäre („die Gegner sind nicht schuld“), wird die Regel nicht erstellt.
- **Deaktivierte Regeln fasst der Bot nicht an:** Er schaltet sie weder ein noch überschreibt er sie. Dasselbe Team wird er sich nicht noch einmal merken, und eine ausgeschaltete „Goldene“ Regel kehrt nicht zurück.
- **Gelöschte Regeln können zurückkehren.** Die „Goldene Regel“ wird beim nächsten Start erneut erstellt, solange es keine andere Regel gegen diese Gegner gibt. Wenn es dir nicht gefällt, schalte sie mit dem Schalter aus. Eine „Auto“-Regel erstellt der Bot erneut, wenn ein Rückzug wieder genauso endet.
- **Solange das Fenster geöffnet ist, kann der Bot eine neue Regel in die Datei schreiben.** Wenn du auf „Einstellungen speichern“ klickst, liest das Fenster die Datei erneut und setzt diese neuen Regeln nach oben, ohne etwas zu verlieren. Schaust du auf den Reiter, ohne etwas zu ändern, siehst du die frische Liste von der Festplatte.

> [!warning] Wenn die Regeldatei eines Elements beschädigt ist (wenn sie beispielsweise manuell bearbeitet wurde und ein Einrückungsfehler vorliegt), schreibt das Fenster, beispielsweise für Wasser: „Die Regeldatei ist beschädigt: bot_data/rules/water.yml — die Regeln dieses Elements ändert das Fenster nicht“. Die restlichen Elemente funktionieren. Es ist nicht nötig, die Datei manuell zu bearbeiten: Klicke auf der Hauptseite auf „Log an den Autor senden“ und schreibe, was passiert ist.

> [!tip] Womit anfangen? Schreibe vorab nichts. Spiele ein paar Dutzend Räume mit aktiviertem „Der Bot entscheidet“ und schaue hier vorbei: Der Bot hat sich dann bereits einige Regeln gemerkt. Deaktiviere die unpassenden, rücke die guten mit den Pfeilen nach oben. Füge eigene Regeln hinzu, wenn du ein sich wiederholendes Problem siehst: „Araji läuft ständig verletzt herum“ — eine Rettungsregel; „diese Gegneraufstellung besiegt immer mein Hauptteam“ — eine Regel gegen Gegner.

> [!done] Jetzt weißt du, wie du dem Bot Ausnahmen beibringst, und verstehst, warum er genau dieses Team einsetzt. Als Nächstes — Telegram und Fenster, die dich um Hilfe rufen. [Nächster Abschnitt →](#10)

## Wenn der Kampf schlecht lief: SOS-Fenster

Fast immer kommt der Bot alleine klar. Aber manchmal gerät er in eine Situation, in der es ohne den Menschen nicht geht: Der Kampf ist gewonnen, aber der Preis war zu hoch, oder die Regeln liefern kein passendes Pack. Dann **hält der Bot an und ruft dich** mit einem Fenster mitten auf dem Bildschirm. SOS ist ein Notsignal wie bei einem Schiff: „Hilfe wird benötigt“. Solange du nicht geantwortet hast, klickt der Bot nichts an und wartet (aber nicht ewig, dazu unten mehr).

Es gibt drei Fenster, jedes für seinen eigenen Fall:

- :triangle-alert: **«Eingriff erforderlich»** — der Kampf ist zu Ende, aber das Ergebnis ist schlecht. Das ist das Hauptfenster, es erscheint am häufigsten.
- :users: **«Kein passendes Pack»** — der Bot hat den Kampf noch nicht begonnen: Die Regeln liefern ihm kein Pack für diesen Raum.
- :check: **«Das Pack hat gewonnen»** — du hast selbst ein anderes Pack gewählt, es hat gewonnen und der Bot fragt, ob er es sich merken soll.

![Fenster «Eingriff erforderlich»: Grund, Raum, Gegner, Dein Pack mit HP-Balken und drei Schaltflächen](images/sos_window.png)

> [!note] Wann das Fenster erscheint: Wenn «Der Bot entscheidet» **ausgeschaltet** ist (Standardeinstellung), öffnet sich das Fenster nach **jedem** schlechten Kampf. Wenn es eingeschaltet ist, versucht der Bot zuerst selbst klarzukommen und ruft nur dann, wenn er es nicht kann: Der Kampf wurde manuell geführt (Angus), das Ergebnisfenster konnte nicht gelesen werden, du hast das Pack gewählt, im Raum hat der Bot bereits so oft zurückgesetzt wie erlaubt, oder es gibt kein Ersatzteam. Was ein „schlechter Kampf“ ist und wie man das einstellt — in den Abschnitten zu «Basis und Räume» und «Auto-Taktik und HP».

### Das Fenster «Eingriff erforderlich»

Oben — kurz: «Der Kampf lief schlecht. Was tun wir?». Darunter — Fakten, damit du entscheiden kannst, ohne in das Logbuch zu schauen:

- **Grund.** Was genau dem Bot nicht gefallen hat. Zum Beispiel: „Kritische Schwelle! Araji hat 12% HP (Schwelle: 40%)“, „Verlust-Delta überschritten! Rigel hat 45% HP verloren (Toleranz: 30%)“, „FATAL! Iyari ist tot…“, „Große Pack-Verluste!…“ oder „Ergebnisfenster konnte nicht gelesen werden: nicht gefunden…“. Die Namen der Titanen stehen in der Sprache des Programms.
- **Raum.** Element der Tür und Raumnummer: „Feuer · Raum 54“.
- **Gegner.** Quadrate der Titanen, gegen die gekämpft wurde. Werden die Gegner nicht erkannt, gibt es diese Zeile nicht.
- **Dein Pack.** Jeder Titan mit seinem eigenen Gesundheitsbalken und der Aufschrift „HP vor dem Kampf → HP danach“: „36% → 12%“. Wenn die HP eines Titans unter seiner Panikschwelle (allgemein oder persönlich) liegen, sind der Balken und die Zahl **rot**. Schon verwundet in den Kampf gegangen und fast ohne HP herausgekommen — das sieht man sofort.
- **Timer.** Unten: «Ohne Antwort entscheidet der Bot in 9:41 selbst». Die letzte Minute ist gelb, danach „Der Bot entscheidet selbst…“. Wenn in «Auto-Taktik und HP» 0 steht, gibt es die Zeile nicht: Der Bot wartet immer auf dich.

Schaltflächen (von rechts nach links, die wichtigste ganz rechts):

1. **«Kampf zurücksetzen»** (blau). Dienten Kampf mit einem anderen Pack erneut spielen. Das Fenster blendet sich aus, «Team zusammenstellen» mit dem aktuellen Pack öffnet sich; tausche die Titanen aus und klicke auf «Mit diesem Pack zurücksetzen». Wie es weitergeht — im Abschnitt «Rückzug» unten. Wenn du «Team zusammenstellen» ohne Auswahl schließt, kehrt das SOS-Fenster zurück, nichts ist verloren.
2. **«Ignorieren»** (grau). Den Kampf so annehmen, wie er ist: Der Raum wird gewertet, der Bot macht mit den verbleibenden HP weiter. Passend, wenn die Verluste für dich in Ordnung sind (zum Beispiel ging der Titan ohnehin verwundet hinein und insgesamt ist alles normal).
3. **«Manuell spielen»** (grau). Der Bot klickt nichts an, sondern du spielst diesen Raum selbst im Spiel. Der Bot wartet, bis du in den Korridor zurückkehrst: Das Türfähnchen muss 2 Sekunden lang ununterbrochen sichtbar sein. Wenn das Ergebnisfenster das Letzte war — der Raum wird gewertet; hast du dich zurückgezogen, ohne zu siegen — nicht. Wenn du das Ergebnisfenster geschlossen hast, ohne erneut zu spielen — der Kampf wird wie gehabt gewertet. Nach dem manuellen Spielen vergisst der Bot die HP der Titanen und die Aufstellungen in den Slots (liest sie selbst vom Teamauswahl-Bildschirm neu ab) und spielt danach selbst weiter.

> [!warning] Ein Kampf, bei dem die **manuelle Ulti von Angus** verwendet wurde, kann nicht zurückgesetzt werden: Auf seinem Ergebnisfenster gibt es keine Schaltfläche „Nochmal“. Anstelle von «Kampf zurücksetzen» erscheint im Fenster das rote **«Bot stoppen»**, und es bleiben nur «Ignorieren» oder «Manuell spielen».

### Rückzug des Kampfes: Was der Bot nach deiner Auswahl tut

Das Fenster hat sich geschlossen, der Befehl ging an den Bot. Danach macht er alles selbst, und im Logbuch erkennt man das am Tag `[ОТКАТ]`:

1. Klickt auf **«Nochmal»** auf dem Ergebnisfenster und wartet auf das Laden des Kampfes (manchmal dauert das 20–30 Sekunden und mehr, daher wartet er bis zu einer Minute).
2. Setzt den Kampf **auf Pause** (einmal) und klickt auf **«Rückzug»**.
3. Kehrt in den Korridor zurück, betritt **denselben Raum** und stellt dein neues Pack auf.

Ist der Kampf wieder schlecht gelaufen — erscheint das Fenster erneut. Lief er gut — hier erscheint das Fenster «Das Pack hat gewonnen» (siehe unten).

Wenn die Verbindung zum Spiel verloren ging (das Ladebild endet nicht), gibt der Bot nicht auf: Er wartet bis zu 15 Minuten auf das Spiel und schreibt dies ins Logbuch. Nur wenn der Rückzug endgültig fehlschlägt, speichert der Bot einen Screenshot unter `bot_data/debug/`, legt eine sanfte Pause ein und sendet dir eine Nachricht auf Telegram. Mehr dazu im Abschnitt über Störungen.

### Das Fenster «Kein passendes Pack»

Erscheint, wenn der Bot bereits die Tür ausgewählt und die Gegner angeschaut hat, aber **nichts aufzustellen ist**. Das geschieht aus zwei Gründen, beide aufgrund deiner Regeln:

- Es hat die Regel „Mich fragen“ ausgelöst (sie wurde genau dafür gemacht);
- Das Hauptpack des Raums enthält einen Titanen, den die Regel „Skip“ verboten hat (der Bot schreibt etwa «ФАТАЛЬНО: Все паки отбракованы…»).

Das Fenster fragt: «Die Regeln liefern kein Pack für diesen Raum. Was tun wir?» Darin befinden sich dieselben Angaben zu «Grund», «Raum» und «Gegner», aber ohne Balken: Es gab noch keinen Kampf. Schaltflächen:

- **«Neues Pack bauen»** (blau) — öffnet «Team zusammenstellen», die Schaltfläche dort heißt «Anwenden». Der Bot stellt die ausgewählten Titanen auf und **merkt sich das Pack sofort als Regel** „gegen diese Gegner“ (hier gibt es keine Prüfung vor dem Speichern, sei vorsichtig).
- **«Manuell spielen»** — du absolvierst den Raum selbst, der Bot wartet im Korridor. Der Raum wird gewertet, wenn ihr siegt.
- **«Bot stoppen»** (rot) — der Bot schreibt die Sitzungsbilanz und schaltet sich aus.

Die Schaltfläche «Ignorieren» gibt es hier nicht: Es gibt nichts anzunehmen, da kein Kampf stattfand.

### Das Fenster «Das Pack hat gewonnen»

Dieses Fenster erscheint, wenn ein Pack den Kampf gewonnen hat, das **du ausgewählt hast** (über «Kampf zurücksetzen» oder «Anderes testen», im Fenster oder auf Telegram). Hat der Bot selbst ein Ersatzteam gewählt und es hat gewonnen, merkt sich der Bot es selbst und fragt nichts.

Darin — Raum, Gegner (aus dem letzten SOS-Fenster, wenn es nicht länger als 15 Minuten her ist) und dein Pack mit den HP nach dem Kampf. Frage: «Das getestete Pack hat gewonnen. Als Regel gegen diese Gegner speichern?» Schaltflächen:

- **«Pack speichern»** (grün) — der Bot merkt sich die Regel „gegen diese Gegner“ mit diesem Pack. In der Regelliste erscheint sie als «Auto: … im Raum» oder «Dein Pack nach einem Rückzug, vom Bot gemerkt».
- **«Anderes testen»** — erneut «Team zusammenstellen» und Rückzug: Der Bot spielt den gewonnenen Kampf mit einem anderen Pack noch einmal.

Antwortest du nicht — speichert der Bot nach Ablauf des Timers (Beschriftung «Ohne Antwort speichert der Bot das Pack in… selbst») das Pack selbst, als hättest du auf «Pack speichern» geklickt.

### Das Schließen-Kreuz des Fensters und «Bot stoppen?»

Die Fenster haben kein „einfach schließen“: Wird das Fenster geschlossen, wartet der Bot weiterhin auf eine Antwort. Daher fragt das Kreuz: **«Bot stoppen?»**. Antwortest du mit «Bot stoppen», beendet der Bot die Arbeit, schreibt die Bilanz und sendet sie an Telegram. Reagiert er binnen 10 Sekunden nicht, stoppt das Programm ihn selbst. Beim Fenster «Das Pack hat gewonnen» ist die Frage eine andere: Der Stopp dort gleicht dem „STOPP F10“, **die Sitzungsbilanz wird nicht an Telegram gesendet**. Hast du es dir anders überlegt — klicke auf «Abbrechen», das Fenster bleibt bestehen.

### Was passiert, wenn man nicht antwortet

Jedes Mal, wenn du innerhalb der Zeit aus der «Auto-Taktik und HP» nicht geantwortet hast («SOS-Fenster ohne Antwort, Zeitlimit in Min»: standardmäßig 10, bis zu 60, 0 — immer warten), schreibt der Bot `[ТАКТИКА] Ответа нет 10 мин. Решаю сам.`, das Fenster schließt sich und du erhältst eine Telegram-Nachricht, dass der Bot selbst entschieden hat. Das funktioniert auch bei ausgeschaltetem «Der Bot entscheidet». Die Entscheidung hängt vom Fenster ab:

- **«Eingriff erforderlich»:** Es gibt ein Ersatzteam und der Kampf kann zurückgesetzt werden (nicht Angus, Versuche im Raum sind nicht aufgebraucht) — **Rückzug** und Ersatzteam; andernfalls sind alle Titanen am Leben — Kampf wird **angenommen** («Ignorieren»); andernfalls (jemand ist gestorben oder wurde auf dem Fenster nicht erkannt) — **sanfte Pause**.
- **«Kein passendes Pack»:** Ein Ersatzteam ohne Verletzte und ohne verbotene Titanen passt — der Bot stellt es auf **und merkt sich die Regel nicht**; gibt es ein solches nicht — **sanfte Pause**.
- **«Das Pack hat gewonnen»:** Das Pack wird gespeichert.

Eine sanfte Pause ist wie die Schaltfläche „Pause F9“: Der Bot wartet im Korridor, bis du auf «Fortsetzen» klickst.

> [!tip] Hast du im selben Moment geantwortet, in dem der Bot bereits selbst entschieden hat? Nicht schlimm: Die alte Antwort überspringt der Bot und schreibt `[ЛОГИКА] Пропускаю ответ ...: он пришёл на прошлое окно.`

### Über Telegram antworten

Wenn Telegram eingerichtet ist, kommt **dieselbe Frage** auch in den Chat: ein Screenshot des Spiels, Beschriftung (Raum, Gegner, Grund, Pack mit HP) und Schaltflächen. Du kannst dort antworten, wo es bequemer ist: Antwortest du im Chat, schließt sich das Fenster auf dem Computer von selbst, und umgekehrt.

- **«Zurücksetzen (Pack erstellen)»** (grün) — der Bot bittet dich, die Namen von **3–5 Titanen** durch Komma oder Leerzeichen getrennt in den Chat zu schreiben, zeigt an, wen er erkannt hat, und fragt „Alles richtig?“ («Pack bestätigen» / «Ein anderes schreiben»). Für den manuellen Kampf von Angus und für «Kein passendes Pack» steht anstelle dieser Schaltfläche das rote «Bot stoppen».
- **«Manuell spielen»** und **«Ignorieren (Fortsetzen)»** — dasselbe wie im Fenster. Bei «Kein passendes Pack» gibt es «Fortsetzen» nicht.
- «Das Pack hat gewonnen» kommt in Telegram nur an, wenn du das Pack auch von dort gesendet hast: «Bestätigen und Speichern» oder «Zurücksetzen und Erneut versuchen».

Wenn das Internet ausfällt, wird die Nachricht später gesendet (der Bot wiederholt die Versuche), und das Fenster selbst auf dem Computer bleibt bestehen. Die Einrichtung von Telegram befindet sich im entsprechenden Abschnitt.

### Minibar und SOS-Fenster

Wenn das Programmfenster in die Minibar minimiert ist, erscheint das SOS-Fenster **in der Mitte des Spiels**. Die Minibar ist in dieser Zeit rot, und ihre Schaltfläche „SOS“ bringt das verloren gegangene Fenster wieder über das Spiel.

> [!tip] Wie wählt man aus? Schau auf «Dein Pack». Ein Titan ging verwundet hinein und hat HP verloren, die anderen sind in Ordnung — oft reicht «Ignorieren». Die Gegner sind dir bekannt und deutlich stürker — «Kampf zurücksetzen» mit einem anderen Pack. Nichts ist klar — «Manuell spielen». Ein Rückzug kostet Zeit (der Kampf muss neu geladen werden, das dauert 20–30 Sekunden und mehr), «Ignorieren» hingegen nichts.

> [!done] Jetzt weißt du, was jedes SOS-Fenster bedeutet, was die Schaltflächen tun und was der Bot ohne dich macht. Als Nächstes — wie der Bot selbst entscheidet, während du nicht in der Nähe bist. [Nächster Abschnitt →](#11)

## Wie der Bot selbst entscheidet

Im Abschnitt über die SOS-Fenster hast du gesehen, dass der Bot dich nach einem schlechten Kampf ruft. Aber er ruft dich nicht immer: Wenn du «Der Bot entscheidet» einschaltest (Registerkarte «Basis und Räume», Abschnitt 7), versucht der Bot **zuerst selbst klarzukommen** und wendet sich erst dann um Hilfe an dich, wenn es nicht geklappt hat. Hier gehen wir der Frage nach, wie er denkt. Formeln gibt es keine: nur Fragen, die sich der Bot stellt, und Beispiele.

Stell dir einen erfahrenen Mitspieler vor, der neben dir am Telefon sitzt. Der Kampf lief schlecht, und du bist kurz Tee holen gegangen. Er wird nicht einfach dasitzen und warten. Er erinnert sich daran, was gegen solche Gegner bereits geholfen hat, spielt den Kampf mit einer anderen Aufstellung neu durch und schreibt auf, was funktioniert hat. Ungefähr so verhält sich auch der Bot. Nur dass er Regeln hat, um keinen Unsinn zu machen.

> [!note] «Der Bot entscheidet» ist standardmäßig **ausgeschaltet**, und alles, wovon unten die Rede ist, findet dann nicht statt: Nach jedem schlechten Kampf öffnet der Bot einfach das SOS-Fenster. Schaltest du den Schalter ein und klickst auf «Einstellungen speichern», wird das ab dem nächsten «Farmen starten» wirksam. Was man genau anpassen kann, haben wir in Abschnitt 8 («Auto-Taktik und HP») besprochen, hier geht es darum, **was der Bot mit diesen Zahlen macht**.

### Schlechter Kampf: Was der Bot der Reihe nach tut

1. **Bemerkt, dass der Kampf schlecht war.** Jemand ist gestorben oder liegt unter der Panikschwelle, hat mehr als die Toleranz verloren oder gleich drei sind „eingebrochen“ (Abschnitte 7 und 8). Im Logbuch steht die Zeile `[ТАКТИКА] Плохой бой: ...` mit dem Grund.
2. **Prüft, ob er selbst zurücksetzen kann.** In vier Fällen geht das nicht: Der Kampf wurde manuell geführt (Ulti von Angus, auf seinem Ergebnisfenster gibt es keine Schaltfläche „Nochmal“), das Ergebnisfenster wurde nicht gelesen, das Pack hast **du** aufgestellt (dann liegt die Entscheidung auch bei dir) oder der Bot hat seine Versuche in diesem Raum bereits aufgebraucht. Geht es nicht — öffnet sich das SOS-Fenster, und im Logbuch steht `[ТАКТИКА] Сам не откатываю: ... Спрашиваю вас.` mit dem Grund.
3. **Sucht nach einem Ersatzteam.** Wie — im nächsten Abschnitt. Gibt es kein passendes — erneut das SOS-Fenster.
4. **Setzt zurück und spielt neu.** Dieselben Schritte `[ОТКАТ]` wie nach deiner Wahl („Nochmal“, Pause, „Rückzug“), und im selben Raum wird das Ersatzteam aufgestellt. Im Logbuch steht `[ТАКТИКА] Откатываю бой сам и переиграю паком ... (взят: ...)`.
5. **Schaut auf das Ergebnis.** Hat das Ersatzteam gewonnen — macht der Bot weiter und merkt sich in der Regel das Pack (dazu unten mehr). Ist der Kampf wieder schlecht — zweiter Versuch, und so weiter, bis die Versuche aufgebraucht sind («Ersatzteams pro Raum probieren», standardmäßig 2, maximal 3). Danach ruft er dich.

> [!tip] Der Bot setzt den Kampf jedes Mal vollständig zurück und „korrigiert ihn nicht im Laufenden“. Ein Rückzug kostet Zeit (der Kampf muss neu geladen werden, das dauert 20–30 Sekunden und mehr), daher mag er keine leeren Versuche: Siehe unten, wie er das Pack auswählt.

### Woher der Bot das Ersatzteam nimmt

Er geht die Liste von oben nach unten durch und nimmt das **erste passende**:

1. **Deine «Ersatzteams»** — Registerkarte «Basis und Räume», Raumkarte. Werden in der Reihenfolge genommen, wie du sie aufgebaut hast. Im Logbuch wird die Quelle „deine Liste der Ersatzteams“ genannt.
2. **Packs aus den Regeln dieses Elements** — im Logbuch „Elementregeln“. Darin gilt eine eigene Reihenfolge: Zuerst Regeln „gegen diese Gegner“, dann Packs, die genau diese Gegner schon einmal besiegt haben (die besten nach verbleibenden HP zuerst), dann die restlichen „Anti-Packs“, dann alles Übrige inklusive des Hauptpacks des Raums.
3. **Kampfverlauf** — im Logbuch „Kampfverlauf“. Das ist die letzte Reihe, und es werden nur Packs genommen, die diese Gegner bereits besiegt haben. Der Bot erinnert sich an die Kämpfe der letzten 20 Starts.

Was der Bot **niemals als Ersatzteam aufstellt**:

- Ein Pack, das in diesem Raum bereits verloren hat (um Fehler nicht zu wiederholen);
- Ein Pack, das „gegen diese Gegner verliert“: Beim letzten Mal gegen sie wurde der Kampf wegen der Gegner zurückgesetzt, und das Pack hat nicht mehr Siege als Niederlagen. Eine einzige Niederlage **macht ein gutes Pack nicht schlecht**: Hat es gegen diese Gegner fünfmal gewonnen und einmal verloren, nimmt der Bot es weiterhin;
- Ein Pack mit einem Titanen, den die Regel „Skip“ verboten hat;
- Ein Pack mit einem Titanen, dessen HP bereits **unter der Panikschwelle** liegen: Diesen schickt der Bot nicht in den sicheren Tod;
- Aus dem Verlauf — ein Pack, in dem ein Titan enthalten ist, den du nirgendwo angegeben hast (weder in Packs noch in Regeln). Im Verlauf verbleiben Packs längst gelöschter Regeln, und der Bot erweckt sie nicht wieder zum Leben.

Außerdem gibt es „gefährliche“ Packs: Solche, bei denen ein verwundeter Titan nach den bisherigen Kämpfen das Ende des Kampfes voraussichtlich nicht erlebt. Diese nimmt der Bot **an letzter Stelle**, nur wenn es nichts Besseres gibt. Wie er das feststellt — im Abschnitt „Verletzter Titan“ unten.

Warum der Bot das eine oder andere Pack nicht genommen hat, sieht man im Logbuch: `[ТАКТИКА] Не беру запасной пак ...` und der Grund. Wenn die Ersatzteams aufgebraucht sind und der Kampf immer noch schlecht ist — das ist kein Defekt, sondern ein ehrliches „ich weiß nicht, was ich sonst aufstellen soll“.

### Merken oder nicht: Die Regel «Auto: …»

Das Ersatzteam hat gewonnen. Der Bot trägt dies in die Regel „gegen diese Gegner — stelle dieses Pack auf“ ein, und wenn er das nächste Mal auf dieselbe Gegneraufstellung trifft, stellt er es sofort auf. In der Regelliste steht diese Regel als «Auto: … im Raum» an erster Stelle (Abschnitt 9). Im Logbuch: `[ТАКТИКА] Запасной пак ... справился. Запоминаю его против этих врагов.`

Manchmal darf man sich das aber **nicht merken**. Beispiel: Araji ging mit 36% Gesundheit in den Kampf und fiel auf 5%. Das Hauptpack kann nichts dafür: Wäre Araji gesund gewesen, wäre der Kampf normal verlaufen. Würde der Bot die Regel „gegen diese Gegner stelle das Ersatzteam auf“ speichern, würde er das Ersatzteam auch dort aufstellen, wo das Hauptpack bestens zurechtkommt, und deine Kraft unnötig verschwenden. Daher prüft der Bot: **„Wäre der Kampf auch mit 100% HP bei allen schlecht gewesen?“** Nein — das bedeutet, die Gegner haben keine Schuld, die Hilfe war einmalig, es wird keine Regel erstellt.

Im Logbuch sieht man das sofort: `[ТАКТИКА] Враги ни при чём: в бой вошли раненые ...` und danach `Правило не запоминаю: это была разовая помощь раненым титанам`.

Das Merken klappt auch in drei anderen Fällen nicht:

- Der Bot hat die Gegner nicht erkannt (`[ОБУЧЕНИЕ] Враги не распознаны — правило не сохраняю`): Eine Regel „ohne Gegner“ würde in jedem Raum auslösen;
- Du hast eine Regel mit demselben Pack per Kippschalter ausgeschaltet: Eine ausgeschaltete Regel rührt der Bot nicht an;
- Du hast das Pack selbst ausgewählt: Dann entscheidet dein Fenster «Das Pack hat gewonnen» (Abschnitt 10).

### Verletzter Titan: Hilfe im Voraus, nicht erst nach dem Kampf

Das Wertvollste, was der Bot kann, ist **einen schlechten Kampf gar nicht erst zuzulassen**, anstatt ihn hinterher auszubügeln. Während er sich auf dem Teamauswahl-Bildschirm befindet, schaut er auf die Gesundheit der Titanen und auf den Verlauf: „Wie sind die Kämpfe mit diesem Pack in diesem Raum ausgegangen?“ Dazu speichert der Bot, wie viel HP ein Titan im Kampf mit diesem Pack gewöhnlich **verliert** (Durchschnitt der letzten fünf Kämpfe, es werden mindestens zwei Kämpfe benötigt). Wenn die HP des Verletzten am Eingang minus den üblichen Verlust **unter die Panikschwelle fallen würden** — geht der Bot kein Risiko ein und stellt sofort, noch vor dem Kampf, das Ersatzteam auf.

Beispiel: Araji geht mit 36% HP ins Feuer. In den letzten Kämpfen hier hat er gewöhnlich etwa 29% verloren. Es ergibt sich: 36 − 29 = 7%, während die Panikschwelle bei 40 liegt. Der Kampf geht fast sicher schlecht aus, und der Bot stellt **sofort** ein Ersatzteam auf, zum Beispiel mit Moloch. Das ist eine einmalige Hilfe, die Regel wird nicht gemerkt.

Zwei Feinheiten, damit der Bot nicht merkwürdig wirkt:

- **Energie ist ebenfalls wichtig.** Hat der Titan derzeit etwa so viel Energie wie in den vergangenen Kämpfen (Abweichung nicht mehr als 25%), zieht der Bot für die Prognose genau diese Kämpfe heran. Araji mit guter Energie verliert im Feuer wenig, mit leerer Energie viel, und die Prognose berücksichtigt das.
- **Ein Kampf ist keine Statistik.** Bei weniger als zwei Kämpfen glaubt der Bot der Prognose nicht und ändert nichts.

Die Packs der Rettungsregeln („wenn Araji unter 50% — stelle Sigurd auf“, Abschnitt 9) tauscht der Bot im Voraus nicht aus: Du hast sie genau für den Verletzten aufgestellt, und deine Absicht ist wichtiger als seine Prognose.

### Tür nach Gesundheit

Wenn der Bot selbst entscheidet und im Korridor **mehrere erlaubte Türen** sichtbar sind, wählt er nicht einfach der Reihe nach (Abschnitt 8, «Türreihenfolge»), sondern mit Rücksicht auf die Verletzten:

1. Zuerst geht er in eine Tür, **hinter der der Verletzte geheilt wird**: Es greift deine Rettungsregel oder der Bot stellt selbst ein Heilungspack zusammen.
2. Eine Tür, hinter der dem Verletzten nach den bisherigen Kämpfen Unheil droht, **überspringt** der Bot, wenn es eine andere gibt.
3. Ansonsten alles wie gewohnt, der Reihe nach.

Erkennbar an der Zeile `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...`. Eine durch die Regel „Skip“ verbotene Tür wird der Bot weiterhin niemals öffnen. Die Gegner hinter der Tür sieht der Bot noch nicht, daher stützt er sich hier auf das Basispack der Tür.

### Heilungspack im «Gemischten» Raum

Kann der Verletzte geheilt werden und deine Heilungsregel hat nicht gegriffen, **stellt der Bot selbst ein Heilungspack zusammen**: Er stellt den Verletzten und bei Bedarf einen gesunden, aufgeladenen Heiler in den «Gemischten» Raum. Geheilt wird einzeln, Haupttitanen vor Ersatztitanen, und wer unter der Panikschwelle liegt, wird gar nicht geheilt. Alle Einzelheiten (Schwelle «Titan heilen, wenn HP unter, %», «Wen für den Verletzten aus dem Team nehmen», eben jener Sigurd für Rigel) — in Abschnitt 8. Hier ist eines wichtig: Das ist dieselbe **einmalige Hilfe** wie das Ersatzteam aus der Prognose. Eine Regel wird danach nicht erstellt, und in der Bilanz wird sie separat gezählt („Heilungspacks (vom Bot selbst zusammengestellt)“).

### «Goldene Regeln»: Der Bot lernt aus dem gesamten Verlauf

All diese Entscheidungen trifft der Bot im Laufe des Spiels. Und die „goldenen Regeln“ zieht er **einmalig beim Starten des Farmens** nach. Der Bot durchsucht den Kampfverlauf und sucht nach einem Pack, das gegen dieselbe Gegneraufstellung **5 Kämpfe oder mehr absolviert und 80% oder mehr gewonnen hat**. Ein solches Pack trägt er als Regel «Gold: … im Raum» ein (Abschnitt 9). Im Logbuch: `[ОБУЧЕНИЕ] ...: 'Золотое правило против: ...' — пак ... Сохранено на 1-е место.`

Nicht golden wird:

- Das Hauptpack des Raums, Packs von Rettungsregeln und deine «Ersatzteams» (sie dienen der Hilfe und nicht jedem Kampf);
- Heilungspacks, die der Bot selbst zusammengestellt hat: Sie werden nur benötigt, solange der Titan verwundet ist;
- Ein Pack mit einem Titanen, der in deinen Packs und Regeln nicht vorkommt;
- Ein Pack gegen Gegner, für die bereits eine Regel existiert (deine eigene, «Auto» oder eine ausgeschaltete).

Es gibt keine goldenen Regeln, solange «Der Bot entscheidet» ausgeschaltet ist. Ist eine unpassende aufgetaucht? **Schalte sie per Kippschalter aus**, anstatt sie zu löschen: Eine gelöschte Regel kehrt beim nächsten Start zurück, eine ausgeschaltete rührt der Bot nicht an.

### Wenn du auf das SOS-Fenster nicht geantwortet hast

Das ist nicht mehr „der Bot entscheidet selbst“, sondern „der Bot entscheidet an deiner Stelle“ (Abschnitt 10, „Was passiert, wenn man nicht antwortet“). Das funktioniert auch bei ausgeschaltetem «Der Bot entscheidet»: Nach Ablauf des Zeitlimits («SOS-Fenster ohne Antwort, Zeitlimit in Min») setzt der Bot den Kampf mit einem Ersatzteam zurück, nimmt ihn an oder wechselt in eine sanfte Pause. Jedes Mal schreibt er `[ТАКТИКА] Ответа нет N мин. Решаю сам.`, schließt das Fenster und sendet eine Nachricht an Telegram.

### Wie man versteht, was der Bot ohne dich getan hat

Am Ende der Sitzung gibt es im Block «Sitzungsbilanz» (Schaltfläche «Details») und in der Zeile `[ИТОГ]` folgende Zähler:

- **«Rücksetzungen: {n}»**: Wie viele Kämpfe insgesamt neu gespielt wurden;
- **«из них без вас»**: Wie viele dieser Rücksetzungen der Bot selbst durchgeführt hat, ohne zu fragen, sowohl nach Prognose als auch nach Zeitlimit;
- **«паки отхила (бот собрал сам)»**: Wie oft er den Verletzten mit einem Heilungspack geheilt hat.

Dieselbe Bilanz kommt auf Telegram an: „Rücksetzungen: 6 (бот сам: 5)“. Wenn fast alles „без вас“ gelaufen ist, kommt der Bot gut zurecht. Steigt die Zahl und es erscheinen keine „Goldene Regeln“, bedeutet das, dass dieselben Gegner immer wieder das Hauptpack schlagen. Wirf einen Blick auf die Registerkarte «Regeln und Eingriffe», welche Regeln er sich gemerkt hat, und überlege, ob es nicht an der Zeit ist, das Hauptpack zu wechseln.

> [!warning] Der Bot entscheidet anhand des **Verlaufs** und der Prognose, er sieht den Kampf nicht im Voraus voraus. Er kann sich irren: In den ersten Tagen, wenn der Verlauf noch gering ist, wird das Ersatzteam auf gut Glück ausgewählt. Erschrecke nicht, wenn «Der Bot entscheidet» in den ersten Dutzend Räumen öfter zurücksetzt, als dir lieb ist. Je mehr Kämpfe im Verlauf sind, desto präziser ist die Auswahl.

> [!tip] Womit anfangen? Lege mindestens ein bis zwei **«Ersatzteams»** in jedem Raum fest (Abschnitt 7): Dann muss der Bot nicht blind suchen. Schalte «Der Bot entscheidet» ein und beobachte ein paar Tage lang einfach die Zeilen `[ТАКТИКА]` und die «Sitzungsbilanz». Gefällt dir nicht, was der Bot tut — schalte den Schalter aus, und alles kehrt zu den SOS-Fenstern zurück.

> [!done] Jetzt verstehst du, wann und wie der Bot ohne dich klarstellt, was er sich merkt und wann er um Hilfe ruft. Als Nächstes — Telegram: Wie man Nachrichten erhält, wenn man nicht am Computer sitzt. [Nächster Abschnitt →](#12)

## Telegram

Der Bot kann dir auf Telegram schreiben, während du nicht am Computer bist: du bist in die Küche gegangen, schlafen gegangen, zur Arbeit gefahren. Wenn der Kampf deine Hilfe braucht, kommt ein Screenshot und Schaltflächen in den Chat. Drückst du eine Taste auf dem Telefon, macht der Bot, was du gesagt hast. Wenn alles glatt läuft, schweigt der Bot: Nachrichten kommen **nur bei Problemen** und **einmal am Ende der Sitzung**.

Was du brauchst: die Telegram-App und fünf Minuten Zeit. Das Einrichten ist nur einmal nötig.

> [!note] Telegram ist optional. Ohne Telegram funktioniert der Bot genauso, nur dass du die SOS-Fenster nur auf dem Computerbildschirm siehst und es keine Zusammenfassung der Sitzung gibt. Wenn du aber planst, den Bot über Nacht laufen zu lassen, richte es ein: So erfährst du sofort von einem Problem und nicht erst am Morgen.

### Was vorbereitet werden muss

Du brauchst zwei Dinge, beide holt man direkt in Telegram:

- :send: **Bot-Token** (der Schlüssel, mit dem sich das Programm bei deinem Bot anmeldet). Das ist eine lange Zeichenkette aus Zahlen und Buchstaben, zum Beispiel `123456789:AAH…`. Den Token gibt der spezielle Bot **@BotFather** aus.
- :user: **Chat ID** (die Chat-Nummer). Das ist eine Zahl, mit der Telegram versteht, an wen die Nachricht zugestellt werden soll: an dich und nicht an jemand anderen.

> [!warning] Der Token ist wie ein Passwort für deinen Bot. Zeige ihn niemandem, sende ihn nicht auf Screenshots oder in E-Mails (nicht einmal dem Autor des Programms). Mache einen Screenshot des Fensters „Telegram-Einstellungen“ nur, solange der Token mit Punkten verdeckt ist.

### Schritt für Schritt

1. **Erstelle deinen Bot.** Suche in Telegram nach **@BotFather** (der echte hat ein blaues Häkchen daneben) und klicke auf „Starten“. Schreibe ihm `/newbot`, denke dir einen Namen aus (beliebig, den siehst nur du) und einen Benutzernamen, der auf `bot` endet, zum Beispiel `moi_titan_bot`. Als Antwort sendet BotFather eine Nachricht mit dem Token: kopiere ihn.
2. **Finde deine Chat ID heraus.** Suche den Bot **@getmyid_bot**, klicke auf „Starten“ — er antwortet mit der Zeile `Your user ID` und einer Zahl. Das ist die Chat ID, kopiere die Zahl. Wenn dieser Bot nicht antwortet, gibt es einen Ausweichweg: Schreibe ein beliebiges Wort an **deinen** Bot aus Schritt 1, öffne im Browser die Adresse `https://api.telegram.org/bot<твой токен>/getUpdates` (ersetze `<твой токен>` durch deinen Token) und suche in der Antwort nach `"chat":{"id":` — die Zahl direkt danach ist die Chat ID.
3. **Klicke bei deinem Bot auf „Starten“.** Suche den Bot, den du in Schritt 1 erstellt hast, und klicke auf „Starten“ (oder schreibe ihm `/start`). Ohne dies **erlaubt** Telegram dem Bot nicht, dich zuerst anzuschreiben. Das ist der häufigste Grund, warum Nachrichten nicht ankommen.
4. **Öffne das Fenster im Programm.** Klicke auf den Telegram-Punkt in der Leiste links oder auf die Schaltfläche **„Telegram einrichten“** im Reiter „Basis und Räume“ (Abschnitt 7). Es öffnet sich das Fenster „Telegram-Einstellungen“.
5. **Fülle es aus.** Aktiviere den Schalter „Nachrichten an Telegram senden“. Füge in das Feld „Bot-Token (von @BotFather)“ den Token ein, in das Feld „Chat-ID“ die Zahl. Am bequemsten ist die Schaltfläche **„Einfügen“** neben dem Feld: Sie nimmt das, was du kopiert hast. Der Token wird mit Punkten angezeigt; das Augensymbol zeigt ihn an, um zu prüfen, ob er richtig eingefügt wurde. Ein Rechtsklick auf das Feld ist ebenfalls „Einfügen“.
6. **Teste die Verbindung.** Klicke auf **„Telegram testen“**. Nach einigen Sekunden erscheint rechts in Grün „Nachricht gesendet — Telegram prüfen“ und im Chat mit deinem Bot die Nachricht „Verbindungstest: alles funktioniert“. Wenn sie angekommen ist — alles fertig.
7. **Speichern.** Klicke auf **„Übernehmen“**, dann unten auf der Seite auf **„Einstellungen speichern“**.

![Das Fenster „Telegram-Einstellungen“: Schalter, Felder für Token und Chat-ID, Schaltflächen „Einfügen“ und „Telegram testen“](images/telegram_window.png)

> [!warning] „Übernehmen“ überträgt die Werte nur auf die Seite „Regel-Assistent“, in die Datei werden sie **nicht geschrieben**. Solange du nicht auf „Einstellungen speichern“ geklickt hast, leuchtet unten „Ungespeicherte Änderungen“ und der Bot weiß nichts von Telegram. Wenn du die Seite ohne Speichern verlässt, fragt das Programm „Änderungen speichern?“.

> [!tip] „Telegram testen“ prüft das, was aktuell im Fenster steht, selbst wenn du noch nichts gespeichert hast. Teste deshalb **vor** dem „Übernehmen“: Fehler gefunden — korrigiert — erneut getestet. Der Test läuft im Hintergrund, das Fenster friert nicht ein und du musst nicht länger als 20 Sekunden auf eine Antwort warten.

### Wenn der Test fehlschlägt

Unter der Schaltfläche erscheint eine rote Zeile „Nicht gesendet: …“ mit der Ursache. Die häufigsten:

- **„Token und Chat-ID ausfüllen“** — eines der Felder ist leer.
- `Unauthorized` — der Token ist falsch: ein Zeichen ging verloren, ein überflüssiges Leerzeichen oder nicht vollständig kopiert. Füge ihn mit der Schaltfläche „Einfügen“ erneut ein.
- `chat not found` oder `Forbidden` — die Chat ID ist falsch oder du hast bei **deinem** Bot nicht auf „Starten“ geklickt (Schritt 3). Überprüfe beide Punkte.
- **„Telegram-Verbindungsfehler“** — kein Internet oder Telegram lässt sich von diesem Computer aus nicht öffnen. Überprüfe, ob Telegram (oder die Website telegram.org) auf diesem PC funktioniert.

Wenn es nach der Korrektur immer noch nicht ankommt, erstelle bei @BotFather einen neuen Bot (Schritt 1) und fange von vorne an: Das geht schneller, als nach einem Tippfehler zu suchen.

### Woran man erkennt, dass Telegram aktiviert ist

Auf der Leiste links hat die Telegram-Schaltfläche einen Punkt: Wenn du den Mauszeiger darauf bewegst, erscheint der Hinweis **„Telegram: an“** oder **„Telegram: nicht eingerichtet“**. An bedeutet, dass der Schalter aktiviert ist und beide Felder ausgefüllt sind. Das ist **keine Verbindungsprüfung**: Ob der Token funktioniert, zeigt nur die Schaltfläche „Telegram testen“. Dasselbe sieht man im Reiter „Basis und Räume“: Neben der Schaltfläche „Telegram einrichten“ leuchtet grün „SOS-Benachrichtigungen an“ oder grau „Telegram nicht eingerichtet“. Der Punkt aktualisiert sich einige Sekunden nach dem Speichern von selbst.

### Welche Nachrichten ankommen

Die Sprache der Nachrichten ist dieselbe, die im Programmfenster ausgewählt ist.

- :swords: **SOS-Fenster** — Titel „Deine Hilfe wird gebraucht“ (oder „Kein passendes Pack“), Screenshot des Spiels und Beschriftung: Raum, Gegner (auf wen gekämpft wurde), Ursache, dein Pack mit TP- und Energie-Balken. Unten Schaltflächen. Das ist dieselbe Frage wie im Fenster auf dem Computer (Abschnitt 10).
- :triangle-alert: **Warnungen** — eine kurze Nachricht ohne Schaltflächen, die mitteilt, was passiert ist und was zu tun ist. Hier sind sie: „Zurücksetzen des Kampfes fehlgeschlagen“ (Bot im sanften Pause-Modus, schau auf den Telefonbildschirm), „Der Bot scheint zu hängen“ (5 Minuten ohne Raum) und dieselbe Nachricht, wenn ein Kampf nicht gestartet werden kann (höchstwahrscheinlich keine Verbindung zum Spielserver), „PC-Bildschirm ist gesperrt“ (der Bot sieht das Spiel länger als eine Minute nicht; entsperre den PC, und er macht von selbst weiter) und „Keine Antwort — der Bot hat selbst entschieden“.
- :chart-no-axes-column: **Ergebnis der Sitzung** — wenn der Bot anhält: wie viel Zeit vergangen ist, wie viele Räume, Etagen und Titanit gesammelt wurden, ob es Rücksetzungen und SOS-Fenster gab („vom Bot selbst: {n}“ — das sind Rücksetzungen, die er ohne dich gemacht hat), die längsten Räume. Wenn der Bot mit einem Fehler abgestürzt ist, steht im Titel „Der Bot ist mit einem Fehler abgestürzt“ und der Grund.

Das Ergebnis kommt bei jedem Stopp: Ziel erreicht, Ctrl+Q gedrückt, Ctrl+Shift+Q gedrückt, Bot ist mit einem Fehler abgestürzt. Es kommt **nicht** nach „STOP F10“ und nach „Stoppen und schließen“ (Abschnitt 6), weil diese den Bot sofort beenden.

### Schaltflächen unter der SOS-Nachricht

Drücke sie in Telegram genauso wie im Fenster auf dem Computer:

- **„Zurücksetzen (Pack erstellen)“** (grün). Der Bot sendet: „Schreiben Sie die Namen von 3-5 Titanen in den Chat“. Schreibe sie durch Komma oder Leerzeichen getrennt in den Chat, zum Beispiel `гиперион, сигурд, нова` oder kurz mit den ersten drei Buchstaben: `гип сиг нов`. Der Bot antwortet, wen er erkannt hat, und fragt „Alles richtig?“: **„Pack bestätigen“** startet das Zurücksetzen, **„Ein anderes schreiben“** lässt dich erneut eingeben. Werden nicht 3–5 Titanen erkannt, sagt der Bot, wie viele er erkannt hat, und bittet dich, noch einmal zu schreiben.
- **„Manuell spielen“** (blau). Der Bot drückt nichts und wartet, bis du den Raum selbst zu Ende spielst.
- **„Ignorieren (Fortsetzen)“** (grau). Den Kampf so akzeptieren, wie er ist, und weitergehen.
- **„Bot stoppen“** (rot). Anstelle von „Zurücksetzen“ wird sie angezeigt, wenn der Kampf manuell lief (Angus-Ulti) oder kein passendes Pack vorhanden ist. Beim Fenster „Kein passendes Pack“ gibt es keine Schaltfläche „Fortsetzen“.

Wenn das von dir gewählte Pack erfolgreich war, kommt die Frage „Das Pack hat gewonnen“ in Telegram mit zwei Schaltflächen: **„Bestätigen und Speichern“** (das Pack in einer Regel speichern) und **„Zurücksetzen und Erneut versuchen“** (ein anderes schreiben). Sie geht nur dann in den Chat, wenn du das Pack ebenfalls aus Telegram gesendet hast.

Nach dem Drücken bleibt unter der Nachricht eine einzelne grüne Schaltfläche „Ausgewählt: …“ zurück, die anderen verschwinden. Man kann **nur einmal** antworten: Klicks auf alte Nachrichten hört der Bot nicht ab. Antwortest du im Chat, schließt sich das Fenster auf dem Computer von selbst; antwortest du auf dem Computer, hört der Bot auf, auf eine Antwort aus Telegram zu warten.

> [!tip] Hat der Bot selbst entschieden, während du nach dem Telefon gesucht hast? Nicht schlimm. Es kommt die Nachricht „Keine Antwort — der Bot hat selbst entschieden“, und die Schaltflächen der alten Frage bewirken nichts mehr. Wie lange der Bot auf dich wartet, wird in „Auto-Taktik“ eingestellt (Abschnitt 8, „SOS-Fenster ohne Antwort, Zeitlimit in Min“).

### Wenn das Internet ausfällt

Der Bot hält nicht an und wartet nicht auf Telegram: Die Nachricht wird im Hintergrund gesendet. Hat es wegen der Verbindung nicht geklappt, versucht er es nach **30 Sekunden, 1, 2, 5 und 10 Minuten** (ca. 18 Minuten) erneut, und im Protokoll sind die Zeilen `Сообщение в Telegram не ушло (...). Пробую снова через N с.` und am Ende `Сообщение в Telegram: отправлено с N-й попытки` zu sehen. Dasselbe gilt für das SOS-Fenster: Es bleibt auf dem Computerbildschirm, und die Frage geht an Telegram raus, wenn die Verbindung wieder da ist. Die Zusammenfassung der Sitzung wiederholt der Bot kürzer (nach 10 und 30 Sekunden), weil er sich danach ausschaltet. Fehler von Telegram selbst (falscher Token) wiederholt der Bot nicht: Diese müssen in den Einstellungen korrigiert werden.

> [!note] Der Bot nimmt von dir keine Befehle „jederzeit“ entgegen (aus dem Chat stoppen, pausieren). Telegram antwortet nur auf Fragen, die der Bot selbst gestellt hat. Den Bot aus dem Chat zu stoppen ist nicht möglich, außer über die Schaltfläche „Bot stoppen“ unter der SOS-Nachricht.

> [!done] Telegram ist eingerichtet, und jetzt kann dich der Bot rufen, egal wo du bist. Als Nächstes kommt die Statistik: wie viele Räume, Etagen und Titanit nach Tagen gesammelt wurden. [Nächster Abschnitt →](#13)

## Statistiken

Die Seite „Statistiken“ beantwortet die Frage „Wie viel habe ich gespielt?“: Wie viel Titanit, Räume, Etagen und Titanentrank sich in einer Woche, einem Monat und für die gesamte Zeit angesammelt haben. Sie wird über die Schaltfläche **„Statistiken“** auf der linken Leiste geöffnet, oben steht „Aktivitätsstatistik“.

Diese Zahlen **berechnet der Bot selbst** und liest sie nicht vom Spielbildschirm ab. Einen Raum geschafft — eingetragen: **6 Titanit und 25 Trank**, und wenn im Ergebnisfenster ein „x2“-Symbol war — **12 Titanit und 50 Trank**. Belohnung am Speicherpunkt erhalten — Etage eingetragen. Einen Raum, den du manuell gespielt hast und den der Bot gewertet hat (Abschnitt 10), trägt er ebenfalls ein. Die Ergebnisse liegen in der Datei `bot_data/stats.json` und werden „nach Spieltagen“ gespeichert.

> [!note] Ein **Spieltag** beginnt nicht um Mitternacht, sondern zur Zurücksetzungszeit, die du im „Regel-Master“ festgelegt hast (Standard 5:00 Uhr, Abschnitt 7). Daher wird alles, was der Bot um 02:30 Uhr nachts gesammelt hat, für den **gestrigen** Tag eingetragen: Im Spiel läuft zu dieser Zeit noch der gestrige Tag. Wenn „Titanit (heute)“ am Morgen null ist, obwohl du nachts gespielt hast, ist das genau so gewollt.

### Was auf der Seite zu sehen ist

Oben links befindet sich ein Hinweis, rechts die Auswahl **„Zeitraum“**, darunter fünf Kacheln, ein Diagramm und unten „Manuelle Korrektur“.

- :calendar: **Zeitraum** — „7 Tage“, „14 Tage“, „30 Tage“ oder „Gesamte Zeit“. Der ausgewählte leuchtet blau. Beim ersten Öffnen ist „14 Tage“ eingestellt.
- :gem: **„Titanit“** — Summe für den Zeitraum.
- :calendar: **„Titanit (heute)“** — nur für den aktuellen Spieltag. Unabhängig vom Zeitraum.
- :flask-conical: **„Titanentrank“**, :door-open: **„Räume“** und :layers: **„Etagen“** — Summen für den Zeitraum.

Zahlen bis 100 000 sind in der Kachel vollständig geschrieben (`98 540`), längere sind abgekürzt: `105.5K` bedeutet einhundertfünftausendfünfhundert, `1.24M` eine Million zweihundertvierzigtausend. Die vollständige Zahl erscheint, wenn du mit der Maus über die Kachel fährst. „Gesamte Zeit“ nimmt die Gesamtzähler aus der Datei und nicht die Summe der Balken, weshalb die Kacheln mit dem Verlauf übereinstimmen, selbst wenn es viele Balken gibt.

> [!tip] Die Seite liest die Zahlen **bei jedem Öffnen**, nicht im laufenden Spielbetrieb. Der Bot läuft, aber die Zahlen ändern sich nicht? Wechsle auf eine andere Seite und kehre zurück.

![Seite „Statistiken“: Kacheln, Diagramm nach Tagen und ausgewählter Balken mit Plakette](images/stats_page.png)

### Diagramm: Balken und Klicks

Unter der Überschrift „Titanit-Aktivität“ steht ein Hinweis, wie die Balken zusammengefasst sind: „nach Tagen“, „nach Wochen“ oder „nach Monaten“. Es gibt nicht mehr als fünfzehn Balken, damit sich das Diagramm nicht in einen Lattenzaun verwandelt:

- **7 Tage und 14 Tage** — ein Tag pro Balken.
- **30 Tage** — eine Woche pro Balken (von Montag bis Sonntag; die äußeren Wochen sind unvollständig — sie enthalten nur die Tage, die in den Zeitraum fallen).
- **„Gesamte Zeit“** — nach Tagen, solange weniger als zwei Wochen an Daten vorliegen; danach nach Wochen, und wenn es mehr als fünfzehn Wochen sind — nach Monaten.

Links befindet sich eine Skala mit gestricheltem Netz, die Zahlen auf der Skala sind kurz (`3.6K`, `140K`). Beschriftungen unter den Balken werden, wenn sie nicht passen, jede zweite angezeigt; die letzte (heutige) ist immer sichtbar. Ein Tag ohne Spiel ist eine leere Stelle, es gibt keinen Balken. Für einen Zeitraum ohne Daten meldet das Diagramm „Keine Daten für diesen Zeitraum“.

1. **Fahre mit der Maus über einen Balken.** Darüber erscheint die genaue Titanit-Zahl. Das ist nur ein Hinweis, es ändert sich nichts.
2. **Klicke auf einen Balken.** Er wird heller, die anderen verblassen, daneben erscheint eine Plakette mit Datum und Zahl. Bei einer Woche sind in der Plakette die Titanit-Werte **nach Tagen** aufgeschlüsselt, bei einem Monat **nach Wochen**. Oben links leuchtet eine blaue Beschriftung auf, zum Beispiel „Angezeigter Tag: 19.10.2026 · heute“ (oder „Angezeigte Woche“, „Angezeigter Monat“).
3. **Sieh dir die Kacheln an.** Sie zeigen nun die Zahlen dieses Balkens: Titanit, Trank, Räume und Etagen für den Tag, die Woche oder den Monat. „Titanit (heute)“ bleibt der aktuelle Wert.
4. **Kehre zur Gesamtsumme zurück.** Klicke erneut auf denselben Balken oder auf die blaue Beschriftung mit dem Kreuz (✕). Wenn du den Zeitraum wechselst, wird die Auswahl ebenfalls zurückgesetzt.

### Tabelle

Die Schaltfläche **„Tabelle“** rechts über dem Diagramm zeigt dieselben Balken als Liste: „Datum“, „Titanit“, „Räume“, „Etagen“, „Titanentrank“. Neueste Daten stehen oben, unten die Zeile **„Gesamt“**. Eine Zeile kann ebenfalls per Klick ausgewählt werden, und die Kacheln zeigen ihre Zahlen an. Die Schaltfläche verwandelt sich dabei in **„Diagramm“** und bringt die Grafik zurück. Die Tabelle ist praktisch, wenn du genaue Zahlen für alle Tage auf einmal brauchst.

![Tabelle: Daten, Titanit, Räume, Etagen und Trank, unten „Gesamt“](images/stats_table.png)

### Manuelle Korrektur

Der Bot rechnet nach seiner eigenen Arithmetik (6 oder 12 Titanit pro Raum), aber im Spiel kann die Zahl anders sein: Du hast selbst gespielt, der Bot war ausgeschaltet, das Programm wurde nicht gleich am Morgen gestartet. Damit die Statistik mit dem Spiel übereinstimmt, gibt es die Karte **„Manuelle Korrektur“**.

1. **Wähle einen Tag.** In der Liste stehen „Heute“, „Gestern“ und fünf weitere vergangene Tage, insgesamt sieben. Brauchst du einen älteren Tag? Wähle den Zeitraum „7 Tage“ oder „14 Tage“ und klicke auf seinen Balken: Dieser Tag wird von selbst in die Liste eingetragen (über einen Wochen- oder Monatsbalken klappt das nicht — nur über einen Tagesbalken).
2. **Trage die Gesamtzahl aus dem Spiel ein.** Im Feld „Titanit pro Tag“ steht das, was im Spiel **für den gesamten Tag** angezeigt wird, und nicht „wie viel hinzugefügt werden soll“. Für den ausgewählten Tag steht dort bereits der aktuell eingetragene Wert.
3. **Klicke auf „Übernehmen“** (oder Drücke Eingabe im Feld).

Beispiel: Der Bot hat für den Tag 90 Titanit eingetragen, im Spiel stehen für denselben Tag aber 150. Du gibst **150** ein — das Programm fügt die Differenz von 60 hinzu und berechnet den Rest selbst neu: ungefähr **+5 Räume, +1 Etage und +250 Trank**. Das ist eine Schätzung: Es wird davon ausgegangen, dass die ersten 10 Räume des Tages jeweils 6 Titanit brachten und die restlichen jeweils 12. Wenn du anders gespielt hast, können Räume und Etagen leicht von den tatsächlichen abweichen, das Titanit stimmt aber exakt mit deinem Wert überein.

Wenn alles geklappt hat, erscheint unten die Benachrichtigung „Titanit für 19.10.2026: 150“, und im Protokoll auf der Hauptseite wird die Zeile `[СТАТИСТИКА] Данные за 2026-10-19 синхронизированы! Дельта: +60 тит., +5 комн., +250 зелий.` eingetragen. Wenn du weniger eingibst als eingetragen ist, verringern sich die Zahlen.

Was schiefgehen kann:

- **„Ganze Zahl ab 0 eingeben“** — im Feld befinden sich Buchstaben, Komma, Minus oder es ist leer. Das Feld wird rot.
- **„Der Bot hat an diesem Tag selbst 90 gesammelt, weniger geht nicht“** — man kann nicht weniger angeben, als der Bot **selbst** gesammelt hat, da dies korrekt aufgezeichnet wurde. Die Zahl lässt sich nur bis zu diesem Wert senken.
- **„Für diesen Tag ist genau das schon eingetragen“** — du hast exakt dieselbe Zahl eingegeben, es gibt nichts zu ändern.

> [!warning] „Übernehmen“ speichert die Zahlen **sofort** in `bot_data/stats.json`. Eine Schaltfläche „Einstellungen speichern“ gibt es hier nicht und wird nicht benötigt, anders als im „Regel-Master“ (Abschnitt 7). Ein Rückgängigmachen per Schaltfläche ist nicht möglich, aber es hindert dich nichts daran, den vorherigen Wert erneut einzugeben.

> [!note] Die Korrektur ändert **nur die Statistik**. Die „Sitzungsbilanz“ auf der Hauptseite und das Sitzungsziel (Abschnitt 4) werden separat berechnet, basierend auf dem, was der Bot in diesem Durchlauf gesammelt hat, und sind unabhängig von der Seite „Statistiken“.

### „Zurücksetzen“: Den gesamten Verlauf löschen

Die Schaltfläche **„Zurücksetzen“** (mit Papierkorb, rechts in der Karte „Manuelle Korrektur“) setzt die gesamte Statistik zurück: Titanit, Räume, Etagen und Trank für alle Tage. Aus Versehen gedrückt? Es passiert nichts: Zuerst fragt das Programm „Statistik zurücksetzen?“ und erinnert daran, dass dies nicht rückgängig gemacht werden kann. Mit der Schaltfläche „Zurücksetzen“ im Fenster bestätigst du, mit der Schaltfläche „Abbrechen“ lehnst du ab. Nach dem Zurücksetzen erscheint die Benachrichtigung „Statistik zurückgesetzt“ und im Protokoll die Zeile `[СТАТИСТИКА] Вся история полностью сброшена!`.

Es wird nur die Statistik gelöscht. Regeln, Packs, Einstellungen, `profile.yml` und Kampfprotokolle bleiben erhalten. Läuft der Bot in diesem Moment, macht er weiter und zählt ab null weiter, und das Sitzungsziel wird nicht zurückgesetzt.

> [!tip] Möchtest du es „versuchsweise“ zurücksetzen? Sichere zuerst eine Kopie: Schließe das Programm und kopiere die Datei `bot_data/stats.json` an einen anderen Ort (den Bot-Ordner öffnest du über die Schaltfläche „Bot-Ordner“ auf der Seite „Über das Programm“). Du kannst den Verlauf wiederherstellen, indem du die Datei zurücklegst.

### Häufig gestellte Fragen

- **Zahlen stimmen nicht mit dem Spiel überein.** Der Bot rechnet und liest nicht den Bildschirm ab: 6 oder 12 Titanit pro Raum. Wenn du Titanit aus anderen Quellen erhalten hast, zeigt das Spiel mehr an. Vergleiche und korrigiere es über „Manuelle Korrektur“.
- **Der heutige Tag ist leer, obwohl ich gespielt habe.** Überprüfe die Zurücksetzungszeit: Vor dieser Zeit schreibt der Bot nach „gestern“ (siehe „Spieltag“ oben). Hast du die Uhrzeit im „Regel-Master“ geändert? Starte das Programm neu, damit die Seite diese ebenfalls übernimmt.
- **Es gibt wenige Balken, aber der Zeitraum ist groß.** Tage, an denen der Bot nicht gelaufen ist, sind im Diagramm leer. „Gesamte Zeit“ und Monate komprimieren das Diagramm standardmäßig: Um bestimmte Tage zu sehen, wähle „7 Tage“ oder „14 Tage“.
- **Im Protokoll steht `[СТАТИСТИКА] ВНИМАНИЕ: Файл stats.json поврежден`.** Die Datei mit dem Verlauf konnte nicht gelesen werden (zum Beispiel wurde der Computer im Moment des Speicherns ausgeschaltet). Der Bot startet eine neue Statistik bei null und überschreibt die Datei. Kopiere sie vorab, wenn der alte Verlauf wichtig ist.

> [!done] Jetzt weißt du, wie man die Zahlen liest, Zeiträume wechselt, Statistiken mit dem Spiel abgleicht und sie löscht. Als Nächstes: Was zu tun ist, wenn etwas schiefgeht. [Nächster Abschnitt →](#14)

## Wenn etwas schiefgelaufen ist

Gute Nachricht: Der Bot kann sich aus den meisten Problemen selbst befreien. Bleibt er hängen – sieht er sich um und fängt von vorne an. Ist das Internet weg – wartet er. Hast du den Computer gesperrt – wartet er kurz und macht weiter. Du wirst nur gebraucht, wenn er **selbst darum bittet** (auf Pause gegangen ist, in Telegram geschrieben hat) oder wenn er nichts drückt und man im Log nicht versteht warum. Dieser Abschnitt behandelt beide Fälle: was der Bot ohne dich tut, wie man versteht, wo der Fehler liegt, und was man drücken muss.

Regel für alle Fälle: **Keine Panik und nichts überstürzen**. Es ist nicht schlimm, den Bot zu stoppen, neu zu starten und wieder auszuführen: Statistiken, Teams, Regeln und Einstellungen liegen in Dateien und gehen nirgendwo verloren.

### Wie man erkennt, dass etwas не stimmt

- :triangle-alert: **Rote Zahl auf dem Badge „Fehler“** im Log auf der Hauptseite. Sie zählt nicht nur Abstürze: Hier landen auch Warnungen (zum Beispiel „Spielfenster überdeckt“). Die Zahl an sich ist kein Grund zur Sorge, du musst nur den Badge öffnen und die Zeilen lesen.
- :pause: **Status „Pause“ und grüne Schaltfläche „Fortsetzen“, obwohl du die Pause nicht gedrückt hast.** Das bedeutet, der Bot hat selbst angehalten und wartet auf dich. Im Log steht dabei die Zeile `[ВНИМАНИЕ] Бот на мягкой паузе: ...` mit dem Grund.
- :send: **Nachricht in Telegram** (falls eingerichtet, Abschnitt 12): „Der Bot scheint zu hängen“, „Zurücksetzen des Kampfes fehlgeschlagen“, „PC-Bildschirm ist gesperrt“.
- :eye: **Stille.** Im Log erscheinen eine Minute oder länger keine Zeilen, und im Spiel passiert nichts. Das ist auch ein Zeichen: Siehe Abschnitt „Häufige Fälle“ unten.

Tags im Log, die auf ein Problem hinweisen:

- `[СТОРОЖ]` — der Bot meinte, er sei hängengeblieben, und hat von selbst neu gestartet.
- `[СЕТЬ]` — scheinbar keine Verbindung zum Spielserver.
- `[ЭКРАН]` — der Computer lässt keinen Screenshot zu (er ist gesperrt).
- `[ОТКАТ]` — Schritte zum Zurücksetzen des Kampfes und seine Fehler (Abschnitt 10).
- `[ВНИМАНИЕ]` — der Bot bittet um Aufmerksamkeit: Pause, geschlossenes Spielfenster.
- `[ОШИБКА]` — etwas ist fehlgeschlagen; daneben steht, was.
- `[ADB]` und `[VISION]` — Verbindung zum Handy und Klicks.

### Was der Bot selbst tut

Hier drückst du nichts. Wisse einfach, dass das normal ist und die Sitzung nicht beschädigt.

- :gauge: **Hängengeblieben: 5 Minuten ohne einen einzigen Raum.** Das ist der „Watchdog“ (so heißt die Überprüfung, die aufpasst, ob der Bot feststeckt). Der Bot schreibt `[СТОРОЖ] Бот 5 мин не прошёл ни одной комнаты ... Тревога 1 из 3.`, speichert einen Screenshot, sendet eine Nachricht in Telegram (falls eingerichtet) und macht einen **„smarten Start“**: Er schaut sich den Bildschirm neu an und entscheidet, wo er weitermacht. Hat es nicht geholfen, gibt es nach weiteren 5 Minuten erneut Alarm. **Der dritte Alarm in Folge** (also etwa 15 Minuten ohne Räume) — der Bot geht in eine sanfte Pause und wartet auf dich. Die Zeit, in der der Bot auf dich gewartet hat (SOS-Fenster, Pause, fremdes Fenster über dem Spiel), zählt der Watchdog nicht.
- :activity: **An einer Stelle feststecken.** Der Teamauswahl-Bildschirm ist nach 30 Sekunden nicht erschienen oder das Ergebnis-Fenster erschien nach 3 Minuten nicht. Dann folgt `[СТОРОЖ] Зависание: ...`, ein Screenshot und derselbe smarte Start, jedoch ohne Alarm in Telegram.
- :globe: **Der Kampf beginnt не (wahrscheinlich keine Verbindung zum Spielserver).** Die Schaltfläche „Auto“ ist gedrückt, aber der Kampf startet nicht. Der Bot versucht es sofort noch zwei Mal, wartet dann und versucht es erneut: nach 30 Sekunden, 1, 2, 4 und 8 Minuten. All das steht im Log als `[СЕТЬ] Бой не начался N раз(а) подряд ... Жду N с и пробую снова.` Hat auch das nicht geholfen (ca. 15 Minuten): Screenshot, Nachricht „Der Bot scheint zu hängen“ und sanfte Pause.
- :rotate-ccw: **Verbindung beim Zurücksetzen des Kampfes verloren.** Der Bot gibt nicht auf, sondern **wartet bis zu 15 Minuten auf das Spiel**: Er schreibt `[ОТКАТ] Бой не загрузился ... Не сдаюсь`, speichert einen Screenshot und meldet einmal pro Minute `Всё ещё жду игру`. Ist die Verbindung wieder da – wird das Zurücksetzen von selbst zu Ende geführt (`Игра снова откликается`). Ist sie nach 15 Minuten nicht zurückgekehrt – „Zurücksetzen des Kampfes fehlgeschlagen“, Nachricht in Telegram und Pause.
- :monitor: **Computer gesperrt (Win+L) oder Bildschirm ausgeschaltet.** Windows erlaubt keine Screenshots und der Bot sieht nichts. Er **stürzt nicht ab**, sondern versucht es alle 2 Sekunden erneut: `[ЭКРАН] Не удаётся сделать снимок экрана ... Похоже, ПК заблокирован`. Länger als eine Minute – eine Nachricht „PC-Bildschirm ist gesperrt“. Hast du entsperrt – `[ЭКРАН] Снимок экрана снова работает`, der Bot macht selbst weiter.
- :layers: **Spielfenster von einem anderen Fenster verdeckt.** Der Bot wartet, bis es wieder im Vordergrund steht (`[ВНИМАНИЕ] Окно игры перекрыто ... Бот ждет фокуса`). Klicke auf das Spielfenster und er macht weiter. Warum das so ist – in Abschnitt 5.
- :target: **Klick ist nicht angekommen.** Wenn sich der Bildschirm 4 Sekunden nach dem Klick nicht verändert hat, klickt der Bot noch einmal: `[VISION] Клик по '...' не зарегистрирован сервером ... Повторяю...`. Solche seltenen Zeilen sind normal: Das Handy „überlegt“ manchmal.
- :smartphone: **Kabelverbindung zum Handy hat kurz gewackelt.** Der Bot schreibt `[ADB] Постоянное соединение с телефоном оборвалось ... Переподключусь при следующем нажатии` und verbindet sich erneut.
- :send: **Telegram-Nachricht konnte wegen des Internets не gesendet werden.** Der Bot wiederholt sie später (Abschnitt 12) und arbeitet weiter.

> [!note] Wie oft der Bot während der Sitzung hängengeblieben ist, siehst du im Block `[ИТОГ]` im Log (Zeile mit dem Wort „зависания“). Seltene Fälle sind kein Problem. Wenn es viele sind, suche die Ursache im Abschnitt „Häufige Fälle“ unten.

### Der Bot ist selbst auf Pause gegangen: Was tun?

Er hat angehalten, weil es без dich не weitergeht. Gehe der Reihe nach vor:

1. **Sieh dir den Spielbildschirm an.** Das Fenster `HeroWarsBot_Arena` показывает, где бот застрял: окно результата, бой, меню паузы, «грибок» загрузки или что-то неожиданное (чужое окно, реклама, запрос игры).
2. **Lies die letzten Zeilen des Logs.** Öffne den Badge „Fehler“ und schau ganz unten nach: Dort steht, почему бот остановился (`[СТОРОЖ]`, `[ОТКАТ] ОШИБКА`, `[СЕТЬ]`).
3. **Bringe das Spiel zurück in den Korridor des Dungeons.** Schließe Überflüssiges, warte, bis der Kampf zu Ende ist oder geladen hat, und gehe zum Bildschirm mit der Tür und dem Fähnchen.
4. **Klicke auf „Fortsetzen“.** Der Bot sieht sich erneut um (smarter Start) und macht weiter.

> [!note] Eine Pause nach einem fehlgeschlagenen Zurücksetzen kommt auch vor: Der manuelle Kampf ist bereits zu Ende gegangen, „Noch einmal“ gibt es auf dem Ergebnis-Fenster nicht mehr und ein Zurücksetzen ist nicht möglich. Das Ergebnis-Fenster bleibt auf dem Bildschirm – du musst nichts schließen, nach „Fortsetzen“ klickt der Bot selbst auf „OK“. Sieh dir auf diesem Fenster an, wer überlebt hat.

> [!tip] Der Bot geht nicht wegen jeder Kleinigkeit auf Pause, sondern wenn er es versucht hat und es не geklappt hat. Finde daher vor dem Klick auf „Fortsetzen“ heraus, **was genau** schiefgelaufen ist. Wenn die Ursache bestehen bleibt (kein Internet, Spiel geschlossen), geht der Bot nach einigen Minuten erneut auf Pause.

### Häufige Fälle: Was prüfen und was tun?

**Der Bot drückt nichts, und im Log ist es ruhig.** Wahrscheinlich sieht er das Spiel nicht или kann darin nichts finden. Überprüfe der Reihe nach:

1. **Das Spielfenster ist da.** Es heißt `HeroWarsBot_Arena`, ist weder minimiert noch geschlossen. Wenn das Fenster fehlt, schreibt der Bot nichts darüber, sondern prüft es stillschweigend alle halbe Sekunde. Stille im Log bei verschwundenem Fenster ist daher völlig normal. Klicke auf „Handy verbinden“: Das Fenster wird erneut geöffnet.
2. **Die Fenstergröße wurde не verändert.** Der Bot misst das Fenster einmal beim Start und nutzt danach diese Maße. Hast du das Fenster nach dem Start vergrößert, maximiert oder verschoben – stoppe den Bot (F10), klicke auf „Größe des Spielfensters zurücksetzen“ und erneut auf „Farmen starten“. Details dazu in Abschnitt 3.
3. **Im Spiel ist der Korridor des Dungeons**, und не das Menü, der Laden, ein anderes Event oder ein Werbefenster.
4. **Die Sprache des Programms stimmt mit der Sprache des Spiels überein** (zwei Buchstaben unten in der linken Leiste). Andernfalls erkennt der Bot die Schaltflächen не.
5. **Nichts verdeckt das Spielfenster.** Sobald ein anderes Fenster über dem Spiel liegt, wartet der Bot auf den Fokus.

**Der Bot „sieht“ und drückt, aber im Spiel passiert ничего.** Im Log erscheinen nacheinander Zeilen wie „Клик по ... не зарегистрирован сервером ... Повторяю...“. Das означает, dass der Klick-Befehl das Handy не erreicht. Prüfe:

- Es sind **beide** Debugging-Einstellungen auf dem Handy aktiviert: „USB-Debugging“ und „USB-Debugging (Sicherheitseinstellungen)“. Ohne die zweite ist zwar ein Bild da, aber Klicks funktionieren не (Abschnitt 2).
- Das Handy ist entsperrt, das Kabel sitzt fest. Versuche einen anderen USB-Anschluss.
- In der Eingabeaufforderung zeigt `adb devices` neben dem Handy `device` an und nicht `unauthorized` или eine leere Liste.
- Wenn das не geholfen hat: Stoppe den Bot, klicke auf „scrcpy neu starten“, dann auf „Farmen starten“.

**Der Bot klickt an die falsche Stelle или verwechselt Titanen.** Meistens hat das Spielfenster die falsche Größe или wurde nach dem Start angetippt (Größe zurücksetzen, wie oben). Ist die Größe richtig, aber der Bot klickt trotzdem daneben – speichere einen Screenshot dieses Moments und sende ihn zusammen mit dem Log an den Autor (siehe unten).

**Das Programmfenster „reagiert не“.** Das Programm überwacht sich selbst: Wenn das Fenster 5 Sekunden lang не reagiert, schreibt es in eine Datei, bei welcher Codezeile es hängengeblieben ist. Die Datei liegt in `bot_data/debug/` und heißt `ui_freeze_<дата>_<время>.txt`. Was tun?

1. **Warte eine Minute.** Oft erwacht das Fenster von selbst wieder zum Leben: Es ist mit schwerer Arbeit beschäftigt.
2. **Der Bot arbeitet unabhängig vom Fenster.** Du musst ihn stoppen, aber die Schaltflächen reagieren не? Drücke Strg+Umschalt+Q: Auf diese Taste hört der Bot selbst und не das Programmfenster (Abschnitt 6).
3. **Ist es не aufgewacht – schließe das Fenster über das X.** Lässt es sich не schließen – über den Task-Manager (Strg+Umschalt+Esc). Schau danach dort nach, ob `HeroWarsBot.exe` или `python` noch in der Liste steht: Wenn ja, schließe auch diesen Prozess, sonst drückt der Bot ohne Fenster im Spiel weiter.
4. **Sende die Datei `ui_freeze_...txt` an den Autor.** Darin stehen nur Dateinamen und Codezeilen des Programms, ничего Persönliches.

**Der Bot hat angehalten, obwohl du ihn не gestoppt hast.** Öffne die Karte „Sitzungsbilanz“ auf der Hauptseite (Schaltfläche „Details“) und schau nach der Ursache:

- „scrcpy-Fenster geschlossen“ — das Spielfenster wurde geschlossen или ist verschwunden (Kabel herausgezogen, Handy hat sich gesperrt). Verbinde das Handy erneut.
- „der Bot hat sich beendet“ — der Prozess endete без offensichtlichen Grund. Wenn Telegram eingerichtet ist, kam die Bilanz dorthin; если нет, suche im Log nach der Zeile `[ОШИБКА] Бот остановился из-за ошибки:` und dem Text darunter.
- „Пак не найден в правилах“ — für den Raum wurde kein Hauptteam festgelegt. Öffne „Regelmeister“ → „Basis und Räume“ und lege es für alle vier Räume fest (Abschnitt 7).
- „Ошибка: ...“ — das Programm ist abgestürzt. Sende das Log an den Autor (siehe unten).

> [!warning] Nach „STOPP“ (F10) schafft es der Bot не mehr, den Block `[ИТОГ]` zu schreiben, und sendet keine Bilanz an Telegram: Er wird sofort beendet (Abschnitt 6). Das ist kein Fehler.

**Handy ist „eingeschlafen“ или der Bildschirm ging aus.** Das Programm startet scrcpy mit dem Modus „Handy не einschlafen lassen“ (`--stay-awake`). Die Schaltfläche „Telefonbildschirm ausschalten“ schaltet nur den **Bildschirm** aus: Das Spiel läuft weiter und der Bot sieht alles. Wenn sich das Handy jedoch gesperrt hat или vom Kabel getrennt wurde, erscheint im Spielfenster der Sperrbildschirm или Leere, und der Bot findet ничего. Entsperre das Handy, prüfe das Kabel und klicke auf „scrcpy neu starten“.

**Es kommen keine Nachrichten in Telegram an.** Wahrscheinlich wurde bei deinem Bot не auf „Starten“ gedrückt oder das Token/die Chat-ID ist falsch – Erklärung in Abschnitt 12. Der Bot funktioniert dabei wie gewohnt weiter.

**Der Bot setzt die falschen Titanen ein или entscheidet anders, als du wolltets.** Das ist kein Fehler, sondern liegt an den Regeln: Gehe die Abschnitte 7–11 durch (Teams, Schwellenwerte, Regeln, „Bot entscheidet selbst“). Die Entscheidung des Bots lässt sich im Log immer anhand der Zeilen `[ТАКТИКА]` nachvollziehen.

### Wo Logs und Screenshots liegen

Die Schaltfläche **„Bot-Ordner“** auf der Seite „Über das Programm“ öffnet den Ordner, aus dem das Programm gestartet wurde. Darin liegen Dateien, die der Bot selbst erstellt. Das Wichtigste befindet sich im Ordner `bot_data`:

- :file-text: `bot_data/logs/bot_log_<дата>_<время>.txt` — **vollständiges Log jedes Bot-Starts.** Der Bot schreibt es selbst, Zeile für Zeile, daher bleibt es selbst nach einem Absturz oder Schließen des Programms erhalten. Das ist die wichtigste Datei für die Analyse.
- :gauge: `bot_data/logs/timings_<дата>_<время>.csv` — wie lange jeder Raum gedauert hat (Korridor, Aufstellung, Kampf, Ergebnis).
- :swords: `bot_data/logs/battle_log_<дата>_<время>.jsonl` und `battle_log.csv` — Kampfverlauf: Raum, Gegner, Team, Ergebnis, TP und Energie der Titanen.
- :image: `bot_data/debug/` — **Screenshots zur Analyse.** Der Name verrät, was passiert ist: `stuck_...` — hängengeblieben, `sos_...` — SOS-Fenster, `rollback_wait_...` — hat während des Zurücksetzens auf das Spiel gewartet, `rollback_fail_...` — Zurücksetzen fehlgeschlagen, `start_fail_...` — Kampf hat nicht begonnen, `result_unreadable_...` — Ergebnis-Fenster konnte nicht gelesen werden. Danach folgen Raumnummer, Element und Uhrzeit (`stuck_комната12_water_2026-10-19_14-03-21.png`). Dort liegt auch `ui_freeze_...txt`, falls das Programmfenster hängengeblieben ist.

> [!warning] Der Bot räumt Altes selbst auf: Beim Start bleiben in `bot_data/logs/` jeweils 20 neueste Dateien jeder Art (`.txt`, `.jsonl`, `timings_*.csv`) und in `bot_data/debug/` 50 neueste Screenshots erhalten. Wenn du die Logs nach einer problematischen Nacht aufbewahren möchtest, **kopiere sie vor dem nächsten Start des Bots an einen anderen Ort**. Genauso wird das Log gelöscht, das du mit der Schaltfläche „Log speichern“ im Standardordner gespeichert hast: Speichere es an einem anderen Ort, zum Beispiel auf dem Desktop.

> [!warning] Lösche oder benenne `profile.yml` (deine Einstellungen und Telegram) sowie den Ordner `bot_data` не um: Darin befinden sich Statistiken, vom Bot gelernte Regeln und der Kampfverlauf. Gelöscht werden dürfen nur `bot_data/debug` und alte Logs, und auch das nur, wenn sie не mehr benötigt werden.

### Wie man dem Autor das Log sendet

Wenn sich ein Problem не lösen ließ, ist der schnellste Weg, dem Autor mitzuteilen, was passiert ist.

1. **Merke dir, wann es war.** Die Uhrzeit und die ungefähre Anzahl der Räume (`[СТАТИСТИКА] Комнат: N`) helfen dabei, die richtige Stelle im langen Log zu finden.
2. **Finde die Dateien.** Das Log — `bot_data/logs/bot_log_...` aus dieser Nacht, Screenshots — aus `bot_data/debug/` mit ähnlicher Uhrzeit im Namen und bei einem Einfrieren des Fensters zusätzlich `ui_freeze_...txt`.
3. **Klicke auf „Log an den Autor senden“** unter dem Log auf der Hauptseite. Das Programm bietet an, den aktuellen Inhalt des Logs zu speichern (das ist die Datei `gui_log_...txt`), und öffnet danach dein E-Mail-Programm mit einer vorgefertigten Nachricht an den Autor.
4. **Füge die Dateien selbst als Anhang hinzu.** Das Programm kann keine Dateien an die E-Mail anhängen: Es öffnet sie nur. Füge `gui_log_...txt` oder `bot_log_...txt`, Screenshots und (falls vorhanden) `ui_freeze_...txt` bei.
5. **Beschreibe in Worten:** was du getan hast, was du erwartet hast, was du gesehen hast und wann das war. Ein einzelner Satz wie „funktioniert nicht“ hilft dem Autor kaum weiter.

> [!warning] **Füge niemals** `profile.yml` und `bot_data/profile.yml.bak` bei: Darin befindet sich das Token deines Telegram-Bots. Sende auch einen Screenshot des Fensters „Telegram-Einstellungen“ nur mit verborgenem Token (mit Punkten).

> [!note] E-Mail wurde не geöffnet (kein E-Mail-Programm eingerichtet)? Auf der Seite „Über das Programm“ gibt es die Schaltfläche „Dem Autor schreiben“: Konnte die E-Mail не geöffnet werden, kopiert sie die Adresse in die Zwischenablage und du kannst von jedem beliebigen E-Mail-Konto schreiben.

### Wenn ничего не hilft

Gehe vom Einfachen zum Komplexen vor und prüfe nach jedem Schritt, ob der Bot wieder läuft:

1. **„Pause“ → Bringe das Spiel zurück in den Korridor → „Fortsetzen“.**
2. **„STOPP“ (F10) → „Farmen starten“.** Der Bot beginnt mit einem smarten Start und findet selbst heraus, wo er ist.
3. **Stoppe den Bot und klicke auf „scrcpy neu starten“.** Danach erneut „Farmen starten“.
4. **Schließe das Programm und öffne es erneut.** Wenn das Handy hängengeblieben ist, ziehe das Kabel heraus und stecke es wieder ein.
5. **Starte den Computer und das Handy neu.** Klingt wie ein Scherz, löst aber die Hälfte aller seltsamen Probleme.

Die Sitzungsziele (Zeit, Räume, Etagen, Titanit) werden nach einem Neustart von neuem gezählt, aber Statistiken, Teams und Regeln bleiben erhalten: Sie liegen in Dateien.

> [!done] Jetzt weißt du, wie sich der Bot selbst rettet, was zu tun ist, wenn er angehalten hat, und wie man ein Log sammelt und sendet. Es bleibt noch der letzte Abschnitt: Über das Programm und wie du das Projekt unterstützen kannst. [Nächster Abschnitt →](#15)

## Über das Programm und Unterstützung

Die letzte Seite im linken Menü ist „Über das Programm“. Sie handelt vom Programm selbst: welche Version du hast, ob alles vorhanden ist, wohin du dem Autor schreiben kannst und wie du „Danke“ sagen kannst. Du musst darauf nichts einstellen, dafür befinden sich hier zwei nützliche Schaltflächen: „Nach Updates suchen“ und „Bot-Ordner“.

### Was auf der Seite ist

- :shield-check: **Programmkarte** oben. Name „Hero Wars: Knowledge Engine Bot“, daneben — **Versionsnummer** (zum Beispiel `v1.6.1`) und das Label `Beta`. „Beta“ bedeutet „wird in der Praxis getestet“: Das Programm funktioniert, aber der Autor entwickelt es noch weiter und Fehler sind möglich. Unter dem Namen — eine kurze Beschreibung. Rechts befinden sich vier Schaltflächen, dazu unten mehr.
- :user: **„Autor und Lizenz“**: Name des Autors, seine E-Mail-Adresse und Lizenz. Klicke auf die E-Mail-Adresse — eine Nachricht wird geöffnet.
- :monitor: **„Status der Komponenten“**: Überprüfung, ob auf dem Computer alles Notwendige für den Betrieb vorhanden ist. Details unten.
- :heart: **„Das Projekt unterstützen“**: Möglichkeiten, sich beim Autor zu bedanken. Das ist freiwillig.

> [!tip] Nenne dem Autor die Version, wenn du über ein Problem schreibst: Sie zeigt sofort, welche genaue Programmversion du nutzt. Die Version befindet sich in der Karte oben neben dem Namen.

### Vier Schaltflächen in der Karte

1. **„Nach Updates suchen“.** Öffnet im Browser die Release-Seite des Projekts auf GitHub (GitHub ist die Website, auf der der Autor das Programm speichert; ein „Release“ ist eine fertige Version zum Herunterladen). Vergleiche dort die neueste Nummer mit deiner. Ist sie neuer – kannst du aktualisieren; ist sie gleich – hast du die aktuellste Version.
2. **„Bot-Ordner“.** Öffnet im Windows-Explorer den Ordner, aus dem das Programm gestartet wurde: genau den, in dem deine Einstellungen und Daten liegen. Nützlich, wenn du Dateien kopieren oder ein Log finden musst.
3. **„Dem Autor schreiben“.** Öffnet eine E-Mail an den Autor in deinem E-Mail-Programm. Wenn auf dem Computer kein E-Mail-Programm installiert ist, wird die E-Mail не geöffnet. In diesem Fall legt das Programm die Adresse selbst in die Zwischenablage (der Zwischenspeicher, aus dem man mit Strg+V einfügt) und meldet unten im Fenster: „Konnte не geöffnet werden – in die Zwischenablage kopiert“. Füge die Adresse in eine E-Mail von einem beliebigen Konto ein.
4. **„Projekt-GitHub“.** Öffnet die Hauptseite des Projekts auf GitHub: Dort befinden sich Quellcode und Beschreibung.

> [!note] Das Programm **sucht von selbst не im Internet nach Updates**: „Nach Updates suchen“ öffnet nur die Seite, und du entscheidest. Das ist so gewollt, damit sich без dein Wissen ничего не ändert.

### Wie man das Programm aktualisiert

Ein Update wird не „drüberinstalliert“ — du lädst die neue Version herunter und überträgst deine Daten hinein. So gehen deine Teams und Statistiken не verloren.

1. **Stoppe den Bot und schließe das Programm.** Das X-Symbol des Fensters fragt bei laufendem Bot, ob er gestoppt werden soll.
2. **Lade die новая Version herunter** auf der Release-Seite (Schaltfläche „Nach Updates suchen“) und entpacke sie in einen neuen Ordner, не über den alten.
3. **Übertrage deine Daten.** Kopiere aus dem alten Ordner die Datei `profile.yml` und den gesamten Ordner `bot_data` in den neuen Ordner. Ohne sie startet das neue Programm „bei Null“: leere Einstellungen und leere Statistiken.
4. **Starte das neue Programm** und schau unter „Über das Programm“ nach: Die Versionsnummer sollte neu sein und alle drei Komponenten in Ordnung.
5. **Lösche den alten Ordner vorerst не.** Arbeite ein paar Tage mit der neuen Version. Wenn alles gut ist — kannst du ihn entfernen.

> [!warning] Kopiere не einzelne Dateien aus `bot_data`, die du für nötig hältst, sondern übertrage den Ordner als Ganzes: Die vom Bot gelernten Regeln, der Kampfverlauf und die Statistiken hängen miteinander zusammen und können не neu erstellt werden.

### „Status der Komponenten“

Das Programm prüft selbst, ob alles vorhanden ist, без das der Bot не funktioniert. Die Prüfung läuft im Hintergrund bei jedem Aufruf der Seite. Während sie läuft, steht dort „prüfe…“.

- :smartphone: **ADB** — der Dienst, über den der Computer Klicks auf dem Handy ausführt. Es muss „gefunden“ dastehen.
- :monitor: **scrcpy** — das Programm, das den Handybildschirm in einem Fenster auf dem Computer anzeigt. Es muss „gefunden“ dastehen.
- :image: **Vorlagen-Datenbank** — Musterbilder von Schaltflächen und Titanen, anhand derer der Bot erkennt, was sich auf seinem Bildschirm befindet. Es muss „geladen“ dastehen.

Was tun, wenn etwas rot angezeigt wird:

- **ADB или scrcpy „не найден“.** Das bedeutet, der Ordner mit ihnen wurde не zu `PATH` hinzugefügt (die Liste der Orte, an denen Windows nach Programmen sucht). Wie das geht — in Abschnitt [„Was du benötigst und Installation“](#2). Schließe das Programm nach der Bearbeitung von `PATH` und öffne es erneut: Ein bereits laufendes Programm sieht den neuen `PATH` не.
- **Vorlagen-Datenbank „не найдена“.** Aus dem Programmordner sind Dateien verschwunden. Meistens wurde das Archiv не vollständig entpackt oder der Virenscanner hat etwas entfernt. Entpacke das Archiv erneut in einen neuen Ordner und übertrage `profile.yml` und `bot_data` wie bei einem Update.

### Was im Bot-Ordner liegt и что нельзя удалять

Öffne ihn mit der Schaltfläche „Bot-Ordner“. Es gibt dort viele Dateien, aber du brauchst nur einige davon. Der Rest ist systembedingt und wird vom Programm für den Betrieb benötigt.

- :file-text: `HeroWarsBot.exe` — das Programm selbst. Der Bot läuft ebenfalls daraus, er hat keine separate Datei. Alle anderen Dateien und Ordner daneben (`guide`, `ui`, Bibliotheken, Dateien mit der Endung `.dll` und andere) sind Teil des Programms. **Lösche или benenne ничего davon um**, sonst lässt es sich не mehr starten.
- :file-text: `profile.yml` — deine Einstellungen: Sitzungsziel, Schwellenwerte, Telegram. **Darin befindet sich das Token deines Telegram-Bots, sende es daher niemandem.** Erscheint nach dem ersten Klick auf „Einstellungen speichern“.
- :folder: `bot_data` — alles, was das Programm und der Bot selbst gespeichert haben. Das ist das **Wertvollste**, was du hast. Darin:
  - `stats.json` — Statistiken (Seite „Statistiken“);
  - Ordner `rules` — deine Teams und Regeln, einschließlich der vom Bot gemerkten;
  - Ordner `logs` — Kampfverlauf und Bot-Log (`bot_log_...txt`);
  - Ordner `debug` — Screenshots zur Analyse (SOS-Fenster, Aufhänger, fehlgeschlagene Rücksetzungen);
  - `titan_state.json` — Gesundheit und Energie der Titanen für den Spieltag;
  - `profile.yml.bak` — Sicherung der Einstellungen. Daraus funktioniert „Wiederherstellen / Zurücksetzen“ im „Regelmeister“. **Darin befindet sich ebenfalls das Telegram-Token**;
  - `ui_settings.json` — ausgewählte Fenstersprache;
  - `sos_info.json`, `temp_sos.png`, `temp_test.png` — kleine Arbeitsdateien für Telegram-Nachrichten.
- :pause: `pause.flag` — die „Pause-Flagge“. Erscheint, wenn sich der Bot in einer sanften Pause befindet. Wenn sie vom letzten Mal übrig geblieben ist, löscht das Programm sie beim Start selbst.

> [!warning] **Lösche und benenne** `profile.yml` und `bot_data` **не um**. Wenn du `bot_data` löschst, gehen Statistiken, Teams, Regeln und alles, was der Bot gelernt hat, verloren. Wenn du unbedingt Speicherplatz freimachen musst, kannst du den Inhalt von `bot_data/debug` und alte Logs in `bot_data/logs` löschen. Der Bot selbst behält jedoch nur die 20 neuesten Logs und 50 neuesten Screenshots, sodass Speicherplatz meist kein Problem ist.

> [!tip] **Erstelle einmal pro Woche ein Backup.** Kopiere `profile.yml` und den Ordner `bot_data` auf einen USB-Stick oder in die Cloud. Wenn der Computer kaputtgeht или du Windows neu installierst, lädst du das Programm neu herunter und stellst Teams sowie Statistiken aus dem Backup wieder her. Das Telegram-Token ist im Backup enthalten — bewahre es bei dir auf und не in einem freigegebenen Ordner.

### Autor und Lizenz

Das Programm wurde von **Platon Petrunin** entwickelt und wird von ihm gepflegt. Fragen, Fehler und Ideen — Schaltfläche „Dem Autor schreiben“ или E-Mail-Adresse in der Karte „Autor und Lizenz“.

Die Lizenz heißt **PolyForm Noncommercial 1.0.0**. In einfachen Worten:

- :check: Für sich selbst, für das eigene Spiel kostenlos nutzen — beliebig oft;
- :check: Den Code studieren und für sich selbst anpassen — ebenfalls erlaubt;
- :x: **Kein Geld damit verdienen**: Das Programm oder seine `.exe` verkaufen, unter anderem Namen als das eigene ausgeben, in kostenpflichtige Dienste einbinden. Dafür ist eine schriftliche Genehmigung des Autors erforderlich.

> [!note] Dies ist eine kurze Zusammenfassung, kein rechtlicher Text. Bei ungewöhnlichen Fällen (zum Beispiel, если ты хочешь раздать программу друзьям или сообществу), schreibe zuerst dem Autor. Der vollständige Lizenztext befindet sich in der Datei `LICENSE` im Projekt auf GitHub.

### Wie du das Projekt unterstützen kannst

Das Programm ist kostenlos und der Autor entwickelt es in seiner Freizeit. Wenn es dir Zeit und Nerven spart, kannst du dich mit einer Spende bedanken. Das ist **freiwillig**: Der Bot funktioniert absolut gleich, egal ob du etwas gezahlt hast или не, und es gibt keinerlei „kostenpflichtige Funktionen“.

Unten auf der Seite „Über das Programm“ gibt es три Blöcke:

1. **„Kryptowährung“.** Drei Wallets: `USDT · TRC20`, `Bitcoin · BTC` und `Ethereum · ETH`. Die vollständige Adresse ist im Feld sichtbar. Du kannst sie mit der Schaltfläche „Kopieren“ rechts kopieren (unten erscheint „Adresse kopiert“), per Doppelklick auf das Feld (wählt alles aus) oder per Rechtsklick — „Kopieren“.
2. **„Spende über Telegram“.** Drei Zeilen — Rubel (`RUB`), Euro (`EUR`) und Dollar (`USD`). In jeder gibt es zwei Schaltflächen: **„App“** öffnet die Zahlung in der Telegram-App, **„Browser“** — im Browser, falls Telegram не installiert ist. Wähle die Währung, die für dich am bequemsten ist.
3. **„Direktüberweisungen“.** Schaltflächen „Auf Boosty unterstützen“ und „YooMoney (RUB)“: Es öffnen sich die Seiten dieser Dienste, danach geht es wie bei einer normalen Zahlung weiter.

> [!warning] **Sei vorsichtig mit Kryptowährung.** Überweise nur im Netzwerk, das neben der Wallet angegeben ist: Für `USDT` ist das `TRC20`, kein anderes. Geld, das an das falsche Netzwerk gesendet wurde, **kann не zurückgeholt werden**. Nimm die Adresse nur aus dem Programm über die Schaltfläche „Kopieren“: Auf Websites und in fremden Nachrichten könnte sie ausgetauscht worden sein. Sende beim ersten Mal einen kleinen Betrag.

### Häufige Fragen

- **Meine Version ist alt — ist das schlimm?** Nein. Das Programm hört не auf zu funktionieren, nur weil eine новая Version erschienen ist. In neuen Versionen sind jedoch meist Fehler behoben, schau daher alle paar Wochen auf der Release-Seite vorbei.
- **„Bot-Ordner“ wurde не geöffnet.** Es erscheint die Meldung „Ordner konnte не geöffnet werden“. Öffne ihn selbst: Explorer, Ordner, in den du das Programm entpackt hast.
- **Warum gibt es keine Schaltfläche „Aktualisieren“?** Das Programm lädt von selbst ничего herunter, um deine Einstellungen не ungefragt zu beschädigen. Du aktualisierst selbst nach den oben genannten Schritten.
- **Ändert sich etwas, если я не поддержал проект?** Nichts. Der Bot funktioniert für alle genau gleich.

> [!done] Das ist der letzte Abschnitt. Jetzt weißt du alles, um den Bot zu starten, ihn für dich einzurichten, seine Entscheidungen zu verstehen und Korrekturen vorzunehmen, falls etwas schiefgelaufen ist. Viel Spaß beim Spielen! Falls noch Fragen offen sind: die Schaltfläche „Dem Autor schreiben“ befindet sich unten.
