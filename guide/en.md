# Hero Wars: Knowledge Engine Bot

Hi! This is a program that clears the Titan Dungeon in Hero Wars for you automatically. You turn it on, go about your business — and it opens doors, builds teams, and collects rewards.

This guide is written so that anyone can understand it. We explain unfamiliar words right away, and at the end of each section we tell you where to go next.

## What the bot can do

The bot is not a mindless "clicker". It looks at the game screen just like you would, and decides what to do next on its own. Here is what it can do:

- :eye: **Sees the screen.** Every fraction of a second, it takes a screenshot of the game window and recognizes buttons, doors, and enemies.
- :door-open: **Chooses a door.** It enters rooms in the order you specified, bypassing those that are currently dangerous.
- :users: **Sets up the team.** For each room, it has a "pack" (that's what we call a team of five titans). The bot places the titans in their positions automatically.
- :heart-pulse: **Monitors health.** After each battle, it reads titan HP (health) and energy, deciding if the pack is ready for the next fight.
- :swords: **Calls you if the fight went badly.** An "Intervention required" window appears: you can replay the battle with another pack, accept it, or clear it manually. If you stepped away from the computer, the bot can decide on its own.
- :chart-no-axes-column: **Learns from its battles.** It remembers which pack defeated which enemies and sets it up immediately next time.
- :send: **Writes in Telegram.** If you want, it will send a session summary and an alert when something goes wrong.

> [!note] Example. Araji entered the battle with 36% health and dropped to 8% after the fight. The bot sees this, understands that the battle went badly, and either asks you or automatically rolls back the fight and replays it with another pack.

### What the bot does not do

- It clears **only the Titan Dungeon**. It does not know other game modes.
- It does **not play "in the cloud"**. The game runs on your Android phone, and a Windows PC looks at the phone screen and clicks on it via a USB cable. You need both a phone and a computer.
- It is not a wizard: if connection to the game is lost, it patiently waits for it to return and informs you about it.

### Is this safe for my account?

The bot tries to behave like a real person, not a robot:

- every click lands on a **random point** of the button, rather than the exact same spot;
- before clicking, it holds a **reaction pause** — from 0.3 to 0.8 seconds after the button appears;
- it clicks **no more than twice a second**.

> [!warning] No software can give a full guarantee: game rules are set by its publisher. The bot does nothing "inhumanly fast", but the decision whether to use it remains yours.

### What's next in the guide

- **What you need and installation** — what to buy and set up once.
- **Connecting the phone** — first farming run.
- **Main and mini-bar** — how to read the window and the small bar below the game.
- **Pause and stop** — buttons and hotkeys.
- **Rules Master** — how to teach the bot your packs and door order.
- **When a fight goes badly** — intervention windows and how the bot decides on its own.
- **Telegram, statistics, if something goes wrong** — everything else.

> [!done] Now you know what the bot can do. Next is what needs to be installed once. [Next section →](#2)

## What you need and installation

This is done **once**. Afterwards, you just launch the program with a double-click. Spend about fifteen minutes on this — it will be easy after that.

### What you need to have

- :monitor: **Windows computer.** The program and bot run on it.
- :smartphone: **Android phone with Hero Wars.** The game runs on the phone, while the computer looks at its screen and clicks on it.
- :terminal: **USB cable.** Preferably the one used to charge the phone and transfer files: there are "charge-only" cables through which the computer will not see the phone.
- :folder: **Program archive** (`.zip` file containing `HeroWarsBot.exe`).

> [!note] The game stays on the phone. The bot doesn't install anything extra into it or touch game files: it only looks at the screen and clicks on it just like you would with your finger.

### Step A. Unpack the program

1. **Unpack the archive** — right-click it and select "Extract All...". Choose a simple folder without non-English characters, for example `C:\HeroWarsBot`.
2. **Check that the files are in place** — `HeroWarsBot.exe` should be in the folder alongside other files and folders.

> [!warning] Unpack the archive first, and only then run the program. If you open `.exe` directly from the archive, the rest of the program files will be unavailable, and it won't work properly.

> [!tip] This folder is the bot's "home". Next to `HeroWarsBot.exe`, it will create its own files: settings, statistics, battle history. Therefore, do not move `.exe` separately from the other files, and if you move locations — move the entire folder.

### Step B. Install scrcpy

scrcpy is a small program that shows your phone screen in a window on your computer. The bot "looks" at this exact window. Together with it, **adb** is installed — a helper through which the bot clicks on the phone screen.

1. **Download scrcpy** — on the [project page](https://github.com/Genymobile/scrcpy/releases), choose the latest version for Windows (`.zip` archive with "win64" in the name).
2. **Unpack the archive** — best into a simple folder without spaces or non-English characters, for example `C:\scrcpy`. Inside there should be `scrcpy.exe` and `adb.exe` files.
3. **Add the folder to PATH** — this way Windows will know where to find these programs. How to do this, see below.

**How to add a folder to PATH:**

1. **Open settings** — press the Windows key, type "environment variables" and select "Edit the system environment variables".
2. **Find "Path"** — in the window that opens, click "Environment Variables", select the `Path` line in the upper list and click "Edit".
3. **Add the folder** — click "New", enter `C:\scrcpy` (your folder if it is different), and close all windows with the "OK" button.

> [!note] PATH is a list of folders where Windows looks for programs when you call them by name. Add a folder to the list — and `scrcpy` with `adb` can be found from anywhere.

### Step C. Verify that scrcpy is installed

1. **Open "Command Prompt"** — Windows key, type `cmd`, press Enter. If the window was already open before installation, close it and open it again: the old one doesn't know about new folders.
2. **Check scrcpy** — type `scrcpy --version` and press Enter. The program version should appear.

If Windows writes "is not recognized as an internal or external command" instead of the version, it means the folder was not added to PATH. Go back to step B and check that the folder containing `scrcpy.exe` is entered in PATH.

### Step D. Set up your phone

The phone must allow the computer to control it. This is called "USB debugging" (a mode designed for app developers). The bot uses it to click on the screen.

1. **Open developer mode** — go to "Settings" → "About phone" and tap "Build number" **7 times in a row**. The phone will say that you are now a developer.
2. **Find "Developer options"** — this item will appear in settings (sometimes inside "System" or "Additional settings").
3. **Enable two settings** — "USB debugging" **and** "USB debugging (Security settings)".
4. **Connect the cable** — when the phone asks "Allow USB debugging from this computer?", check "Always allow" and tap "OK".

!["Developer options" section with two debugging settings enabled](images/usb_debug.png)

> [!warning] Enable **both** settings. If only the first one is enabled, the image from the phone will reach the computer, but clicks won't reach the game: the bot will "tap", but the game won't register anything.

Now let's check the connection. Connect the phone with a cable, open "Command Prompt" and type `adb devices`. There should be a line in the list with the word `device` next to the phone number.

- :check: `device` — everything is good, the phone is ready.
- :triangle-alert: `unauthorized` — the phone is waiting for your authorization. Look at its screen and tap "Allow".
- :triangle-alert: list is empty — the computer cannot see the phone. Try another cable or a different USB port.

### Step E. First program launch

1. **Open the program folder** — the one where you unpacked the archive.
2. **Double-click `HeroWarsBot.exe`** — the program window will open.
3. **Look around** — on the left is a section bar, in the middle is the main page. While the phone is not connected, the header says "Waiting for phone" — this is normal.

> [!tip] Always launch the program from its folder (or create a shortcut for `HeroWarsBot.exe`: right-click → "Send to" → "Desktop"). Then it will find its settings and files.

> [!done] Everything is ready: the program is unpacked, scrcpy and phone are configured. Now let's connect the phone and launch the first farming run. [Next section →](#3)

## Connecting the phone and first farm

Now we'll connect the phone and launch the bot for the first time — everything will take about five minutes. First, remember: there will be **two windows** on the monitor.

- :monitor: **Program window** — the one where you are reading this guide. It contains buttons, settings, and the log (that's what we call the message feed where the bot records what it does).
- :smartphone: **Game window** — a "mirror" of the phone screen on the monitor, named `HeroWarsBot_Arena`. The bot "looks" into this exact window.

### What's on the main page on first launch

Until you save settings for the first time, the main page (first button on the left bar) has a "Getting started" card with the subtitle "3 steps · about 5 minutes".

![First launch: "Getting started" card, red label "Waiting for phone..." and blue button "Connect phone"](images/connect_phone.png)

- :smartphone: **"Connect your phone"** — marked with the word "now". When the phone connects, the step number will change to a green checkmark. That's what we'll do right now.
- :sliders-vertical: **"Check the packs for each room"** — the link "Open →" leads to "Rules Master" (second button on the left bar, slider icon). There you tell the bot which titans to enter each room with.
- :send: **"Set up Telegram for SOS"** — optional. The bot will message you on Telegram if it needs help.

> [!warning] Packs are the most important thing before the first farming session. The bot sets up for each of the four rooms (water, earth, fire, and mix) the pack written in the "Rules Master", and it cannot guess your titans. How to set this up is covered in the "Rules Master" section later in the guide. The "Getting started" card will disappear when you save settings in the "Rules Master" for the first time.

### Step A. Connect your phone

1. **Prepare your phone** — connect it with a cable and unlock the screen. Both USB debugging settings must be enabled, as shown in [section 2](#2).
2. **Click "Connect phone"** — this is the large blue button on the top right. While the program searches for the phone, it says "Connecting". It can take up to 20 seconds.
3. **Find the game window** — a new `HeroWarsBot_Arena` window with the phone screen will appear. Don't see it? It might have hidden behind the program window: look for it on the taskbar at the bottom of the screen.
4. **Check the header banner** — the red "Waiting for phone..." should turn green: "connected". And the blue button will turn into a green "Start farming". (The header is the top bar of the window, the banner is the rectangle with text.)

![Phone connected: green label "connected", button "Start farming" and game window nearby](images/phone_connected.png)

If the window didn't appear and the log says "scrcpy window did not appear or utility not found!", check in order:

- :smartphone: Phone screen is unlocked, cable is plugged in firmly. Try another USB port.
- :terminal: In the command prompt, `adb devices` shows the word `device` next to your phone. If it says `unauthorized` — allow debugging on the phone screen.
- :terminal: In the command prompt, `scrcpy --version` responds with a version. Doesn't respond? The scrcpy folder was not added to PATH — go back to [section 2](#2). After editing PATH, close and reopen the program.

### Step B. Go to the Dungeon hallway

Titan Dungeon is a game mode where you descend floors and fight enemies in each room. The **hallway** is the screen between battles: a door with a flag is visible on it, and nothing else is open. The bot starts from the hallway.

1. **Open the game** — launch Hero Wars on your phone and enter the Titan Dungeon.
2. **Stand in the hallway** — if a battle is ongoing, finish it manually and close the result window. You need a calm screen with a door and flag.

![Titan Dungeon hallway: flag is visible near the door](images/dungeon_corridor.png)

> [!warning] Do not start farming in the middle of a battle. First, the bot inspects the screen and cleans up: if it sees a battle — it will retreat from it; if it sees a result window with a "Try again" button — it will cancel that battle and replay the room; if it sees team selection — it will complete the battle and immediately cancel it. It will work afterwards, but your victory will be wasted.

### Step C. Start farming

> [!warning] **The program language must match the game language.** Buttons with text ("Fight", "OK", "Try again") and the flag near the door are recognized by the bot using images in the language selected in the program. This is the button with two letters ("RU") at the bottom of the left bar. If the game is in Russian — "RU" must be set in the program. If the languages are different, the bot simply won't find the buttons.

1. **Click "Start farming"** — the green button in place of "Connect phone". The program will automatically adjust the game window to the required size and place it in the top left corner of the screen.
2. **Don't panic if the program window disappears** — it minimized to the taskbar, and a narrow bar appeared under the game — the **mini-bar**. It shows what the bot is doing. To bring the window back: click the "Open the program window" icon on the mini-bar (hover your mouse to see a tooltip) or the button on the taskbar.
3. **Watch the game** — after a few seconds, the bot will click on the door, and the first room will start. One room takes about half a minute to a minute.
4. **Remember how to stop the bot** — the F10 key stops it immediately, F9 pauses it (the bot will finish playing the room and wait). The keys work when either the game window or program window is active.

After expanding the program window, take a look at the log. Before each line there is a timestamp — we omitted it. Here is what should appear:

- `[УМНЫЙ СТАРТ] Сканирую экран для восстановления контекста...` — the bot is looking around.
- `[УМНЫЙ СТАРТ] Контекст не требует экстренных действий. Начинаю с HALLWAY.` — everything is fine, it starts from the hallway ("HALLWAY" means hallway in English).
- `[СТАТИСТИКА] Комнат: 1` — the first room is cleared. Everything is working!
- :triangle-alert: `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` — the bot is waiting for the game window to become focused again. Click on it with your mouse, and work will resume.

A minute has passed and the bot isn't clicking anything? Check:

- :gamepad-2: The game is currently in the Titan Dungeon hallway, not a menu, shop, or battle.
- :globe: The program language matches the game language (warning above).
- :maximize-2: The game window is fully on screen: not stretched, not maximized, not shifted past the edge. Otherwise stop the bot (F10), click "Reset game window size" and start over.
- :terminal: There are no lines with "[ОШИБКА]" in the log. If there are — we'll cover them in the "If something goes wrong" section.

### While the bot is running

- :monitor: The game window must be visible: do not cover it with other windows or minimize it. Clicked another window — the bot will pause and wait.
- :smartphone: Do not close the game window or yank the cable. If the window disappears — the program will stop the bot automatically ("scrcpy window closed — stopping the bot").
- :maximize-2: Do not stretch or maximize the game window: the bot measures it at launch and uses this measurement going forward.
- :gamepad-2: Do not click the phone screen yourself: the bot clicks via ADB, and you will interfere with each other. Want to play manually — pause the bot (F9) and wait until it stands in the hallway.
- :triangle-alert: Do not lock the computer (Win+L): on a locked PC, the bot cannot see the screen and waits until you return.
- :moon: For overnight farming, disable computer sleep: in Windows Settings, open "System" → "Power" and select "Never" for screen and sleep. A sleeping or turned-off monitor is the same as a locked PC: the bot will stop and wait. Item names depend on your Windows version.

### Header buttons

Top right, next to the banner, are three icons. Hover your mouse over any of them — a tooltip will appear.

![Window header: phone banner, three buttons and window buttons](images/header_buttons.png)

- :moon: **"Turn off phone screen"** — turns off the phone screen, but the game keeps running and the bot sees everything. Convenient at night: less strain on the screen and battery. The program brings the game window forward and presses Alt+O in it (this is how scrcpy turns off the screen). To restore the screen — press the power button on the phone. A matching button is also available on the mini-bar.
- :refresh-cw: **"Restart scrcpy"** — closes the game window and opens it again. Useful if the phone image freezes. Works only with the window launched by the program itself. Do not click it while the bot is running: the program will consider the missing window a connection loss and stop the bot.
- :maximize-2: **"Reset game window size"** — resets the `HeroWarsBot_Arena` window to 1606 × 748 size and places it in the top left corner. This is the model size: button search is tuned for it. Stretched or maximized the window — click this button before "Start farming" (although "Start farming" does the same automatically). The window is wide: on a Full HD (1920 × 1080) monitor it fits completely, while the bot only sees what is on screen.

### Program window without Windows border

The program window has no standard Windows border, so it has its own buttons at the top right behind a thin line:

- :minus: **"Minimize"** — minimizes the window to the taskbar.
- :square: **"Maximize"** — maximizes the window to full screen; afterwards the button is called "Restore size". Double-clicking the header does the same.
- :x: **"Close"** — closes the program, and with it the game window if it was opened by the program. If the bot is running, it will ask "Stop the bot?" first; the "Stop and close" button will stop it immediately, but the session summary won't be sent to Telegram.
- :grip-vertical: **Move window** — drag by the header: by empty space at the top or by title.
- **Resize window** — drag the bottom right corner (three diagonal slashes). The window will not become extremely small.

> [!note] Do not confuse "Minimize" and "Minimize to mini-bar". "Minimize" simply hides the window to the taskbar. "Minimize to mini-bar" is a button on the main page while the bot is running: it also shows the mini-bar under the game.

> [!done] Phone connected, bot cleared the first room — the basics are ready. Next, let's look at what the main page shows and how to read the log. [Next section →](#4)

## Main page and log

Main is the first button in the left sidebar, and it is the one you see most often. It looks like a car dashboard: at the top are numbers ("where we are going" and "how we are driving"), at the bottom is the log where the bot writes what it is doing. Let's look at where everything is and how not to get lost in the log lines.

### Top card: it changes its view automatically

In the upper part of the Main page there is one big card, but it displays different things depending on what is happening with the bot:

- :sliders-vertical: **"Launch settings"** — the bot is stopped, and settings are already saved. This is "what the bot will go into battle with": goal, mode, and thresholds.
- :activity: **"Current session"** — the bot is running. Live figures: how much gathered, cleared, elapsed time.
- :file-text: **"Session summary"** — the bot has stopped. The card shows what was achieved and why it stopped.
- :list: **"Getting started"** — only shown if you haven't saved settings yet (described in [Section 3](#3)).

A session is a single bot run: from "Start farming" to stopping.

### Launch settings

Four tiles, each answering one question. The numbers come from your settings, so if you want to change something, click "Change in the Rules Master →" at the top right of the card: the "Rules Master" will open.

![Main page before launch: "Launch settings" card and empty log](images/main_config.png)

- :target: **"Session goal"** — when the bot should stop. There is **one** goal: titanite, rooms, floors, or time. If several are set in settings, the first one in order is taken: "titanite → rooms → floors → time". If you haven't changed anything, the default goal is 120 titanite, which is 10–20 rooms. "No limit" means all goals are zero and the bot will keep going until you stop it.
- :shield-check: **"Mode"** — the "Bot decides itself" tile marked "ON" or "OFF". Enabled: in case of a bad battle, the bot will replay the fight with another team itself. Disabled: it will call you. Details are in the sections about the "Rules Master".
- :heart-pulse: **"HP panic threshold"** — for example, 40%. If after a battle any titan has less health left, the battle is considered bad. A team (pack) is a group of five titans; HP is health.
- :calendar: **"Day reset"** — for example, 05:00. From this hour, a new day begins in the game: the bot calculates daily stats and resets yesterday's titan health values.

> [!note] The bot reads settings **once, when you click "Start farming"**. If you change something while it is running, the bot will only learn about it on the next launch. Therefore, while the bot is running, the card shows the exact settings it started with.

### Current session

When the bot is running, the card turns into "Current session". The status lights up at the top right:

- :activity: **"Farming"** — everything is fine, the bot is working.
- :pause: **"Paused"** — you clicked "Pause" (or the bot paused automatically). The button has changed to "Continue".
- :triangle-alert: **"Waiting for your decision"** — the "Intervention required" window is on screen, the bot is waiting for your response.
- :refresh-cw: **"Starting the bot…"** — the first few seconds after clicking "Start farming".

![Farming: session tiles with progress bars toward the goal](images/main_session.png)

There are four tiles:

1. **"Titanite this session"** — how much titanite the bot has collected. This is a **counter, not screen reading**: 6 per room and 12 if the "x2" icon is active in the game. If the goal is titanite, "collected / required", percentage, and a progress bar will appear nearby.
2. **"Floors cleared"** — a floor counts when the bot collects the reward at a save point (the spot at the end of a floor where you tap "Activate" and "Collect"). Next to it, it shows which door was entered last: water, earth, fire, or mixed.
3. **"Battles this session"** — for example, "12 wins of 14". A victory is a completed room. A rollback is a battle the bot replayed: it also counts as a battle, which is why "total" can be greater than "wins".
4. **"Session time"** — hours:minutes:seconds and small text "avg room 28 s". The average is calculated per room, excluding wait time at save points.

> [!tip] If the goal is rooms or time, percentages are shown on the right as "35% of 100" or "35% of 120 min" — the goal does not fit inside the number itself. The bar below the tile is the same.

> [!note] When the goal is reached, the bot does not abandon the floor in the middle. It will write `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.` in the log, play the remaining rooms and stop in front of the save point without tapping "Activate": it will collect the floor reward first thing on the next launch. The exception is a floor goal: in that case, the bot stops immediately after receiving the reward.

### Session summary

The bot has stopped — the card shows the summary, and the window automatically restores from the mini-bar. The reason for stopping is shown at the top: "STOP" button, closed scrcpy window, normal completion, or something written by the bot itself (for example, that the goal was reached).

![Session summary: stop reason, figures, and "Details" button](images/main_summary.png)

The same four tiles as in the session, but now these are final numbers; in "Battles", "SOS windows: N" is added (how many times the bot called for help). The **"Details"** button opens a window with the full bot report: average times by stage, longest rooms, number of rollbacks, and how many of them the bot did **without you**. The ✕ icon on the right hides the summary, restoring "Launch settings". Clicking "Start farming" will clear the summary automatically.

> [!note] If Telegram is configured, the summary will be sent there automatically upon any normal stop. The "STOP" button (F10) kills the bot instantly, so the summary is not sent to Telegram in that case.

### Log: what is in it and how to read it

The bottom part of the Main page is the **"Activity log"**. The bot writes its every step into it, and the application displays it in the window. Don't be scared by the number of lines: you don't need to read everything; the log is needed when something goes wrong or out of curiosity.

Every line is structured the same way:

`10:26:17.486 [НАВИГАЦИЯ] Двери (слева направо): EARTH (0.98), FIRE (0.97)`

1. **Time** — in gray. Hours:minutes:seconds and milliseconds.
2. **Tag in square brackets** — "who is speaking" and on what matter. It is color-coded: the color tells you which log tab the line belongs to.
3. **Text** — what exactly happened. A long line wraps, and the continuation aligns under the text, not under the timestamp.

A line without a tag (for example, ` ---> HYPERION: ХП 100%, Энергия 79%`) is a continuation of the line above it and belongs to the same section.

### Filter "pills"

Above the log are five "pill" buttons. Click one, and only the lines of that section will remain in the log. The selection is remembered: open the program tomorrow, and the same pill will be selected.

![Log with "All", "Battles", "Rules", "System", and "Errors" pills](images/journal_pills.png)

- **"All"** — everything.
- **"Battles"** (green tags) — progress details: rooms, time, titan health, rollbacks. Tags `[КОМБАТ]`, `[СТАТИСТИКА]`, `[ВРЕМЯ]`, `[СОСТОЯНИЕ]`, `[АНАЛИЗАТОР]`, `[ОТКАТ]`, `[ЛИМИТ]`, `[ИТОГ]`.
- **"Rules"** (yellow tags) — bot decisions: which team to pick, why it rolled back a fight, what it remembered. Tags `[ТАКТИКА]`, `[КОМАНДА]`, `[ПРАВИЛА]`, `[ОБУЧЕНИЕ]`, `[SOS_CLOSE]`.
- **"System"** (blue tags) — everything else: corridor and doors (`[НАВИГАЦИЯ]`), launch (`[УМНЫЙ СТАРТ]`), connection. Lines from the app itself with the `[GUI]` tag are gray, but are also located here.
- **"Errors"** (red tags) — everything requiring attention: `[ОШИБКА]`, `[ВНИМАНИЕ]`, `[СТОРОЖ]`, `[SOS]`. Next to the name is a number indicating how many such lines occurred.

> [!warning] A red number on "Errors" is not always a malfunction. It also includes `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` — the bot is simply waiting for you to bring the game window back to the foreground. Read the text of the line, don't be scared by the color.

### Examples of real log lines

These are lines from an actual bot session (timestamps omitted for brevity). Learn to read these five, and you'll understand any log.

- `[НАВИГАЦИЯ] Выбрана комната EARTH (порядок: water → mix → earth → fire)` — the bot chose the earth door. Your door priority order is shown in parentheses. The number in the "Doors (left to right)" line above indicates how confident the bot is in recognizing the door (1 means absolutely).
- `[ВРЕМЯ] Комната 2 (earth): коридор 12.8 с | сборка 3.3 с | бой 8.0 с | результат 9.1 с | всего 33.2 с` — room report: time spent traveling to the door, selecting team, battle, and closing the result window.
- `[СТАТИСТИКА] Комнат: 3 | Титанит: 36` — third room cleared, 36 titanite collected. These numbers populate the session tiles.
- `[ТАКТИКА] Откатываю бой сам и переиграю паком [...] (взят: ваш список запасных паков).` — the battle turned out bad, and the bot ("Bot decides itself" mode) replays it with a reserve team. If the reserve team succeeds: `[ТАКТИКА] Запасной пак [...] справился. Запоминаю его против этих врагов.`
- `[ОТКАТ] Запускаю протокол отката боя...` — start of rollback: "Try again" → pause → "Retreat". Each such line adds one battle to the "Battles this session" tile.

> [!tip] At the start of every session, the bot writes `[ТАКТИКА] Плохой бой: ХП ниже 30% | потеря больше 60% | ...` — the thresholds by which it will judge battles. If something goes "not as expected", check this line against your settings first.

### Buttons below the log

![Buttons below the log: "Save log", "Send log to author", "Clear"](images/journal_buttons.png)

- :save: **"Save log"** — writes the entire log to a text file. The program will suggest the filename `gui_log_...txt` and folder `bot_data/logs`; you can choose another.
- :mail: **"Send log to author"** — performs the same save first, then opens your email client with a prepared email. **Attach the file to the email yourself** (along with `battle_log.csv` from the same folder): the program cannot do this automatically. No email client installed? Write to the author using the address in the "About" section.
- :x: **"Clear"** — removes lines from the window, asking "Clear the log?" first. This is safe: the full log is automatically saved by the bot in the `bot_data/logs` folder, and session figures are not reset.

You can select text in the log with the mouse, copy with Ctrl+C or right-click ("Copy"). The log cannot be edited — it is read-only. If you scroll up to read, it won't jump down with new lines; scroll back to the bottom, and it will resume auto-scrolling with the bot.

> [!note] The window remembers the last 50,000 lines, but displays the last 4,000 — otherwise, it would lag during long farming runs. Everything else is stored in the `bot_data/logs/bot_log_...txt` file: the bot maintains it automatically, so saving the log manually is rarely needed.

While the log is empty, the message "The log is empty" is displayed in its place. Lines will appear after connecting the phone. An empty pill tab shows "Nothing here yet" and "There were no such lines yet" — for "Errors", this is good news.

> [!done] Now you read the main page like a dashboard: you know what the tiles and log tag colors mean. Next up is the mini-bar, a small panel below the game. [Next section →](#5)

## Mini-bar under the game

While the bot is running, you usually don't need the main program window. That's why it automatically minimizes to the taskbar, and a narrow panel appears under the game picture — the **mini-bar**. It's like a dashboard in a car: at a single glance, you can see if the bot is moving, what it's doing right now, how far it has come, and if it's calling for you.

![Mini-bar under the game window during farming](images/mini_bar.png)

### When it appears and where it stays

- :monitor: **Appears automatically.** Once the bot starts («Start farming»), the program window minimizes, and the mini-bar appears right under the game. If you maximize the program window and want to hide it again while the bot is running, click «Minimize to mini-bar» on the main tab.
- :smartphone: **Sits right under the game** and has the exact same width as the game image. Move the game window — the mini-bar follows it (the program checks this twice a second).
- :eye: **Does not overlap the game by even a single pixel.** This is important: the bot "looks" at the screen by taking screenshots of the window. If the panel overlapped the game, the bot would see it instead of the buttons.
- :maximize-2: **No room at the bottom** (the game window is at the bottom edge of the screen) — the panel will stay above the window header. If there's no room there either, it won't show up, and the program window will remain on the taskbar. Minimize the game window — the panel will hide and return together with it.

> [!tip] Mini-bar not visible while the bot is running? Move the game window higher: it needs about 100 pixels of free space beneath it. You can move the window, but you cannot resize it (we covered this in section 3).

### What's on the panel: five columns left to right

- :activity: **Status.** A word and a colored dot that "breathes" while everything is fine: «STARTING», «FARMING», «PAUSED», «DEBUG PAUSE», or a red «SOS». Below is **what the bot is doing right now** and for how many seconds: for example, "Battle · Fire · 12 s". Then «Rooms: 12 · floors: 2» and session time, for example «Time 00:42:17».
- :target: **Goal.** Goal name, how much is done, how much is needed, and a bar. Below — «~28 s per room» (average time; before the first room it shows «room time — after the first one») and estimated «goal in ≈ 1 h 10 min». The bot calculates the estimate based on the speed of **this** session, so at the beginning it fluctuates, then settles down. If there is no goal («No limit») — there is no bar, and instead of an estimate it shows «≈ N titanite per hour».
- :heart-pulse: **Team health.** Squares of the titans from the last battle and their HP after it — in the exact order they stand on the game screen. Before the first battle, it says «no battles yet». The color of the number gives a hint: red — HP is below the panic threshold (global or personal), yellow — below the threshold at which the bot heals the titan, normal color — everything is fine. A dash "—" means the titan icon could not be found on the result window.
- :list: **Events.** The last four lines, the newest on top and slightly larger. Colored tag on the left, time on the right.
- :gamepad-2: **Buttons.** Four buttons arranged in a 2×2 square.

### What the bot can be "doing right now"

In the first column, the bot names its current stage. Here is what these words mean:

- **«Corridor»**, **«Choosing a door»**, **«Setting up the team»**, **«Battle»**, **«Result window»** — the regular cycle of one room. For the stages «Setting up the team», «Battle», «Result window», and «Rolling back», the room's element is appended: "Battle · Water · 12 s".
- **«Save point»** — floor cleared, the bot collects the reward.
- **«Rolling back»** — the battle went badly, the bot retreats and prepares a replay.
- **«Looking at the screen»** — after starting, the bot looks around and decides where to begin (this is the "smart start").
- **«Paused in the corridor»**, **«Waiting for your decision»**, **«You are playing»** — the bot is paused because you pressed pause, because it asked you, or because you selected «Play manually».
- **«Waiting for the game window»** and **«Waiting for connection»** — the bot is waiting: either the game is not in the foreground (see below), or there is no connection to the game server.

If the same text stays longer than usual, the number of seconds on the right grows and will let you know that the bot is actually stuck/idle.

### Events: labels and what they mean

The label on the left shows what the event is about:

- **Element name** («Water», «Earth», «Fire», «Mixed») — room cleared. A line like "Room 45 cleared · 28 s · lowest HP: Araji 36%" shows how many seconds the room took and who was left with the lowest health.
- **«Floor»** — floor cleared («Floor cleared, 3 in total»).
- **«Rollback»** — battle is being replayed. **«SOS»** — the reason for the call in plain words.
- **«Pause»** — «Pause: the bot will finish the battle and wait», then «The bot is waiting in the corridor».
- **«Bot»** — «Bot started», «Pause lifted, the bot goes on», «No answer for 10 min — the bot decided itself».
- **«Limit»** — session reached the goal, the bot finishes up to the save point.
- **«Notice»** — «The game window is not active — the bot waits. Click the game».
- **«Error»** — error text as written by the bot.

Long lines are truncated with an ellipsis. The full text is always available in the log on the main tab.

### Buttons

Hover your mouse over a button to see its tooltip. All buttons do the same as their "big" counterparts on the main tab and in the header.

- :pause: **Pause / Continue** — «Soft pause: the bot finishes the battle and waits (F9)». When paused, the icon turns into a green triangle, and the same button unpauses. While the bot is still starting up, the button is disabled.
- :square-filled: **Stop** — «Emergency stop: the bot stops at once, no summary in Telegram (F10)».
- :moon: **Phone screen** — «Turn off phone screen», while the game keeps running.
- :maximize-2: **Maximize** — «Open the program window». The mini-bar will disappear. The program window button on the taskbar produces the same result. If you want to bring the panel back, click «Minimize to mini-bar» on the main tab.

> [!note] When the bot calls for you, the mini-bar turns red, and the «Intervention required» window pops up automatically in the center of the game image — no need to open the program window. At that moment, the first button does not pause or continue: it shows the SOS window if it got hidden under other windows (tooltip — «Show the SOS window: the bot is waiting for your decision»). Once you respond in the window, the mini-bar goes back to normal. How to respond will be covered in the section on SOS windows.

![Mini-bar during SOS](images/mini_bar_sos.png)

### Main rule: the bot works only while the game is in the foreground

The bot takes screenshots and looks for buttons on them. If another browser, messenger, or file explorer covers the game, the screenshot will capture them instead of the game, and the bot might click the wrong spot. Therefore, as soon as another window becomes active, it stops and waits. A line appears in the log: "[ВНИМАНИЕ] Окно игры перекрыто … Бот ждет фокуса…", the mini-bar shows the label «Notice» and the stage «Waiting for the game window». Click on the game — "[ИНФО] Окно снова активно. Продолжаем работу."

- :monitor: **Clicks on the mini-bar do not stop the bot.** The mini-bar is designed so that it doesn't become the active window: the game remains "main" while you press buttons on the panel.
- :triangle-alert: **«Maximize» temporarily stops the bot.** The program window becomes active while the game is not, so the bot will pause at the next step. When you are done, click the game window, and the bot will proceed. The watchdog does not count this waiting time as a "hang".
- :gamepad-2: Want to work on your computer while the bot is farming? Open other windows **side by side**, not over the game, and don't click on them. Or postpone your task until pause (F9).

> [!warning] Hotkeys F9 and F10 only work when the game window or the program window is active. Pressing F10 in a browser won't stop the bot: the hotkeys aren't captured when you are busy in another app. More details in the section on pause and stop.

> [!done] Now you can read the mini-bar like a dashboard and know why you shouldn't hide the game under other windows. Next up — pause, stop, and hotkeys. [Next section →](#6)

## Pause, stop, and hotkeys

The bot navigates the Dungeon on its own, but sometimes you need to slow it down: you want to play manually, step away for errands, or simply finish. There are **four ways** to do this, differing in **how smoothly** the bot stops. Think of a car: "pause" is pulling over to the curb and turning off the engine, while "emergency stop" is pulling out the key while driving. Both work, but differently.

### Soft pause: "Pause F9"

The gentlest method. Press the «Pause» button on the main tab, on the mini-bar, or the **F9** key.

1. **Press «Pause» or F9.** The log will show the line `[GUI] Сигнал 'Мягкая пауза' отправлен. Бот остановится перед следующей дверью.`
2. **Wait for the bot to finish the room.** It won't abandon an ongoing battle: it will complete it, close the result window, and record the room's summary.
3. **The bot pauses in the corridor.** In the log: `[МЯГКАЯ ПАУЗА] Бот ждет в коридоре...`. The status on the main tab becomes «Pause», on the mini-bar — «PAUSED», and the button turns green as «Continue».
4. **Do your things and press «Continue» (or F9 again).** The bot writes `[ИНФО] Пауза снята. Кэш составов и здоровья очищен. Включаю механизм Умного Старта.` and continues.

> [!note] "Cache cleared" means the bot has **forgotten** which teams were selected and how much health the titans had: while you were interacting with the game, everything could have changed. Before the next battle, it will look at the team selection screen again and read the health from it. "Smart start" means the bot first inspects what is currently on the screen before deciding what to do (for example, closing a forgotten result window).

- :eye: **While paused, you can check your phone and change settings in the program window.** However, the bot will only apply new settings on the next «Start farming» (more details in the main tab section).
- :door-open: **If you clicked anything in the game — return it to the Dungeon corridor** (where the flag next to the door is visible), and only then press «Continue». This ensures the bot correctly understands where it is.
- :gauge: **Time keeps ticking during pause.** If the session goal is time ("120 minutes"), the pause will use up part of that time. However, the watchdog (which monitors whether the bot is frozen) does not count pause time and won't raise an alarm.

> [!tip] Want to leave overnight or for a long time? You don't need a soft pause for this: set a goal (titanite, rooms, floors, or time) on the main tab, and the bot will automatically reach the save point, stop, and send the summary.

### When the bot pauses automatically

Sometimes the bot asks for help and soft pauses automatically. Then the button also displays «Continue», and the log shows `[ВНИМАНИЕ] Бот на мягкой паузе: ...` along with the reason. This happens when:

- the bot failed to clear any room for 5 minutes three times in a row (watchdog decided it froze);
- rolling back a battle failed (screen wasn't recognized, buttons weren't clicked);
- the battle never started, even after waiting for a long time;
- you didn't answer the «No suitable pack» window, and there is no backup team.

In such cases, first **check your phone screen**, fix whatever went wrong (close extra windows, return to the corridor), and only then click «Continue». If Telegram is configured, the bot will send a message with a screenshot.

### Emergency stop: "STOP F10"

The red «STOP» button (or the **F10** key) stops the bot **immediately**: the program kills the bot process. In the log — `[GUI] ЭКСТРЕННЫЙ СТОП. Процесс убит.`, on the summary card the reason is "stopped by «STOP» button".

> [!warning] What is lost with F10: the bot doesn't have time to write the `[ИТОГ]` block to the log and **does not send the session summary to Telegram**. If it was in battle at that moment, the battle in the game will continue (or remain on the screen) — you will see this on your phone. Rooms already cleared are saved in statistics: the bot records them immediately after each room.

When you need this specific button: the bot behaves strangely (clicks wrong spots, doesn't react to «Pause») or you need to terminate everything right now. Otherwise, pause or Ctrl+Q is preferred.

### Hotkeys: what works where

- :pause: **F9** — pause / «Continue» (same as the «Pause» button on the main tab).
- :square-filled: **F10** — «STOP».
- :gamepad-2: **Ctrl+Q** — stop **with summary**: the bot finishes the current room, waits in the corridor, stops, and sends the session summary. In the log: `[ИНФО] Команда 'Ctrl+Q' принята! Бот завершит бой и остановится.`, stop reason — "Manual stop by user (Ctrl+Q)".
- :triangle-alert: **Ctrl+Shift+Q** — stop **immediately, but with summary**: the bot prints `[ЭКСТРЕННАЯ ОСТАНОВКА]`, writes `[ИТОГ]`, and makes **one** attempt to send the summary to Telegram (without retries, so it doesn't stall).

Important details why hotkeys sometimes "don't work":

- **F9 and F10 are monitored by the program window** and only when **the game window or the program window is active**. Pressing F10 in a browser or messenger does nothing. If the game is minimized or hidden behind another window, use the buttons on the mini-bar: they always work because the mini-bar doesn't steal focus from the game.
- **Ctrl+Q and Ctrl+Shift+Q are monitored by the bot itself**, not the program window, so they work as long as the bot is running, even if another window is active.
- **These shortcuts are common in other software.** Ctrl+Q closes many applications (Word, Telegram Desktop), while Ctrl+Shift+Q closes browsers. While the bot is running, avoid pressing them in other windows: the bot will "hear" them too and stop.
- **The bot checks Ctrl+Q when it is in the corridor** before the next door. During a soft pause, it stands still and doesn't check anything, so Ctrl+Q will only trigger after «Continue». But if the bot is waiting for your answer in an SOS window, Ctrl+Q stops it immediately.
- **Holding down a key does not repeat the command:** one press = one command.
- If you press F9 or F10 when the bot is not running, the log will show `[GUI] Нажата F9, но бот не запущен.`

### Window close button (X) and closing scrcpy

- :x: **Closing the program window while the bot is running.** A confirmation dialog will ask «Stop the bot?». Clicking «Stop and close» will close the program and the bot, and the game window (scrcpy) — if it was launched by the program itself — immediately, without sending the summary to Telegram. If you don't want this, cancel the dialog and soft-stop the bot first.
- :smartphone: **Closing the game window (`HeroWarsBot_Arena`) manually.** The program will write `[GUI] Окно scrcpy закрыто — останавливаю бота (он напишет итог и пришлёт его в Telegram).` The bot will finish writing the session summary and send it to Telegram; if it doesn't respond within 10 seconds, the program will terminate it as if F10 was pressed.
- :pencil: If there are unsaved changes in the «Rules Master», closing will first ask «Save changes?».

### What to choose

- **Want to take a break and return** — «Pause» (F9). Click «Continue» when you are ready.
- **Want to finish and get the summary** — Ctrl+Q (the bot will finish the room, stop, and send the summary to Telegram).
- **Need to stop right now, but still need the summary** — Ctrl+Shift+Q.
- **The bot is broken or acting strangely** — «STOP» (F10), then check the log to figure it out.
- **The bot called you with an SOS window and you want to quit** — the «Stop the bot» button in that window: the bot will stop on its own and send the summary. We will cover the SOS window separately.

### Session summary in Telegram

If Telegram is configured, a summary arrives upon any stop, **except for the «STOP» button** and closing the program window: the bot notes whether you stopped it yourself («Bot stopped by you»), completed the goal («Farming finished»), or crashed with an error, how much time elapsed, how many rooms, floors, and titanite were gathered, and whether there were rollbacks and SOS windows. If there is no internet connection, the bot will attempt to send the summary twice more (after 10 and 30 seconds) before shutting down. How to set up Telegram is in a dedicated section.

> [!done] Now you know how to gently pause the bot, how to stop it completely, and what each key does. Next — configuring rules: teaching the bot to select the right teams. [Next section →](#7)

## Rules Master: "Base and rooms"

"Rules Master" is the second button in the left bar (icon with sliders). Here you explain three things to the bot: **when to stop**, **what counts as a bad battle**, and **which team to use for each room**. A team is a group of 3–5 Titans. The page is divided into three tabs at the top: "Base and rooms", "Auto-tactics and HP", and "Rules and overrides". This section covers the first and most important one: without it, the bot doesn't even know who to send into battle.

![Tab "Base and rooms": two cards with settings at the top, four rows with teams below](images/rules_base.png)

At the top — "Session settings" (two cards), below — "Teams by room". At the bottom of the page, identical on every tab, is a gray bar with buttons: "Save settings" and "Restore / Reset". More about it at the end of the section. The main thing to remember right away: **until you click "Save settings", nothing is saved** — not a single edit will reach the bot.

### Card "Goals and limits"

- :target: **"Session goal"** — when the bot should finish. The goal is always **one** of four: "Titanite", "Rooms", "Floors", or "Time" (time is in minutes). Select the type from the list and enter a number in the field. The field accepts digits only. The label "0 — unlimited" means: zero turns off the goal, and the bot will keep going until you stop it. The circular arrow on the right ("Reset goal") sets it to 0.
- :gem: **The bot counts Titanite itself** instead of reading it from the screen: 6 for a regular room and 12 if there is an "x2" icon on the result screen. So "120 titanite" is about 20 rooms without "x2". If you haven't saved settings yet, the bot defaults to "120 titanite".
- :layers: **The bot does not leave a floor mid-way.** Upon reaching the "Titanite", "Rooms", or "Time" goal, it doesn't stop immediately: it writes to the log `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.`, plays the remaining rooms of the floor and stops in front of the save point without tapping "Activate". This ensures the floor isn't left unfinished, and on the next launch the bot collects the reward and counts the floor first thing. If a save point isn't found within 6 rooms (there are 5 on a floor), the bot stops as is. The "Floors" goal triggers as soon as a save point is passed.
- :gauge: **Time ticks even while paused.** A goal of "Time — 120" means 120 minutes from clicking "Start farming", including all pauses.
- :calendar: **"Day reset hour (local time)"** — when your new game day starts. Default is 05:00. It determines which day battles belong to in statistics, as well as the bot's memory of Titan health: it lasts within a single game day, starting fresh on a new day. Set the hour after which you consider the day new (for example, when you go to sleep).
- :send: **"Set up Telegram"** — opens a separate window where messenger connection is enabled. Next to the button is a dot and label: green "SOS notifications on" or gray "Telegram not set up". How to connect it will be covered in the Telegram section. One thing is important here: the "Apply" button in that window only changes this page. For the setting to be saved to the file, click "Save settings" as well.

> [!tip] Which goal to choose? "Time" is convenient when you have a window in your schedule ("let the bot run for an hour while I cook dinner"). "Titanite" is when you need to gather a specific amount of rewards. "Rooms" and "Floors" are when you want to clear an exact amount. If unsure, leave "Titanite" and 120: it's a short test run.

### Card "Safety and mode"

Here you decide **what counts as a bad battle**. The bot reads Titan health on the result screen and compares two numbers against yours.

- :heart-pulse: **"HP panic threshold, %"** — health level after a battle below which the battle is considered bad. Default is 40.
- :swords: **"HP loss delta, %"** — how much health a single Titan can lose in one battle. Default is 30.

Both fields accept integers from 0 to 100; if you enter anything else, the field turns red with the label "Enter a number from 0 to 100", and settings cannot be saved until fixed.

Real example with a threshold of 40 and delta of 30:

- Araji entered battle at 100%, exited at 80% — **all good**: lost 20, stayed above 40.
- Araji entered at 100%, exited at 55% — **bad battle**. 55 is above threshold, but lost 45, while 30 is allowed.
- Araji entered at 50%, exited at 35% — **bad battle**. Lost only 15, but 35 is below panic threshold.
- Any Titan died or was not found on the result screen — **bad battle** always, no matter what you set.

Losses are calculated from the health the Titan **entered** battle with, not from 100%. Therefore, an injured Titan hits the threshold sooner than a healthy one. The higher the threshold and the smaller the delta, the stricter the bot and the more often it calls for you; zero threshold disables the "below threshold" check (except for dead Titans), and 100 delta disables loss check.

> [!note] Threshold and delta are common to all Titans. You can set individual thresholds for specific Titans and enable the rule "if three lost a lot — bad battle". This is done on the adjacent tab "Auto-tactics and HP".

Below are two toggles:

- :shield-check: **"Bot decides itself"** ("Rolls back bad battles and picks a team") — **disabled** by default. Disabled: bad battle → "Intervention required" window, bot waits for you. Enabled: bot rolls back battle without questions and replays with a backup team, and automatically picks a team based on Titan health. Details in the autonomous bot operation section. Enable when you've watched the bot work and trust backup teams.
- :swords: **"Manual Angus ult control"** ("Global, in all rooms") — **disabled** by default, so any battle, including with Angus, runs on auto-battle. Enabled — for teams with Angus, the bot clicks "To Battle", turns auto-battle on for a couple of seconds for Angus's ult, and turns it off again. The bot does not roll back such battles on its own and calls you instead. On launch, the log shows what's selected: `[ТАКТИКА] Ангус: ...`.

### Teams by room

Under the label "The main team goes first, backups in order if a battle goes badly" stand four rows — by room: "Earth", "Water", "Fire", and "Mixed". Each is an individual card.

- :users: **Main team** — Titan squares under the room name. The bot deploys it unless there is a reason not to (for example, a rule from the "Rules and overrides" tab triggered). Titans are shown left to right, **just as they stand on the game screen**. If no team is set, "Pack not set" is shown instead of squares.
- :pencil: **Pencil ("Change team")** — opens the "Build a team" window.
- :list: **"Backup teams"** with count "N pcs." — expandable list (arrow down/up). The bot tries backup teams in order if a battle is bad and it decides itself ("Bot decides itself" is on or you didn't answer the window in time). Up to 5 per room. Inside, each backup team is a row `#1`, `#2`, and so on, with a cross on the right ("Remove team"). The "Add team" button opens the same "Build a team" window.
- :plus: **"Condition"** — "+ Condition": shortcut to a rule for this room, for example "if against Angus — use this team". Opens the "New rule" window with the room pre-selected. How to set it up will be covered in the rules section.

Set the main team in all four rooms **before your first farm run**: the bot doesn't know your Titans and has no teams "out of the box".

How to build a team:

1. **Click the pencil** in the desired room. The "Build a team" window opens.
2. **Click the Titans** you want to deploy. Click again to remove. Count at top: "Selected: 3 / 5" and hint "Ready to apply" (with two it says "At least 3 · 1 more needed").
3. **Consider the room's element.** Only Titans of that element go into "Earth", "Water", and "Fire", while all Titans go into "Mixed", along with Metis (she is "Elarite" and doesn't enter other rooms: "Metis — mixed room only"). When 5 are selected, remaining Titans are locked.
4. **Click "Apply"** (or "Cancel" if you changed your mind; "Clear" removes all Titans at once).

![Window "Build a team" for room "Water": three Titans selected, "Apply" at the bottom](images/rules_picker.png)

> [!warning] "Apply" in the "Build a team" window only updates the page: the team is **not saved** to the file yet. It gets saved when you click "Save settings". Each room's main team is stored in file `bot_data/rules/<стихия>.yml`, backups and all numbers in `profile.yml`. No need to edit these files manually.

A backup team already on the list (in any Titan order) cannot be added a second time: a notification "This backup team already exists" will appear.

> [!tip] Which teams to set as backup? Give the bot choices: make the backup team differ from the main team by at least a couple of Titans. If Araji often leaves battle injured, put Titans in backup who hold damage better.

### Saving and "Restore / Reset"

The bottom bar shows the state: "All changes saved" (green checkmark) or "Unsaved changes" (yellow icon). While the bot is running, "The bot will use the new settings on its next start" is shown next to it.

- :save: **"Save settings"** writes only what you changed and shows notification "Settings saved". Until the button is clicked, the bot is unaware of your edits. The log will display `[GUI] Профиль настроек сохранен!`.
- :rotate-ccw: **"Restore / Reset"** — red button; first asks "Restore settings?". Settings return to the **last saved** (copy `bot_data/profile.yml.bak`). If no copy exists, `profile.yml` will be deleted, and the bot will take default values. Unsaved edits will be lost. Main teams and rules in `bot_data/rules` files are untouched by this button, but the page form re-reads them from disk.
- :triangle-alert: **If you leave the page with unsaved edits** (to another section or with the window cross), "Save changes?" will pop up with buttons "Save", "Don't save", and "Cancel".

The bot reads settings **once when you click "Start farming"**. Changing them while running is possible, but they will take effect only after stopping and restarting. Even "Pause" and "Continue" do not refresh them. The "Launch settings" card on the main screen shows the exact settings the bot is currently using.

> [!warning] If file `profile.yml` is corrupted, `[ОШИБКА] Файл profile.yml поврежден!` will appear at top of the main log, default values will show on the page, and "Save settings" will refuse to write ("profile.yml is damaged — settings not saved"). Click "Restore / Reset".

> [!done] Now you know how to set goals, thresholds, and teams for each room. Next up — "Auto-tactics and HP" tab: door order and how the bot heals and switches Titans. [Next section →](#8)

## Rule wizard: "Auto-tactics and HP"

The second tab of the "Rule wizard". On the first one ("Base and rooms"), you set teams and common thresholds. Here you explain to the bot **how to behave when something goes wrong**: which door to enter first, what to consider a bad battle, how many times to try another team, how long to wait for you, and how to heal wounded titans. All fields are already filled with reasonable numbers, so the bot works fine without your edits. Change them when you see it behaving differently from what you want.

![The "Auto-tactics and HP" tab: banner at the top, four doors, two cards side by side, and personal thresholds at the bottom](images/tactics_tab.png)

Just like on the first tab, **nothing is saved until you click "Save settings"**, and the bot reads settings once when you click "Start farming". If you change them during farming, changes will take effect after stopping and restarting.

### Blue banner at the top

It briefly tells what the bot does during a bad battle: rolls it back and replays with a backup team, saving a successful team into a rule.

If the "Bot decides itself" switch is disabled on the first tab, another sentence is added to the banner. It is important, so let's look at it separately. **Without "Bot decides itself", two things do not work: backup teams and the healing team.** Everything else on this tab works always:

- :door-open: door priority;
- :gauge: waiting for your answer to the SOS window (the window where the bot calls you when a battle is bad);
- :triangle-alert: bad battle criteria;
- :heart-pulse: personal panic thresholds.

### "Door priority"

In the corridor, the bot often sees several doors at once: one per element ("Water", "Earth", "Fire") or "Mixed". Inside the room, enemies await you, and the team for each element is different. Priority determines **which door the bot will open first**. By default: "Water", "Mixed", "Earth", "Fire".

Four slots go left to right with arrows between them; each has a number from 1 to 4. Click a slot and select an element. There are no duplicates: if you select an element that is already in another slot, they simply **swap places**. If it was "Water, Mixed, Earth, Fire" and you picked "Fire" for the first slot, it will become "Fire, Mixed, Earth, Water".

Two notes so you aren't surprised in the game:

- If a door is **forbidden by a "Skip" rule** (read about them in the "Rules and overrides" section), the bot will skip it, even if it is first in order. If all doors are forbidden, it will take the first one in order.
- If "Bot decides itself" is enabled, the bot will sometimes **choose another door itself**, out of order: where healing will work for a wounded titan, or bypassing a door dangerous for the wounded. Such a choice is visible in the log as `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...`.

### "Bad battle criteria and SOS" card

- :swords: **"Backup teams to try per room"** — how many times per room the bot can roll back a battle itself and replay with another team. From 1 to 3, default is 2. If attempts are exhausted and the battle is still bad, the bot calls you. Works only with "Bot decides itself". More than three is not allowed: there's no point in replaying one battle ten times, and each attempt takes time.
- :gauge: **"SOS window timeout without an answer, min"** — how many minutes the bot waits for your answer to the "Intervention required" window before deciding itself. From 0 to 60, default is 10. The label under the field says "0 — wait forever": **zero means "wait forever"**, the bot will stand and wait for you until morning if needed. This works **even without** "Bot decides itself". What exactly the bot decides itself (roll back, accept, or pause) — read in the SOS windows section.
- :users: **"Count the battle as bad if"** — overall team losses: "titans ≥ 3" and "lost ≥ 40" "% HP each". This check catches cases when **each titan holds on individually**, but together the team "collapsed". Three titans lost 40% or more — the battle is bad, even if none dropped below their panic threshold. The label "0 titans — do not check" means: set the first field to 0, and the check turns off. The first field is from 0 to 5, the second from 0 to 100.

A practical example. Team: Araji, Hyperion, Rigel, Iyari, Lumira. After the battle, Araji lost 45%, Rigel 42%, Iyari 40%, and the rest 10% each. Three lost "40 or more" — the battle is bad, even if everyone has more than their panic threshold left. If Iyari had lost only 35%, there would be only two such titans, and the general check would find no fault.

> [!note] Other signs of a bad battle — panic threshold and loss allowance — are located on the first tab "Base and rooms". A battle is bad if **at least one** sign triggered: someone died or was not found on screen, someone's HP is below threshold, someone lost more than allowed, or total loss check triggered.

If you enter an invalid number (a letter or a number out of range), the field turns red, "A number from … to …" appears under it, and you won't be able to save settings until you fix it.

### "Auto healing team in the Mixed room" card

It often happens like this: a titan gets beaten up for a couple of battles in a row and walks around with half health. Sooner or later it will drop below threshold, and the battle will become bad. "Healing" is when the bot **builds a special team itself** to heal the wounded titan (a healer is put into it, raising the wounded titan's health). The bot builds such a team only for the "Mixed" room because you can place anyone there.

This works only with "Bot decides itself", and only if your own healing rule hasn't triggered (a rule is stronger).

- :heart-pulse: **"Heal a titan if HP is below, %"** — default is 60. A titan healthier than this number is considered healthy. **0 turns off** the healing team entirely. But there is a lower boundary: if a titan's HP is already **below the panic threshold**, it cannot be healed in "Mixed", and the bot leaves it alone.
- :users: **"Who to remove from the team for the wounded"** — three slots with arrows. When a wounded titan needs to be placed and there's no room in the team, someone leaves. Click a slot and select a titan: the list is divided into columns by element. **"— auto —"** (default) means: the bot removes from the end of the team, but **does not touch healers**. For the team "Hyperion, Rigel, Iyari, Lumira, Amon", this will be Amon, then Lumira. If you pick a titan already in another slot, they will swap places.

How the bot heals, in simple words:

1. Checks who has HP below 60% but above the panic threshold, and who among them isn't forbidden by "Skip" rules.
2. Heals **one by one**, starting with the one closest to their threshold. First main titans (from base teams), then backups.
3. If the wounded titan is not in the team — it takes the place of the removed one. But titans that are already healed in "their own" room (Water and Earth: their base team has a healer) are not pulled into "Mixed" by the bot unless they fail to rise above threshold for two battles in a row. Fire titans have nothing to heal them in "their own" room, so healing turns on for them immediately.
4. If the wounded titan is already in the team but doesn't rise for two battles in a row — a **healthy and charged healer** (HP from 80%, energy from 60%) takes the place of the removed one.
5. A team is not taken if no healer is left in it, it loses to these enemies, is dangerous for the wounded, or requires manual battle (Angus).

Why is the bot so cautious? It won't heal someone you haven't specified anywhere: the bot won't place a titan that isn't in your teams or rules. If it couldn't assemble a team (the titan never entered a slot), the bot doesn't stop, places a regular team, and **does not heal this titan again until the end of the run**.

In the log, this can be seen in lines `[ТАКТИКА] Пак отхила (бот собрал сам): ...` and `[ТАКТИКА] Отхил: ...` (why the wounded titan is not being healed).

### "Personal panic thresholds of titans, % HP" card

The common panic threshold (40 by default) applies to everyone. But there are titans you'd regret losing earlier than others, and those that easily survive low HP. For them, you can set **their own threshold**.

- At the bottom, the note says "Other titans use the common threshold 40%" (the number is from the first tab). While there are no personal thresholds, it says "No personal thresholds — all titans use the common one".
- Click "Set a personal threshold for a titan". A small window "Personal panic threshold" opens: select a titan from the list and enter a number from 0 to 100. Click "Apply". The window prompts "Common threshold — 40%" so you have something to compare against. The list contains only titans that don't have a personal threshold yet.
- Each set threshold is a tag with a titan and a yellow number. Click the tag to edit the threshold (you cannot change the titan, you'd have to remove and add it again). The **cross** on the tag removes the threshold, and the titan goes back to using the common one.

A battle is bad if this titan's HP after battle is **below its personal threshold**. Example: common threshold is 40, but Rigel is set to 60. Rigel came out with 55% — battle is bad, even though 55 would be fine for others.

> [!tip] Where to start? Don't change anything until you see a couple dozen rooms. If you notice the bot calling you because of the exact same titan, set a lower personal threshold for it. If the bot changes teams for healing too often, **decrease** the number in "Heal a titan if HP is below, %". If you don't want it to heal at all, set it to 0.

> [!warning] If you set "SOS window timeout without an answer, min" to 0 and go to sleep, and the bot calls you in the window, it will wait until morning. Better leave 10–15 minutes and set up Telegram: then you'll know about the issue immediately, and if you don't make it, the bot will decide itself.

> [!done] Now you know how to set door priority, what counts as a bad battle, and how the bot heals the wounded. Next — Telegram and windows calling you for help. [Next section →](#9)

## Rule Wizard: "Rules and overrides"

The third tab of "Rule Wizard". On the first tab, you set the **main pack** for each room, and on the second — how the bot behaves in trouble. Here, you teach it **exceptions**: "usually set the main pack, but if this happened — do it differently". Each such exception is called a **rule**. An "override" is when a rule "overrides" the main pack selection and sets its own.

A rule is always read the same way: **"if [condition] — then [action]"**. For example:

- :heart-pulse: "If Araji's HP is below 50% — set a pack with healer Sigurd".
- :swords: "If Angus, Sylva, and Verdok are in the room — set this pack".
- :door-open: "If Araji's HP is below 30% — do not enter "Fire"".
- :users: "If Angus, Avalon, and Eden are in the room — stop and ask me".

!["Rules and overrides" tab: element filters, rule list with icons, packs, and toggles](images/rules_intercepts.png)

Rules are separate for each element: "Earth", "Water", "Fire", and "Mixed" have separate lists. When the bot enters a "Fire" door, it looks only at "Fire" rules. As on other tabs, **nothing is saved until you click "Save settings"**, and the bot reads rules once when you click "Start farming".

> [!note] You won't have to write many rules at all. If "Bot decides itself" is enabled, the bot **remembers successful packs on its own** after a rollback and adds "golden rules" by itself. They will appear in this same list (more on them below). Your own rules are needed when you already know that "you shouldn't do this" or "in this exact situation, this specific pack is needed".

### Types of rules

A rule has one of three conditions and one of three actions. Together they give the familiar types:

- :heart-pulse: **Rescue by HP or energy.** Condition — "HP (or energy) of a given titan is below N%", action — set a different pack. In the list, the icon is **"HEAL"** (by HP) or **"ENERGY"**. This is how healing is done: when a titan is injured, a pack with a healer is set.
- :swords: **Against these enemies.** Condition — "all these enemies are in the room", action — set your own pack. Icon **"ENEMIES"**. You can choose enemies from the 13 that the bot recognizes in the Dungeon.
- :door-open: **"Skip" — prohibition.** Condition — "titan's HP or energy is below N%", action — do not set this titan and do not enter this room. Icon **"SKIP"**, with a note "Skip the room" on the right.
- :users: **"Ask me".** Any condition, and action — don't decide on its own, but call you. On the right, a note **"Ask you"**, and the icon depends on the condition ("HP", "ENERGY", "ENEMIES"). When it fires, the bot will open the "No suitable pack" window and wait for your response. If you don't answer within the time specified in "Auto-tactics", it will decide by itself.

The "HP" icon (instead of "HEAL") means the condition is by HP, and the action is "Ask you". If there is no condition at all, there is no icon, and below the name it says "No condition — the rule never fires".

Now about "Skip", because it has two jobs at once. Example: in "Fire" there is a rule "Araji, HP below 30%".

1. **Door.** While Araji has less than 30%, the bot will not go into "Fire" and will choose another door. If all doors are forbidden, the bot will take the first one in order.
2. **"Blacklist".** Araji will not be deployed in this room: the bot will discard any pack that contains him and take the next one. If the **main** pack also contains a forbidden titan, there is nothing to deploy — the bot will stop and open the "No suitable pack" window.

> [!warning] "Skip" cannot be made by enemies. The bot recognizes enemies **only after** entering the door, so it cannot choose a door based on them. In the rule window for "By enemies", the "Skip" checkbox is unavailable. If you want to bypass a room with certain enemies, set an "Ask me" rule, then the decision will be yours.

### In what order the bot checks rules

When a battle starts, the bot goes through the room's rules **in this order**:

1. **"Skip".** First, the bot builds a "blacklist" of titans: who was forbidden by a triggered "Skip" rule. A pack with such a titan won't fit, even if a rule itself requests it (this is called a veto: a prohibition is stronger than any rule).
2. **Rescue.** Rules where the condition includes a titan's HP or energy. Rules "against enemies, when Araji < 50% HP" (enemies plus HP) belong here too: they are checked right here, **before** regular enemy rules.
3. **Against enemies.** Rules where the condition includes only enemies.
4. **Main pack** of the room — if nothing matched.

Inside each group, the bot goes **from top to bottom** and takes the first rule that fired. That's why arrows are needed: if two enemy rules match at the same time, the one higher up wins. However, a "Rescue" rule is always stronger than "Against enemies", wherever they are in the list. **Disabled** rules do not participate in checking.

Conditions are compared with what the bot knows about your titans (it gets HP and energy from the team selection screen and after battles). If the bot hasn't seen a titan's health yet, it considers it full, and a "below N%" rule won't fire. If there are several titans in a condition (this happens in rules that the bot remembered on its own), **all** conditions must be met at once. It's the same with enemies: the rule will fire only if **all** listed enemies are in the room.

### Rule list: what's in a line

At the top — "Active rules" and a gray badge with the number of rules, on the right a tip: "Choose one element to change the order" (when all are shown) or "The rule higher in the list is checked first" (when one is selected). Below are filter buttons "All", "Earth", "Water", "Fire", "Mixed" and the "New rule" button. Below them are column headers "№", "Condition", "Action", "On".

In each row from left to right:

- **Number** — position in its element's list. The smaller the number, the earlier the rule is checked. When **one** element is selected, "Up" and "Down" arrows appear next to the number. When "All" is selected, there are no arrows: elements are shown in sequence, and they don't compete with each other.
- **Icons** — room element and rule type ("HEAL", "HP", "ENERGY", "ENEMIES", "SKIP").
- **Name** and a gray line below it — the condition in words, for example "Araji: HP below 50%" or "Enemies in the room: Angus, Sylva".
- **Action** — an arrow and titan squares of the pack (left to right, like in the game) labeled "pack change". Or an "Ask you" / "Skip the room" badge.
- **"On" toggle** — enable or disable the rule.
- **Pencil** "Edit" and **cross** "Delete".

If there are no rules, in place of the list it says: "No rules. Click "New rule" — or the bot will remember a rule itself after a rollback."

### Toggle, arrows, cross, and "Clear"

- :check: **Toggle.** A disabled rule becomes dim, but **remains in the list**, and the bot simply skips it. This is the best way to "remove a rule temporarily": no need to assemble the pack again. Upon launch, a log line will appear `[ПРАВИЛА] Выключено правил: N, бот их пропускает.`
- :chevron-up: **"Up" and "Down" arrows** swap the rule with its neighbor. They are needed when two rules of the same group can match at once and it matters which one is checked first.
- :x: **Cross "Delete".** A notification "Rule "..." deleted" with an **"Undo"** button will appear at the bottom. While the notification is on screen, the rule can be restored to the same place.
- :trash-2: **"Clear all rules"** deletes only what is **currently visible**. If "Water" is selected — water rules are deleted, if "All" is selected — all rules. First, the bot will re-ask: "Delete all rules?" and state how many and of which kind (the "Delete all" button). Then there will also be a notification "Rules deleted: N" with an "Undo" button.

All these actions change only the page. They will reach files after "Save settings", and **only elements where something changed** will be written. If you leave the page without saving, the window will ask "Save changes?".

> [!tip] If you are unsure whether to delete a rule, it's better to turn it off with the toggle. For rules that the bot remembered on its own, there is another reason (see below): the bot doesn't touch or recreate a disabled rule, whereas a deleted one might appear again.

### Step-by-step: "New rule" window

Click "New rule" (or the "Condition" button on the first tab, at the bottom of a room card). A window will open. If one element is selected, it will immediately suggest it. The pencil in a row opens the same window titled "Edit rule".

!["New rule" window: element and name, three triggers, condition fields, action, and team](images/rule_editor.png)

1. **Select an element in the "Room element" field.** The rule will work only there. The available titans depend on the element: in "Earth" only earth titans, in "Water" only water titans, and in "Mixed" any titan. If you change the element later, the window will auto-adjust the selection.
2. **Name the rule (optional).** The "Rule name" field can be left blank: then the name will be composed from the condition, for example "Araji: HP below 50%". The bot then writes this name in the log when the rule fires.
3. **Choose a "Trigger"** — what the bot should look at: "By HP", "By energy", or "By enemies".
   - "By HP" and "By energy": select **"Titan"** and enter a number in the "HP below, %" (or "Energy below, %") field from 0 to 100. By default, HP is 35, energy is 100. If you enter a non-number or a number out of range, the field turns red and "A number from 0 to 100" appears below it.
   - "By enemies": check everyone who must be **together** in the "Dangerous enemies in the room" grid. Nearby it says "· selected: N". If you select no one, you cannot save.
4. **Choose "Action when it fires".** There are two mutually exclusive checkboxes: "Stop and ask me" and "Forbid entering the room (Skip)". If neither is checked, the rule will **set a pack**.
5. **Require titan break-in (optional).** The rule will fire only if the selected titans (from 1 to 5, of any element) have already fought a battle in this run. For example, a pack requests Sigurd, but you don't want to deploy him until he has fought at all. The cross nearby removes the break-in requirement. Break-in is available only for rules that set a pack. After a soft pause and manual battle, the bot forgets titan states, and break-in starts over.
6. **Choose "Team for this rule".** Click "Choose team" and in the "Build a team" window pick **from 3 to 5 titans** (the same way as for the main pack). For "Ask me" and "Skip", no team is needed, and it says "This action needs no team".
7. **Click "Save rule".** While the button is grayed out, the bottom of the window shows what's missing: "Choose a team: 3 to 5 titans", "Choose at least one enemy", or "Fix the number: 0 to 100". "Cancel" closes the window without changes.

The new rule takes **first place** for its element, while an edited rule stays in its place (if you changed the element, it goes first in the new one). Into the file, like everything else, it will go after "Save settings". If you opened the window using the "Condition" button from the first tab, after saving a notification will appear: "Rule "..." added to the "Rules and overrides" tab".

> [!note] A rule that the bot remembered on its own can be opened with the pencil and edited. Everything not visible in the window (for example, "loss tolerance" or an extra HP condition) **will be preserved as is**. The window will show such a condition in a gray line "Also in condition (preserved as is): ...".

### Rules remembered by the bot

If "Bot decides itself" is enabled, rules you didn't write appear in the list. You can recognize them by their name:

- :refresh-cw: **"Auto: Angus + Sylva in the room"** — the bot rolled back a bad battle, replayed with another pack, and that pack succeeded. The bot remembered: "against these enemies, set this pack". Below the title it says "Remembered by the bot after a rollback" (or "Your pack after a rollback, remembered by the bot", if you chose the pack in the SOS window). If the pack lost due to a condition (for example, "Araji below 50%"), it gets added to the condition. Such a rule takes first place.
- :star: **"Golden: Angus + Sylva in the room"** — "The pack often beat these enemies". Upon launch, the bot reviews history and takes a pack that against this composition of enemies had **5 battles or more** and won **80% or more**. Main pack, rescue rule packs, and your backup packs do not end up in "golden" rules.

In the file, these rules are named differently ("Anti-pack against: ...", "Golden rule against: ..."), and that's how they are written in the log: `[ОБУЧЕНИЕ] Новое правило '…': пак […]. Сохранено на 1-е место.` The window simply shows them concisely and clearly. If you rename a rule, you will see your own name.

What is useful to know about these rules:

- **The bot does not spawn duplicates.** A rule with the same condition is not created a second time: the old one gets its pack updated and moves to the top.
- **Not every successful rollback is remembered.** If a bad battle happened only because a titan entered it injured, and at 100% HP everything would be fine ("enemies had nothing to do with it"), a rule is not created.
- **The bot does not touch disabled rules:** it doesn't enable or overwrite them. It won't remember that same pack again, and a disabled "golden" rule won't return.
- **Deleted rules can return.** A "golden rule" will be created again on the next launch as long as there is no other rule against those enemies. If you don't like it, disable it with the toggle. An "Auto" rule will be created again by the bot if a rollback ends up the same way again.
- **While the window is open, the bot can write a new rule to the file.** When you click "Save settings", the window will re-read the file and put these new rules at the top without losing anything. If you visited the tab without changing anything, you will see a fresh list from the disk.

> [!warning] If an element's rules file is damaged (for example, edited by hand with an indentation error), the window will say, e.g. for water: "The rules file is damaged: bot_data/rules/water.yml — the window does not change this element's rules". Other elements will work. No need to edit the file by hand: click "Send log to author" on the main tab and describe what happened.

> [!tip] Where to start? Don't write anything in advance. Play a couple dozen rooms with "Bot decides itself" enabled and take a look here: the bot will already remember several rules. Disable unsuccessful ones, move good ones higher with the arrows. Add your own rules when you see repeating trouble: "Araji is constantly injured" — rescue rule; "this enemy squad always kills my main pack" — rule against enemies.

> [!done] Now you know how to teach the bot exceptions and understand why it deploys a specific pack. Next up — Telegram and windows asking for your help. [Next section →](#10)

## When a battle goes badly: SOS windows

Almost always, the bot manages on its own. But sometimes it runs into a situation where a human is required: the battle is won, but the price is too high, or the rules give no suitable pack. Then the bot **stops and calls you** with a window in the middle of the screen. SOS is a distress signal, like on a ship: "help needed". Until you answer, the bot doesn't click anything and waits (but not forever, more on this below).

There are three windows, each for its own case:

- :triangle-alert: **"Intervention required"** — the battle has ended, but the result is bad. This is the main window, it appears most often.
- :users: **"No suitable pack"** — the bot hasn't started the battle yet: the rules give no pack for this room.
- :check: **"The pack won"** — you picked another pack yourself, it won, and the bot asks whether to remember it.

!["Intervention required" window: reason, room, enemies, your pack with HP bars, and three buttons](images/sos_window.png)

> [!note] When the window appears: if "Bot decides itself" is **disabled** (default), the window opens after **every** bad battle. If enabled, the bot first tries to handle it without you and calls only when it cannot: the battle was manual (Angus), the result window could not be read, the pack was selected by you, the bot has already rolled back in this room as many times as allowed, or there is no backup pack. What a "bad battle" is and how to configure it is described in the sections on "Base and rooms" and "Auto-tactics".

### "Intervention required" window

At the top, briefly: "The battle went badly. What do we do?". Below are the facts so you can decide without checking the log:

- **Reason.** What exactly the bot didn't like. For example: "Критический порог! Араджи имеет 12% ХП (порог: 40%)", "Превышена Дельта потерь! Ригель потерял 45% ХП (допуск: 30%)", "ФАТАЛЬНО! Ияри мертв…", "Большие потери пака!…" or "Не удалось прочитать окно результата: не найдены…". Titan names are in the program language.
- **Room.** Door element and room number: "Fire · room 54".
- **Enemies.** Squares of titans fought against. If enemies weren't recognized, there will be no line.
- **Your pack.** Each titan with its health bar and the text "HP before battle → HP after": "36% → 12%". If a titan's HP is below its panic threshold (general or personal), the bar and number are **red**. If you entered the battle already wounded and left with almost no HP, it is immediately visible.
- **Timer.** At the bottom: "If you don't answer, the bot decides itself in 9:41". The last minute is yellow, then "The bot is deciding…". If 0 is set in "Auto-tactics", there is no line: the bot waits for you forever.

Buttons (from right to left, the main one is on the far right):

1. **"Roll back the battle"** (blue). Replay this battle with another pack. The window will hide, "Build a team" will open with the current pack; change the titans and click "Roll back with this pack". What happens next is in the "Rolling back" section below. If you close "Build a team" without selecting, the SOS window will return and nothing is lost.
2. **"Ignore"** (grey). Accept the battle as is: the room counts, the bot continues with whatever HP remains. Suitable when you are fine with the losses (for example, the titan entered wounded anyway and overall everything is fine).
3. **"Play manually"** (grey). The bot clicks nothing, and you play this room in the game yourself. The bot waits until you return to the corridor: the door flag must be visible for 2 consecutive seconds. If the last screen was the result window, the room counts; if you retreated without winning, it doesn't. If you closed the result window without replaying, the battle counts as it was. After playing manually, the bot forgets titan HP and slot lineups (it will re-read them itself from the team selection screen) and continues playing on its own.

> [!warning] A battle where **manual Angus ult** was used cannot be rolled back: there is no "Try Again" button on its result window. Instead of "Roll back the battle", the window will have a red **"Stop the bot"**, leaving only "Ignore" or "Play manually".

### Rolling back: what the bot does after your choice

The window closes, the command goes to the bot. Then it does everything on its own, which can be seen in the log by the `[ОТКАТ]` tag:

1. Clicks **"Try Again"** on the result window and waits for the battle to load (sometimes this takes 20–30 seconds or more, so it waits up to a minute).
2. Pauses the battle **once** and clicks **"Retreat"**.
3. Returns to the corridor, enters **the same room**, and deploys your new pack.

If the battle turns out bad again, the window returns. If it turns out good, the "The pack won" window appears (described below).

If connection with the game is lost (the "loading" icon doesn't end), the bot doesn't give up: it waits for the game up to 15 minutes and logs this. Only if rolling back fails completely, the bot saves a screenshot to `bot_data/debug/`, triggers a soft pause, and sends you a message in Telegram. Details are in the troubleshooting section.

### "No suitable pack" window

Appears when the bot has already chosen a door and looked at enemies, but **there is nothing to deploy**. This happens for two reasons, both from your rules:

- the "Ask me" rule triggered (it is designed specifically for this);
- the main pack for the room contains a titan forbidden by the "Skip" rule (the bot writes something like "ФАТАЛЬНО: Все паки отбракованы…").

The window asks: "The rules give no pack for this room. What do we do?" It contains the same "Reason", "Room", and "Enemies", but without HP bars: there was no battle yet. Buttons:

- **"Build a new pack"** (blue) — opens "Build a team", where the button is named "Apply". The bot will deploy the selected titans and **immediately save the pack as a rule** "against these enemies" (there is no check before saving here, be careful).
- **"Play manually"** — you play the room yourself, the bot waits in the corridor. The room counts if you win.
- **"Stop the bot"** (red) — the bot writes the session summary and turns off.

There is no "Ignore" button here: there is nothing to accept, as there was no battle.

### "The pack won" window

This window appears when a battle is won by a pack **selected by you** (via "Roll back the battle" or "Try another", in the window or in Telegram). If the backup pack was selected by the bot itself and succeeded, the bot will remember it on its own without asking anything.

Inside — room, enemies (from the last SOS window, if it was no more than 15 minutes ago), and your pack with HP after the battle. Question: "The pack under test won. Save it as a rule against these enemies?" Buttons:

- **"Save pack"** (green) — the bot will remember the rule "against these enemies" with this pack. In the rules list, it will appear as "Auto: …" or "Your pack after a rollback, remembered by the bot".
- **"Try another"** — "Build a team" and rollback again: the bot will replay the won battle with another pack.

If you don't answer, after the timer expires (label "If you don't answer, the bot saves the pack itself in…"), the bot will save the pack itself, as if you clicked "Save pack".

### Window close button and "Stop the bot?"

The windows don't have a simple "close": if you close the window, the bot will keep waiting for an answer. Therefore, the close button asks: **"Stop the bot?"**. If you answer "Stop the bot", the bot will finish, write the summary, and send it to Telegram. If it doesn't respond in 10 seconds, the program will stop it automatically. On "The pack won" window, the question is different: stopping there is the same as "STOP F10", **the session summary will not be sent to Telegram**. Changed your mind — click "Cancel", and the window will stay.

### What happens if you don't answer

Every time you don't answer within the time set in "Auto-tactics" ("SOS window timeout without an answer, min": default 10, up to 60, 0 — always wait), the bot writes `[ТАКТИКА] Ответа нет 10 мин. Решаю сам.`, the window closes, and you receive a message in Telegram that the bot decided itself. This also works when "Bot decides itself" is disabled. The decision depends on the window:

- **"Intervention required":** if there is a backup pack and the battle can be rolled back (not Angus, room attempts haven't run out) — **rollback** and the backup pack; otherwise, if all titans are alive — the battle is **accepted** ("Ignore"); otherwise (someone died or was not found on screen) — **soft pause**.
- **"No suitable pack":** if a backup pack without wounded and without forbidden titans fits — the bot deploys it **and does not save the rule**; if there is none — **soft pause**.
- **"The pack won":** the pack is saved.

Soft pause is like the "Pause F9" button: the bot waits in the corridor until you click "Continue".

> [!tip] Answered at the exact moment when the bot had already decided itself? No worries: the bot will skip the old response and log `[ЛОГИКА] Пропускаю ответ ...: он пришёл на прошлое окно.`

### Answer from Telegram

If Telegram is configured, **the same question** comes to the chat: a game screenshot, caption (room, enemies, reason, pack with HP), and buttons. You can answer wherever it's convenient: answered in chat — the window on the computer closes automatically, and vice versa.

- **"Rollback (Assemble pack)"** (green) — the bot will ask you to write the names of **3–5 titans** in chat separated by commas or spaces, show whom it recognized, and ask "Is everything correct?" ("Confirm pack" / "Write another"). For Angus manual battles and for "No suitable pack", a red "Stop the bot" appears instead.
- **"Play manually"** and **"Ignore (Continue)"** — same as in the window. "No suitable pack" does not have "Continue".
- "The pack won" in Telegram appears only if you also sent the pack from there: "Confirm and Save" or "Rollback and Try Again".

If the internet connection is lost, the message will be sent later (the bot retries), while the window on the computer remains. Telegram setup is in the section about it.

### Mini-bar and SOS windows

If the program window is minimized to the mini-bar, the SOS window will appear **in the center of the game**. The mini-bar is red during this time, and its "SOS" button brings the lost window above the game.

> [!tip] How to choose? Look at "Your pack". One titan entered wounded and dropped low, while the rest are fine — often "Ignore" is enough. Enemies are familiar and much stronger — "Roll back the battle" with another pack. Not sure at all — "Play manually". Rolling back costs time (the battle needs to reload, which can take 20–30 seconds or more), while "Ignore" costs nothing.

> [!done] Now you know what each SOS window means, what every button does, and what the bot will do without you. Next — how the bot decides on its own while you're away. [Next section →](#11)

## How the bot decides itself

In the section about SOS windows, you saw that the bot calls you after a bad fight. But it doesn't always call: if you enable "Bot decides itself" ("Base and rooms" tab, section 7), the bot **first tries to handle it without you** and asks for help only when it fails. Here we will look at how it thinks. There will be no formulas: just questions the bot asks itself and examples.

Imagine an experienced partner sitting next to you at the phone. A battle went poorly, and you stepped away for tea. They won't just sit and wait. They will remember what previously helped against such enemies, replay the fight with a different team, and record what worked. That's roughly how the bot behaves. It just has rules to avoid messing things up.

> [!note] "Bot decides itself" is **disabled** by default, and everything discussed below does not happen then: after every bad fight, the bot simply opens an SOS window. Turn on the toggle, click "Save settings" — it will take effect from the next "Start farming". Exactly what can be adjusted was covered in section 8 ("Auto-tactics and HP"), while here we discuss **what the bot does with these numbers**.

### Bad fight: what the bot does in order

1. **Notices that the fight is bad.** Someone died or is below the panic threshold, lost more HP than allowed, or three titans crumbled at once (sections 7 and 8). In the log, there is a line `[ТАКТИКА] Плохой бой: ...` with the reason.
2. **Checks if it can roll back on its own.** Impossible in four cases: the fight was manual (Angus's ultimate, the result window has no "Try again" button), the result window couldn't be read, **you** set the team (the decision is then yours too), or the bot has already used up its attempts in this room. If impossible, an SOS window opens, and the log shows `[ТАКТИКА] Сам не откатываю: ... Спрашиваю вас.` with the reason.
3. **Looks for a backup team.** How — in the next section. If no suitable team is found — an SOS window again.
4. **Rolls back and replays.** The same `[ОТКАТ]` steps as after your choice ("Try again", pause, "Retreat"), and a backup team is set in the same room. In the log: `[ТАКТИКА] Откатываю бой сам и переиграю паком ... (взят: ...)`.
5. **Looks at the result.** If the backup team succeeded, the bot moves on and usually remembers the team (more on this below). If the fight is bad again — a second attempt, and so on until attempts run out ("Backup teams to try per room", default 2, no more than 3). Then it calls you.

> [!tip] The bot rolls back the entire fight each time, rather than "fixing on the fly". A rollback takes time (the fight must be reloaded, which can take 20–30 seconds or more), so it dislikes wasted attempts: see below how it selects a team.

### Where the bot gets a backup team

It goes down the list from top to bottom and takes the **first suitable one**:

1. **Your "Backup teams"** — "Base and rooms" tab, room card. Taken in order, as you arranged them. In the log, the source is called "ваш список запасных паков".
2. **Teams from the rules of this element** — in the log, "правила стихии". Inside, its own order: first rules "against these enemies", then teams that have already defeated these exact enemies (best by remaining HP first), then other "anti-teams", then everything else, including the room's main team.
3. **Battle history** — in the log, "история боёв". This is the last priority, and only teams that have already defeated these enemies are taken. The bot remembers battles from the last 20 runs.

What the bot will **never set** as a backup:

- a team that has already lost in this room (not to repeat a mistake);
- a team that "loses to these enemies": last time against them, the fight was rolled back due to the enemies, and the team has no more wins than losses. A single failure **does not ruin a good team**: if it won against these enemies five times and lost once, the bot will still take it;
- a team with a titan forbidden by a "Skip" rule;
- a team with a titan whose HP is already **below the panic threshold**: the bot will not send it into battle to certain death;
- from history — a team containing a titan you haven't specified anywhere (neither in teams nor in rules). History retains teams from long-deleted rules, and the bot will not resurrect them.

There are also "dangerous" teams: those where a wounded titan, judging by past battles, won't survive until the end of the fight. The bot takes them **as a last resort**, only if there is nothing better. How it determines this is explained in the "Wounded titan" section below.

Why the bot didn't take a particular team can be seen in the log: `[ТАКТИКА] Не беру запасной пак ...` and the reason. If backup teams run out and the fight is still bad, this is not a glitch, but an honest "don't know what else to use".

### To save or not: the "Auto: …" rule

The backup team succeeded. The bot writes this into a rule "against these enemies — use this team", and next time it encounters the same composition, it will use it immediately. In the list, this is the rule "Auto: … in the room", which takes first place (section 9). In the log: `[ТАКТИКА] Запасной пак ... справился. Запоминаю его против этих врагов.`

But sometimes **saving is not allowed**. Example: Araji entered the battle with 36% health and dropped to 5%. The main team is not to blame: if Araji had been healthy, the fight would have gone fine. Had the bot recorded the rule "against these enemies use the backup", it would start placing the backup team where the main team copes perfectly, wasting your strength. Therefore, the bot checks: **"would the fight have been bad with 100% HP for everyone?"** If no — the enemies are not to blame, the help was a one-time affair, and no rule is created.

In the log, this is immediately visible: `[ТАКТИКА] Враги ни при чём: в бой вошли раненые ...` and then `Правило не запоминаю: это была разовая помощь раненым титанам`.

Saving will also not happen in three other cases:

- the bot did not recognize enemies (`[ОБУЧЕНИЕ] Враги не распознаны — правило не сохраняю`): a rule "without enemies" would trigger in any room;
- you turned off a rule with the same team using the toggle: the bot does not touch disabled rules;
- you picked the team yourself: then your "The pack won" window decides (section 10).

### Wounded titan: help in advance, not after the fight

The most valuable thing the bot can do is **prevent a bad fight** rather than clean up after it. While on the team selection screen, it looks at the titans' health and at history: "how did fights with this team in this room end?" For this, the bot stores how much HP a titan usually **loses** in battle with this team (average over the last five fights, requires at least two fights). If the wounded titan's entry HP minus usual loss **drops below the panic threshold**, the bot won't take risks and will immediately set a backup team, before the fight.

Example. Araji with 36% HP enters fire. In recent battles here, he usually lost about 29%. That leaves: 36 − 29 = 7%, and the panic threshold is 40. The fight is almost certain to end poorly, so the bot sets a backup team, for example with Moloch, **immediately**. This is a one-time help, and the rule is not remembered.

Two nuances so the bot doesn't seem strange:

- **Energy is also important.** If a titan currently has roughly the same energy as in previous fights (difference no more than 25%), the bot uses those exact fights for the forecast. Araji with good energy in fire loses little, while with empty energy he loses a lot, and the forecast takes this into account.
- **One fight is not statistics.** With fewer than two fights, the bot does not trust the forecast and changes nothing.

Teams from rescue rules ("if Araji is below 50% — use Sigurd", section 9) are not replaced by the bot in advance: you set them specifically for the wounded titan, and your intention is more important than its forecast.

### Door by health

If the bot decides itself and **several allowed doors** are visible in the hallway, it chooses not simply in order (section 8, "Door priority"), but with an eye on the wounded:

1. First goes to the door **behind which the wounded titan will be healed**: your rescue rule will trigger or the bot itself will assemble a heal team.
2. A door behind which the wounded titan faces trouble, judging by past battles, the bot **skips** if there is another.
3. Otherwise, everything is as usual, in order.

Visible in the line `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...`. A door forbidden by a "Skip" rule will still never be opened by the bot. The bot cannot see the enemies behind the door yet, so here it relies on the door's base team.

### Heal team in "Mixed"

If a wounded titan can be healed and your heal rule didn't trigger, the bot **assembles a heal team itself**: it places the wounded titan and, if needed, a healthy charged healer into the "Mixed" room. They heal one by one, main titans before backups, and those below the panic threshold are not healed at all. All details (threshold "Heal a titan if HP is below, %", "Who to remove from the team for the wounded", that very Sigurd for Rigel) — in section 8. One thing matters here: this is the same kind of **one-time help** as a backup team from a forecast. No rule is created after it, and in the summary it is counted separately ("heal teams (bot assembled itself)").

### "Golden rules": the bot learns from all history

The bot makes all these decisions on the fly. As for "golden rules", it summarizes them **once, when starting farming**. The bot reviews the battle history and searches for a team that played **5 battles or more and won 80% or more** against the exact same enemy lineup. It records such a team with the rule "Golden: … in the room" (section 9). In the log: `[ОБУЧЕНИЕ] ...: 'Золотое правило против: ...' — пак ... Сохранено на 1-е место.`

Will not become golden:

- the room's main team, rescue rule teams, and your "Backup teams" (they are for help, not for every fight);
- heal teams assembled by the bot itself: they are needed only while the titan is wounded;
- a team with a titan not present in your teams or rules;
- a team against enemies for which a rule already exists (yours, "Auto", or disabled).

There are no golden rules while "Bot decides itself" is disabled. Has an unsuccessful one appeared? **Turn it off with the toggle** instead of deleting it: a deleted one will return on the next launch, while a disabled one will not be touched by the bot.

### If you didn't answer the SOS window

This is no longer "bot decides itself", but "bot decides instead of you" (section 10, "What happens if you don't answer"). It works even when "Bot decides itself" is disabled: upon timeout ("SOS window timeout without an answer, min"), the bot will roll back the fight with a backup team, accept it, or enter a soft pause. Each time, it writes `[ТАКТИКА] Ответа нет N мин. Решаю сам.`, closes the window, and sends a message to Telegram.

### How to understand what the bot did without you

At the end of the session in the "Session summary" block ("Details" button) and in the `[ИТОГ]` line, there are counters:

- **"rollbacks"**: how many battles were replayed in total;
- **"of which without you"**: how many of these rollbacks the bot made on its own without asking, both by forecast and by timeout;
- **"heal teams (bot assembled itself)"**: how many times it healed a wounded titan with a heal team.

The same summary will arrive in Telegram: "Rollbacks: 6 (bot itself: 5)". If "without you" is almost everything, the bot is coping well. If the number grows while "Golden rules" do not appear, it means the same enemies break the main team time after time. Check the "Rules and overrides" tab to see which rules it remembered, and consider whether it's time to change the main team.

> [!warning] The bot decides based on **history** and forecast, rather than seeing the battle ahead. It can make mistakes: in the first few days, when there is little history, a backup team is selected randomly. Don't be alarmed if, during the first few dozen rooms, "Bot decides itself" rolls back more often than you'd like. The more battles in history, the more accurate the choice.

> [!tip] Where to start? Set at least one or two **"Backup teams"** in each room (section 7): then the bot won't be searching blindly. Enable "Bot decides itself" and just watch the `[ТАКТИКА]` lines and the "Session summary" for a couple of days. If you don't like what the bot is doing, turn off the toggle, and everything will return to SOS windows.

> [!done] Now you understand when and how the bot manages without you, what it remembers, and when it calls for help. Next is Telegram: how to receive messages when you are away from the computer. [Next section →](#12)

## Telegram

The bot can text you on Telegram while you are away from your computer: went to the kitchen, went to sleep, or left for work. If a battle needs your help, a screenshot and buttons will arrive in the chat. You press a button on your phone — the bot does as you said. If everything goes smoothly, the bot stays quiet: messages arrive **only when there are problems** and **once at the end of the session**.

What you will need: the Telegram app and five minutes. You only need to set it up once.

> [!note] Telegram is optional. Without it, the bot works just the same, you just see SOS windows only on your computer screen, and there is no session summary. But if you plan to leave the bot running overnight, set it up: that way you will learn about a problem right away, not in the morning.

### What you need to prepare

You need two things, both taken directly from Telegram:

- :send: **Bot token** (the key the program uses to log into your bot). This is a long string of numbers and letters, for example `123456789:AAH…`. The token is issued by a special bot **@BotFather**.
- :user: **Chat ID** (chat number). This is a number that helps Telegram understand whom to deliver the message to: you, and not someone else.

> [!warning] The token is like a password to your bot. Do not show it to anyone, do not send it in screenshots or emails (even to the author of the program). Take a screenshot of the "Telegram settings" window while the token is hidden with dots.

### Step by step

1. **Create your bot.** In Telegram, find **@BotFather** (the real one has a blue checkmark next to it) and click "Start". Send it `/newbot`, come up with a name (any name, only you will see it) and a username ending in `bot`, for example `moi_titan_bot`. In response, BotFather will send a message with the token: copy it.
2. **Find out your Chat ID.** Find the bot **@getmyid_bot**, click "Start" — it will reply with the string `Your user ID` and a number. This is your Chat ID, copy the number. If this bot does not answer, there is a backup method: send any word to **your** bot from step 1, open the URL `https://api.telegram.org/bot<твой токен>/getUpdates` in your browser (instead of `<твой токен>` paste your token) and find `"chat":{"id":` in the response — the number right after it is your Chat ID.
3. **Click "Start" in your bot.** Find the bot you created in step 1 and click "Start" (or send it `/start`). Without this, Telegram **will not allow** the bot to message you first. This is the most common reason why messages do not arrive.
4. **Open the window in the program.** Click the Telegram dot on the left bar or the **"Set up Telegram"** button in the "Base and rooms" tab (section 7). The "Telegram settings" window will open.
5. **Fill it in.** Turn on the "Send messages to Telegram" switch. Paste the token into the "Bot token (from @BotFather)" field, and paste the number into the "Chat ID" field. The **"Paste"** button next to the field is the most convenient: it takes whatever you copied. The token is shown with dots; the eye icon shows it so you can verify that it was pasted correctly. Right-clicking the field also gives "Paste".
6. **Test the connection.** Click **"Test Telegram"**. After a few seconds, a green "Message sent — check Telegram" will appear on the right, and a "Connection test: everything works" message will appear in the chat with your bot. If it arrived, everything is ready.
7. **Save.** Click **"Apply"**, then click **"Save settings"** at the bottom of the page.

![The "Telegram settings" window: switch, token and Chat ID fields, "Paste" and "Test Telegram" buttons](images/telegram_window.png)

> [!warning] "Apply" only transfers the values to the "Rule Wizard" page; they are **not written** to the file. Until you click "Save settings", "Unsaved changes" is lit at the bottom, and the bot knows nothing about Telegram. If you leave the page without saving, the program will ask "Save changes?".

> [!tip] "Test Telegram" tests what is currently written in the window, even if you haven't saved anything yet. So test **before** clicking "Apply": found an error — fixed it — tested again. The test runs in the background, the window does not freeze, and you won't have to wait for a response longer than 20 seconds.

### If the test failed

A red line "Failed to send: …" with the reason will appear under the button. The most common ones:

- **"Fill in the token and Chat ID"** — one of the fields is empty.
- `Unauthorized` — the token is incorrect: a character is missing, an extra space, or it wasn't copied completely. Paste it again using the "Paste" button.
- `chat not found` or `Forbidden` — the Chat ID is incorrect or you didn't click "Start" in **your** bot (step 3). Check both points.
- **"Telegram connection error"** — no internet connection or Telegram cannot be opened from this computer. Make sure Telegram (or the telegram.org website) works on the same PC.

If it still doesn't arrive after fixing, create a new bot with @BotFather (step 1) and start over: it's faster than searching for a typo.

### How to know that Telegram is enabled

On the bar on the left, next to the Telegram button, there is a dot: hovering over it displays a tooltip **"Telegram: on"** or **"Telegram: not set up"**. On means the switch is enabled and both fields are filled. This is **not a connection check**: whether the token works will only be shown by the "Test Telegram" button. The same is visible on the "Base and rooms" tab: next to the "Set up Telegram" button, a green "SOS notifications on" or a gray "Telegram not set up" is lit. The dot updates automatically a couple of seconds after saving.

### What messages arrive

The message language is the same as chosen in the program window.

- :swords: **SOS window** — header "Your help is needed" (or "No suitable pack"), a game screenshot, and a caption: room, enemies (who you were attacking), reason, your pack with HP and energy bars. Buttons at the bottom. This is the same question as in the window on the computer (section 10).
- :triangle-alert: **Alerts** — a short message without buttons that tells you what happened and what to do. Here they are: "Battle rollback failed" (the bot is on soft pause, look at the phone screen), "The bot seems to be stuck" (5 minutes without a room) and the same message when a battle cannot be started (most likely no connection to the game server), "PC screen is locked" (the bot cannot see the game for more than a minute; unlock your PC, and it will continue on its own), and "You did not answer — the bot decided itself".
- :chart-no-axes-column: **Session summary** — when the bot stopped: how much time, rooms, floors, and titanite have passed, whether there were rollbacks and SOS windows ("by the bot: N" are rollbacks it performed without you), the longest rooms. If the bot crashed with an error, the header will say "The bot crashed with an error" along with the reason.

The summary arrives upon any stop: reached the goal, pressed Ctrl+Q, Ctrl+Shift+Q, or the bot crashed with an error. It **does not arrive** after "STOP F10" or after "Stop and close" (section 6) because they kill the bot instantly.

### Buttons under the SOS message

Press them in Telegram the same way as in the window on your computer:

- **"Rollback (Assemble pack)"** (green). The bot will send: "Write the names of 3-5 titans in chat". Type them in the chat separated by commas or spaces, for example `гиперион, сигурд, нова` or short, by the first three letters: `гип сиг нов`. The bot will reply with whom it recognized and ask "Is everything correct?": **"Confirm pack"** will start the rollback, **"Write another"** will let you enter them again. If it found other than 3–5 titans, the bot will tell you how many it recognized and ask you to write them again.
- **"Play manually"** (blue). The bot doesn't press anything and waits for you to finish the room yourself.
- **"Ignore (Continue)"** (gray). Accept the battle as is and move on.
- **"Stop the bot"** (red). Instead of "Rollback", it is shown when the battle was played manually (Angus's ultimate) or there is no suitable pack. The "No suitable pack" window does not have a "Continue" button.

When the pack you selected succeeds, the question "The pack won" comes to Telegram with two buttons: **"Confirm and Save"** (remember the pack with a rule) and **"Rollback and Try Again"** (write another). It is sent to the chat only if you also sent the pack from Telegram.

After clicking, a single green button "Selected: …" remains under the message, and the rest disappear. You can reply **once**: the bot does not listen to clicks on old messages. If you answered in the chat, the window on the computer will close by itself; if you answered on the computer, the bot will stop waiting for a response from Telegram.

> [!tip] Did the bot decide on its own while you were looking for your phone? No worries. A message "You did not answer — the bot decided itself" will arrive, and the buttons on the old question will no longer do anything. How long the bot waits for you is configured in "Auto-tactics" (section 8, "SOS window timeout without an answer, min").

### If internet connection is lost

The bot does not stop and does not wait for Telegram: the message is sent in the background. If it fails due to connection issues, it tries again in **30 seconds, 1, 2, 5, and 10 minutes** (about 18 minutes), and the log shows lines `Сообщение в Telegram не ушло (...). Пробую снова через N с.` and at the end `Сообщение в Telegram: отправлено с N-й попытки`. The same goes for the SOS window: it remains on the computer screen, and the question will be sent to Telegram when the connection returns. The bot retries the session summary faster (after 10 and 30 seconds) because it turns off afterwards. The bot does not retry errors caused by Telegram itself (invalid token): those need to be fixed in the settings.

> [!note] The bot does not accept commands from you "at any time" (stop, pause from chat). Telegram only responds to questions that the bot asked itself. You cannot stop the bot from the chat, except using the "Stop the bot" button under the SOS message.

> [!done] Telegram is configured, and now the bot will be able to call you wherever you are. Up next is statistics: how many rooms, floors, and titanite were gained by day. [Next section →](#13)

## Statistics

The «Statistics» page answers the question "how much did I play?": how much titanite, rooms, floors, and titan potion were gathered over a week, a month, and all time. Opened by the **«Statistics»** button on the left bar, «Activity statistics» is written at the top.

The bot **calculates these numbers itself**, rather than reading them from the game screen. Completed a room — recorded: **6 titanite and 25 potion**, and if there was an "x2" icon in the result window — **12 titanite and 50 potion**. Received a reward at a save point — recorded a floor. A room you passed manually and that the bot counted (section 10) is also recorded. Totals are located in `bot_data/stats.json` and stored "by game days".

> [!note] A **game day** starts not at midnight, but at the reset hour you set in «Rule Master» (by default 5:00, section 7). Therefore, everything the bot gathered at 02:30 AM is recorded under **yesterday's** day: in game at this time yesterday's day is still ongoing. If «Titanite (today)» is zero in the morning although you played at night, that's how it should be.

### What's on the page

At the top left is a hint, at the top right is the **«Period»** selector, below them five tiles, a chart, and «Manual correction» at the bottom.

- :calendar: **Period** — «7 days», «14 days», «30 days», or «All time». The selected one is lit in blue. When opened for the first time, it is set to «14 days».
- :gem: **«Titanite»** — total for the period.
- :calendar: **«Titanite (today)»** — only for the current game day. Does not depend on the period.
- :flask-conical: **«Titan potion»**, :door-open: **«Rooms»**, and :layers: **«Floors»** — totals for the period.

Numbers up to 100,000 in the tile are written in full (`98 540`), while long ones are shortened: `105.5K` is one hundred five and a half thousand, `1.24M` is one million two hundred forty thousand. The full number will appear if you hover the mouse over the tile. «All time» takes general counters from the file rather than the sum of bars, so tiles match history even if there are many bars.

> [!tip] The page reads numbers **every time it opens**, not during gameplay. Bot is working but numbers don't change? Switch to another page and return.

![The «Statistics» page: tiles, chart by days, and selected bar with callout](images/stats_page.png)

### Chart: bars and clicks

Under the «Titanite activity» header is a note showing how bars are grouped: «by day», «by week», or «by month». There are no more than fifteen bars so the chart doesn't turn into a fence:

- **7 days and 14 days** — one day per bar.
- **30 days** — by week (Monday to Sunday; outer weeks are incomplete — containing only days within the period).
- **«All time»** — by days while data is less than two weeks; then by weeks, and when weeks exceed fifteen, — by months.

On the left is a scale with a dashed grid, numbers on the scale are short (`3.6K`, `140K`). Labels under bars, if they don't fit, are shown every second one; the last one (today's) is always visible. A day without playing is an empty space, no bar. For a period without data, the chart will say «No data for this period».

1. **Hover mouse over a bar.** The exact amount of titanite will appear above it. This is just a tooltip, nothing changes.
2. **Click on a bar.** It will become brighter, others will pale, a callout with date and number will appear nearby. For a week, titanite in the callout is detailed **by day**, for a month — **by week**. A blue label lights up at top left, for example «Showing day: 19.10.2026 · today» (or "Showing week", "Showing month").
3. **Look at the tiles.** They now show numbers for this bar: titanite, potion, rooms, and floors for the day, week, or month. «Titanite (today)» remains current.
4. **Return to totals.** Click the same bar again or the blue label with a cross (✕). Changing the period will also reset the selection.

### Table

The **«Table»** button at top right above the chart shows the same bars as a list: «Date», «Titanite», «Rooms», «Floors», «Titan potion». Recent dates on top, **«Total»** row at the bottom. A row can also be selected by clicking, and tiles will show its numbers. The button turns into **«Chart»** and returns the picture. The table is convenient when exact numbers for all days at once are needed.

![Table: dates, titanite, rooms, floors, and potion, «Total» at the bottom](images/stats_table.png)

### Manual correction

The bot calculates by its own math (6 or 12 titanite per room), but in game the number might be different: you played yourself, the bot was off, the program was launched later in the day. To make statistics match the game, there is a **«Manual correction»** card.

1. **Select a day.** The list has "Today", "Yesterday", and five previous days, seven total. Need an older day? Choose period «7 days» or «14 days» and click its bar: this day will be put in the list automatically (won't work for week or month bars — only daily).
2. **Enter the total number from game.** In «Titanite per day» field — what is shown in game **for the whole day**, not "how much to add". For the selected day, what is currently recorded is already filled in.
3. **Click «Apply»** (or Enter in the field).

Example. The bot recorded 90 titanite for the day, but in game for the same day it's 150. You enter **150** — the program adds the difference of 60 and recalculates the rest: roughly **+5 rooms, +1 floor, and +250 potion**. This is an estimate: it assumes the first 10 rooms of the day gave 6 titanite each, and the rest 12 each. If you played differently, rooms and floors might slightly differ from actual ones, but titanite will be exactly as you set.

When done, a notification «Titanite for 19.10.2026: 150» will appear at the bottom, and the log on the main page will get the line `[СТАТИСТИКА] Данные за 2026-10-19 синхронизированы! Дельта: +60 тит., +5 комн., +250 зелий.` (Data for 2026-10-19 synchronized! Delta: +60 tit., +5 rooms, +250 potions.). If you entered less than recorded, numbers will decrease.

What could go wrong:

- **«Enter a whole number from 0»** — letters, comma, minus, or empty field. Field will turn red.
- **«The bot collected 90 on this day by itself, you can't enter less»** — you cannot specify less than what the bot gathered **itself**, since that was recorded honestly. You can only lower the number down to this value.
- **«This day already has exactly that»** — you entered the same number, nothing to change.

> [!warning] «Apply» writes numbers **immediately** to `bot_data/stats.json`. There is no «Save settings» button here and none needed, unlike in «Rule Master» (section 7). You cannot undo an edit with a button, but nothing stops you from entering the previous number again.

> [!note] Correction changes **only statistics**. «Session summary» on the main page and the session target (section 4) are calculated separately based on what the bot gathered in this run, and do not depend on the «Statistics» page.

### «Reset»: clear all history

The **«Reset»** button (with a trash can icon, on the right in «Manual correction» card) resets all statistics to zero: titanite, rooms, floors, and potion for all days. Clicked by accident? Nothing will happen: first the program will ask «Reset statistics?» and remind you that this cannot be undone. You confirm with «Reset» button in the window, or decline with «Cancel» button. After resetting, «Statistics reset» notification will appear, and the log will get line `[СТАТИСТИКА] Вся история полностью сброшена!`.

Only statistics are wiped. Rules, packs, settings, `profile.yml`, and battle logs remain. If the bot is running at that moment, it continues and counts further from zero, while session target is not reset.

> [!tip] Want to reset "for a test"? Save a copy first: close the program and copy `bot_data/stats.json` file to another location (the program folder is opened by «Bot folder» button on «About» page). You can restore history by placing the file back.

### Frequently asked questions

- **Numbers don't match the game.** The bot calculates rather than reading the screen: 6 or 12 titanite per room. If you obtained titanite from other sources, the game will show more. Compare and adjust via «Manual correction».
- **Today is empty, but I played.** Check the reset hour: before it, the bot writes to "yesterday" (see "Game day" above). Changed hour in «Rule Master»? Restart the program so the page picks it up too.
- **Few bars, but large period.** Days when the bot didn't run are empty on the chart. «All time» and months compress the chart by default: to see specific days, choose «7 days» or «14 days».
- **In the log `[СТАТИСТИКА] ВНИМАНИЕ: Файл stats.json поврежден`.** History file could not be read (for example, PC shut down during writing). The bot starts new statistics from zero and will overwrite the file. Copy it in advance if old history is important.

> [!done] Now you know how to read numbers, switch periods, check statistics against the game, and erase it. Next — what to do if something goes wrong. [Next section →](#14)

## If something went wrong

Good news: the bot knows how to get out of most troubles on its own. Stuck — it will look around and start over. Lost internet connection — it will wait. Computer locked — it will hold on and continue. You are needed only when it **asked itself** (paused, wrote to Telegram) or when it clicks nothing and the log doesn't explain why. This section covers both cases: what the bot does without you, how to figure out where the issue is, and what to click.

Rule for all cases: **do not panic and do not rush**. It is not scary to stop, restart, and launch the bot again: stats, teams, rules, and settings are stored in files and won't go anywhere.

### How to tell if something is wrong

- :triangle-alert: **Red number on the "Errors" pill** in the log on the main tab. It counts not only breakdowns: warnings get here too (for example, "game window is covered"). The number itself is no reason to be scared; you need to open the pill and read the lines.
- :pause: **"Pause" state and green "Continue" button, even though you didn't press pause.** This means the bot paused itself and is waiting for you. The log will show a `[ВНИМАНИЕ] Бот на мягкой паузе: ...` line with the reason.
- :send: **Telegram message** (if configured, section 12): "The bot seems to be stuck", "Battle rollback failed", "PC screen is locked".
- :eye: **Silence.** Lines do not appear in the log for a minute or longer, and nothing happens in the game. This is also a sign: see the "Common cases" section below.

Log tags that indicate a problem:

- `[СТОРОЖ]` — the bot decided it was stuck and started over on its own.
- `[СЕТЬ]` — looks like no connection to the game server.
- `[ЭКРАН]` — the computer won't allow taking a screenshot (it is locked).
- `[ОТКАТ]` — battle rollback steps and its errors (section 10).
- `[ВНИМАНИЕ]` — the bot requests attention: pause, closed game window.
- `[ОШИБКА]` — something broke; written right next to it.
- `[ADB]` and `[VISION]` — phone connection and clicks.

### What the bot does on its own

You don't press anything here. Just know that this is normal and doesn't break the session.

- :gauge: **Stuck: 5 minutes without a single room.** This is the "watchdog" (the name of the check that monitors whether the bot is stuck). The bot writes `[СТОРОЖ] Бот 5 мин не прошёл ни одной комнаты ... Тревога 1 из 3.`, saves a screenshot, sends a message to Telegram (if configured), and performs a **"smart start"**: looks at the screen again and decides where to continue from. Didn't help, and 5 minutes later there is another alarm. **Third alarm in a row** (about 15 minutes without rooms) — the bot enters soft pause and waits for you. The watchdog doesn't count time while the bot was waiting for you (SOS window, pause, another window over the game).
- :activity: **Stuck in one place.** Team selection screen didn't appear in 30 seconds or result window didn't appear in 3 minutes. Then `[СТОРОЖ] Зависание: ...`, screenshot, and the same smart start, but without a Telegram alarm.
- :globe: **Battle doesn't start (most likely no connection to the game server).** "Auto" button is pressed, but there is no battle. The bot tries two more times immediately, then waits and tries again: after 30 seconds, 1, 2, 4, and 8 minutes. All this appears in the log as `[СЕТЬ] Бой не начался N раз(а) подряд ... Жду N с и пробую снова.` If this didn't help either (around 15 minutes): screenshot, message "The bot seems to be stuck", and soft pause.
- :rotate-ccw: **Lost connection during battle rollback.** The bot doesn't give up, but **waits for the game for up to 15 minutes**: writes `[ОТКАТ] Бой не загрузился ... Не сдаюсь`, saves a screenshot, and reports once a minute `Всё ещё жду игру`. Connection restored — rollback will finish on its own (`Игра снова откликается`). Not restored in 15 minutes — "Battle rollback failed", Telegram message, and pause.
- :monitor: **Computer is locked (Win+L) or screen turned off.** Windows doesn't allow taking screenshots, and the bot sees nothing. It **does not crash**, but retries every 2 seconds: `[ЭКРАН] Не удаётся сделать снимок экрана ... Похоже, ПК заблокирован`. Longer than a minute — a single "PC screen is locked" message. Unlocked — `[ЭКРАН] Снимок экрана снова работает`, the bot continues on its own.
- :layers: **Game window is covered by another window.** The bot waits for it to become active again (`[ВНИМАНИЕ] Окно игры перекрыто ... Бот ждет фокуса`). Click on the game window, and it will continue. Why this happens is in section 5.
- :target: **Click didn't go through.** If 4 seconds after clicking the screen hasn't changed, the bot clicks again: `[VISION] Клик по '...' не зарегистрирован сервером ... Повторяю...`. Occasional lines like this are normal: the phone sometimes "thinks".
- :smartphone: **Cable connection to phone flickered.** The bot writes `[ADB] Постоянное соединение с телефоном оборвалось ... Переподключусь при следующем нажатии` and reconnects.
- :send: **Telegram message was not sent due to internet issue.** The bot will retry it later (section 12) and keep working.

> [!note] How many times the bot froze during a session can be seen in the `[ИТОГ]` block in the log (line with the word "зависания"). Rare occurrences are fine. If there are many, look for the reason in the "Common cases" section below.

### The bot paused on its own: what to do

It stopped because it cannot proceed without you. Follow these steps in order:

1. **Look at the game screen.** The `HeroWarsBot_Arena` window shows where the bot got stuck: result window, battle, pause menu, loading "mushroom", or something unexpected (another window, ad, game prompt).
2. **Read the last lines of the log.** Open the "Errors" pill and look at the bottom: it says why the bot stopped (`[СТОРОЖ]`, `[ОТКАТ] ОШИБКА`, `[СЕТЬ]`).
3. **Return the game to the Dungeon corridor.** Close extra windows, wait until the battle ends or loads, and reach the screen with the door and flag.
4. **Click "Continue".** The bot will re-examine the screen (smart start) and keep going.

> [!note] Pause after an unsuccessful rollback can also happen like this: manual battle finished in time, "Try again" is no longer on the result window, and it cannot be rolled back. The result window stays on screen — no need to close anything; after clicking "Continue", the bot will click "OK" itself. Look at this window to see who survived.

> [!tip] The bot doesn't pause over every little thing, but when it tried and failed. Therefore, before clicking "Continue", figure out **what exactly** went wrong. If the cause remains (no internet, game closed), the bot will pause again in a few minutes.

### Common cases: what to check and what to do

**The bot clicks nothing, and the log is silent.** Most likely, it doesn't see the game or can't find anything in it. Check in order:

1. **Game window is in place.** It is named `HeroWarsBot_Arena`, not minimized and not closed. If there is no window, the bot doesn't write about it, but silently checks for it every half second. Therefore, silence in the log when the window is missing is normal. Click "Connect phone": the window will open again.
2. **Window size hasn't changed.** The bot measures the window once on startup and uses this measurement going forward. If you stretched, maximized, or moved the window after starting — stop the bot (F10), click "Reset game window size", and then "Start farming" again. Details are in section 3.
3. **The game shows the Dungeon corridor**, not a menu, shop, another event, or ad window.
4. **Program language matches game language** (two letters at the bottom of the left bar). Otherwise, the bot won't recognize buttons.
5. **Nothing obstructs the game window.** Any window on top of the game — and the bot waits for focus.

**The bot "sees" and clicks, but nothing happens in the game.** The log shows consecutive lines "Клик по ... не зарегистрирован сервером ... Повторяю...". This means click commands aren't reaching the phone. Check:

- **Both** debug settings are enabled on the phone: "USB debugging" and "USB debugging (Security settings)". Without the second one, video works, but taps do not (section 2).
- Phone is unlocked, cable is firmly plugged in. Try another USB port.
- In command prompt `adb devices` shows `device` next to the phone, not `unauthorized` or an empty list.
- If it didn't help: stop the bot, click "Restart scrcpy", then "Start farming".

**The bot clicks in the wrong spot or confuses titans.** Most often the game window is the wrong size or was moved after launch (reset window size as above). If the size is correct but the bot still misses — save a screenshot of that moment and send it to the author along with the log (below).

**Program window is "not responding".** The program monitors itself: if the window doesn't respond for 5 seconds, it records in a file which line of code it got stuck on. The file is located in `bot_data/debug/` and is named `ui_freeze_<дата>_<время>.txt`. What to do:

1. **Wait a minute.** Often the window revives on its own: it is busy with heavy work.
2. **The bot runs separately from the window.** Need to stop it, but buttons don't respond? Press Ctrl+Shift+Q: this hotkey is listened to by the bot itself, not the program window (section 6).
3. **Didn't revive — close the window with the cross icon.** If it doesn't close — use Task Manager (Ctrl+Shift+Esc). Then check there if `HeroWarsBot.exe` or `python` is still running: if so, end it as well, otherwise the bot will continue clicking in the game without a window.
4. **Send the `ui_freeze_...txt` file to the author.** It contains only file names and program code lines, nothing personal.

**The bot stopped, but you didn't stop it.** Open the "Session summary" card on the main tab ("Details" button) and check the reason:

- "scrcpy window closed" — game window was closed or disappeared (cable unplugged, phone locked). Connect phone again.
- "the bot finished" — process ended without reason. If Telegram is set up, the summary arrived there; if not, look in the log for `[ОШИБКА] Бот остановился из-за ошибки:` line and the text below it.
- "Team not found in rules" — main team is not set for the room. Open "Rules Master" → "Base and rooms" and set it in all four rooms (section 7).
- "Error: ..." — program crashed. Send log to author (below).

> [!warning] After "STOP" (F10), the bot doesn't have time to write the `[ИТОГ]` block and doesn't send a summary to Telegram: it was terminated on the fly (section 6). This is not a failure.

**Phone "went to sleep" or screen turned off.** The program runs scrcpy with "keep phone awake" mode (`--stay-awake`). "Turn off phone screen" button turns off only the **screen**: the game runs, and the bot sees everything. But if the phone locked or disconnected from cable, the game window will show the lock screen or emptiness, and the bot won't find anything. Unlock phone, check cable, and click "Restart scrcpy".

**Telegram messages do not arrive.** Most likely, "Start" was not pressed in your bot or token/Chat ID is incorrect — detailed in section 12. The bot works as usual in the meantime.

**The bot picks wrong titans or decides differently than you wanted.** This is not a bug, but rules: re-read sections 7–11 (teams, thresholds, rules, "Bot decides itself"). The bot's decision can always be found in the log in `[ТАКТИКА]` lines.

### Where logs and screenshots are stored

The **"Bot folder"** button on the "About" page opens the folder where the program was launched. It contains files created by the bot itself. What you need is inside the `bot_data` folder:

- :file-text: `bot_data/logs/bot_log_<дата>_<время>.txt` — **full log of every bot run.** The bot writes it itself, line by line, so it remains even after a crash or closing the program. This is the main file for troubleshooting.
- :gauge: `bot_data/logs/timings_<дата>_<время>.csv` — how long each room took (corridor, squad building, battle, result).
- :swords: `bot_data/logs/battle_log_<дата>_<время>.jsonl` and `battle_log.csv` — battle history: room, enemies, team, result, HP and energy of titans.
- :image: `bot_data/debug/` — **screenshots for troubleshooting.** The name tells what happened: `stuck_...` — stuck, `sos_...` — SOS window, `rollback_wait_...` — waited for the game during rollback, `rollback_fail_...` — rollback failed, `start_fail_...` — battle didn't start, `result_unreadable_...` — result window unreadable. Followed by room number, element, and time (`stuck_комната12_water_2026-10-19_14-03-21.png`). Also `ui_freeze_...txt` if the program window froze.

> [!warning] The bot cleans up old files automatically: on startup, 20 newest files of each type (`.txt`, `.jsonl`, `timings_*.csv`) remain in `bot_data/logs/`, and 50 newest screenshots in `bot_data/debug/`. If you want to keep logs after a problematic night, **copy them elsewhere before starting the bot next time**. The log saved via the "Save log" button to the default folder is cleared the same way: save it to another location, e.g. to Desktop.

> [!warning] Do not delete or rename `profile.yml` (your settings and Telegram) and the `bot_data` folder: it stores statistics, rules remembered by the bot, and battle history. You can only wipe `bot_data/debug` and old logs, and only when they are not needed.

### How to send log to author

When an issue cannot be resolved, the fastest way is to send the author what happened.

1. **Remember when it happened.** Time and approximate room count (`[СТАТИСТИКА] Комнат: N`) help find the right spot in a long log.
2. **Find the files.** The log is `bot_data/logs/bot_log_...` for that night, screenshots are from `bot_data/debug/` with similar time in the filename, and if the window froze — also `ui_freeze_...txt`.
3. **Click "Send log to author"** under the log on the main tab. The program will offer to save current log contents (as `gui_log_...txt`), then open your email client with a draft addressed to the author.
4. **Attach the files to the email yourself.** The program cannot attach files to an email: it only opens it. Attach `gui_log_...txt` or `bot_log_...txt`, screenshots, and (if present) `ui_freeze_...txt`.
5. **Describe in words:** what you did, what you expected, what you saw, when it happened. A single phrase "it doesn't work" hardly helps the author.

> [!warning] **Never attach** `profile.yml` and `bot_data/profile.yml.bak`: they contain your Telegram bot token. Screenshots of the "Telegram settings" window should also be sent only with the token masked (dots).

> [!note] Email client didn't open (no email app configured)? On the "About" page there is a "Write to author" button: if opening email failed, it copies the address to the clipboard so you can write from any email service.

### If nothing helps

Go from simple to complex, checking after each step if the bot revived:

1. **"Pause" → return game to corridor → "Continue".**
2. **"STOP" (F10) → "Start farming".** The bot will perform a smart start and figure out where it is on its own.
3. **Stop the bot and click "Restart scrcpy".** Then "Start farming" again.
4. **Close the program and open it again.** If the phone got stuck, unplug and reconnect the cable.
5. **Reboot computer and phone.** Sounds like a joke, but solves half of weird issues.

Session goals (time, rooms, floors, titanite) restart counting from scratch after launch, while stats, teams, and rules remain: they are stored in files.

> [!done] Now you know how the bot rescues itself, what to do when it pauses, and how to gather and send logs. Only the last section remains: about the program and how to support the project. [Next section →](#15)

## About and Support

The last page in the left menu is "About". It is about the program itself: what version you have, whether everything is in place, where to write to the author, and how to say "thank you". You don't need to configure anything on it, but it contains two useful buttons: "Check for updates" and "Bot folder".

### What is on the page

- :shield-check: **Program card** at the top. Name "Hero Wars: Knowledge Engine Bot", next to it — **version number** (for example, `v1.6.1`) and `Beta` label. "Beta" means "tested in action": the program works, but the author is still refining it, and errors are possible. Below the name is a short description. On the right are four buttons, more about them below.
- :user: **"Author and license"**: author's name, email, and license. Click on the email address to open a new email.
- :monitor: **"Component status"**: a check that the computer has everything needed for operation. Details below.
- :heart: **"Support the project"**: ways to thank the author. This is optional.

> [!tip] Tell the version to the author when writing about a problem: it immediately shows which exact program you are using. The version is in the top card, next to the name.

### Four buttons in the card

1. **"Check for updates".** Opens the project's releases page on GitHub in your browser (GitHub is the website where the author hosts the program; "release" is a ready version that can be downloaded). Compare the newest number there with yours. If newer — you can update, if the same — you have the latest version.
2. **"Bot folder".** Opens in Windows Explorer the folder from which the program was launched: the exact one where your settings and data are located. Useful when you need to copy files or find a log.
3. **"Write to author".** Opens an email addressed to the author in your email client. If there is no email client on your computer, the email won't open. Then the program will automatically put the address into the clipboard (temporary memory from which you paste with Ctrl+V) and report this at the bottom of the window: "Could not open it — copied to the clipboard". Paste the address into an email from any email provider.
4. **"Project GitHub".** Opens the main page of the project on GitHub: source code and description are located there.

> [!note] The program **does not access the Internet for updates on its own**: "Check for updates" only opens the page, and you decide. This is intended so that nothing changes without your knowledge.

### How to update the program

The update does not "install over" the existing version — you download the new version and transfer your data into it. This way, your teams and statistics won't be lost.

1. **Stop the bot and close the program.** The window close button (X), if the bot is running, will ask whether to stop it.
2. **Download the new version** on the releases page ("Check for updates" button) and unpack it into a new folder, not over the old one.
3. **Transfer your data.** Copy the `profile.yml` file and the entire `bot_data` folder from the old folder to the new one. Without them, the new program starts from scratch: empty settings and empty statistics.
4. **Launch the new program** and look at "About": the version number should be new, and all three components should be fine.
5. **Do not delete the old folder yet.** Work on the new version for a couple of days. If everything is fine, then remove it.

> [!warning] Do not copy files from `bot_data` one by one "what's needed", but transfer the whole folder: the rules learned by the bot itself, battle history, and statistics are interconnected, and they cannot be reassembled manually.

### "Component status"

The program itself checks that everything required for the bot to work is present. The check runs in the background every time you visit the page. While it is running, you will see "checking...".

- :smartphone: **ADB** — the service through which the computer taps on the phone. Must be "found".
- :monitor: **scrcpy** — the program that displays the phone screen in a window on the computer. Must be "found".
- :image: **Template database** — "sample images" of buttons and titans that the bot uses to recognize what is on its screen. Must be "loaded".

What to do if something is red:

- **ADB or scrcpy "not found".** This means the folder containing them is not added to `PATH` (the list of places where Windows looks for programs). How to do this is described in the ["Requirements and Installation"](#2) section. After editing `PATH`, close the program and open it again: an already running program does not see the new `PATH`.
- **Template database "not found".** Files are missing from the program folder. Most often, the archive was not fully unpacked, or the antivirus removed something. Unpack the archive again into a new folder and transfer `profile.yml` and `bot_data`, just like during an update.

### What is inside the bot folder and what cannot be deleted

Open it using the "Bot folder" button. There are many files there, but you only need a few. The rest is system data, and the program needs it to run.

- :file-text: `HeroWarsBot.exe` — the program itself. The bot also runs from it; it doesn't have a separate file. All other files and folders next to it (`guide`, `ui`, libraries, files with the `.dll` extension, and others) are part of the program. **Do not delete or rename any of them**, otherwise it will stop launching.
- :file-text: `profile.yml` — your settings: session target, thresholds, Telegram. **It contains your Telegram bot token, so do not send it to anyone.** Appears after clicking "Save settings" for the first time.
- :folder: `bot_data` — everything that the program and the bot recorded on their own. This is the **most valuable** thing you have. Inside:
  - `stats.json` — statistics ("Statistics" page);
  - `rules` folder — your teams and rules, including those learned by the bot;
  - `logs` folder — battle history and bot log (`bot_log_...txt`);
  - `debug` folder — screenshots for troubleshooting (SOS windows, freezes, failed rollbacks);
  - `titan_state.json` — health and energy of titans for the game day;
  - `profile.yml.bak` — settings backup. The "Restore / Reset" function in the Rule Wizard works from it. **It also contains the Telegram token**;
  - `ui_settings.json` — selected window language;
  - `sos_info.json`, `temp_sos.png`, `temp_test.png` — minor operational files for Telegram messages.
- :pause: `pause.flag` — "pause flag". Appears when the bot is on a soft pause. If it remained from last time, the program will automatically delete it on startup.

> [!warning] **Do not delete or rename** `profile.yml` and `bot_data`. If you delete `bot_data`, statistics, teams, rules, and everything the bot learned will disappear. If you really need to free up space, you can delete the contents of `bot_data/debug` and old logs in `bot_data/logs`. However, the bot itself keeps only the last 20 logs and the last 50 screenshots, so space is usually not an issue.

> [!tip] **Make a backup once a week.** Copy `profile.yml` and the `bot_data` folder to a flash drive or to the cloud. If your computer breaks or you reinstall Windows, you will download the program again, and restore teams and statistics from the backup. There is a Telegram token in the backup — keep it to yourself, not in a shared folder.

### Author and license

The program was written and is maintained by **Platon Petrunin**. Questions, bugs, and ideas — use the "Write to author" button or the address in the "Author and license" card.

The license is called **PolyForm Noncommercial 1.0.0**. In simple terms:

- :check: you can use it for yourself, for your game for free — as much as you want;
- :check: studying the code and modifying it for yourself is also allowed;
- :x: **no commercial use**: selling the program or its `.exe`, passing it off as your own under another name, or embedding it into paid services is forbidden. This requires written permission from the author.

> [!note] This is a brief summary, not a legal text. If your case is unusual (for example, you want to distribute the program to friends or a community), write to the author first. The full text of the license is located in the `LICENSE` file in the project on GitHub.

### How to support the project

The program is free, and the author creates it in their free time. If it saves you time and nerves, you can say "thank you" with money. This is **voluntary**: the bot works the same whether you paid or not, and there are no "paid features".

At the bottom of the "About" page there are three blocks:

1. **"Cryptocurrency".** Three wallets: `USDT · TRC20`, `Bitcoin · BTC` and `Ethereum · ETH`. The full address is visible in the field. You can copy it with the "Copy" button on the right ("Address copied" will appear at the bottom), by double-clicking on the field (selects everything), or by right-clicking — "Copy".
2. **"Donate via Telegram".** Three lines — rubles (`RUB`), euros (`EUR`), and dollars (`USD`). Each has two buttons: **"App"** opens the payment in the Telegram app, **"Browser"** — in the browser if Telegram is not installed. Choose the currency that is most convenient.
3. **"Direct transfers".** Buttons "Support on Boosty" and "YooMoney (RUB)": pages of these services open, then proceed as with a regular payment.

> [!warning] **Be careful with cryptocurrency.** Transfer only on the network specified next to the wallet: for `USDT` it is `TRC20`, not another. Money sent to the wrong network **cannot be refunded**. Take the address only from the program using the "Copy" button: on websites and in other people's messages, it might be spoofed. Send a small amount for the first time.

### Frequently Asked Questions

- **My version is old — is that bad?** No. The program does not stop working just because a new version was released. But new versions usually fix bugs, so check the releases page every few weeks.
- **"Bot folder" did not open.** The message "Could not open the folder" will appear. Open it yourself: File Explorer, the folder where you unpacked the program.
- **Why is there no "Update" button?** The program does not download anything on its own so as not to break your settings without asking. You update yourself, following the steps above.
- **If I don't support, will anything change?** Nothing. The bot works the same for everyone.

> [!done] This is the final section. Now you know everything to launch the bot, customize it for yourself, understand its decisions, and adjust it if something goes wrong. Have a great game! If you still have questions, the "Write to author" button is below.
