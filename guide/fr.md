# Hero Wars: Knowledge Engine Bot

Salut ! Voici un programme qui parcourt automatiquement le Donjon des titans pour toi dans le jeu Hero Wars. Tu l'allumes, tu vas à tes occupations — et il ouvre les portes, forme les équipes et récupère les récompenses.

Ce manuel est rédigé pour que n'importe qui puisse comprendre. Les mots inconnus sont expliqués immédiatement, et à la fin de chaque section, nous t'indiquons où aller ensuite.

## Ce que sait faire le bot

Le bot n'est pas un « clicker » stupide. Il regarde l'écran du jeu exactement comme tu le ferais, et décide lui-même de la suite des actions. Voici ce qu'il sait faire :

- :eye: **Il voit l'écran.** Toutes les fractions de seconde, il prend une capture d'écran de la fenêtre du jeu et y reconnaît les boutons, les portes et les ennemis.
- :door-open: **Il choisit la porte.** Il entre dans les salles dans l'ordre que tu as défini, et évite celles qui sont actuellement dangereuses.
- :users: **Il place l'équipe.** Pour chaque salle, il a un « pack » (c'est ainsi que nous appelons une équipe de cinq titans). Le bot place lui-même les titans à leurs postes.
- :heart-pulse: **Il surveille la santé.** Après chaque combat, il lit les PV (points de vie) et l'énergie des titans, puis décide si le pack est prêt pour le combat suivant.
- :swords: **Il t'appelle si le combat s'est mal passé.** La fenêtre «Intervention requise» apparaît : tu peux rejouer le combat avec un autre pack, l'accepter ou le faire à la main. Si tu t'es éloigné de l'ordinateur, le bot peut décider lui-même.
- :chart-no-axes-column: **Il apprend de ses combats.** Il mémorise quel pack a vaincu quels ennemis, et la fois suivante, il le place immédiatement.
- :send: **Il écrit sur Telegram.** Si tu le souhaites, il t'enverra le bilan de session et une alerte si quelque chose s'est mal passé.

> [!note] Exemple. Araji est entré en combat avec 36 % de santé et est tombé à 8 % après le combat. Le bot le voit, comprend que le combat s'est mal passé, et soit te demande quoi faire, soit annule lui-même le combat et le rejoue avec un autre pack.

### Ce que le bot ne fait pas

- Il parcourt **uniquement le Donjon des titans**. Les autres modes de jeu lui sont inconnus.
- Il **ne joue pas « dans le cloud »**. Le jeu tourne sur ton téléphone Android, et le PC Windows regarde l'écran du téléphone et clique dessus via un câble USB. Un téléphone ET un ordinateur sont nécessaires.
- Ce n'est pas un magicien : s'il n'y a pas de connexion avec le jeu, il attend honnêtement qu'elle revienne et t'en informe.

### Est-ce sûr pour le compte ?

Le bot s'efforce de se comporter comme une vraie personne, pas comme un robot :

- chaque clic atterrit à un **point aléatoire** du bouton, et non au même endroit ;
- avant de cliquer, il respecte une **pause de réaction** — de 0,3 à 0,8 seconde après l'apparition du bouton ;
- il ne clique **pas plus de deux fois par seconde**.

> [!warning] Aucun programme ne peut donner de garantie absolue : les règles du jeu sont fixées par son éditeur. Le bot ne fait rien d'« inhumainement rapide », mais la décision de l'utiliser ou non t'appartient.

### La suite dans le manuel

- **Что понадобится и установка** — ce qu'il faut acheter et installer une fois pour toutes.
- **Подключаем телефон** — le premier lancement du farm.
- **Главная и мини-бар** — comment lire la fenêtre et le petit panneau sous le jeu.
- **Пауза и остановка** — les boutons et les raccourcis clavier.
- **Мастер правил** — comment apprendre au bot tes packs et l'ordre des portes.
- **Когда бой прошёл плохо** — les fenêtres d'intervention et la prise de décision autonome du bot.
- **Telegram, статистика, если что-то пошло не так** — tout le reste.

> [!done] Tu sais maintenant ce que sait faire le bot. Ensuite — ce qu'il faut installer, une seule fois. [Section suivante →](#2)

## Что понадобится и установка

Cela se fait **une seule fois**. Ensuite, tu lances simplement le programme en double-cliquant. Consacre une quinzaine de minutes à tout cela — la suite sera facile.

### Ce qu'il faut avoir

- :monitor: **Un ordinateur sous Windows.** C'est là que tournent le programme et le bot.
- :smartphone: **Un téléphone sous Android avec Hero Wars.** Le jeu tourne sur le téléphone, et l'ordinateur regarde son écran et clique dessus.
- :terminal: **Un câble USB.** De préférence celui qui sert à charger le téléphone et à transférer des fichiers : il existe des câbles « de charge uniquement », à travers lesquels l'ordinateur ne verra pas le téléphone.
- :folder: **L'archive du programme** (fichier `.zip` contenant `HeroWarsBot.exe`).

> [!note] Le jeu reste sur le téléphone. Le bot n'y installe rien de superflu et ne touche pas aux fichiers du jeu : il regarde seulement l'écran et clique dessus comme tu le ferais avec ton doigt.

### Étape A. Décompresse le programme

1. **Décompresse l'archive** — fais un clic droit dessus et choisis « Extraire tout... ». Choisis un dossier simple sans lettres cyrilliques, par exemple `C:\HeroWarsBot`.
2. **Vérifie que les fichiers sont en place** — le dossier doit contenir `HeroWarsBot.exe` à côté d'autres fichiers et dossiers.

> [!warning] Décompresse d'abord l'archive, et ensuite seulement lance le programme. Si tu ouvres le `.exe` directement depuis l'archive, les autres fichiers du programme ne seront pas accessibles et il ne fonctionnera pas correctement.

> [!tip] Ce dossier est la « maison » du bot. À côté de `HeroWarsBot.exe`, il créera lui-même ses fichiers : paramètres, statistiques, historique des combats. Ne déplace donc pas le `.exe` séparément des autres fichiers, et si tu déménages, déplace le dossier entier.

### Étape B. Installe scrcpy

scrcpy est un petit programme qui affiche l'écran du téléphone dans une fenêtre sur l'ordinateur. Le bot « regarde » précisément cette fenêtre. **adb** est installé avec lui — l'assistant par lequel le bot clique sur l'écran du téléphone.

1. **Télécharge scrcpy** — sur la [page du projet](https://github.com/Genymobile/scrcpy/releases), choisis la dernière version pour Windows (archive `.zip` avec « win64 » dans le nom).
2. **Décompresse l'archive** — le plus pratique est dans un dossier simple sans espaces ni lettres cyrilliques, par exemple `C:\scrcpy`. À l'intérieur doivent se trouver les fichiers `scrcpy.exe` et `adb.exe`.
3. **Ajoute le dossier au PATH** — ainsi Windows saura où chercher ces programmes. Pour savoir comment faire, regarde ci-dessous.

**Comment ajouter un dossier au PATH :**

1. **Ouvre les paramètres** — appuie sur la touche Windows, tape « variables d'environnement » et choisis « Modifier les variables d'environnement système ».
2. **Trouve « Path »** — dans la fenêtre qui s'ouvre, clique sur « Variables d'environnement », dans la liste du haut choisis la ligne `Path` et clique sur « Modifier ».
3. **Ajoute le dossier** — clique sur « Nouveau », tape `C:\scrcpy` (ton dossier, s'il est différent) et ferme toutes les fenêtres avec le bouton « OK ».

> [!note] Le PATH est une liste de dossiers dans lesquels Windows cherche les programmes lorsque tu les appelles par leur nom. Tu ajoutes le dossier à la liste — et `scrcpy` ainsi que `adb` deviennent trouvables de n'importe où.

### Étape C. Vérifie que scrcpy est bien installé

1. **Ouvre l'« Invite de commandes »** — touche Windows, tape `cmd`, appuie sur Entrée. Si la fenêtre était déjà ouverte avant l'installation, ferme-la et rouvre-la : l'ancienne ne connaît pas les nouveaux dossiers.
2. **Vérifie scrcpy** — tape `scrcpy --version` et appuie sur Entrée. La version du programme doit apparaître.

Si au lieu de la version Windows écrit « n'est pas reconnu comme une commande interne ou externe », cela signifie que le dossier n'est pas tombé dans le PATH. Reviens à l'étape B et vérifie que le dossier où se trouve `scrcpy.exe` est bien inscrit dans le PATH.

### Étape D. Configure le téléphone

Le téléphone doit autoriser l'ordinateur à le contrôler. Cela s'appelle le « débogage USB » (un mode conçu pour les développeurs d'applications). Le bot l'utilise pour cliquer sur l'écran.

1. **Active le mode développeur** — va dans « Paramètres » → « À propos du téléphone » et appuie **7 fois d'affilée** sur « Numéro de build ». Le téléphone t'indiquera que tu es devenu développeur.
2. **Trouve « Options pour les développeurs »** — cette option apparaîtra dans les paramètres (parfois à l'intérieur de « Système » ou « Paramètres avancés »).
3. **Active deux paramètres** — « Débogage USB » **et** « Débogage USB (Paramètres de sécurité) ».
4. **Branche le câble** — lorsque le téléphone demande « Autoriser le débogage USB à partir de cet ordinateur ? », coche « Toujours autoriser » et appuie sur « OK ».

![Section « Options pour les développeurs » avec deux paramètres de débogage activés](images/usb_debug.png)

> [!warning] Active les **deux** paramètres. Si seul le premier est activé, l'image du téléphone arrivera sur l'ordinateur, mais les clics n'atteindront pas le jeu : le bot « tapotera », mais le jeu ne remarquera rien.

Vérifions maintenant la connexion. Connecte le téléphone avec le câble, ouvre l'« Invite de commandes » et tape `adb devices`. La liste doit contenir une ligne avec le mot `device` à côté du numéro du téléphone.

- :check: `device` — tout va bien, le téléphone est prêt.
- :triangle-alert: `unauthorized` — le téléphone attend ton autorisation. Regarde son écran et appuie sur « Autoriser ».
- :triangle-alert: liste vide — l'ordinateur ne voit pas le téléphone. Essaie un autre câble ou un autre port USB.

### Étape E. Premier lancement du programme

1. **Ouvre le dossier du programme** — celui où tu as décompressé l'archive.
2. **Double-clique sur `HeroWarsBot.exe`** — la fenêtre du programme s'ouvrira.
3. **Regarde autour de toi** — à gauche une bande avec les sections, au milieu la page principale. Tant que le téléphone n'est pas connecté, l'en-tête indique «En attente du téléphone» — c'est normal.

> [!tip] Lance toujours le programme depuis son dossier (ou crée un raccourci vers `HeroWarsBot.exe` : clic droit → « Envoyer vers » → « Bureau »). Il trouvera alors ses paramètres et ses fichiers.

> [!done] Tout est prêt : le programme est décompressé, scrcpy et le téléphone sont configurés. Maintenant, connectons le téléphone et lançons le premier farm. [Section suivante →](#3)

## Подключаем телефон и первый фарм

Nous allons maintenant connecter le téléphone et lancer le bot pour la première fois — le tout prendra environ cinq minutes. Retiens d'abord : il y aura **deux fenêtres** sur l'écran.

- :monitor: **La fenêtre du programme** — celle où tu lis ce manuel. Elle contient les boutons, les paramètres et le journal (c'est ainsi qu'on appelle le fil de messages où le bot enregistre ce qu'il fait).
- :smartphone: **La fenêtre du jeu** — le « miroir » de l'écran du téléphone sur le moniteur, elle s'appelle `HeroWarsBot_Arena`. C'est précisément dans celle-ci que le bot « regarde ».

### Ce qu'il y a sur la page d'accueil au premier lancement

Tant que tu n'as pas encore enregistré les paramètres, la page d'accueil (premier bouton de la bande de gauche) contient la carte «Pour commencer» avec la mention «3 étapes · environ 5 minutes».

![Premier lancement : carte «Pour commencer», mention rouge «En attente du téléphone…» et bouton bleu «Connecter le téléphone»](images/connect_phone.png)

- :smartphone: **«Connecte le téléphone»** — marqué du mot «maintenant». Une fois le téléphone connecté, le numéro de l'étape sera remplacé par une coche verte. C'est ce dont nous allons nous occuper maintenant.
- :sliders-vertical: **«Vérifie les packs par salle»** — le lien «Ouvrir →» mène au «Maître des règles» (deuxième bouton de la bande de gauche, icône avec des curseurs). C'est là que tu indiques au bot quels titans utiliser pour entrer dans chaque salle.
- :send: **«Configure Telegram pour le SOS»** — optionnel. Le bot t'écrira sur Telegram s'il a besoin d'aide.

> [!warning] Les packs sont la chose la plus importante avant le premier farm. Le bot place dans chacune des quatre salles (eau, terre, feu et mixte) le pack inscrit dans le «Maître des règles», et il ne peut pas deviner tes titans. Comment configurer cela — dans la section dédiée au «Maître des règles» plus loin dans le manuel. La carte «Pour commencer» disparaîtra dès que tu enregistreras les paramètres dans le «Maître des règles» pour la première fois.

### Étape A. Connecte le téléphone

1. **Prépare le téléphone** — branche-le avec le câble et déverrouille l'écran. Les deux paramètres de débogage USB doivent être activés, comme indiqué dans la [section 2](#2).
2. **Clique sur «Connecter le téléphone»** — c'est le grand bouton bleu en haut à droite. Pendant que le programme cherche le téléphone, il affiche «Connexion...». L'attente peut durer jusqu'à 20 secondes.
3. **Trouve la fenêtre du jeu** — une nouvelle fenêtre `HeroWarsBot_Arena` apparaîtra avec l'écran du téléphone. Tu ne la vois pas ? Elle s'est peut-être cachée derrière la fenêtre du programme : cherche-la dans la barre des tâches en bas de l'écran.
4. **Vérifie le bandeau dans l'en-tête** — la mention rouge «En attente du téléphone…» doit devenir verte : «connecté». Et le bouton bleu se transformera en bouton vert «Lancer le farm». (L'en-tête est la bande supérieure de la fenêtre, le bandeau est le rectangle contenant l'inscription.)

![Téléphone connecté : inscription verte «connecté», bouton «Lancer le farm» et fenêtre du jeu à côté](images/phone_connected.png)

La fenêtre n'est pas apparue, et le journal indique «Окно scrcpy не появилось или утилита не найдена!» ? Vérifie dans l'ordre :

- :smartphone: L'écran du téléphone est déverrouillé, le câble est bien inséré. Essaie un autre port USB.
- :terminal: Dans l'invite de commandes, `adb devices` affiche le mot `device` à côté de ton téléphone. S'il y a `unauthorized` — autorise le débogage sur l'écran du téléphone.
- :terminal: Dans l'invite de commandes, `scrcpy --version` répond par la version. Pas de réponse ? Le dossier scrcpy n'est pas tombé dans le PATH — reviens à la [section 2](#2). Après modification du PATH, il faut fermer et rouvrir le programme.

### Étape B. Place-toi dans le couloir du Donjon

Le Donjon des titans est un mode de jeu où tu descends les étages et affrontes des ennemis dans chaque salle. Le **couloir** est l'écran entre les combats : on y voit la porte avec un drapeau, et rien d'autre n'est ouvert. C'est depuis le couloir que le bot commence.

1. **Ouvre le jeu** — sur le téléphone, lance Hero Wars et va dans le Donjon des titans.
2. **Place-toi dans le couloir** — si un combat est en cours, termine-le toi-même et ferme la fenêtre de résultat. Il faut un écran calme avec la porte et le drapeau.

![Couloir du Donjon des titans : le drapeau est visible près de la porte](images/dungeon_corridor.png)

> [!warning] Ne lance pas le farm au milieu d'un combat. Le bot inspecte d'abord l'écran et met de l'ordre : s'il voit un combat, il bat en retraite ; s'il voit une fenêtre de résultat avec le bouton «Rejouer», il annule ce combat et rejoue la salle ; s'il voit la sélection d'équipe, il mène le combat puis l'annule immédiatement. Il fonctionnera ensuite, mais ta victoire sera perdue pour rien.

### Étape C. Commence le farm

> [!warning] **La langue du programme doit correspondre à la langue du jeu.** Les boutons avec du texte («Attaquer», «OK», «Rejouer») et le drapeau près de la porte sont reconnus par le bot grâce aux images dans la langue choisie dans le programme. C'est le bouton avec deux lettres («RU») en bas de la bande de gauche. Si le jeu est en russe, le programme doit être sur «RU». Si les langues diffèrent, le bot ne trouvera tout simplement pas les boutons.

1. **Clique sur «Lancer le farm»** — le bouton vert à la place de «Connecter le téléphone». Le programme ajustera lui-même la fenêtre du jeu à la bonne taille et la placera dans le coin supérieur gauche de l'écran.
2. **Ne te panique pas si la fenêtre du programme disparaît** — elle s'est réduite dans la barre des tâches, et une bande étroite est apparue sous le jeu — la **mini-barre**. On y voit ce que fait le bot. Pour restaurer la fenêtre : l'icône «Ouvrir la fenêtre du programme» sur la mini-barre (survole avec la souris — une info-bulle apparaîtra) ou le bouton dans la barre des tâches.
3. **Observe le jeu** — après quelques secondes, le bot cliquera sur la porte et la première salle commencera. Une salle prend environ une demi-minute à une minute.
4. **Rappelle-toi comment arrêter le bot** — la touche F10 l'arrête immédiatement, F9 le met en pause (le bot finira la salle et attendra). Les touches fonctionnent lorsque la fenêtre du jeu ou du programme est active.

En agrandissant la fenêtre du programme, jette un œil au journal. Chaque ligne est précédée de l'heure — nous l'avons omise. Voici ce qui devrait apparaître :

- `[УМНЫЙ СТАРТ] Сканирую экран для восстановления контекста...` — le bot inspecte les lieux.
- `[УМНЫЙ СТАРТ] Контекст не требует экстренных действий. Начинаю с HALLWAY.` — tout est en ordre, il commence par le couloir («HALLWAY» veut dire «couloir» en anglais).
- `[СТАТИСТИКА] Комнат: 1` — la première salle est franchie. Tout fonctionne !
- :triangle-alert: `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` — le bot attend que la fenêtre du jeu redevienne principale. Clique dessus avec la souris pour reprendre l'activité.

Une minute a passé et le bot ne clique sur rien ? Vérifie :

- :gamepad-2: Dans le jeu, c'est actuellement le couloir du Donjon des titans, pas un menu, un magasin ou un combat.
- :globe: La langue du programme correspond à la langue du jeu (avertissement ci-dessus).
- :maximize-2: La fenêtre du jeu est entièrement à l'écran : ni étirée, ni agrandie, ni dépassée du bord. Sinon arrête le bot (F10), clique sur «Réinitialiser la taille de la fenêtre du jeu» et recommence.
- :terminal: Le journal ne contient aucune ligne avec «[ОШИБКА]». S'il y en a, nous les analyserons dans la section «En cas de problème».

### Pendant que le bot travaille

- :monitor: La fenêtre du jeu doit rester visible : ne la recouvre pas avec d'autres fenêtres et ne la réduis pas. Si tu cliques sur une autre fenêtre, le bot s'arrêtera et attendra.
- :smartphone: Ne ferme pas la fenêtre du jeu et ne tire pas sur le câble. Si la fenêtre disparaît, le programme arrêtera lui-même le bot («La fenêtre scrcpy est fermée — arrêt du bot»).
- :maximize-2: Ne redimensionne pas et n'agrandis pas la fenêtre du jeu : le bot la mesure au lancement et utilise cette mesure par la suite.
- :gamepad-2: Ne clique pas toi-même sur l'écran du téléphone : le bot clique via ADB, et vous allez vous gêner mutuellement. Si tu veux jouer à la main, mets le bot en pause (F9) et attends qu'il s'arrête dans le couloir.
- :triangle-alert: Ne verrouille pas l'ordinateur (Win+L) : sur un PC verrouillé, le bot ne voit pas l'écran et attend ton retour.
- :moon: Pour le farm nocturne, désactive la veille de l'ordinateur : dans les «Paramètres» de Windows, ouvre «Système» → «Alimentation» et choisis «Jamais» pour l'écran et la veille. Un moniteur en veille ou éteint équivaut à un PC verrouillé : le bot s'arrêtera et attendra. Le nom des options dépend de la version de Windows.

### Boutons dans l'en-tête

En haut à droite, à côté du bandeau, se trouvent trois icônes. Survole n'importe laquelle avec la souris — une explication apparaîtra.

![En-tête de la fenêtre : bandeau du téléphone, trois boutons et boutons de la fenêtre](images/header_buttons.png)

- :moon: **«Éteindre l'écran du téléphone»** — éteint l'écran du téléphone, mais le jeu continue d'exécuter et le bot voit tout. Pratique la nuit : moins de charge sur l'écran et la batterie. Le programme amène la fenêtre du jeu au premier plan et appuie sur Alt+O (c'est ainsi que scrcpy éteint l'écran). Pour rallumer l'écran — bouton d'alimentation du téléphone. Un bouton identique se trouve sur la mini-barre.
- :refresh-cw: **«Redémarrer scrcpy»** — ferme la fenêtre du jeu et la rouvre. Utile si l'image du téléphone est gelée. Ne fonctionne qu'avec la fenêtre lancée par le programme lui-même. Ne clique pas dessus pendant que le bot travaille : le programme considérera la fenêtre disparue comme une rupture de connexion et arrêtera le bot.
- :maximize-2: **«Réinitialiser la taille de la fenêtre du jeu»** — ramène la fenêtre `HeroWarsBot_Arena` à la taille 1606 × 748 et la place dans le coin supérieur gauche. C'est la taille de référence : la recherche de boutons est configurée pour elle. Si tu as étiré ou agrandi la fenêtre — clique sur ce bouton avant «Lancer le farm» (bien que «Lancer le farm» le fasse de lui-même). La fenêtre est large : sur un moniteur Full HD (1920 × 1080), elle rentre entièrement, et le bot ne voit que ce qui est à l'écran.

### Fenêtre du programme sans cadre Windows

La fenêtre du programme n'a pas le cadre habituel de Windows, elle a donc ses propres boutons en haut à droite derrière une fine ligne :

- :minus: **«Réduire»** — masque la fenêtre dans la barre des tâches.
- :square: **«Agrandir»** — fenêtre en plein écran ; le bouton s'appelle ensuite «Restaurer la taille». Un double-clic sur l'en-tête fait la même chose.
- :x: **«Fermer»** — ferme le programme, et avec lui la fenêtre du jeu si elle a été ouverte par celui-ci. Si le bot travaille, il demandera d'abord «Arrêter le bot ?» ; le bouton «Arrêter et fermer» l'arrêtera immédiatement et le bilan de session ne sera pas envoyé sur Telegram.
- :grip-vertical: **Déplacer la fenêtre** — par l'en-tête : par l'espace vide en haut ou par le titre.
- **Changer la taille** — par le coin inférieur droit (trois petites barres obliques). La fenêtre ne deviendra pas toute petite.

> [!note] Ne confonds pas «Réduire» et «Réduire en mini-barre». «Réduire» masque simplement la fenêtre dans la barre des tâches. «Réduire en mini-barre» est un bouton sur la page d'accueil pendant que le bot travaille : il affiche également la mini-barre sous le jeu.

> [!done] Le téléphone est connecté, le bot a réussi la première salle — la base est prête. Ensuite, nous verrons ce qu'affiche la page d'accueil et comment lire le journal. [Section suivante →](#4)

## Главная страница и журнал

L'accueil est le premier bouton de la bande de gauche, et c'est celui que tu vois le plus souvent. Elle ressemble au tableau de bord d'une voiture : en haut — les chiffres (« où on va » et « comment on va »), en bas — le journal, où le bot écrit lui-même ce qu'il fait. Voyons ce qui se trouve où et comment ne pas se perdre dans les lignes du journal.

### Carte du haut : elle change d'aspect toute seule

Dans la partie supérieure de l'accueil se trouve une grande carte, mais elle affiche différentes choses selon l'état actuel du bot :

- :sliders-vertical: **«Paramètres de lancement»** — le bot est à l'arrêt, mais les paramètres sont déjà enregistrés. C'est « ce avec quoi le bot ira au combat » : objectif, mode et seuils.
- :activity: **«Session en cours»** — le bot travaille. Des chiffres en direct : combien récolté, combien franchi, combien de temps écoulé.
- :file-text: **«Bilan de session»** — le bot s'est arrêté. La carte montre ce qui a été obtenu et pourquoi il s'est arrêté.
- :list: **«Pour commencer»** — uniquement tant que tu n'as pas encore enregistré de paramètres (elle est décrite dans la [section 3](#3)).

Une session est un seul lancement du bot : de «Lancer le farm» jusqu'à l'arrêt.

### Paramètres de lancement

Quatre bandeaux, et chacun répond à une question. Les chiffres proviennent de tes paramètres, donc si quelque chose ne te plaît pas, clique sur «Modifier dans l'assistant de règles →» en haut à droite de la carte : le «Maître des règles» s'ouvrira.

![Accueil avant lancement : carte «Paramètres de lancement» et journal vide](images/main_config.png)

- :target: **«Objectif de session»** — quand le bot doit s'arrêter. L'objectif est **unique** : titanite, salles, étages ou temps. Si plusieurs sont définis dans les paramètres, le premier par ordre « titanite → salles → étages → temps » est pris en compte. Si tu n'as rien changé — l'objectif est de 120 titanites, soit 10–20 salles. «Sans limite» signifie que tous les objectifs sont à zéro et que le bot continuera jusqu'à ce que tu l'arrêtes.
- :shield-check: **«Mode»** — le bandeau «Le bot décide seul» avec la mention «ON» ou «OFF». Activé : lors d'un mauvais combat, le bot rejouera lui-même le combat avec un autre pack. Désactivé : il t'appellera. Détails dans les sections consacrées au «Maître des règles».
- :heart-pulse: **«Seuil de panique PV»** — par exemple 40 %. Si après un combat la santé d'un des titans tombe en dessous, le combat est considéré comme mauvais. Un pack est une équipe de cinq titans ; PV signifie santé.
- :calendar: **«Réinitialisation du jour»** — par exemple 05:00. À partir de cette heure, une nouvelle journée commence dans le jeu : le bot calcule les statistiques de la journée et oublie la santé qu me avaient les titans hier.

> [!note] Le bot lit les paramètres **une seule fois, quand tu cliques sur «Lancer le farm»**. Si tu modifies quelque chose pendant le travail — le bot ne l'apprendra qu'au lancement suivant. C'est pourquoi, tant que le bot travaille, la carte affiche exactement les paramètres avec lesquels il a démarré.

### Session en cours

Lorsque le bot est lancé, la carte se transforme en «Session en cours». En haut à droite, l'état s'allume :

- :activity: **«Farm en cours»** — tout va bien, le bot travaille.
- :pause: **«Pause»** — tu as appuyé sur «Pause» (ou le bot est passé de lui-même en pause douce). Le bouton est alors devenu «Continuer».
- :triangle-alert: **«Attend ta décision»** — la fenêtre «Intervention requise» est à l'écran, le bot attend une réponse.
- :refresh-cw: **«Lancement du bot…»** — les premières secondes après «Lancer le farm».

![Farm en cours : bandeaux de session avec jauges de progression vers l'objectif](images/main_session.png)

Il y a quatre bandeaux :

1. **«Titanite de la session»** — combien de titanite le bot a collecté. C'est un **décompte, pas une lecture à l'écran** : 6 par salle et 12 si l'icône « x2 » brille dans le jeu. Si l'objectif est la titanite, « récolté / requis », les pourcentages et la jauge apparaîtront à côté.
2. **«Étages franchis»** — un étage est comptabilisé lorsque le bot a récupéré la récompense au point de sauvegarde (c'est ainsi qu'on appelle l'endroit à la fin de l'étage où l'on appuie sur « Activer » et « Récupérer »). À côté est inscrit la dernière porte dans laquelle il est entré : eau, terre, feu ou mixte.
3. **«Combats de la session»** — par exemple « {wins} victoires sur {total} ». Une victoire est une salle validée. Un annulation/rollback est un combat que le bot a rejoué : il est également compté comme combat, c'est pourquoi le « total » est parfois supérieur aux « victoires ».
4. **«Durée de session»** — heures:minutes:secondes et en petit «salle en moyenne 28 s». La moyenne est calculée par salle, sans compter l'arrêt au point de sauvegarde.

> [!tip] Si l'objectif porte sur les salles ou la durée, les pourcentages apparaissent à droite sous la forme « 35 % sur 100 » ou « 35 % sur 120 min » — l'objectif ne rentre pas dans le chiffre lui-même. La jauge sous le bandeau reste la même.

> [!note] Lorsque l'objectif est atteint, le bot n'abandonne pas l'étage au milieu. Il écrira dans le journal `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.`, franchira les salles restantes et s'arrêtera devant le point de sauvegarde sans appuyer sur « Activer » : la récompense de l'étage sera récupérée en premier lieu au lancement suivant. Exception — l'objectif par étages : le bot s'arrête alors immédiatement après la récompense.

### Bilan de session

Le bot s'est arrêté — la carte affiche le bilan, et la fenêtre s'agrandit automatiquement depuis la mini-barre. En haut est inscrite la raison de l'arrêt : bouton «STOP», fenêtre scrcpy fermée, fin normale du travail ou ce que le bot a écrit lui-même (par exemple que l'objectif est atteint).

![Bilan de session : raison de l'arrêt, chiffres et bouton «Détails»](images/main_summary.png)

Les mêmes quatre bandeaux que dans la session, mais ce sont maintenant les chiffres définitifs ; dans «Combats», la mention «fenêtres SOS : N» est ajoutée (combien de fois le bot t'a appelé). Le bouton **«Détails»** ouvre une fenêtre contenant tout le rapport du bot : durées moyennes par étapes, salles les plus longues, combien il y a eu de rejoués et combien d'entre eux le bot a faits **sans toi**. L'icône ✕ à droite masque le bilan, et les «Paramètres de lancement» réapparaissent à la place. Si tu cliques sur «Lancer le farm», le bilan disparaîtra de lui-même.

> [!note] Si Telegram est configuré, le bilan y sera envoyé automatiquement lors de n'importe quel arrêt normal. Le bouton «STOP» (F10) tue le bot instantanément, c'est pourquoi le bilan n'est pas envoyé sur Telegram dans ce cas.

### Journal : ce qu'il contient et comment le lire

La partie inférieure de l'accueil est le **«Journal d'activité»**. Le bot y inscrit chacune de ses actions, et le programme l'affiche dans la fenêtre. Ne t'effraie pas du nombre de lignes : il n'est pas nécessaire de tout lire, le journal sert quand quelque chose s'est mal passé, ou par curiosité.

Chaque ligne est structurée de la même manière :

`10:26:17.486 [НАВИГАЦИЯ] Двери (слева направо): EARTH (0.98), FIRE (0.97)`

1. **Heure** — en gris. Heures:minutes:secondes et millisecondes.
2. **Étiquette entre crochets** — « qui parle » et à quel sujet. Elle est colorée : la couleur indique à quelle section du journal la ligne appartient.
3. **Texte** — ce qui s'est passé exactement. Une ligne longue s'étale sur la ligne suivante, et la suite se place sous le texte, pas sous l'heure.

Une ligne sans étiquette (par exemple ` ---> HYPERION: ХП 100%, Энергия 79%`) est la suite de la ligne située au-dessus d'elle et appartient à la même section.

### « Pastilles »-filtres

Au-dessus du journal se trouvent cinq boutons-« pastilles ». Clique sur l'un d'eux — et seules les lignes de cette section resteront dans le journal. Le choix est mémorisé : si tu ouvres le programme demain, la même pastille sera sélectionnée.

![Journal avec les pastilles «Tout», «Combats», «Règles», «Système» et «Erreurs»](images/journal_pills.png)

- **«Tout»** — tout à la suite.
- **«Combats»** (étiquettes vertes) — le déroulement : salles, temps, santé des titans, annulations/rejoués. Étiquettes `[КОМБАТ]`, `[СТАТИСТИКА]`, `[ВРЕМЯ]`, `[СОСТОЯНИЕ]`, `[АНАЛИЗАТОР]`, `[ОТКАТ]`, `[ЛИМИТ]`, `[ИТОГ]`.
- **«Règles»** (étiquettes jaunes) — les décisions du bot : quel pack placer, pourquoi le combat a été rejoué, ce qu'il a mémorisé. Étiquettes `[ТАКТИКА]`, `[КОМАНДА]`, `[ПРАВИЛА]`, `[ОБУЧЕНИЕ]`, `[SOS_CLOSE]`.
- **«Système»** (étiquettes bleues) — tout le reste : couloir et portes (`[НАВИГАЦИЯ]`), lancement (`[УМНЫЙ СТАРТ]`), connexion. Les lignes du programme lui-même avec l'étiquette `[GUI]` sont grises, mais se trouvent également ici.
- **«Erreurs»** (étiquettes rouges) — tout ce qui requiert de l'attention : `[ОШИБКА]`, `[ВНИМАНИЕ]`, `[СТОРОЖ]`, `[SOS]`. Un chiffre figure à côté du nom — le nombre de ces lignes accumulées.

> [!warning] Un chiffre rouge sur «Erreurs» n'est pas toujours une panne. On y trouve aussi `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` — le bot attend simplement que tu ramènes la fenêtre du jeu au premier plan. Lis le texte de la ligne et ne te laisse pas effrayer par la couleur.

### Exemples de vraies lignes

Ce sont des lignes issues d'une session réelle du bot (l'heure est omise par souci de concision). Apprends à lire ces cinq-là — et tu comprendras n'importe quel journal.

- `[НАВИГАЦИЯ] Выбрана комната EARTH (порядок: water → mix → earth → fire)` — le bot a choisi la porte de terre. Entre parenthèses — ton ordre des portes. Le chiffre dans la ligne «Двери (слева направо)» ci-dessus indique le niveau de certitude du bot d'avoir reconnu la porte (1 — absolu).
- `[ВРЕМЯ] Комната 2 (earth): коридор 12.8 с | сборка 3.3 с | бой 8.0 с | результат 9.1 с | всего 33.2 с` — rapport sur la salle : temps consacré au trajet vers la porte, à la composition de l'équipe, au combat et à la fermeture de la fenêtre de résultat.
- `[СТАТИСТИКА] Комнат: 3 | Титанит: 36` — troisième salle franchie, 36 titanites collectées. Ce sont ces chiffres qui apparaissent sur les bandeaux de la session.
- `[ТАКТИКА] Откатываю бой сам и переиграю паком [...] (взят: ваш список запасных паков).` — le combat s'est mal passé et le bot (mode «Le bot décide seul») le rejoue avec un pack de réserve. Si le pack de réserve réussit : `[ТАКТИКА] Запасной пак [...] справился. Запоминаю его против этих врагов.`
- `[ОТКАТ] Запускаю протокол отката боя...` — début du rejoué/rollback : «Rejouer» → pause → «Battre en retraite». Chacune de ces lignes ajoute un combat sur le bandeau «Combats de la session».

> [!tip] Au début de chaque session, le bot écrit `[ТАКТИКА] Плохой бой: ХП ниже 30% | потеря больше 60% | ...` — les seuils selon lesquels il jugera les combats. Si quelque chose s'est passé « différemment de ce que tu attendais », vérifie d'abord cette ligne par rapport à tes paramètres.

### Boutons sous le journal

![Boutons sous le journal : «Enregistrer le journal», «Envoyer le journal à l'auteur», «Effacer»](images/journal_buttons.png)

- :save: **«Enregistrer le journal»** — enregistrera tout le journal dans un fichier texte. Le programme proposera lui-même le nom `gui_log_...txt` et le dossier `bot_data/logs` ; tu peux en choisir un autre.
- :mail: **«Envoyer le journal à l'auteur»** — d'abord la même sauvegarde, puis ta messagerie s'ouvrira avec un e-mail prêt. **Joins toi-même le fichier au message** (ainsi que `battle_log.csv` du même dossier) : le programme ne peut pas le faire. Pas de logiciel de messagerie ? Écris à l'auteur à l'adresse figurant dans la section «À propos».
- :x: **«Effacer»** — supprime les lignes de la fenêtre, mais demandera d'abord «Effacer le journal ?». C'est sans danger : le bot sauvegarde lui-même le journal complet dans le dossier `bot_data/logs`, et les chiffres de la session ne sont pas réinitialisés.

Tu peux sélectionner du texte dans le journal avec la souris et le copier avec Ctrl+C ou un clic droit («Copier»). Il est impossible de modifier le journal — il est en lecture seule. Si tu as fait défiler le journal vers le haut pour lire, il ne « s'échappera » pas vers le bas avec les nouvelles lignes ; défile jusqu'à la fin — et il défilera à nouveau avec le bot.

> [!note] La fenêtre garde en mémoire les 50 000 dernières lignes et affiche les 4 000 dernières — sinon elle ralentirait lors d'un long farm. Tout le reste se trouve dans le fichier `bot_data/logs/bot_log_...txt` : le bot le conserve lui-même, et il n'est généralement pas nécessaire d'enregistrer le journal à la main.

Tant que le journal est vide, l'inscription «Le journal est vide» figure à sa place. Les lignes apparaîtront après la connexion du téléphone. Une pastille vide affiche «Rien ici pour l'instant» et «Aucune ligne de ce type pour l'instant» — pour «Erreurs», c'est une bonne nouvelle.

> [!done] Tu lis maintenant la page d'accueil comme un tableau de bord : tu sais ce que signifient les bandeaux et les couleurs des étiquettes du journal. Ensuite — la mini-barre, le petit panneau sous le jeu. [Section suivante →](#5)

## Mini-barre sous le jeu

Tant que le bot fonctionne, tu n'as généralement pas besoin de la fenêtre principale du programme. Elle se réduit donc toute seule dans la barre des tâches, et une fine bande apparaît sous l'image du jeu — la **mini-barre**. C'est comme le tableau de bord d'une voiture : en un coup d'œil, tu vois si le bot avance, ce qu'il fait en ce moment, combien il a déjà parcouru et s'il t'appelle à l'aide.

![Mini-barre sous la fenêtre du jeu pendant le farm](images/mini_bar.png)

### Quand apparaît-elle et où se place-t-elle

- :monitor: **Elle apparaît toute seule.** Une fois le bot lancé (« Lancer le farm »), la fenêtre du programme se réduit et la mini-barre s'installe sous le jeu. Si tu as agrandi la fenêtre du programme et veux la masquer à nouveau pendant que le bot tourne, clique sur « Réduire en mini-barre » sur la page principale.
- :smartphone: **Elle reste collée sous le jeu** et fait exactement la même largeur que l'image du jeu. Si tu déplaces la fenêtre du jeu, la mini-barre la suit (le programme le vérifie deux fois par seconde).
- :eye: **Elle ne recouvre pas le jeu, pas même d'un pixel.** C'est important : le bot « regarde » l'écran en faisant des captures de la fenêtre. Si la barre se superposait au jeu, le bot la verrait à la place des boutons.
- :maximize-2: **Pas de place en bas** (la fenêtre du jeu touche le bas de l'écran) — la barre se placera au-dessus du titre de la fenêtre. S'il n'y a pas de place là non plus, elle ne s'affichera pas et la fenêtre du programme restera dans la barre des tâches. Si tu réduis la fenêtre du jeu, la barre se masquera et reviendra avec elle.

> [!tip] La mini-barre n'apparaît pas alors que le bot tourne ? Remonte la fenêtre du jeu : il faut environ 100 pixels d'espace libre en dessous. Tu peux déplacer la fenêtre, mais tu ne dois pas changer sa taille (nous avons vu cela dans la section 3).

### Ce qu'il y a sur la barre : cinq colonnes de gauche à droite

- :activity: **État.** Un mot et un point coloré qui « respire » tant que tout va bien : « DÉMARRAGE », « FARM EN COURS », « PAUSE », « PAUSE DE DÉBOGAGE » ou un « SOS » rouge. En dessous — **ce que fait le bot en ce moment même** et depuis combien de secondes : par exemple, « Combat · Feu · 12 s ». Puis « Salles : 12 · étages : 2 » et la durée de la session, par exemple « Temps 00:42:17 ».
- :target: **Objectif.** Le nom de l'objectif, ce qui a été fait, ce qu'il faut faire, et une barre de progression. En dessous — « ~28 s par salle » (temps moyen ; avant la première salle, il y aura « temps par salle — après la première ») et une estimation « objectif dans ≈ 1 h 10 min ». Le bot calcule cette estimation d'après la vitesse de **cette** session, c'est pourquoi elle varie au début avant de se stabiliser. S'il n'y a pas d'objectif (« Sans limite »), la barre n'apparaît pas, et à la place de l'estimation s me s'affiche « ≈ N titanite par heure ».
- :heart-pulse: **Santé de l'équipe.** Les carrés des titans ayant participé au dernier combat et leurs PV après celui-ci — dans l'ordre où ils apparaissent sur l'écran du jeu. Avant le premier combat, il est écrit « pas encore de combats ». La couleur du chiffre indique : rouge — PV sous le seuil de panique (général ou individuel), jaune — sous le seuil à partir duquel le bot soigne le titan, couleur normale — tout va bien. Un tiret « — » signifie que l'icône du titan n'a pas pu être trouvée sur la fenêtre de résultat.
- :list: **Événements.** Les quatre dernières lignes, la plus récente en haut et en plus grand. À gauche une étiquette colorée, à droite l'heure.
- :gamepad-2: **Boutons.** Quatre boutons disposés en carré 2×2.

### Ce que le bot peut « faire actuellement »

Dans la première colonne, le bot indique lui-même son étape. Voici ce que signifient ces mots :

- **« Couloir »**, **« Choix de la porte »**, **« Montage de l'équipe »**, **« Combat »**, **« Fenêtre de résultat »** — la boucle classique d'une salle. Pour les étapes « Montage de l'équipe », « Combat », « Fenêtre de résultat » et « Retraite », l'élément de la salle est ajouté : « Combat · Eau · 12 s ».
- **« Point de sauvegarde »** — l'étage est terminé, le bot récupère la récompense.
- **« Retraite »** — le combat a mal tourné, le bot bat en retraite et prépare un rejouer.
- **« Examine l'écran »** — après le lancement, le bot observe l'écran et décide par quoi commencer (c'est le « démarrage intelligent »).
- **« Pause dans le couloir »**, **« Attend ta décision »**, **« Tu joues toi-même »** — le bot est à l'arrêt parce que tu as appuyé sur pause, parce qu'il t'a posé une question ou parce que tu as choisi « Jouer à la main ».
- **« Attend la fenêtre du jeu »** et **« Attend la connexion »** — le bot attend : soit le jeu n'est pas au premier plan (voir ci-dessous), soit la connexion au serveur du jeu est perdue.

Si la même inscription reste affichée plus longtemps que d'habitude, le nombre de secondes à droite augmente et t'indiquera que le bot est en fait bloqué.

### Événements : étiquettes et leur signification

L'étiquette à gauche indique la nature de l'événement :

- **Nom de l'élément** (« Eau », « Terre », « Feu », « Mixte ») — la salle est terminée. Une ligne telle que « Salle 45 terminée · 28 s · PV les plus bas : Araji 36% » indique combien de secondes la salle a prises et quel titan a fini avec le moins de santé.
- **« Étage »** — l'étage est terminé (« Étage terminé, 3 au total »).
- **« Retraite »** — le combat est rejoué. **« SOS »** — la raison de l'appel en mots simples.
- **« Pause »** — « Pause : le bot finit le combat et attend », puis « Le bot attend dans le couloir ».
- **« Bot »** — « Bot démarré », « Pause levée, le bot continue », « Pas de réponse depuis 10 min — le bot a décidé seul ».
- **« Limite »** — la session a atteint son objectif, le bot finit de jouer jusqu'au point de sauvegarde.
- **« Attention »** — « La fenêtre du jeu n'est pas active — le bot attend. Clique sur le jeu ».
- **« Erreur »** — le texte de l'erreur tel qu'écrit par le bot.

Les lignes longues sont tronquées avec des points de suspension. Le texte complet est toujours disponible dans le journal de la page principale.

### Boutons

Survole avec la souris — une info-bulle apparaîtra. Tous les boutons font la même chose que leurs homologues de la page principale et de l'en-tête.

- :pause: **Pause / Continuer** — « Pause douce : le bot finit le combat et attend (F9) ». En pause, l'icône se transforme en triangle vert, et ce même bouton lève la pause. Tant que le bot est en cours de démarrage, le bouton est indisponible.
- :square-filled: **STOP** — « Arrêt d'urgence : le bot s'arrête aussitôt, pas de bilan sur Telegram (F10) ».
- :moon: **Écran du téléphone** — « Éteindre l'écran du téléphone », le jeu continuant de tourner.
- :maximize-2: **Agrandir** — « Ouvrir la fenêtre du programme ». La mini-barre disparaîtra. Tu obtiendras le même résultat en cliquant sur le bouton du programme dans la barre des tâches. Si tu veux réafficher la barre, clique sur le bouton « Réduire en mini-barre » sur la page principale.

> [!note] Lorsque le bot t'appelle, la mini-barre devient rouge et la fenêtre « Intervention requise » apparaît d'elle-même au centre de l'image du jeu — tu n'as pas besoin d'agrandir la fenêtre du programme. Le premier bouton ne met alors pas en pause et ne fait pas « continuer » : il affiche la fenêtre SOS si elle se trouve sous d'autres fenêtres (info-bulle — « Afficher la fenêtre SOS : le bot attend ta décision »). Une fois que tu as répondu dans la fenêtre, la mini-barre redevient normale. Nous verrons comment répondre dans la section sur les fenêtres SOS.

![Mini-barre pendant un SOS](images/mini_bar_sos.png)

### Règle principale : le bot ne fonctionne que si le jeu est au premier plan

Le bot prend des captures d'écran et y cherche les boutons. Si un navigateur, une messagerie ou l'explorateur de fichiers recouvre le jeu, ils apparaîtront sur la capture à la place du jeu : le bot risque de cliquer au mauvais endroit. C'est pourquoi dès qu'une autre fenêtre devient active, il s'arrête et attend. Dans le journal apparaît la ligne « [ВНИМАНИЕ] Окно игры перекрыто … Бот ждет фокуса… », dans la mini-barre — l'étiquette « Attention » et l'étape « Attend la fenêtre du jeu ». Si tu cliques sur le jeu — « [ИНФО] Окно снова активно. Продолжаем работу. »

- :monitor: **Cliquer sur la mini-barre n'arrête pas le bot.** La mini-barre est conçue pour ne pas devenir la fenêtre active : le jeu reste le programme principal pendant que tu appuies sur les boutons de la barre.
- :triangle-alert: **« Agrandir » met le bot en pause temporairement.** La fenêtre du programme étant devenue active et non celle du jeu, le bot s'arrêtera à la prochaine étape. Une fois terminé, clique sur la fenêtre du jeu et le bot reprendra sa progression. Ce temps d'attente n'est pas considéré comme un plantage par le gardien.
- :gamepad-2: Tu veux travailler sur ton ordinateur pendant que le bot farme ? Ouvre les autres fenêtres **à côté** et non par-dessus le jeu, sans cliquer dessus. Ou reporte ta tâche jusqu'à la pause (F9).

> [!warning] Les raccourcis clavier F9 et F10 ne fonctionnent que lorsque la fenêtre du jeu ou celle du programme est active. Si tu appuies sur F10 dans ton navigateur, le bot ne s'arrêtera pas : les raccourcis ne répondent pas lorsque tu es occupé sur une autre application. En savoir plus dans la section sur la pause et l'arrêt.

> [!done] Tu sais maintenant lire la mini-barre comme un tableau de bord et tu comprends pourquoi il ne faut pas masquer le jeu sous d'autres fenêtres. La suite — pause, arrêt et raccourcis clavier. [Section suivante →](#6)

## Pause, arrêt et raccourcis clavier

Le bot parcourt le Donjon tout seul, mais tu dois parfois le ralentir : tu souhaites jouer manuellement, t'absenter ou tout simplement terminer. Pour cela, il existe **quatre méthodes**, qui diffèrent par la **douceur** avec laquelle le bot s'arrête. Imagine une voiture : la « pause », c'est se garer sur le bas-côté et couper le moteur, tandis que l'« arrêt d'urgence », c'est retirer la clé en roulant. Les deux fonctionnent, mais différemment.

### Pause douce : « Pause F9 »

La méthode la plus douce. Appuie sur le bouton « Pause » sur la page principale, sur la mini-barre ou sur la touche **F9**.

1. **Appuie sur « Pause » ou F9.** Dans le journal apparaîtra la ligne `[GUI] Сигнал 'Мягкая пауза' отправлен. Бот остановится перед следующей дверью.`.
2. **Attends que le bot termine la salle.** Il n'abandonne pas le combat en cours : il le termine, ferme la fenêtre de résultat et enregistre le bilan de la salle.
3. **Le bot s'arrête dans le couloir.** Dans le journal : `[МЯГКАЯ ПАУЗА] Бот ждет в коридоре...`. L'état sur la page principale indique « Pause », sur la mini-barre — « PAUSE », et le bouton est devenu vert « Continuer ».
4. **Fais ce que tu as à faire, puis appuie sur « Continuer » (ou à nouveau sur F9).** Le bot écrit `[ИНФО] Пауза снята. Кэш составов и здоровья очищен. Включаю механизм Умного Старта.` et reprend sa route.

> [!note] « Cache effacé » signifie que le bot a **oublié** quelles équipes étaient sélectionnées et quelle était la santé des titans : pendant que tu manipulais le jeu, tout a pu changer. Avant le prochain combat, il réexaminera l'écran de sélection de l'équipe et y lira la santé. Le « démarrage intelligent » signifie que le bot regarde d'abord ce qui se trouve à l'écran avant de décider quoi faire (par exemple, fermer une fenêtre de résultat oubliée).

- :eye: **Pendant la pause, tu peux regarder ton téléphone et modifier les réglages dans la fenêtre du programme.** Cependant, le bot ne prendra en compte les nouveaux réglages qu'au prochain « Lancer le farm » (plus de détails dans la section sur la page principale).
- :door-open: **Si tu as appuyé sur quelque شيء dans le jeu, ramène-le dans le couloir du Donjon** (où le drapeau près de la porte est visible), puis appuie sur « Continuer ». Le bot saura ainsi exactement où il se trouve.
- :gauge: **Le temps s'écoule aussi pendant la pause.** Si l'objectif de la session est le temps (« 120 minutes »), la pause consommera une partie de ce temps. En revanche, le « gardien » (celui qui surveille si le bot est bloqué) ne compte pas le temps de pause et ne déclenchera pas d'alerte.

> [!tip] Tu veux t'absenter pour la nuit ou pour une longue durée ? La pause douce n'est pas nécessaire pour cela : définis un objectif (titanite, salles, étages ou temps) sur la page principale, et le bot atteindra lui-même le point de sauvegarde, s'arrêtera et t'enverra le bilan.

### Quand le bot se met lui-même en pause

Parfois, le bot demande de l'aide et se met lui-même en pause douce. Le bouton affiche alors également « Continuer », et le journal indique `[ВНИМАНИЕ] Бот на мягкой паузе: ...` avec la raison. Cela se produit lorsque :

- le bot n'a franchi aucune salle trois fois de suite en 5 minutes (le gardien a estimé qu'il était bloqué) ;
- la retraite du combat a échoué (écran non reconnu, boutons non cliqués) ;
- le combat n'a jamais commencé, même après une longue attente ;
- tu n'as pas répondu à la fenêtre « Aucun pack adapté » et qu'il n'y a pas d'équipe de réserve.

Dans ces cas-là, **regarde d'abord l'écran du téléphone**, corrige le problème (ferme la fenêtre inutile, retourne dans le couloir), puis seulement appuie sur « Continuer ». Si Telegram est configuré, le bot t'enverra un message avec une capture d'écran.

### Arrêt d'urgence : « STOP F10 »

Le bouton rouge « STOP » (ou la touche **F10**) arrête le bot **immédiatement** : le programme tue le processus du bot. Dans le journal — `[GUI] ЭКСТРЕННЫЙ СТОП. Процесс убит.`, sur la carte de bilan la raison indique « arrêté par le bouton « STOP » ».

> [!warning] Ce qui est perdu avec F10 : le bot n'a pas le temps d'écrire le bloc `[ИТОГ]` dans le journal et **n'envoie pas le bilan de session sur Telegram**. S'il était en combat à ce moment-là, le combat continuera dans le jeu (ou restera à l'écran) — tu le verras sur le téléphone. Les salles déjà franchies restent enregistrées dans les statistiques : le bot les note immédiatement après chaque salle.

Quand ce bouton est-il nécessaire : le bot se comporte de manière étrange (clique au mauvais endroit, ne réagit pas à « Pause ») ou tu dois tout stopper sur-le-champ. Dans les autres cas, il vaut mieux utiliser la pause ou Ctrl+Q.

### Raccourcis clavier : où fonctionne quoi

- :pause: **F9** — pause / « Continuer » (identique au bouton « Pause » sur la page principale).
- :square-filled: **F10** — « STOP ».
- :gamepad-2: **Ctrl+Q** — s'arrêter **avec un bilan** : le bot finit la salle commencée, s'arrête dans le couloir, stoppe et envoie le bilan de session. Dans le journal : `[ИНФО] Команда 'Ctrl+Q' принята! Бот завершит бой и остановится.`, la raison de l'arrêt étant « Arrêt manuel par l'utilisateur (Ctrl+Q) ».
- :triangle-alert: **Ctrl+Shift+Q** — s'arrêter **immédiatement, mais avec un bilan** : le bot affiche `[ЭКСТРЕННАЯ ОСТАНОВКА]`, enregistre `[ИТОГ]` et fait **une seule** tentative d'envoi du bilan sur Telegram (sans réessai pour ne pas traîner).

Subtilités importantes qui font que les touches semblent parfois « ne pas fonctionner » :

- **F9 et F10 sont écoutés par la fenêtre du programme** et uniquement quand **la fenêtre du jeu ou celle du programme est active**. Si tu appuies sur F10 dans un navigateur ou une messagerie, il ne se passera rien. Si le jeu est réduit ou masqué par une autre fenêtre, utilise les boutons de la mini-barre : ils fonctionnent toujours car la mini-barre ne retire pas l'activité du jeu.
- **Ctrl+Q et Ctrl+Shift+Q sont écoutés par le bot lui-même** et non par la fenêtre du programme ; ils fonctionnent donc tant que le bot tourne, même si une autre fenêtre est active.
- **Ces raccourcis sont aussi connus d'autres programmes.** Ctrl+Q ferme de nombreux programmes (Word, Telegram Desktop), et Ctrl+Shift+Q — les navigateurs. Pendant que le bot fonctionne, ne les utilise pas dans d'autres fenêtres : le bot les « entendra » également et s'arrêtera.
- **Le bot vérifie Ctrl+Q lorsqu'il se trouve dans le couloir** devant la porte suivante. En pause douce, il est à l'arrêt et ne vérifie rien, donc Ctrl+Q ne fonctionnera qu'après « Continuer ». Mais si le bot attend ta réponse dans la fenêtre SOS, Ctrl+Q l'arrêtera immédiatement.
- **Maintenir la touche enfoncée ne répète pas la commande :** une pression = une commande.
- Si tu appuies sur F9 ou F10 quand le bot n'est pas lancé, le journal affichera `[GUI] Нажата F9, но бот не запущен.`.

### La croix de la fenêtre et la fermeture de scrcpy

- :x: **La croix de la fenêtre du programme pendant que le bot tourne.** La question « Arrêter le bot ? » s'affichera. Le bouton « Arrêter et fermer » fermera le programme et le bot, ainsi que la fenêtre du jeu (scrcpy) si elle a été ouverte par le programme lui-même — le bilan ne sera pas envoyé sur Telegram. Si tu ne le souhaites pas, ferme la fenêtre de question et commence par arrêter le bot en douceur.
- :smartphone: **Tu as fermé la fenêtre du jeu (`HeroWarsBot_Arena`) toi-même.** Le programme écrira `[GUI] Окно scrcpy закрыто — останавливаю бота (он напишет итог и пришлёт его в Telegram).` Le bot rédigera lui-même le bilan de la session et l'enverra sur Telegram ; s'il ne répond pas dans les 10 secondes, le programme l'arrêtera comme avec F10.
- :pencil: S'il y a des modifications non enregistrées dans le « Maître des règles », la croix demandera d'abord « Enregistrer les modifications ? ».

### Que choisir

- **Je veux faire une pause et revenir** — « Pause » (F9). Appuie sur « Continuer » lorsque tu seras prêt.
- **Je veux terminer et recevoir le bilan** — Ctrl+Q (le bot finit la salle, s'arrête, envoie le bilan sur Telegram).
- **Je dois m'arrêter immédiatement, mais j'ai besoin du bilan** — Ctrl+Shift+Q.
- **Le bot a planté ou se comporte bizarrement** — « STOP » (F10), puis consulte le journal.
- **Le bot t'a appelé via une fenêtre SOS et tu veux terminer** — le bouton « Arrêter le bot » dans cette fenêtre : le bot s'arrêtera de lui-même et enverra le bilan. Nous verrons la fenêtre SOS séparément.

### Bilan de session sur Telegram

Si Telegram est configuré, le bilan arrive lors de n'importe quel arrêt, **sauf avec le bouton « STOP »** ou la fermeture de la fenêtre du programme : le bot indique si tu l'as arrêté toi-même (« Bot arrêté par vous »), s'il a atteint l'objectif (« Farm terminé ») ou s'il s'est arrêté sur une erreur, le temps écoulé, le nombre de salles, d'étages et de titanite, ainsi que la présence de retraites et de fenêtres SOS. S'il n'y a pas de connexion Internet, le bot essaiera d'envoyer le bilan encore deux fois (après 10 et 30 secondes), puis s'éteindra. Comment connecter Telegram — dans une section dédiée.

> [!done] Tu sais maintenant comment ralentir le bot en douceur, comment l'arrêter définitivement et ce que fait chaque touche. La suite — la configuration des règles : comment apprendre au bot à choisir les bonnes équipes. [Section suivante →](#7)

## Maître des règles : « Base et salles »

Le « Maître des règles » est le deuxième bouton dans la bande de gauche (icône avec des curseurs). Tu y expliques trois choses au bot : **quand s'arrêter**, **ce qui constitue un mauvais combat** et **quelle équipe envoyer dans chaque salle**. Une équipe (pack) est composée de 3 à 5 titans. La page est divisée en trois onglets en haut : « Base et salles », « Auto-tactique et PV » et « Règles et interceptions ». Dans cette section, nous abordons le premier, le plus important : sans lui, le bot ne sait même pas qui aligner en combat.

![Onglet « Base et salles » : en haut deux cartes de réglages, en bas quatre lignes d'équipes](images/rules_base.png)

En haut — « Paramètres de session » (deux cartes), en bas — « Équipes par salle ». En bas de la page, identique sur chaque onglet, se trouve une bande grise avec des boutons : « Enregistrer les réglages » et « Restaurer / Réinitialiser ». Nous en reparlerons à la fin de la section. Le principal point à retenir dès maintenant : **tant que tu n'as pas appuyé sur « Enregistrer les réglages », rien n'est enregistré** — aucune modification ne parvient au bot.

### Carte « Objectifs et limites »

- :target: **« Objectif de session »** — quand le bot doit terminer. L'objectif est toujours **unique**, parmi quatre : « Titanite », « Salles », « Étages » ou « Temps » (temps — en minutes). Choisis le type dans la liste et saisis un nombre dans le champ. Seuls les chiffres sont acceptés dans ce champ. La mention « 0 — sans limite » signifie qu'un zéro désactive l'objectif et que le bot continuera jusqu'à ce que tu l'arrêtes. La flèche circulaire à droite (« Réinitialiser l'objectif ») remet à 0.
- :gem: **Le bot compte la titanite lui-même** sans la lire à l'écran : 6 pour une salle normale et 12 si l'icône « x2 » est présente sur la fenêtre de résultat. Ainsi, « 120 titanite », c'est environ 20 salles sans « x2 ». Tant que tu n'as jamais enregistré les réglages, le bot prend de lui-même l'objectif « 120 titanite ».
- :layers: **Le bot n'abandonne pas un étage en cours.** Une fois l'objectif « Titanite », « Salles » ou « Temps » atteint, il ne s'arrête pas sur place : il écrit dans le journal `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.`, termine les salles restantes de l'étage et s'arrête devant le point de sauvegarde sans appuyer sur « Activer ». Ainsi, l'étage ne reste pas inachevé, et le bot récupérera la récompense et validera l'étage en priorité au prochain lancement. Si aucun point de sauvegarde n'est trouvé après 6 salles (il y en a 5 par étage), le bot s'arrêtera en l'état. L'objectif « Étages » se déclenche dès que le point de sauvegarde est franchi.
- :gauge: **Le temps s'écoule aussi pendant la pause.** Un objectif « Temps — 120 » signifie 120 minutes à partir du clic sur « Lancer le farm », pauses comprises.
- :calendar: **« Heure de changement de jour (heure locale) »** — l'heure à laquelle commence pour toi une nouvelle journée de jeu. Par défaut 05:00. Cela détermine à quel jour se rattachent les combats dans les statistiques, mais aussi la mémoire du bot concernant la santé des titans : elle subsiste pendant une journée de jeu, et lors d'un nouveau jour, le bot repart de zéro. Indique l'heure après laquelle tu considères que le jour a changé (par exemple, quand tu vas te coucher).
- :send: **« Configurer Telegram »** — ouvre une fenêtre distincte où s'active la connexion à la messagerie. À côté du bouton se trouvent un point et une mention : vert « Notifications SOS activées » ou gris « Telegram non configuré ». Nous verrons comment le connecter dans la section dédiée à Telegram. Un point important ici : le bouton « Appliquer » dans cette fenêtre ne modifie que cette page. Pour que la configuration soit enregistrée dans le fichier, tu dois également cliquer sur « Enregistrer les réglages ».

> [!tip] Quel objectif choisir ? « Temps » est pratique si tu as un créneau disponible (« laisse le bot tourner une heure pendant que je prépare le dîner »). « Titanite » — quand tu dois accumuler une quantité précise de récompenses. « Salles » et « Étages » — quand tu veux effectuer un nombre exact de parcours. En cas de doute, laisse « Titanite » et 120 : c'est un court essai.

### Carte « Sécurité et mode »

C'est ici qu'on définit **ce qu'est un mauvais combat**. Le bot lit la santé des titans dans la fenêtre de résultat et compare deux valeurs aux tiennes.

- :heart-pulse: **« Seuil de panique PV, % »** — en dessous de quelle santé après un combat celui-ci est considéré comme mauvais. Par défaut 40.
- :swords: **« Delta de perte de PV, % »** — combien de santé un titan peut perdre lors d'un seul combat. Par défaut 30.

Ces deux champs n'acceptent que des nombres entiers de 0 à 100 ; si tu saisis autre chose, le champ deviendra rouge avec la mention « Saisis un nombre de 0 à 100 », et il sera impossible d'enregistrer les réglages tant que ce n'est pas corrigé.

Exemple concret avec un seuil de 40 et une delta de 30 :

- Araji est entré en combat à 100 %, en est ressorti à 80 % — **tout va bien** : il a perdu 20 et reste au-dessus de 40.
- Araji est entré à 100 %, en est ressorti à 55 % — **mauvais combat**. 55 est au-dessus du seuil, mais il a perdu 45 alors que le maximum toléré est 30.
- Araji est entré à 50 %, en est ressorti à 35 % — **mauvais combat**. Il n'a perdu que 15, mais 35 est en dessous du seuil de panique.
- Si un titan meurt ou qu'il est introuvable sur la fenêtre de résultat — c'est **toujours un mauvais combat**, peu importe tes réglages.

Les pertes sont calculées à partir de la santé avec laquelle le titan est **entré** en combat, et non à partir de 100 %. Un titan blessé atteint donc le seuil plus vite qu'un titan en pleine forme. Plus le seuil est élevé et plus la delta est petite, plus le bot sera strict et t'appellera souvent ; un zéro pour le seuil désactive la vérification « sous le seuil » (sauf pour les morts), et 100 pour la delta désactive la vérification des pertes.

> [!note] Le seuil et la delta sont communs à tous les titans. Il est possible de fixer un seuil spécifique pour un titan particulier, ou d'activer la règle « si trois titans ont perdu beaucoup de PV — mauvais combat ». Cela se fait sur l'onglet voisin « Auto-tactique et PV ».

En dessous se trouvent deux commutateurs :

- :shield-check: **« Le bot décide seul »** (« Annule les mauvais combats et choisit une équipe ») — **désactivé** par défaut. Désactivé : mauvais combat → fenêtre « Intervention requise », le bot t'attend. Activé : le bot annule le combat sans poser de question et rejoue avec une équipe de réserve, tout en sélectionnant l'équipe en fonction de la santé des titans. En détail dans la section sur le fonctionnement autonome du bot. Active-le lorsque tu as déjà vu le bot fonctionner et que tu fais confiance à tes équipes de réserve.
- :swords: **« Contrôle manuel de l'ulti d'Angus »** (« Global, dans toutes les salles ») — **désactivé** par défaut, et ainsi tout combat, y compris avec Angus, se déroule en automatique. S'il est activé — pour les équipes avec Angus, le bot clique sur « En combat », active le combat automatique quelques secondes pour l'ult d'Angus puis le désactive. Le bot n'annule pas lui-même ce type de combat et t'appelle à l'aide. Au lancement, le journal indique le choix retenu : `[ТАКТИКА] Ангус: ...`.

### Équipes par salle

Sous la mention « L'équipe principale passe d'abord, les remplaçantes dans l'ordre si le combat tourne mal » se trouvent quatre lignes — par salle : « Terre », « Eau », « Feu » et « Mixte ». Chacune constitue une carte séparée.

- :users: **Équipe principale** — les carrés des titans sous le nom de la salle. Le bot l'aligne s'il n'y a pas de raison de faire autrement (par exemple si une règle de l'onglet « Règles et interceptions » s'est déclenchée). Les titans sont affichés de gauche à droite, **comme ils sont positionnés sur l'écran du jeu**. S'il n'y a pas d'équipe — la mention « Pack non défini » s'affiche à la place des carrés.
- :pencil: **Crayon (« Changer l'équipe »)** — ouvre la fenêtre « Compose l'équipe ».
- :list: **« Équipes de réserve »** avec le nombre « N шт. » — liste déroulante (flèche bas/haut). Le bot tente les équipes de réserve dans l'ordre si le combat tourne mal et qu'il décide seul (« Le bot décide seul » activé ou absence de réponse à temps dans la fenêtre). Il peut y en avoir jusqu'à 5 par salle. À l'intérieur, chaque équipe de réserve est une ligne `#1`, `#2` et ainsi de suite, avec une croix à droite (« Supprimer l'équipe »). Le bouton « Ajouter une équipe » ouvre la même fenêtre « Compose l'équipe ».
- :plus: **« Condition »** — « + Condition » : un accès rapide à une règle pour cette salle, par exemple « si contre Angus — aligne telle équipe ». La fenêtre « Nouvelle règle » s'ouvrira avec la salle déjà sélectionnée. Nous verrons comment la remplir dans la section sur les règles.

Définis l'équipe principale dans les quatre salles **avant le premier farm** : le bot ne connaît pas tes titans de lui-même et n'a pas d'équipes par défaut.

Comment composer une équipe :

1. **Clique sur le crayon** dans la salle souhaitée. La fenêtre « Compose l'équipe » s'ouvrira.
2. **Clique sur les titans** que tu veux aligner. Clique à nouveau pour retirar. En haut le compteur indique : « Choisis : 3 / 5 » et le conseil « Prêt à appliquer » (s'il y en a deux, il est inscrit « Au moins 3 · encore 1 »).
3. **Prends en compte l'élément de la salle.** Seuls les titans de cet élément peuvent aller en « Terre », « Eau » et « Feu », tandis qu'en « Mixte », tous sont acceptés, y compris Métis (elle est « élarite » et ne va pas dans les autres salles : « Métis — salle mixte uniquement »). Lorsque 5 sont sélectionnés, les autres titans sont bloqués.
4. **Clique sur « Appliquer »** (ou « Annuler » si tu as changé d'avis ; « Effacer » retire tous les titans d'un coup).

![Fenêtre « Compose l'équipe » pour la salle « Eau » : trois titans sélectionnés, en bas « Appliquer »](images/rules_picker.png)

> [!warning] « Appliquer » dans la fenêtre « Compose l'équipe » ne fait que modifier la page : l'équipe n'est pas encore **enregistrée** dans le fichier. Elle sera enregistrée une fois que tu auras cliqué sur « Enregistrer les réglages ». L'équipe principale de chaque salle se trouve dans le fichier `bot_data/rules/<стихия>.yml`, les réserves et tous les chiffres — dans `profile.yml`. Tu n'as pas besoin de modifier ces fichiers à la main.

Une équipe de réserve qui existe déjà dans la liste (quel que soit l'ordre des titans) ne peut pas être ajoutée une seconde fois : une notification « Cette équipe de réserve existe déjà » apparaîtra.

> [!tip] Quelles équipes mettre en réserve ? Donne le choix au bot : fais en sorte que l'équipe de réserve diffère de l'équipe principale d'au moins deux titans. Si chez toi Araji ressort souvent blessé d'un combat, mets dans l'équipe de réserve ceux qui encaissent le mieux.

### Enregistrement et « Restaurer / Réinitialiser »

La bande inférieure indique l'état : « Toutes les modifications sont enregistrées » (coche verte) ou « Modifications non enregistrées » (icône jaune). Pendant que le bot fonctionne, il est écrit à côté « Le bot prendra les nouveaux réglages à son prochain lancement ».

- :save: **« Enregistrer les réglages »** enregistre uniquement ce que tu as modifié et affiche la notification « Réglages enregistrés ». Tant que le bouton n'est pas cliqué, le bot n'est pas au courant de tes modifications. Le journal affichera `[GUI] Профиль настроек сохранен!`.
- :rotate-ccw: **« Restaurer / Réinitialiser »** — bouton rouge ; il demandera d'abord « Restaurer les réglages ? ». Les réglages reviendront aux **derniers enregistrés** (copie `bot_data/profile.yml.bak`). S'il n'y a pas de copie, `profile.yml` sera supprimé et le bot prendra les valeurs par défaut. Les modifications non enregistrées seront perdues. Ce bouton ne touche pas aux équipes principales ni aux règles dans les fichiers `bot_data/rules`, mais le formulaire de la page les relira depuis le disque.
- :triangle-alert: **Si tu quittes la page avec des modifications non enregistrées** (en allant dans une autre section ou en fermant par la croix de la fenêtre), une pop-up « Enregistrer les modifications ? » apparaîtra avec les boutons « Enregistrer », « Ne pas enregistrer » et « Annuler ».

Le bot lit les réglages **une seule fois, lorsque tu appuies sur « Lancer le farm »**. Tu peux les modifier pendant le fonctionnement, mais ils ne prendront effet qu'après un arrêt et un nouveau lancement. Même « Pause » et « Continuer » ne les réactualisent pas. La carte « Paramètres de lancement » sur la page principale affiche exactement les réglages avec lesquels le bot tourne en ce moment.

> [!warning] Si le fichier `profile.yml` est endommagé, en haut du journal de la page principale apparaîtra `[ОШИБКА] Файл profile.yml поврежден!`, la page affichera les valeurs par défaut et « Enregistrer les réglages » refusera d'écrire (« profile.yml est endommagé — réglages non enregistrés »). Clique sur « Restaurer / Réinitialiser ».

> [!done] Tu sais maintenant comment définir un objectif, des seuils et des équipes pour chaque salle. La suite — l'onglet « Auto-tactique et PV » : l'ordre des portes et la façon dont le bot soigne et remplace les titans. [Section suivante →](#8)

## Assistant de règles : « Auto-tactique et PV »

Le deuxième onglet de l'« Assistant de règles ». Sur le premier (« Base et salles »), tu as défini les équipes et les seuils généraux. Ici, tu expliques au bot **comment se comporter quand quelque chose tourne mal** : quelle porte franchir en premier, ce qu'il faut considérer comme un mauvais combat, combien de fois essayer une autre équipe, combien de temps t'attendre et comment soigner les titans blessés. Tous les champs sont déjà remplis avec des valeurs raisonnables, le bot fonctionne donc sans tes modifications. Modifie-les lorsque tu constateras qu'il ne se comporte pas comme tu le souhaites.

![Onglet « Auto-tactique et PV » : bandeau en haut, quatre portes, deux cartes côte à côte et seuils personnels en bas](images/tactics_tab.png)

Comme sur le premier onglet, **rien n'est enregistré tant que tu ne cliques pas sur « Enregistrer les réglages »**, et le bot lit les réglages une seule fois lorsque tu cliques sur « Lancer le farm ». Si tu les modifies pendant le farm, cela prendra effet après l'arrêt et un nouveau lancement.

### Bandeau bleu en haut

Il explique brièvement ce que fait le bot lors d'un mauvais combat : il annule le combat et le rejoue avec une équipe de secours, et retient l'équipe victorieuse dans une règle.

Si l'interrupteur « Le bot décide seul » est désactivé sur le premier onglet, une phrase supplémentaire s'ajoute au bandeau. Elle est importante, nous allons donc l'examiner séparément. **Sans « Le bot décide seul », deux choses ne fonctionnent pas : les équipes de secours et l'équipe de soin.** Tout le reste sur cet onglet fonctionne toujours :

- :door-open: l'ordre des portes ;
- :gauge: l'attente de ta réponse à la fenêtre SOS (la fenêtre dans laquelle le bot t'appelle quand le combat est mauvais) ;
- :triangle-alert: les critères de mauvais combat ;
- :heart-pulse: les seuils de panique personnels.

### « Priorité des portes »

Dans le couloir, le bot voit souvent plusieurs portes à la fois : une par élément (eau, terre, feu) ou « Mixte ». À l'intérieur de la salle, des ennemis t'attendent, et l'équipe est spécifique à chaque élément. L'ordre détermine **quelle porte le bot ouvrira en premier**. Par défaut : « Eau », « Mixte », « Terre », « Feu ».

Les quatre emplacements vont de gauche à droite, séparés par des flèches ; chacun porte un numéro de 1 à 4. Clique sur un emplacement et choisis un élément. Il n'y a pas de doublons : si tu choisis un élément déjà placé ailleurs, ils **échangent simplement leurs positions**. Si l'ordre était « Eau, Mixte, Terre, Feu » et que tu choisis « Feu » en première position, cela deviendra « Feu, Mixte, Terre, Eau ».

Deux précisions pour éviter les surprises en jeu :

- Si une porte est **interdite par une règle « Skip »** (voir la section sur les « Règles et interceptions »), le bot la sautera, même si elle est la première dans l'ordre. Si toutes les portes sont interdites, il prendra la première dans l'ordre.
- Si « Le bot décide seul » est activé, le bot **choisira parfois lui-même une autre porte**, hors ordre : là où le soin du titan blessé fonctionnera, ou en évitant une porte dangereuse pour les blessés. Ce choix est visible dans le journal sous la ligne `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...`.

### Carte « Critères de mauvais combat et SOS »

- :swords: **« Équipes de secours à essayer par salle »** — combien de fois par salle le bot peut lui-même annuler le combat et rejouer avec une autre équipe. De 1 à 3, par défaut 2. Si les tentatives sont épuisées et que le combat est toujours mauvais, le bot t'appelle. Fonctionne uniquement avec « Le bot décide seul ». Impossible de mettre plus de 3 : rejouer un même combat dix fois n'a pas de sens, et chaque tentative prend du temps.
- :gauge: **« Délai de la fenêtre SOS sans réponse, min »** — combien de minutes le bot attend ta réponse à la fenêtre « Intervention requise » avant de décider seul. De 0 à 60, par défaut 10. La légende sous le champ indique « 0 : attendre toujours » : **zéro signifie « attendre toujours »**, le bot s'arrêtera et t'attendra jusqu'au matin. Cela fonctionne aussi **sans** « Le bot décide seul ». Ce que le bot décidera lui-même (annuler le combat, l'accepter ou se mettre en pause) est expliqué dans la section sur les fenêtres SOS.
- :users: **« Considérer le combat comme mauvais si »** — pertes globales de l'équipe : « titans ≥ 3 » et « ont perdu ≥ 40 » « % PV chacun ». Cette vérification détecte le cas où **chaque titan résiste individuellement**, mais où l'équipe dans son ensemble a faibli. Si trois titans ont perdu 40 % ou plus, le combat est mauvais, même si aucun n'est tombé sous son seuil de panique. La mention « 0 titan : ne pas vérifier » signifie : mets 0 dans le premier champ pour désactiver la vérification. Le premier champ va de 0 à 5, le second de 0 à 100.

Un exemple concret. Équipe : Araji, Hyperion, Rigel, Iyari, Lumira. Après le combat, Araji a perdu 45 %, Rigel 42 %, Iyari 40 %, et les autres 10 % chacun. Trois titans ont perdu « 40 % et plus » — le combat est mauvais, même s'il reste à chacun plus que son seuil de panique. Si Iyari n'avait perdu que 35 %, seuls deux titans seraient concernés et la vérification globale n'aurait rien à redire.

> [!note] Les autres signes d'un mauvais combat — le seuil de panique et la tolérance de pertes — se trouvent sur le premier onglet « Base et salles ». Le combat est mauvais si **au moins un** signe se déclenche : quelqu'un est mort ou introuvable sur l'écran, quelqu'un a ses PV sous le seuil, quelqu'un a perdu plus que la tolérance autorisée ou les pertes globales se sont déclenchées.

Si tu entres un nombre incorrect (une lettre ou un nombre hors limites), le champ deviendra rouge, la mention « Un nombre de … à … » apparaîtra en dessous et il sera impossible d'enregistrer les réglages tant que ce ne sera pas corrigé.

### Carte « Équipe de soin automatique dans la salle Mixte »

Il arrive souvent qu'un titan subisse des dégâts plusieurs combats de suite et se retrouve à la moitié de sa santé. Tôt ou tard, il tombera sous le seuil et le combat deviendra mauvais. Le « soin », c'est quand le bot **compose lui-même une équipe spéciale** pour soigner le blessé (en y intégrant un soigneur qui remonte la santé du blessé). Le bot ne compose une telle équipe que pour la salle « Mixte », car on peut y placer n'importe quel titan.

Cela ne fonctionne qu'avec « Le bot décide seul », et seulement si ta propre règle de soin ne s'est pas déclenchée (une règle est plus prioritaire).

- :heart-pulse: **« Soigner le titan si les PV sont sous, % »** — par défaut 60. Un titan avec une santé supérieure à ce chiffre est considéré en bonne santé. **0 désactive** complètement l'équipe de soin. Cependant, il y a une limite inférieure : si les PV du titan sont déjà **sous le seuil de panique**, il ne pourra pas être soigné dans la salle « Mixte » et le bot ne le touchera pas.
- :users: **« Qui retirer de l'équipe pour le blessé »** — trois emplacements avec des flèches. Lorsqu'il faut placer le blessé et qu'il n'y a plus de place dans l'équipe, quelqu'un doit céder sa place. Clique sur un emplacement et choisis un titan : la liste est divisée en colonnes par élément. **« — auto — »** (la valeur par défaut) signifie : le bot retire depuis la fin de l'équipe, mais **ne touche pas aux soigneurs**. Pour l'équipe « Hyperion, Rigel, Iyari, Lumira, Amon », ce sera Amon, puis Lumira. Si tu choisis un titan déjà placé sur un autre emplacement, ils échangeront leurs positions.

Comment le bot soigne, en termes simples :

1. Il regarde qui a des PV sous 60 %, mais au-dessus du seuil de panique, et qui n'a pas été interdit par des règles « Skip ».
2. Il soigne **un par un**, en commençant par celui qui est le plus proche de son seuil. D'abord les principaux (des équipes de base), puis les secouristes.
3. Si le blessé n'est pas dans l'équipe, il prend la place de celui qui a été retiré. Cependant, les titans qui sont déjà soignés dans leur « propre » salle (titans d'eau et de terre : leur équipe de base contient un soigneur) ne sont pas amenés en salle « Mixte », sauf s'ils ne remontent pas au-dessus du seuil après deux combats consécutifs. Les titans de feu n'ont aucun moyen de se soigner dans leur « propre » salle, le soin s'active donc immédiatement pour eux.
4. Si le blessé est déjà dans l'équipe mais ne remonte pas après deux combats consécutifs, un **soigneur en bonne santé et chargé en énergie** (PV à partir de 80 %, énergie à partir de 60 %) prend la place du titan retiré.
5. L'équipe n'est pas choisie s'il ne reste plus de soigneur dedans, si elle perd contre ces ennemis, si elle est dangereuse pour les blessés ou si elle nécessite un combat manuel (Angus).

Pourquoi le bot est-il si prudent ? Il ne soignera pas quelqu'un que tu n'as indiqué nulle part : un titan qui ne figure ni dans tes équipes ni dans tes règles ne sera jamais placé de lui-même par le bot. S'il n'a pas réussi à composer l'équipe (le titan n'a pas pu être placé dans l'emplacement), le bot ne s'arrête pas, il place l'équipe ordinaire et **ne soigne plus ce titan jusqu'à la fin du lancement**.

Dans le journal, cela se voit par les lignes `[ТАКТИКА] Пак отхила (бот собрал сам): ...` et `[ТАКТИКА] Отхил: ...` (pourquoi le blessé n'est pas soigné).

### Carte « Seuils de panique personnels des titans, % PV »

Le seuil de panique commun (40 par défaut) s'applique à tous. Mais il y a des titans qu'on regrette de perdre plus tôt que d'autres, et d'autres qui supportent très bien des PV bas. Tu peux leur définir **ton propre seuil**.

- En bas, la mention « Autres titans : seuil commun 40% » (le nombre vient du premier onglet). Tant qu'il n'y a pas de seuil personnel, il est écrit « Aucun seuil personnel : tous les titans utilisent le seuil commun ».
- Clique sur « Définir un seuil personnel pour un titan ». Une petite fenêtre « Seuil de panique personnel » s'ouvre : choisis un titan dans la liste et entre un nombre de 0 à 100. Clique sur « Appliquer ». La fenêtre indique « Seuil commun : 40% » pour te donner un point de comparaison. Seuls les titans qui n'ont pas encore de seuil personnel apparaissent dans la liste.
- Chaque seuil défini apparaît sous forme d'étiquette avec le titan et un chiffre jaune. Clique sur l'étiquette pour modifier le seuil (impossible de changer de titan, il faudra le supprimer et l'ajouter à nouveau). La **croix** sur l'étiquette supprime le seuil, et le titan réutilise à nouveau le seuil commun.

Le combat est mauvais si les PV de ce titan après le combat sont **inférieurs à son seuil personnel**. Exemple : le seuil commun est de 40, mais celui de Rigel est réglé à 60. Rigel termine avec 55 % — le combat est mauvais, même si pour les autres 55 aurait été correct.

> [!tip] Par quoi commencer ? Ne modifie rien tant que tu n'as pas vu passer deux ou trois dizaines de salles. Si tu remarques que le bot t'appelle à cause d'un même titan, règle-lui un seuil personnel plus bas. Si le bot change trop souvent d'équipe pour soigner, **diminue** le chiffre dans « Soigner le titan si les PV sont sous, % ». Si tu ne veux pas du tout qu'il soigne, mets 0.

> [!warning] Si tu as réglé le « Délai de la fenêtre SOS sans réponse, min » à 0 et que tu es parti dormir, et que le bot t'appelle via une fenêtre, il attendra jusqu'au matin. Il vaut mieux laisser 10–15 minutes et configurer Telegram : tu seras ainsi informé immédiatement du problème, et si tu n'as pas le temps d'intervenir, le bot décidera seul.

> [!done] Tu sais maintenant comment définir l'ordre des portes, ce qu'il faut considérer comme un mauvais combat et comment le bot soigne les blessés. La suite : Telegram et les fenêtres qui t'appellent à l'aide. [Section suivante →](#9)

## Assistant de règles : «Règles et interceptions»

Le troisième onglet de l'«Assistant de règles». Sur le premier, tu as défini le **pack principal** de chaque salle, sur le deuxième — la façon dont le bot se comporte en cas de pépin. Ici, tu lui apprends les **exceptions** : « d'habitude mets le pack principal, mais s'il se passe ceci — fais autrement ». Chaque exception de ce type s'appelle une **règle**. Et une « interception », c'est quand la règle « intercepte » le choix du pack au pack principal et place le sien.

Une règle se lit toujours de la même façon : **« si [condition] — alors [action] »**. Par exemple :

- :heart-pulse: « Si Araji a ses PV sous 50 % — mets le pack avec le soigneur Sigurd ».
- :swords: « Si Angus, Sylva et Verdok sont dans la salle — mets ce pack ».
- :door-open: « Si Araji a ses PV sous 30 % — n'entre pas dans le «Feu» ».
- :users: « Si Angus, Avalon et Eden sont dans la salle — arrête-toi et demande-moi ».

![Onglet «Règles et interceptions» : filtres d'éléments, liste de règles avec icônes, packs et interrupteurs](images/rules_intercepts.png)

Chaque élément a ses propres règles : «Terre», «Eau», «Feu» et «Mixte» ont des listes séparées. Quand le bot entre par la porte du «Feu», il ne regarde que les règles du «Feu». Comme sur les autres onglets, **rien n'est enregistré tant que tu ne cliques pas sur «Enregistrer les réglages»**, et le bot lit les règles une seule fois quand tu cliques sur «Lancer le farm».

> [!note] Tu n'auras pas du tout besoin d'écrire beaucoup de règles. Si «Le bot décide seul» est activé, le bot **retient lui-même** les packs gagnants après un repli et ajoute lui-même les « règles dorées ». Elles apparaîtront dans cette même liste (voir plus bas). Tes propres règles sont utiles quand tu sais déjà que « ceci ne doit pas être fait » ou « dans telle situation, il faut précisément ce pack ».

### Quels types de règles existent

La condition d'une règle est l'une des trois, et l'action est l'une des trois. Ensemble, elles forment les types habituels :

- :heart-pulse: **Sauvetage par PV ou par énergie.** Condition — « PV (ou énergie) de tel titan sous N % », action — mettre un autre pack. Dans la liste, l'icône est **«SOIN»** (par PV) ou **«ÉNERGIE»**. C'est ainsi qu'on soigne : quand un titan est blessé, un pack avec un soigneur est placé.
- :swords: **Contre ces ennemis.** Condition — « tous ces ennemis sont dans la salle », action — mettre son propre pack. Icône **«ENNEMIS»**. Les ennemis peuvent être choisis parmi les 13 que le bot reconnaît dans le Donjon.
- :door-open: **«Skip» — interdiction.** Condition — « PV ou énergie du titan sous N % », action — ne pas placer ce titan et ne pas entrer dans cette salle. Icône **«SKIP»**, à droite la mention «Passer la salle».
- :users: **«Te demander».** N'importe quelle condition, et l'action — ne pas décider seul, mais t'appeler. À droite la mention **«Te demander»**, et l'icône dépend de la condition («PV», «ÉNERGIE», «ENNEMIS»). Quand elle se déclenche, le bot ouvre la fenêtre «Aucun pack adapté» et attend ta réponse. Si tu ne réponds pas pendant le délai défini dans l'« Auto-tactique », il décidera seul.

L'icône « PV » (et non « SOIN ») signifie que la condition porte sur les PV, et l'action est « Te demander ». S'il n'y a aucune condition, il n'y a pas d'icône, et sous le nom il est écrit « Pas de condition — la règle ne se déclenche jamais ».

Parlons maintenant de « Skip », car il a deux fonctions à la fois. Exemple : dans le «Feu» se trouve la règle « Araji, PV sous 30 % ».

1. **Porte.** Tant qu'Araji a moins de 30 %, le bot n'ira pas dans le «Feu» et choisira une autre porte. Si toutes les portes sont interdites, le bot prendra la première dans l'ordre.
2. **« Liste noire ».** Dans cette salle, Araji ne sera pas placé : tout pack où il figure sera rejeté par le bot qui prendra le suivant. Si le pack **principal** contient aussi un titan interdit, il n'y a rien à placer — le bot s'arrêtera et ouvrira la fenêtre «Aucun pack adapté».

> [!warning] On ne peut pas faire un « Skip » par ennemis. Le bot ne découvre les ennemis qu'**après** être entré par la porte, il ne peut donc pas choisir la porte en fonction d'eux. Dans la fenêtre de règle pour « Par ennemis », la case « Skip » n'est pas disponible. Si tu veux contourner une salle avec certains ennemis — mets la règle « Te demander », la décision t'appartiendra alors.

### Dans quel ordre le bot vérifie-t-il les règles

Quand le combat commence, le bot parcourt les règles de la salle **dans cet ordre** :

1. **« Skip ».** D'abord, le bot dresse la « liste noire » des titans : ceux qui ont été interdits par une règle « Skip » déclenchée. Un pack avec un tel titan ne conviendra pas, même si la règle elle-même le demande (c'est ce qu'on appelle un veto : l'interdiction est plus forte que n'importe quelle règle).
2. **Sauvetage.** Les règles où la condition contient les PV ou l'énergie d'un titan. Cela inclut aussi les règles « contre des ennemis, avec Araji < 50 % PV » (ennemis plus PV) : elles sont vérifiées ici même, **avant** les règles ordinaires sur les ennemis.
3. **Contre les ennemis.** Les règles où la condition ne comporte que des ennemis.
4. **Pack principal** de la salle — si rien ne convient.

Au sein de chaque groupe, le bot va **de haut en bas** et prend la première règle déclenchée. C'est pourquoi les flèches sont nécessaires : si deux règles sur les ennemis conviennent en même temps, celle située plus haut l'emportera. En revanche, la règle de « Sauvetage » est toujours plus forte que « Contre les ennemis », quel que soit leur emplacement dans la liste. Les règles **désactivées** ne participent pas à la vérification.

Les conditions sont comparées à ce que le bot sait de tes titans (il prend les PV et l'énergie sur l'écran de sélection de l'équipe et après les combats). Si le bot n'a pas encore vu la santé d'un titan, il la considère comme pleine, et la règle « sous N % » ne se déclenchera pas. Si la condition concerne plusieurs titans (ce qui arrive pour les règles retenues par le bot lui-même), **toutes** les conditions doivent être remplies en même temps. De même pour les ennemis : la règle ne se déclenchera que si **tous** les ennemis énumérés sont dans la salle.

### Liste des règles : contenu d'une ligne

En haut — «Règles actives» et un encadré gris indiquant le nombre de règles, à droite un conseil : «Choisis un élément pour changer l'ordre» (si tout est affiché) ou «La règle plus haut dans la liste est vérifiée en premier» (si un élément est choisi). En dessous, les boutons-filtres «Toutes», «Terre», «Eau», «Feu», «Mixte» et le bouton «Nouvelle règle». En dessous, les en-têtes de colonnes « № », «Condition», «Action», «Act».

Sur chaque ligne, de gauche à droite :

- **Numéro** — la place dans la liste de son élément. Plus le numéro est petit, plus la règle est vérifiée tôt. Quand **un seul** élément est sélectionné, les flèches «Monter» et «Descendre» apparaissent à côté du numéro. Si «Toutes» est sélectionné — pas de flèches : les éléments sont affichés à la suite et ne rivalisent pas entre eux.
- **Icônes** — l'élément de la salle et le type de règle («SOIN», «PV», «ÉNERGIE», «ENNEMIS», «SKIP»).
- **Nom** et la ligne grise en dessous — la condition en mots, par exemple « Araji : PV sous 50 % » ou « Ennemis dans la salle : Angus, Sylva ».
- **Action** — une flèche et les carrés des titans du pack (de gauche à droite, comme dans le jeu) avec la mention «changement de pack». Ou l'encadré «Te demander» / «Passer la salle».
- **Interrupteur «Act»** — activer ou désactiver la règle.
- **Crayon** «Modifier» et **croix** «Supprimer».

S'il n'y a pas de règles, à la place de la liste il est écrit : « Pas de règles. Clique sur « Nouvelle règle » — ou le bot retiendra la règle lui-même après un repli. »

### Interrupteur, flèches, croix et « Effacer »

- :check: **Interrupteur.** Une règle désactivée devient grisée, mais **reste dans la liste**, et le bot la saute simplement. C'est le meilleur moyen de « retirer une règle temporairement » : pas besoin de recomposer le pack. Au lancement, la ligne `[ПРАВИЛА] Выключено правил: N, бот их пропускает.` apparaîtra dans le journal.
- :chevron-up: **Flèches «Monter» et «Descendre»** intervertissent la règle avec sa voisine. Elles sont utiles lorsque deux règles d'un même groupe peuvent convenir en même temps et qu'il est important de savoir laquelle sera vérifiée en premier.
- :x: **Croix «Supprimer».** En bas apparaîtra une notification « Règle « … » supprimée » avec le bouton **«Annuler»**. Tant que la notification est à l'écran, la règle peut être rétablie à la même place.
- :trash-2: **«Effacer toutes les règles»** ne supprime que ce qui est **actuellement visible**. Si «Eau» est sélectionné — les règles de l'eau seront supprimées, si «Toutes» est sélectionné — toutes. D'abord, le bot demandera confirmation : «Supprimer toutes les règles ?» et indiquera combien et lesquelles (bouton «Tout supprimer»). Ensuite, il y aura aussi la notification «Règles supprimées : {n}» avec le bouton «Annuler».

Toutes ces actions ne modifient que la page. Elles n'entreront dans les fichiers qu'après avoir cliqué sur «Enregistrer les réglages», et **seuls les éléments ayant subi des modifications** seront enregistrés. Si tu quittes la page sans enregistrer, la fenêtre demandera «Enregistrer les modifications ?».

> [!tip] Si tu hésites à supprimer une règle ou non, il vaut mieux la désactiver avec l'interrupteur. Pour les règles que le bot a retenues lui-même, il y a une autre raison (voir plus bas) : le bot ne touche pas à une règle désactivée et ne la recrée pas, tandis qu'une règle supprimée peut réapparaître.

### Fenêtre «Nouvelle règle» pas à pas

Clique sur «Nouvelle règle» (ou sur le bouton «Condition» du premier onglet, en bas de la fiche de la salle). Une fenêtre s'ouvrira. Si un seul élément est sélectionné, elle le proposera immédiatement. Le crayon sur la ligne ouvre la même fenêtre avec le titre «Modifier la règle».

![Fenêtre «Nouvelle règle» : élément et nom, trois déclencheurs, champs de condition, action et équipe](images/rule_editor.png)

1. **Choisis l'élément dans le champ «Élément de la salle».** La règle ne fonctionnera que là. L'élément détermine quels titans peuvent être choisis : dans la «Terre» uniquement les titans de terre, dans l'«Eau» uniquement ceux d'eau, et dans la «Mixte» n'importe lesquels. Si tu modifies l'élément plus tard — la fenêtre ajustera le choix elle-même.
2. **Donne un nom à la règle (facultatif).** Le champ «Nom de la règle» peut être laissé vide : le nom sera alors composé à partir de la condition, par exemple « Araji : PV sous 50 % ». C'est ce nom que le bot écrira ensuite dans le journal lorsque la règle s'est déclenchée.
3. **Choisis le «Déclencheur»** — ce que le bot doit surveiller : «Par PV», «Par énergie» ou «Par ennemis».
   - « Par PV » et « Par énergie » : choisis **«Titan»** et entre un nombre dans le champ «PV sous, %» (ou «Énergie sous, %») de 0 à 100. Par défaut, les PV sont à 35, l'énergie à 100. Si tu entres autre chose qu'un nombre ou un nombre hors limites, le champ deviendra rouge et « Un nombre de 0 à 100 » apparaîtra en dessous.
   - « Par ennemis » : coche dans la grille «Ennemis dangereux dans la salle» tous ceux qui doivent être **ensemble**. À côté il est écrit « · choisis : {n} ». Si tu n'en as choisi aucun — impossible d'enregistrer.
4. **Choisis l'«Action au déclenchement».** Il y a deux cases à cocher qui s'excluent mutuellement : « S'arrêter et me demander » et «Interdire l'entrée de la salle (Skip)». Si aucune n'est cochée — la règle **placera un pack**.
5. **Exiger le rodage des titans (facultatif).** La règle ne se déclenchera que si les titans choisis (de 1 à 5, de tous éléments) ont déjà livré un combat lors de cette session. Par exemple, le pack demande Sigurd, mais tu ne veux pas le placer tant qu'il n'a pas encore combattu. La croix à côté retire le rodage. Le rodage n'existe que pour les règles qui placent un pack. Après une pause douce et un combat manuel, le bot oublie l'état des titans et le rodage recommence au début.
6. **Choisis l'«Équipe pour cette règle».** Clique sur «Choisir l'équipe» et dans la fenêtre «Compose l'équipe», place **3 à 5 titans** (de la même manière que pour le pack principal). Pour « Te demander » et « Skip », l'équipe n'est pas nécessaire, il y est inscrit «Cette action n'a pas besoin d'équipe».
7. **Clique sur «Enregistrer la règle».** Tant que le bouton est grisé, il est indiqué en bas de la fenêtre ce qui manque : «Choisis une équipe : 3 à 5 titans», «Choisis au moins un ennemi» ou «Corrige le nombre : de 0 à 100». «Annuler» ferme la fenêtre sans modifications.

Une nouvelle règle se place en **première position** de son élément, une règle modifiée reste à sa place (si tu as changé d'élément, elle va en premier dans le nouveau). Elle entrera dans le fichier, comme tout le reste, après avoir cliqué sur «Enregistrer les réglages». Si tu as ouvert la fenêtre avec le bouton «Condition» du premier onglet, une notification « Règle « … » ajoutée dans l'onglet « Règles et interceptions » » apparaîtra après l'enregistrement.

> [!note] Une règle que le bot a retenue lui-même peut être ouverte avec le crayon et modifiée. Tout ce qui n'est pas visible dans la fenêtre (par exemple, la « tolérance de pertes » ou une condition supplémentaire sur les PV) **sera conservé en l'état**. La fenêtre affichera cette condition sur une ligne grise « Autre condition (conservée en l'état) : … ».

### Règles retenues par le bot lui-même

Si «Le bot décide seul» est activé, des règles que tu n'as pas écrites apparaissent dans la liste. Elles sont reconnaissables à leur nom :

- :refresh-cw: **« Auto : Angus + Sylva dans la salle »** — le bot a annulé un mauvais combat après un repli, a rejoué avec un autre pack, et celui-ci a réussi. Le bot a retenu : « contre ces ennemis, mettre ce pack ». Sous le nom il est écrit «Retenue par le bot après un repli» (ou «Ton pack après un repli, retenu par le bot», si c'est toi qui as choisi le pack dans la fenêtre SOS). Si le pack a perdu en fonction d'une condition (par exemple « Araji sous 50 % »), celle-ci est ajoutée à la condition. Une telle règle se place en première position.
- :star: **« Dorée : Angus + Sylva dans la salle »** — « Le pack a souvent battu ces ennemis ». Au lancement, le bot parcourt l'historique et prend le pack qui, contre cette composition d'ennemis, a livré **5 combats et plus** et a gagné **80 % et plus**. Le pack principal, les packs des règles de sauvetage et tes packs de réserve n'entrent pas dans les règles « dorées ».

Dans le fichier, ces règles s'appellent autrement (« Anti-pack contre : … », « Règle dorée contre : … »), et c'est exactement ainsi qu'elles sont écrites dans le journal : `[ОБУЧЕНИЕ] Новое правило '…': пак […]. Сохранено на 1-е место.` La fenêtre les affiche simplement de manière courte et compréhensible. Si tu renommes la règle — tu verras ton propre nom.

Ce qu'il est utile de savoir sur ces règles :

- **Le bot ne crée pas de doublons.** Une règle avec la même condition n'est pas créée une deuxième fois : le pack de l'ancienne est modifié et elle remonte tout en haut.
- **Chaque repli réussi n'est pas forcément retenu.** Si un mauvais combat est survenu uniquement parce qu'un titan y est entré blessé, alors qu'avec 100 % de PV tout se serait bien passé (« les ennemis n'y sont pour rien »), la règle n'est pas créée.
- **Le bot ne touche pas aux règles désactivées :** il ne les active pas et ne les réécrit pas. Il ne retiendra plus ce même pack, et une règle « dorée » désactivée ne reviendra pas.
- **Les règles supprimées peuvent revenir.** La « règle dorée » sera récréée lors du prochain lancement tant qu'il n'existe pas d'autre règle contre ces ennemis. Si cela ne te plaît pas — désactive-la avec l'interrupteur. Le bot récréera la règle « Auto » si un repli se termine à nouveau de la même manière.
- **Tant que la fenêtre est ouverte, le bot peut enregistrer une nouvelle règle dans le fichier.** Quand tu cliqueras sur «Enregistrer les réglages», la fenêtre relira le fichier et placera ces nouvelles règles en haut sans rien perdre. Si tu jettes un coup d'œil à l'onglet sans rien changer — tu verras la liste fraîchement lue sur le disque.

> [!warning] Si le fichier de règles d'un élément est endommagé (par exemple s'il a été modifié à la main avec une erreur d'indentation), la fenêtre écrira, par exemple pour l'eau : « Le fichier de règles est endommagé : bot_data/rules/water.yml — la fenêtre ne modifie pas les règles de cet élément ». Les autres éléments fonctionnent. Pas besoin de modifier le fichier à la main : clique sur «Envoyer le journal à l'auteur» sur l'accueil et explique ce qui s'est passé.

> [!tip] Par quoi commencer ? N'écris rien à l'avance. Joue une vingtaine de salles avec «Le bot décide seul» activé et jette un coup d'œil ici : le bot aura déjà retenu quelques règles. Désactive celles qui ont échoué, monte les bonnes plus haut avec les flèches. Ajoute tes propres règles quand tu vois un problème récurrent : « Araji marche toujours blessé » — règle de sauvetage ; « cette composition d'ennemis tue toujours mon pack principal » — règle contre les ennemis.

> [!done] Tu sais maintenant apprendre au bot les exceptions et tu comprends pourquoi il place précisément ce pack. La suite concerne Telegram et les fenêtres qui t'appellent à l'aide. [Section suivante →](#10)

## Quand le combat s'est mal passé : les fenêtres SOS

Presque toujours, le bot s'en sort seul. Mais parfois, il se heurte à une situation où l'intervention humaine est indispensable : le combat est gagné, mais le prix est trop élevé, ou les règles ne дают aucun pack adapté. Alors le bot **s'arrête et t'appelle** avec une fenêtre au milieu de l'écran. SOS est un signal de détresses, comme pour un navire : « besoin d'aide ». Tant que tu n'as pas répondu, le bot ne clique sur rien et attend (mais pas éternellement, voir ci-dessous).

Il y a trois fenêtres, et chacune correspond à son propre cas :

- :triangle-alert: **« Intervention requise »** — le combat s'est terminé, mais le résultat est mauvais. C'est la fenêtre principale, elle apparaît le plus souvent.
- :users: **« Aucun pack adapté »** — le bot n'a pas encore commencé le combat : les règles ne lui дают aucun pack pour cette salle.
- :check: **« Le pack a réussi »** — tu as choisi toi-même un autre pack, il a gagné, et le bot demande s'il faut le retenir.

![Fenêtre « Intervention requise » : raison, salle, ennemis, ton pack avec barres de PV et trois boutons](images/sos_window.png)

> [!note] Quand la fenêtre apparaît : si « Le bot décide seul » est **désactivé** (par défaut), la fenêtre s'ouvre après **chaque** mauvais combat. S'il est activé, le bot essaie d'abord de s'en sortir sans toi et ne t'appelle que lorsqu'il ne peut pas : le combat était en manuel (Angus), la fenêtre de résultat n'a pas été lue, tu as choisi le pack, dans la salle le bot a déjà fait un repli autant de fois qu'autorisé, ou il n'y a pas de pack de secours. Ce qu'est un « mauvais combat » et comment le configurer se trouve dans les sections « Base et salles » et « Auto-tactique ».

### Fenêtre « Intervention requise »

En haut — en bref : « Le combat s'est mal passé. Que fait-on ? ». Ci-dessous — les faits pour que tu puisses décider sans consulter le journal :

- **Raison.** Ce qui n'a pas plu au bot. Par exemple : « Критический порог! Араджи имеет 12% ХП (порог: 40%) », « Превышена Дельта потерь! Ригель потерял 45% ХП (допуск: 30%) », « ФАТАЛЬНО! Ияри мертв… », « Большие потери пака!… » ou « Не удалось прочитать окно результата: не найдены… ». Les noms des titans sont dans la langue du programme.
- **Salle.** L'élément de la porte et le numéro de la salle : « Огонь · комната 54 ».
- **Ennemis.** Les cases des titans contre lesquels le combat a eu lieu. Si les ennemis ne sont pas reconnus, la ligne n'apparaîtra pas.
- **Ton pack.** Chaque titan avec sa propre barre de santé et la mention « PV avant le combat → PV après » : « 36% → 12% ». Si les PV d'un titan sont inférieurs à son seuil de panique (général ou individuel), la barre et le nombre sont en **rouge**. Si un titan est entré au combat déjà blessé et en est sorti presque sans PV, cela se voit immédiatement.
- **Minuteur.** En bas : « Sans réponse, le bot décidera seul dans 9:41 ». La dernière minute est en jaune, puis « Le bot décide seul… ». Si 0 est défini dans « Auto-tactique », la ligne n'apparaît pas : le bot t'attend toujours.

Boutons (de droite à gauche, le principal est le plus à droite) :

1. **« Annuler le combat »** (bleu). Rejouer ce combat avec un autre pack. La fenêtre se masquera, « Compose l'équipe » s'ouvrira avec le pack actuel ; change les titans et clique sur « Annuler avec ce pack ». La suite est décrite dans la section « Retraite » ci-dessous. Si tu fermes « Compose l'équipe » sans faire de choix, la fenêtre SOS reviendra, rien n'est perdu.
2. **« Ignorer »** (gris). Accepter le combat tel quel : la salle est validée, le bot continue avec les PV restants. Convient quand les pertes te conviennent (par exemple, le titan est déjà entré blessé et dans l'ensemble tout va bien).
3. **« Jouer à la main »** (gris). Le bot ne clique sur rien et tu joues cette salle toi-même dans le jeu. Le bot attend que tu reviennes dans le couloir : le drapeau de la porte doit être visible pendant 2 secondes d'affilée. Si la dernière fenêtre était celle du résultat, la salle est validée ; si tu t'es replié sans vaincre, non. Si tu fermes la fenêtre de résultat sans rejouer, le combat est validé tel quel. Après avoir joué manuellement, le bot oublie les PV des titans et les compositions dans les emplacements (il les relira lui-même sur l'écran de sélection d'équipe) puis continue à jouer seul.

> [!warning] Un combat où l'**ultime manuelle d'Angus** a été utilisée ne peut pas être annulé : sur sa fenêtre de résultat, il n'y a pas de bouton « Rejouer ». Au lieu de « Annuler le combat », la fenêtre affichera un bouton rouge **« Arrêter le bot »**, et il ne restera que « Ignorer » ou « Jouer à la main ».

### Retraite : ce que fait le bot après ton choix

La fenêtre s'est fermée, la commande est envoyée au bot. Ensuite, il fait tout seul, et dans le journal cela se voit par la balise `[ОТКАТ]` :

1. Clique sur **« Rejouer »** sur la fenêtre de résultat et attend le chargement du combat (parfois cela prend 20–30 secondes ou plus, c'est pourquoi il attend jusqu'à une minute).
2. Met le combat **en pause** (une fois) et clique sur **« Se retirer »**.
3. Revient dans le couloir, entre dans la **même salle** et place ton nouveau pack.

Si le combat s'est à nouveau mal passé, la fenêtre reviendra. S'il s'est bien passé, c'est ici qu me apparaît la fenêtre « Le pack a réussi » (voir ci-dessous).

Si la connexion avec le jeu est perdue (l'image de « chargement » ne se termine pas), le bot n'abandonne pas : il attend le jeu jusqu'à 15 minutes et l'écrit dans le journal. Ce n'est que si le repli échoue définitivement que le bot enregistre une capture d'écran dans `bot_data/debug/`, met une pause douce et t'envoie un message sur Telegram. Plus de détails dans la section sur les problèmes.

### Fenêtre « Aucun pack adapté »

Apparaît lorsque le bot a déjà choisi la porte et regardé les ennemis, mais qu'**il n'y a rien à placer**. Cela arrive pour deux raisons, toutes deux liées à tes règles :

- la règle « Me demander » s'est déclenchée (elle est conçue exactement pour cela) ;
- le pack principal de la salle contient un titan interdit par la règle « Skip » (le bot écrit quelque chose comme « ФАТАЛЬНО: Все паки отбракованы… »).

La fenêtre demande : « Les règles ne дают aucun pack pour cette salle. Que fait-on ? » Elle contient les mêmes mentions « Raison », « Salle » et « Ennemis », mais sans barres : le combat n'a pas encore eu lieu. Boutons :

- **« Composer un nouveau pack »** (bleu) — ouvre « Compose l'équipe », le bouton s'y nomme « Appliquer ». Le bot placera les titans choisis et **enregistrera immédiatement le pack avec une règle** « contre ces ennemis » (il n'y a pas de vérification avant l'enregistrement ici, sois attentif).
- **« Jouer à la main »** — tu joues la salle toi-même, le bot attend dans le couloir. La salle est validée si vous avez gagné.
- **« Arrêter le bot »** (rouge) — le bot écrit le bilan de la session et s'éteint.

Il n'y a pas de bouton « Ignorer » ici : il n'y a rien à accepter, le combat n'a pas eu lieu.

### Fenêtre « Le pack a réussi »

Cette fenêtre apparaît lorsqu'un combat a été gagné par un pack que **tu as choisi** (via « Annuler le combat » ou « Essayer un autre », dans la fenêtre ou sur Telegram). Si le pack de secours a été choisi par le bot lui-même et qu'il a réussi, le bot le retiendra lui-même sans rien demander.

À l'intérieur — la salle, les ennemis (de la dernière fenêtre SOS, si elle date de moins de 15 minutes) et ton pack avec ses PV après le combat. Question : « Le pack testé a gagné. L'enregistrer comme règle contre ces ennemis ? » Boutons :

- **« Enregistrer le pack »** (vert) — le bot retiendra la règle « contre ces ennemis » avec ce pack. Dans la liste des règles, elle apparaîtra sous la forme « Auto : … » ou « Ton pack après un repli, retenu par le bot ».
- **« Essayer un autre »** — à nouveau « Compose l'équipe » et retraite : le bot rejouera le combat gagné avec un autre pack.

Si tu ne réponds pas, après le délai du minuteur (légende « Sans réponse, le bot enregistrera le pack lui-même dans… »), le bot enregistrera le pack lui-même, comme si tu avais cliqué sur « Enregistrer le pack ».

### La croix de la fenêtre et « Arrêter le bot ? »

Les fenêtres n'ont pas de « fermer simplement » : si tu fermes la fenêtre, le bot continuera d'attendre une réponse. C'est pourquoi la croix demande : **« Arrêter le bot ? »**. Si tu réponds « Arrêter le bot », le bot terminera, écrira le bilan et l'enverra sur Telegram. S'il ne répond pas dans les 10 secondes, le programme l'arrêtera lui-même. Sur la fenêtre « Le pack a réussi », la question est différente : l'arrêt y est identique à « STOP F10 », **le bilan de session n'ira pas sur Telegram**. Si tu as changé d'avis, clique sur « Annuler », la fenêtre restera.

### Que se passe-t-il si tu ne réponds pas

Chaque fois que tu ne réponds pas dans le délai défini dans « Auto-tactique » (« Délai de la fenêtre SOS sans réponse, min » : par défaut 10, jusqu'à 60, 0 — toujours attendre), le bot écrit `[ТАКТИКА] Ответа нет 10 мин. Решаю сам.`, la fenêtre se ferme et tu reçois un message sur Telegram indiquant que le bot a décidé seul. Cela fonctionne aussi quand « Le bot décide seul » est désactivé. La décision dépend de la fenêtre :

- **« Intervention requise » :** s'il y a un pack de secours et que le combat peut être annulé (pas Angus, les tentatives dans la salle ne sont pas épuisées) — **retraite** et pack de secours ; sinon tous les titans sont vivants — le combat est **accepté** (« Ignorer ») ; sinon (quelqu'un est mort ou non trouvé dans la fenêtre) — **pause douce**.
- **« Aucun pack adapté » :** un pack de secours sans blessés ni titans interdits convient — le bot le place **et ne retient pas la règle** ; il n'y en a pas — **pause douce**.
- **« Le pack a réussi » :** le pack est enregistré.

La pause douce est comme le bouton « Pause F9 » : le bot attend dans le couloir jusqu'à ce que tu cliques sur « Continuer ».

> [!tip] Tu as répondu à l'instant même où le bot a déjà décidé seul ? Rien de grave : le bot ignorera l'ancienne réponse et écrira `[ЛОГИКА] Пропускаю ответ ...: он пришёл на прошлое окно.`

### Répondre depuis Telegram

Si Telegram est configuré, **la même question** arrive aussi dans le tchat : capture d'écran du jeu, légende (salle, ennemis, raison, pack avec PV) et boutons. Tu peux répondre où cela t'arrange le plus : si tu réponds dans le tchat, la fenêtre sur l'ordinateur se fermera toute seule, et inversement.

- **« Annuler (Former un pack) »** (vert) — le bot demandera d'écrire dans le tchat les noms de **3–5 titans** séparés par des virgules ou des espaces, montrera ceux qu'il a reconnus et demandera « Tout est correct ? » (« Confirmer le pack » / « Écrire un autre »). Pour le combat manuel d'Angus et pour « Aucun pack adapté », un bouton rouge « Arrêter le bot » apparaît à la place.
- **« Jouer à la main »** et **« Ignorer (Continuer) »** — identique à la fenêtre. Pour « Aucun pack adapté », il n'y a pas de « Continuer ».
- « Le pack a réussi » n'arrive sur Telegram que si tu as également envoyé le pack depuis là : « Confirmer et Enregistrer » ou « Annuler et Réessayer ».

Si Internet est coupé, le message partira plus tard (le bot réessaie), tandis que la fenêtre elle-même reste sur l'ordinateur. La configuration de Telegram est dans la section qui lui est consacrée.

### Mini-barre et fenêtres SOS

Si la fenêtre du programme est réduite dans la mini-barre, la fenêtre SOS apparaîtra **au centre du jeu**. La mini-barre est rouge pendant ce temps, et son bouton « SOS » ramène la fenêtre perdue au-dessus du jeu.

> [!tip] Comment choisir ? Regarde « Ton pack ». Un titan est entré blessé et a perdu de la vie, les autres vont bien — « Ignorer » suffit souvent. Tu connais les ennemis et ils sont nettement plus forts — « Annuler le combat » avec un autre pack. Rien n'est clair — « Jouer à la main ». Le repli demande du temps (le combat doit être rechargé, cela peut prendre 20–30 secondes ou plus), alors que « Ignorer » ne coûte rien.

> [!done] Tu sais maintenant ce que signifie chaque fenêtre SOS, ce que fait chaque bouton et ce que le bot fera sans toi. La suite — comment le bot décide seul pendant que tu n'es pas là. [Section suivante →](#11)

## Comment le bot décide seul

Dans la section sur les fenêtres SOS, tu as vu que le bot t'appelle après un mauvais combat. Mais il ne t'appelle pas toujours : si tu actives «Le bot décide seul» (onglet «Base et salles», section 7), le bot **essaie d'abord de s'en sortir sans toi** et ne demande de l'aide que lorsque cela a échoué. Ici, nous allons voir comment il réfléchit. Il n'y aura pas de formules : seulement les questions que le bot se pose et des exemples.

Imagine un coéquipier expérimenté assis à côté de toi devant le téléphone. Le combat s'est mal passé et tu es parti chercher du thé. Il ne va pas rester assis à attendre. Il va se rappeler ce qui a déjà marché contre ces ennemis, rejouer le combat avec une autre composition et noter ce qui a fonctionné. C'est à peu près ainsi que se comporte le bot. Seulement, il a des règles pour éviter de faire des bêtises.

> [!note] «Le bot décide seul» est **désactivé** par défaut, et tout ce dont il sera question ci-dessous ne se produit pas : après chaque mauvais combat, le bot ouvre simplement la fenêtre SOS. Si tu actives l'interrupteur et cliques sur «Enregistrer les réglages», cela prendra effet dès le prochain «Lancer le farm». Ce que l'on peut ajuster a été expliqué dans la section 8 («Auto-tactique et PV»), et ici il s'agit de **ce que le bot fait de ces chiffres**.

### Mauvais combat : ce que fait le bot dans l'ordre

1. **Remarque que le combat est mauvais.** Quelqu'un est mort ou sous le seuil de panique, a perdu plus que la tolérance ou trois titans se sont effondrés d'un coup (sections 7 et 8). Dans le journal, il y a la ligne `[ТАКТИКА] Плохой бой: ...` avec la raison.
2. **Vérifie s'il peut annuler lui-même.** Impossible dans quatre cas : le combat était manuel (ultime d'Angus, il n'y a pas de bouton « Réessayer » sur l'écran de résultat), l'écran de résultat n'a pas été lu, **tu** as placé l'équipe (la décision t'appartient alors) ou le bot a déjà épuisé ses tentatives dans cette salle. Si c'est impossible, la fenêtre SOS s'ouvre, et dans le journal s'affiche `[ТАКТИКА] Сам не откатываю: ... Спрашиваю вас.` avec la raison.
3. **Cherche une équipe de réserve.** Comment — dans la section suivante. S'il n'y en a pas de adaptée — à nouveau la fenêtre SOS.
4. **Annule et rejoue.** Les mêmes étapes `[ОТКАТ]` qu'après ton choix (« Réessayer », pause, « Battre en retraite »), et la même salle reçoit l'équipe de réserve. Dans le journal : `[ТАКТИКА] Откатываю бой сам и переиграю паком ... (взят: ...)`.
5. **Regarde le résultat.** L'équipe de réserve a réussi — le bot continue et, en règle générale, mémorise l'équipe (voir ci-dessous). Le combat est à nouveau mauvais — deuxième tentative, et ainsi de suite jusqu'à épuisement des tentatives («Équipes de secours à essayer par salle», par défaut 2, pas plus de 3). Ensuite, il t'appelle.

> [!tip] Le bot annule à chaque fois le combat en entier, au lieu de « corriger en cours de route ». L'annulation prend du temps (il faut recharger le combat, cela prend parfois 20 à 30 secondes ou plus), c'est pourquoi il n'aime pas les tentatives inutiles : vois ci-dessous comment il choisit l'équipe.

### Où le bot prend-il l'équipe de réserve ?

Il parcourt la liste de haut en bas et prend la **première adaptée** :

1. **Tes «Équipes de réserve»** — onglet «Base et salles», carte de la salle. Prises dans l'ordre où tu les as disposées. Dans le journal, la source est appelée « ваш список запасных паков ».
2. **Équipes des règles de cet élément** — dans le journal « правила стихии ». À l'intérieur, leur propre ordre : d'abord les règles « contre ces ennemis », puis les équipes qui ont déjà vaincu ces mêmes ennemis (les meilleures en PV restants en premier), puis les autres « anti-équipes », puis tout le reste, y compris l'équipe principale de la salle.
3. **Historique des combats** — dans le journal « история боёв ». C'est la dernière file d'attente, et seules les équipes ayant déjà vaincu ces ennemis sont prises. Le bot se souvient des combats des 20 derniers lancements.

Ce que le bot **ne placera jamais** en réserve :

- une équipe qui a déjà perdu dans cette salle (pour ne pas répéter l'erreur) ;
- une équipe qui « perd contre ces ennemis » : la dernière fois contre eux, le combat a été annulé par la faute des ennemis, et l'équipe n'a pas plus de victoires que de défaites. Un seul échec **ne gâche pas une bonne équipe** : si elle a gagné contre ces ennemis cinq fois et perdu une fois, le bot la prendra encore ;
- une équipe avec un titan interdit par la règle « Skip » ;
- une équipe avec un titan dont les PV sont déjà **sous le seuil de panique** : le bot ne l'enverra pas au combat vers une mort certaine ;
- depuis l'historique — une équipe contenant un titan que tu n'as indiqué nulle part (ni dans les équipes, ni dans les règles). Les équipes de règles supprimées depuis longtemps restent dans l'historique, et le bot ne les ressuscite pas.

Il existe aussi des équipes « dangereuses » : celles où le titan blessé, à en juger par les combats passés, ne survivra pas jusqu'à la fin du combat. Le bot les prend **en tout dernier recours**, seulement s'il n'y a rien de mieux. Comment il détermine cela — dans la partie « Titan blessé » ci-dessous.

La raison pour laquelle le bot n'a pas pris telle ou telle équipe est visible dans le journal : `[ТАКТИКА] Не беру запасной пак ...` et la raison. Si les équipes de réserve sont épuisées et que le combat est toujours mauvais — ce n'est pas une panne, mais un honnête « je ne sais plus quoi placer ».

### Mémoriser ou non : la règle « Auto : … »

L'équipe de réserve a réussi. Le bot enregistre cela dans la règle « contre ces ennemis — place cette équipe », et la prochaine fois qu'il rencontrera la même composition, il la placera immédiatement. Dans la liste, c'est la règle « Auto : {names} dans la salle », elle se place en première position (section 9). Dans le journal : `[ТАКТИКА] Запасной пак ... справился. Запоминаю его против этих врагов.`

Mais il arrive que **l'on ne doive pas mémoriser**. Exemple : Araji est entré au combat avec 36 % de santé et a chuté à 5 %. L'équipe principale n'y est pour rien : si Araji avait été en bonne santé, le combat se serait bien passé. Si le bot enregistrait la règle « contre ces ennemis place la réserve », il commencerait à placer l'équipe de réserve là où l'équipe principale réussit très bien, et gaspillerait tes forces pour rien. C'est pourquoi le bot vérifie : **« est-ce qu'avec 100 % de PV pour tous, le combat aurait été mauvais ? »** Non — cela signifie que les ennemis n'y sont pour rien, l'aide était ponctuelle, la règle n'est pas créée.

Dans le journal, cela se voit immédiatement : `[ТАКТИКА] Враги ни при чём: в бой вошли раненые ...` puis `Правило не запоминаю: это была разовая помощь раненым титанам`.

Il sera également impossible de mémoriser dans trois autres cas :

- le bot n'a pas reconnu les ennemis (`[ОБУЧЕНИЕ] Враги не распознаны — правило не сохраняю`) : une règle « sans ennemis » se déclencherait dans n'importe quelle salle ;
- tu as désactivé la règle avec la même équipe via l'interrupteur : le bot ne touche pas à ce qui est désactivé ;
- tu as choisi l'équipe toi-même : c'est alors ta fenêtre « Le pack a réussi » qui décide (section 10).

### Titan blessé : une aide à l'avance, pas après le combat

Le plus précieux dans ce que sait faire le bot, c'est **d'éviter un mauvais combat**, au lieu de réparer les dégâts après coup. Tant qu'il est sur l'écran de sélection de l'équipe, il regarde la santé des titans et l'historique : « comment se sont terminés les combats avec cette équipe dans cette salle ? » Pour cela, le bot conserve combien de PV le titan **perd** généralement au combat avec cette équipe (moyenne des cinq derniers combats, il en faut au moins deux). Si pour le titan blessé à l'entrée, les PV moins la perte habituelle **tombent sous le seuil de panique**, le bot ne prendra pas de risque et placera immédiatement une équipe de réserve, avant le combat.

Exemple. Araji avec 36 % de PV va dans l'élément Feu. Lors des derniers combats ici, il perdait habituellement environ 29 %. Résultat : 36 − 29 = 7 %, et le seuil de panique est de 40. Le combat se terminera presque à coup sûr mal, et le bot place une équipe de réserve, par exemple avec Moloch, **immédiatement**. C'est une aide ponctuelle, la règle n'est pas mémorisée.

Deux subtilités pour que le bot ne paraisse pas bizarre :

- **L'énergie est aussi importante.** Si le titan a actuellement à peu près autant d'énergie que lors des combats précédents (différence pas plus de 25 %), le bot prend précisément ces combats pour la prévision. Araji avec une bonne énergie dans le feu perd peu, avec une énergie vide beaucoup, et la prévision en tient compte.
- **Un seul combat n'est pas une statistique.** Moins de deux combats, le bot ne croit pas la prévision et ne change rien.

Le bot ne remplace pas à l'avance les équipes des règles de sauvetage (« si Araji est sous 50 % — place Sigurd », section 9) : tu les as placées précisément pour le blessé, et ton intention est plus importante que sa prévision.

### Porte selon la santé

Si le bot décide seul et que **plusieurs portes autorisées** sont visibles dans le couloir, il ne choisit pas simplement dans l'ordre (section 8, « Priorité des portes »), mais en gardant un œil sur les blessés :

1. Il va d'abord vers la porte **derrière laquelle le blessé sera soigné** : ta règle de sauvetage se déclenchera ou le bot assemblera lui-même une équipe de soin.
2. La porte derrière laquelle le blessé risque des ennuis, à en juger par les combats passés, est **ignorée** par le bot s'il y en a une autre.
3. Sinon, tout se fait comme d'habitude, dans l'ordre.

Cela se voit à la ligne `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...`. Le bot n'ouvrira jamais une porte interdite par la règle « Skip ». Le bot ne voit pas encore les ennemis derrière la porte, il s'appuie donc ici sur l'équipe de base de la salle.

### Équipe de soin dans la salle « Mixte »

Si le blessé peut être soigné et que ta règle de soin ne s'est pas déclenchée, le bot **assemble lui-même une équipe de soin** : il place dans la salle « Mixte » le blessé et, si nécessaire, un soigneur en bonne santé et chargé. Ils soignent un par un, les principaux avant les réserves, et ceux qui sont sous le seuil de panique ne sont pas soignés du tout. Tous les détails (seuil « Soigner le titan si les PV sont sous, % », « Qui retirer de l'équipe pour le blessé », ce même Sigurd pour Rigel) — dans la section 8. Une seule chose est importante ici : il s'agit d'une **aide ponctuelle**, tout comme l'équipe de réserve issue de la prévision. Aucune règle n'est créée après cela, et au bilan, elle est comptabilisée séparément (« équipes de soin (le bot a assemblé seul) »).

### « Règles dorées » : le bot apprend de tout l'historique

Toutes ces décisions, le bot les prend en cours de jeu. Quant aux « règles dorées », il les établit **une seule fois, lors du lancement du farm**. Le bot parcourt l'historique des combats et cherche une équipe qui, contre la même composition d'ennemis, a effectué **5 combats ou plus et gagné 80 % ou plus**. Une telle équipe est enregistrée par la règle « Dorée : {names} dans la salle » (section 9). Dans le journal : `[ОБУЧЕНИЕ] ...: 'Золотое правило против: ...' — пак ... Сохранено на 1-е место.`

Ne deviendra pas dorée :

- l'équipe principale de la salle, les équipes des règles de sauvetage et tes « Équipes de réserve » (elles sont là pour aider, pas pour chaque combat) ;
- les équipes de soin que le bot a assemblées lui-même : elles ne servent que tant que le titan est blessé ;
- une équipe avec un titan qui n'existe pas dans tes équipes et règles ;
- une équipe contre des ennemis pour lesquels une règle existe déjà (la tienne, « Auto » ou désactivée).

Il n'y a pas de règles dorées tant que « Le bot décide seul » est désactivé. Une règle malencontreuse est apparue ? **Désactive-la avec l'interrupteur**, ne la supprime pas : ce qui est supprimé reviendra au prochain lancement, ce qui est désactivé ne sera pas touché par le bot.

### Si tu n'as pas répondu à la fenêtre SOS

Ce n'est plus « le bot décide seul », mais « le bot décide à ta place » (section 10, « Ce qui se passe si l'on ne répond pas »). Cela fonctionne aussi lorsque « Le bot décide seul » est désactivé : en cas de dépassement du délai (« Délai de la fenêtre SOS sans réponse, min »), le bot annulera le combat avec une équipe de réserve, l'acceptera ou passera en pause douce. À chaque fois, il écrit `[ТАКТИКА] Ответа нет N мин. Решаю сам.`, ferme la fenêtre et envoie un message sur Telegram.

### Comment comprendre ce que le bot a fait sans toi

À la fin de la session, dans le bloc « Bilan de session » (bouton « Détails ») et dans la ligne `[ИТОГ]`, il y a des compteurs :

- **« annulations »** : combien de combats ont été rejoués au total ;
- **« dont sans vous »** : combien de ces annulations le bot a faites lui-même, sans demander, aussi bien par prévision que par dépassement de délai ;
- **« équipes de soin (le bot a assemblé seul) »** : combien de fois il a soigné un blessé avec une équipe de soin.

Le même bilan arrivera sur Telegram : « Annulations : 6 (bot seul : 5) ». Si « sans vous » représente presque tout, le bot s'en sort bien. Si ce nombre augmente et que les « Règles dorées » n'apparaissent pas, cela signifie que les mêmes ennemis détruisent sans cesse l'équipe principale. Jette un œil à l'onglet « Règles et interceptions » pour voir quelles règles il a mémorisées, et demande-toi s'il n'est pas temps de changer l'équipe principale.

> [!warning] Le bot décide en fonction de **l'historique** et de la prévision, il ne voit pas le combat à l'avance. Il peut se tromper : les premiers jours, quand il y a peu d'historique, l'équipe de réserve est choisie au hasard. Ne t'inquiète pas si lors des premières dizaines de salles, « Le bot décide seul » annule plus souvent que tu ne le souhaiterais. Plus il y a de combats dans l'historique, plus le choix est précis.

> [!tip] Par quoi commencer ? Définis au moins une ou deux **« Équipes de réserve »** dans chaque salle (section 7) : le bot ne cherchera alors pas à l'aveugle. Active « Le bot décide seul » et pendant deux jours, observe simplement les lignes `[ТАКТИКА]` et le « Bilan de session ». Si ce que fait le bot ne te plaît pas, désactive l'interrupteur et tout reviendra aux fenêtres SOS.

> [!done] Tu comprends désormais quand et comment le bot s'en sort sans toi, ce qu'il mémorise et quand il appelle à l'aide. La suite concerne Telegram : comment recevoir des messages lorsque tu n'es pas devant l'ordinateur. [Section suivante →](#12)

## Telegram

Le bot peut t'écrire sur Telegram pendant que tu n'es pas devant l'ordinateur : tu es allé à la cuisine, tu es parti dormir, tu es parti au travail. Si le combat a besoin de ton aide, une capture d'écran et des boutons arriveront dans le chat. Tu appuies sur un bouton sur ton téléphone — le bot fait ce que tu as dit. Si tout se passe bien, le bot reste silencieux : les messages n'arrivent **qu'en cas de problème** et **une seule fois à la fin de la session**.

Ce qu'il te faut : l'application Telegram et cinq minutes. La configuration ne se fait qu'une seule fois.

> [!note] Telegram — facultatif. Sans lui, le bot fonctionne de la même manière, c'est juste que tu ne verras les fenêtres SOS que sur l'écran de l'ordinateur, et qu'il n'y aura pas de bilan de session. Mais si tu prévois de laisser le bot tourner la nuit, configure-le : ainsi tu seras informé d'un problème immédiatement, et non au réveil.

### Ce qu'il faut préparer

Tu as besoin de deux choses, toutes deux s'obtiennent dans Telegram même :

- :send: **Jeton du bot** (la clé par laquelle le programme se connecte à ton bot). C'est une longue chaîne de chiffres et de lettres, par exemple `123456789:AAH…`. Le jeton est fourni par un bot spécial, **@BotFather**.
- :user: **Chat ID** (numéro du chat). C'est le numéro grâce auquel Telegram comprend à qui délivrer le message : à toi, et non à quelqu'un d'autre.

> [!warning] Le jeton est comme le mot de passe de ton bot. Ne le montre à personne, ne l'envoie pas dans des captures d'écran ni par e-mail (même pas à l'auteur du programme). Prends la capture d'écran de la fenêtre «Réglages Telegram» pendant que le jeton est masqué par des points.

### Étape par étape

1. **Crée ton bot.** Dans Telegram, cherche **@BotFather** (le vrai a une coche bleue à côté) et appuie sur «Démarrer». Écris-lui `/newbot`, invente un nom (n'importe lequel, toi seul le verras) et un identifiant se terminant par `bot`, par exemple `moi_titan_bot`. En réponse, BotFather t'enverra un message avec le jeton : copie-le.
2. **Obtiens ton Chat ID.** Cherche le bot **@getmyid_bot**, appuie sur «Démarrer» — il répondra avec la ligne `Your user ID` et un numéro. C'est le Chat ID, copie ce numéro. Si ce bot ne répond pas, il y a un moyen alternatif : écris n'importe quel mot à **ton** bot créé à l'étape 1, ouvre dans ton navigateur l'adresse `https://api.telegram.org/bot<твой токен>/getUpdates` (remplace `<твой токен>` par le jeton) et cherche dans la réponse `"chat":{"id":` — le numéro juste après est le Chat ID.
3. **Appuie sur «Démarrer» auprès de ton bot.** Cherche le bot que tu as créé à l'étape 1 et appuie sur «Démarrer» (ou écris-lui `/start`). Sans cela, Telegram **n'autorisera pas** le bot à t'écrire en premier. C'est la cause la plus fréquente de non-réception des messages.
4. **Ouvre la fenêtre dans le programme.** Appuie sur le point Telegram sur la barre de gauche ou sur le bouton **«Configurer Telegram»** dans l'onglet «Base et salles» (section 7). La fenêtre «Réglages Telegram» s'ouvrira.
5. **Remplis-la.** Active l'interrupteur «Envoyer des messages sur Telegram». Dans le champ «Jeton du bot (de @BotFather)», colle le jeton, dans le champ «ID du chat», colle le numéro. Le plus pratique est le bouton **«Coller»** à côté du champ : il prend ce que tu as copié. Le jeton est masqué par des points ; l'icône de l'œil l'affiche pour vérifier s'il a été collé correctement. Un clic droit de la souris sur le champ propose aussi «Coller».
6. **Teste la connexion.** Appuie sur **«Tester Telegram»**. Après quelques secondes, un texte vert «Message envoyé : vérifiez Telegram» apparaîtra à droite, et dans le chat avec ton bot — le message «Test de connexion : tout fonctionne». Si tu l'as reçu, tout est prêt.
7. **Enregistre.** Appuie sur **«Appliquer»**, puis en bas de la page sur **«Enregistrer les réglages»**.

![Fenêtre «Réglages Telegram» : interrupteur, champs du jeton et de l'ID du chat, boutons «Coller» et «Tester Telegram»](images/telegram_window.png)

> [!warning] «Appliquer» ne fait que transférer les valeurs sur la page du «Мастера правил», elles **ne sont pas enregistrées** dans le fichier. Tant que tu n'as pas appuyé sur «Enregistrer les réglages», le message «Modifications non enregistrées» reste affiché en bas, et le bot ne sait rien sur Telegram. Si tu quittes la page sans enregistrer, le programme demandera «Enregistrer les modifications ?».

> [!tip] «Tester Telegram» teste ce qui est actuellement écrit dans la fenêtre, même si tu n'as encore rien enregistré. Par conséquent, teste **avant** d'«Appliquer» : tu trouves une erreur — tu la corriges — tu testes à nouveau. Le test s'effectue en arrière-plan, la fenêtre ne gèle pas et tu n'auras pas à attendre une réponse plus de 20 secondes.

### Si le test a échoué

Sous le bouton, une ligne rouge «Не ушло: …» apparaîtra avec la raison. Les plus fréquentes :

- **«Remplissez le jeton et l'ID du chat»** — l'un des champs est vide.
- `Unauthorized` — jeton incorrect : un caractère a été perdu, un espace en trop s'est glissé ou il n'a pas été copié entièrement. Colle-le à nouveau avec le bouton «Coller».
- `chat not found` ou `Forbidden` — Chat ID incorrect ou tu n'as pas appuyé sur «Démarrer» auprès de **ton** bot (étape 3). Vérifie les deux points.
- **«сбой связи с Telegram»** — pas d'Internet ou Telegram ne s'ouvre pas depuis cet ordinateur. Vérifie que Telegram (ou le site telegram.org) fonctionne sur ce même PC.

Si après correction le message n'arrive toujours pas, crée un nouveau bot auprès de @BotFather (étape 1) et recommence au début : c'est plus rapide que de chercher une coquille.

### Comment savoir si Telegram est activé

Sur la barre de gauche, le bouton Telegram comporte un point : en survolant la souris, l'infobulle affichera **«Telegram : activé»** ou **«Telegram : non configuré»**. Activé signifie que l'interrupteur est positionné et que les deux champs sont remplis. Ce n'est **pas un test de connexion** : seul le bouton «Tester Telegram» indiquera si le jeton est valide. Il en va de même sur l'onglet «Base et salles» : à côté du bouton «Configurer Telegram», un texte vert indique «Notifications SOS activées» ou un texte gris «Telegram non configuré». Le point se met à jour automatiquement quelques secondes après l'enregistrement.

### Quels messages sont envoyés

La langue des messages est la même que celle choisie dans la fenêtre du programme.

- :swords: **Fenêtre SOS** — titre «Votre aide est nécessaire» (ou «Aucun pack adapté»), capture d'écran du jeu et légende : salle, ennemis (qui étaient visés), raison, ton pack avec les barres de PV et d'énergie. Des boutons sont en bas. C'est la même question que dans la fenêtre sur l'ordinateur (section 10).
- :triangle-alert: **Alertes** — message court sans boutons indiquant ce qui s'est passé et ce qu'il faut faire. Les voici : «L'annulation du combat a échoué» (le bot est en pause douce, regarde l'écran du téléphone), «Le bot semble bloqué» (5 minutes sans salle) ainsi qu'un message similaire lorsque le combat ne peut pas commencer (très probablement pas de connexion au serveur du jeu), «L'écran du PC est verrouillé» (le bot ne voit plus le jeu depuis plus d'une minute ; déverrouille le PC et il continuera seul) et «Pas de réponse — le bot a décidé seul».
- :chart-no-axes-column: **Bilan de session** — quand le bot s'est arrêté : temps écoulé, nombre de salles, d'étages et de titanite, présence d'annulations et de fenêtres SOS («par le bot : {n}» — ce sont les annulations qu'il a effectuées sans toi), les salles les plus longues. Si le bot s'est arrêté sur une erreur, le titre contiendra «Le bot s'est arrêté sur une erreur» ainsi que la raison.

Le bilan arrive à chaque arrêt : objectif atteint, pression sur Ctrl+Q, Ctrl+Shift+Q, arrêt du bot sur une erreur. Il **n'arrive pas** après «СТОП F10» ni après «Arrêter et fermer» (section 6), car ils arrêtent le bot instantanément.

### Boutons sous le message SOS

Appuie dessus dans Telegram de la même manière que dans la fenêtre sur l'ordinateur :

- **«Annuler (Former un pack)»** (vert). Le bot enverra : «Напишите имена 3-5 титанов в чат». Écris-les dans le chat séparés par des virgules ou des espaces, par exemple `гиперион, сигурд, нова` ou sous forme courte par leurs trois premières lettres : `гип сиг нов`. Le bot répondra en indiquant qui il a reconnu et demandera «Все верно?» : **«Confirmer le pack»** lancera l'annulation, **«Écrire un autre»** permettra de saisir à nouveau. S'il ne trouve pas 3 à 5 titans, le bot dira combien il en a reconnu et demandera d'écrire à nouveau.
- **«Jouer à la main»** (bleu). Le bot n'appuie sur rien et attend que tu finisses toi-même la salle.
- **«Ignorer (Continuer)»** (gris). Accepter le combat tel quel et continuer.
- **«Arrêter le bot»** (rouge). Elle est affichée au lieu de «Oткатить» lorsque le combat s'est déroulé manuellement (ultime d'Angus) ou qu'aucun pack adapté n'est disponible. La fenêtre «Aucun pack adapté» ne possède pas de bouton «Continuer».

Lorsque le pack que tu as choisi a réussi, la question «Le pack a réussi» arrive sur Telegram avec deux boutons : **«Confirmer et Enregistrer»** (mémoriser le pack par une règle) et **«Annuler et Réessayer»** (en écrire un autre). Elle n'est envoyée dans le chat que si tu as également envoyé le pack depuis Telegram.

Après avoir appuyé, un seul bouton vert «Выбрано: …» reste sous le message, les autres disparaissent. Tu ne peux répondre qu'**une seule fois** : le bot n'écoute pas les clics sur un ancien message. Si tu as répondu dans le chat, la fenêtre sur l'ordinateur se fermera toute seule ; si tu as répondu sur l'ordinateur, le bot cessera d'attendre la réponse depuis Telegram.

> [!tip] Le bot a décidé seul pendant que tu cherchais ton téléphone ? Pas de souci. Un message «Pas de réponse — le bot a décidé seul» arrivera, et les boutons de l'ancienne question ne feront plus rien. Le temps d'attente du bot est défini dans «Авто-тактике» (section 8, «Délai de la fenêtre SOS sans réponse, min»).

### Si la connexion Internet est coupée

Le bot ne s'arrête pas et n'attend pas Telegram : le message part en arrière-plan. Si cela échoue en raison de la connexion, il réessaye après **30 secondes, 1, 2, 5 et 10 minutes** (environ 18 minutes), et le journal affiche les lignes `Сообщение в Telegram не ушло (...). Пробую снова через N с.` et à la fin `Сообщение в Telegram: отправлено с N-й попытки`. Il en va de même pour la fenêtre SOS : elle reste sur l'écran de l'ordinateur et la question sera envoyée dans Telegram lorsque la connexion sera rétablie. Le bot répète le bilan de session de façon plus courte (après 10 et 30 secondes), car il s'éteint ensuite. Le bot ne répète pas les erreurs de Telegram lui-même (jeton incorrect) : elles doivent être corrigées dans les réglages.

> [!note] Le bot n'accepte pas de commandes de ta part «à tout moment» (arrêter, mettre en pause depuis le chat). Telegram ne répond qu'aux questions que le bot a lui-même posées. Il est impossible d'arrêter le bot depuis le chat, à l'exception du bouton «Arrêter le bot» sous le message SOS.

> [!done] Telegram est configuré, et désormais le bot pourra t'appeler où que tu sois. Ensuite — les statistiques : combien de salles, d'étages et de titanite ont été accumulés par jour. [Section suivante →](#13)

## Statistiques

La page «Statistiques» répond à la question «combien ai-je joué ?» : combien de titanite, de salles, d'étages et de potion de titans ont été accumulés sur une semaine, un mois et tout le temps. Elle s'ouvre avec le bouton **«Statistiques»** sur la barre de gauche, et «Statistiques d'activité» est écrit en haut.

Le bot **calcule lui-même** ces chiffres au lieu de les lire sur l'écran du jeu. Il a réussi une salle — il a enregistré : **6 titanite et 25 potions**, et si la fenêtre de résultat affichait l'icône «x2» — **12 titanite et 50 potions**. Il a reçu une récompense au point de sauvegarde — il a enregistré un étage. Une salle que tu as jouée à la main et que le bot a comptabilisée (section 10) est également enregistrée. Les bilans se trouvent dans le fichier `bot_data/stats.json` et sont conservés «par jours de jeu».

> [!note] Le **jour de jeu** ne commence pas à minuit, mais à l'heure de réinitialisation que tu as définie dans le «Мастере правил» (par défaut 5:00, section 7). Par conséquent, tout ce que le bot a accumulé à 02:30 du matin est enregistré pour le jour **d'hier** : dans le jeu, la journée d'hier est encore en cours à ce moment-là. Si «Titanite (aujourd'hui)» est égal à zéro le matin alors que tu as joué la nuit, c'est tout à fait normal.

### Ce qui se trouve sur la page

En haut à gauche se trouve une explication, à droite le choix de la **«Période»**, sous lesquels se trouvent cinq tuiles, un graphique et en bas la **«Correction manuelle»**.

- :calendar: **Période** — «7 jours», «14 jours», «30 jours» ou «Tout le temps». L'élément sélectionné est surligné en bleu. Lors de la première ouverture, «14 jours» est sélectionné.
- :gem: **«Titanite»** — total pour la période.
- :calendar: **«Titanite (aujourd'hui)»** — uniquement pour le jour de jeu actuel. Ne dépend pas de la période.
- :flask-conical: **«Potion de titans»**, :door-open: **«Salles»** et :layers: **«Étages»** — totaux pour la période.

Les nombres jusqu'à 100 000 sont écrits en entier dans la tuile (`98 540`), et les plus longs sont abrégés : `105.5K` correspond à cent cinq mille cinq cents, `1.24M` à un million deux cent quarante mille. Le nombre complet apparaît lorsque tu survoles la tuile avec la souris. «Tout le temps» extrait les compteurs généraux du fichier et non la somme des barres, ainsi les tuiles correspondent à l'historique même si les barres sont nombreuses.

> [!tip] La page lit les chiffres **à chaque ouverture**, et non en cours de jeu. Le bot fonctionne et les nombres ne changent pas ? Va sur une autre page puis reviens.

![Page «Statistiques» : tuiles, graphique par jour et barre sélectionnée avec étiquette](images/stats_page.png)

### Graphique : barres et clics

Sous le titre «Activité de titanite» se trouve l'indication sur le regroupement des barres : «par jour», «par semaine» ou «par mois». Il n'y a pas plus de quinze barres pour éviter que le graphique ne devienne illisible :

- **7 jours et 14 jours** — une journée par barre.
- **30 jours** — une semaine par barre (du lundi au dimanche ; les semaines d'extrémité sont incomplètes — elles ne contiennent que les jours inclus dans la période).
- **«Tout le temps»** — par jour tant que les données couvrent moins de deux semaines ; puis par semaine, et lorsque le nombre de semaines dépasse quinze — par mois.

À gauche se trouve une échelle avec un quadrillage pointillé, les nombres sur l'échelle sont courts (`3.6K`, `140K`). Si les légendes sous les barres ne rentrent pas, elles sont affichées une sur deux ; la dernière (celle d'aujourd'hui) est toujours visible. Une journée sans jeu est un espace vide, sans barre. Pour une période sans données, le graphique affichera «Aucune donnée pour cette période».

1. **Survole une barre avec la souris.** Le nombre exact de titanite apparaîtra au-dessus. C'est juste une infobulle, rien ne change.
2. **Clique sur une barre.** Elle deviendra plus lumineuse, les autres s'assombriront, et un encadré avec la date et le nombre apparaîtra à côté. Pour une semaine, l'encadré détaille la titanite **par jour**, pour un mois — **par semaine**. En haut à gauche, un libellé bleu s'allumera, par exemple «Jour affiché : 19.10.2026 · aujourd'hui» (ou «Показана неделя», «Показан месяц»).
3. **Examine les tuiles.** Elles affichent désormais les chiffres de cette barre : titanite, potions, salles et étages pour la journée, la semaine ou le mois. «Titanite (aujourd'hui)» reste celui d'aujourd'hui.
4. **Reviens aux totaux.** Clique à nouveau sur la même barre ou sur le libellé bleu avec une croix (✕). Si tu modifies la période, la sélection sera également réinitialisée.

### Tableau

Le bouton **«Tableau»** en haut à droite du graphique affiche les mêmes barres sous forme de liste : «Date», «Titanite», «Salles», «Étages», «Potion de titans». Les dates récentes sont en haut, et la ligne **«Total»** est en bas. Une ligne peut également être sélectionnée par un clic, et les tuiles afficheront ses chiffres. Le bouton se transforme alors en **«Graphique»** et ramène l'image. Le tableau est pratique lorsque tu as besoin des chiffres exacts pour tous les jours à la fois.

![Tableau : dates, titanite, salles, étages et potion, en bas «Total»](images/stats_table.png)

### Correction manuelle

Le bot calcule selon sa propre arithmétique (6 ou 12 titanite par salle), mais dans le jeu, le chiffre peut être différent : tu as joué toi-même, le bot était éteint, le programme n'a pas été lancé dès le matin. Pour que les statistiques correspondent au jeu, il existe la carte **«Correction manuelle»**.

1. **Choisis un jour.** Dans la liste — «Сегодня», «Вчера» et encore cinq jours passés, soit sept au total. Tu as besoin d'un jour plus ancien ? Choisis la période «7 jours» ou «14 jours» et clique sur sa barre : ce jour s'insérera automatiquement dans la liste (il ne s'insérera pas à partir d'une barre hebdomadaire ou mensuelle — uniquement quotidienne).
2. **Saisis le chiffre total issu du jeu.** Dans le champ «Titanite par jour» — ce qui est affiché dans le jeu **pour toute la journée**, et non «combien ajouter». Pour le jour sélectionné, la valeur actuellement enregistrée est déjà affichée.
3. **Appuie sur «Appliquer»** (ou Entrée dans le champ).

Exemple. Le bot a enregistré 90 titanite pour la journée, alors que le jeu en affiche 150 pour la même journée. Tu saisis **150** — le programme ajoute la différence de 60 et recalcule automatiquement le reste : environ **+5 salles, +1 étage et +250 potions**. C'est une estimation : on considère que les 10 premières salles de la journée ont donné 6 titanite chacune, et les autres 12. Si tu as joué différemment, les salles et les étages peuvent être légèrement différents des valeurs réelles, mais la titanite sera exactement conforme à ta saisie.

Lorsque tout a réussi, la notification «Titanite du 19.10.2026 : 150» apparaît en bas, et la ligne `[СТАТИСТИКА] Данные за 2026-10-19 синхронизированы! Дельта: +60 тит., +5 комн., +250 зелий.` entre dans le journal principal. Si tu as saisi un montant inférieur à celui enregistré, les chiffres diminueront.

Ce qui peut mal tourner :

- **«Saisissez un nombre entier à partir de 0»** — le champ contient des lettres, une virgule, un signe moins ou est vide. Le champ deviendra rouge.
- **«Le bot a collecté 90 ce jour-là, impossible d'indiquer moins»** — il est impossible d'indiquer moins que ce que le bot a collecté **lui-même**, car cela est enregistré honnêtement. Tu ne peux réduire le chiffre que jusqu'à cette valeur.
- **«Ce jour contient déjà exactement cela»** — tu as saisi le même nombre, il n'y a rien à modifier.

> [!warning] «Appliquer» enregistre les chiffres **immédiatement** dans `bot_data/stats.json`. Il n'y a pas de bouton «Enregistrer les réglages» ici et ce n'est pas nécessaire, contrairement au «Мастере правил» (section 7). Il n'est pas possible d'annuler la modification avec un bouton, mais rien ne t'empêche de saisir à nouveau l'ancien nombre.

> [!note] La correction ne modifie **que les statistiques**. Le «Bilan de session» sur la page principale et l'objectif de session (section 4) sont calculés séparément, en fonction de ce que le bot a accumulé lors de ce lancement, et ne dépendent pas de la page «Statistiques».

### «Réinitialiser» : effacer tout l'historique

Le bouton **«Réinitialiser»** (avec la corbeille, à droite dans la carte «Correction manuelle») réinitialise toutes les statistiques à zéro : titanite, salles, étages et potions pour tous les jours. Tu as appuyé par accident ? Rien ne se passera : le programme demandera d'abord «Réinitialiser les statistiques ?» et rappellera que cela ne peut pas être annulé. Avec le bouton «Réinitialiser» de la fenêtre tu confirmes, avec le bouton «Annuler» tu refuses. Après la réinitialisation, une notification «Statistiques réinitialisées» apparaîtra, ainsi que la ligne `[СТАТИСТИКА] Вся история полностью сброшена!` dans le journal.

Seules les statistiques sont effacées. Les règles, les packs, les réglages, `profile.yml` et les journaux de combat restent inchangés. Si le bot est en train de fonctionner à ce moment-là, il continue et reprend ses calculs à partir de zéro, sans réinitialiser l'objectif de session.

> [!tip] Tu veux réinitialiser «pour essayer» ? Enregistre d'abord une copie : ferme le programme et copie le fichier `bot_data/stats.json` ailleurs (le dossier du programme s'ouvre via le bouton «Dossier du bot» sur la page «À propos»). Tu peux restaurer l'historique en remettant le fichier à sa place.

### Questions fréquentes

- **Les chiffres ne correspondent pas au jeu.** Le bot calcule au lieu de lire l'écran : 6 ou 12 titanite par salle. Si tu as obtenu de la titanite d'autres sources, le jeu en affichera davantage. Compare et corrige via la «Correction manuelle».
- **Aujourd'hui est vide alors que j'ai joué.** Vérifie l'heure de réinitialisation : avant celle-ci, le bot enregistre pour «hier» (voir «Jour de jeu» ci-dessus). Tu as changé l'heure dans le «Мастере правил» ? Redémarre le programme pour que la page la prenne également en compte.
- **Il y a peu de barres alors que la période est longue.** Les jours où le bot n'a pas fonctionné sont vides sur le graphique. «Tout le temps» et les mois compressent le graphique par défaut : pour voir des jours précis, choisis «7 jours» ou «14 jours».
- **Dans le journal `[СТАТИСТИКА] ВНИМАНИЕ: Файл stats.json поврежден`.** Le fichier d'historique n'a pas pu être lu (par exemple, l'ordinateur s'est éteint au moment de l'écriture). Le bot commence une nouvelle statistique à partir de zéro et réécrira le fichier. Copie-le au préalable si l'ancien historique est important.

> [!done] Tu sais maintenant comment lire les chiffres, changer de période, vérifier les statistiques avec le jeu et les effacer. La suite — que faire si quelque chose tourne mal. [Section suivante →](#14)

## En cas de problème

Bonne nouvelle : le bot sait se sortir seul de la plupart des ennuis. S'il plante, il fait un état des lieux et recommence. En cas de perte d'Internet, il attend. Si l'ordinateur est verrouillé, il patiente et reprend. Tu n'es nécessaire que lorsqu'il l'a **demandé lui-même** (mis en pause, envoyé un message dans Telegram) ou quand il ne clique sur rien et que le journal ne permet pas de comprendre pourquoi. Cette section traite de ces deux cas : ce que fait le bot sans toi, comment comprendre où se situe la panne et sur quoi cliquer.

Règle pour tous les cas : **ne panique pas et ne te précipite pas**. Il n'y a aucun risque à arrêter le bot, le redémarrer et le relancer : les statistiques, les compositions, les règles et les réglages sont stockés dans des fichiers et ne disparaîtront nulle part.

### Comment savoir si quelque chose ne va pas

- :triangle-alert: **Chiffre rouge sur la pilule «Erreurs»** dans le journal sur la page principale. Il ne compte pas seulement les pannes : des avertissements y apparaissent aussi (par exemple, «fenêtre du jeu recouverte»). Le chiffre en soi n'est pas une raison d'avoir peur, il faut ouvrir la pilule et lire les lignes.
- :pause: **État «Pause» et bouton vert «Continuer», alors que tu n'as pas appuyé sur pause.** Cela signifie que le bot s'est arrêté lui-même et t'attend. Dans le journal, il y a alors la ligne `[ВНИМАНИЕ] Бот на мягкой паузе: ...` avec la raison.
- :send: **Message dans Telegram** (s'il est configuré, section 12) : «Le bot semble bloqué», «L'annulation du combat a échoué», «L'écran du PC est verrouillé».
- :eye: **Silence.** Aucune ligne n'apparaît dans le journal depuis une minute ou plus, et il ne se passe rien dans le jeu. C'est aussi un signe : consulte la section «Cas fréquents» ci-dessous.

Balises dans le journal indiquant un problème :

- `[СТОРОЖ]` — le bot a estimé qu'il était bloqué et a recommencé de lui-même.
- `[СЕТЬ]` — il semble n'y avoir aucune connexion avec le serveur du jeu.
- `[ЭКРАН]` — l'ordinateur empêche de faire une capture d'écran (il est verrouillé).
- `[ОТКАТ]` — étapes d'annulation de combat et ses erreurs (section 10).
- `[ВНИМАНИЕ]` — le bot demande de l'attention : pause, fenêtre du jeu fermée.
- `[ОШИБКА]` — quelque chose est cassé ; ce qui s'est produit est écrit à côté.
- `[ADB]` et `[VISION]` — connexion avec le téléphone et clics.

### Ce que le bot fait lui-même

Ici, tu n'appuies sur rien. Sache simplement que c'est normal et que cela ne casse pas la session.

- :gauge: **Bloqué : 5 minutes sans la moindre salle.** C'est le «garde» (c'est le nom de la vérification qui surveille si le bot est coincé). Le bot écrit `[СТОРОЖ] Бот 5 мин не прошёл ни одной комнаты ... Тревога 1 из 3.`, enregistre une capture d'écran, envoie un message dans Telegram (s'il est configuré) et effectue un **«démarrage intelligent»** : il regarde à nouveau l'écran et décide par où continuer. Si cela n'a pas aidé, 5 minutes plus tard, nouvelle alerte. **Troisième alerte consécutive** (soit environ 15 minutes sans salles) — le bot passe en pause douce et t'attend. Le temps pendant lequel le bot t'attendait (fenêtre SOS, pause, autre fenêtre par-dessus le jeu) n'est pas compté par le garde.
- :activity: **Coincé au même endroit.** L'écran de sélection d'équipe n'est pas apparu en 30 secondes ou la fenêtre de résultat n'est pas apparue en 3 minutes. Dans ce cas `[СТОРОЖ] Зависание: ...`, capture d'écran et même démarrage intelligent, mais sans alerte dans Telegram.
- :globe: **Le combat ne commence pas (très probablement pas de connexion avec le serveur du jeu).** Le bouton «Auto» est enfoncé, mais il n'y a pas de combat. Le bot réessaie deux fois immédiatement, puis attend et réessaie : après 30 secondes, 1, 2, 4 et 8 minutes. Tout cela apparaît dans le journal sous la forme `[СЕТЬ] Бой не начался N раз(а) подряд ... Жду N с и пробую снова.` Si cela n'a pas aidé non plus (environ 15 minutes) : capture d'écran, message «Le bot semble bloqué» et pause douce.
- :rotate-ccw: **Perte de connexion pendant l'annulation du combat.** Le bot ne baisse pas les bras et **attend le jeu jusqu'à 15 minutes** : il écrit `[ОТКАТ] Бой не загрузился ... Не сдаюсь`, enregistre une capture d'écran et signale une fois par minute `Всё ещё жду игру`. La connexion est revenue — l'annulation se terminera d'elle-même (`Игра снова откликается`). Si elle n'est pas revenue au bout de 15 minutes — «L'annulation du combat a échoué», message dans Telegram et pause.
- :monitor: **Ordinateur verrouillé (Win+L) ou écran éteint.** Windows empêche de faire des captures d'écran et le bot ne voit rien. Il **ne plante pas**, mais réessaie toutes les 2 secondes : `[ЭКРАН] Не удаётся сделать снимок экрана ... Похоже, ПК заблокирован`. Au-delà d'une minute — un seul message «L'écran du PC est verrouillé». Déverrouillé — `[ЭКРАН] Снимок экрана снова работает`, le bot reprend seul.
- :layers: **La fenêtre du jeu est recouverte par une autre fenêtre.** Le bot attend qu'elle redevienne principale (`[ВНИМАНИЕ] Окно игры перекрыто ... Бот ждет фокуса`). Clique sur la fenêtre du jeu et il continuera. Pourquoi c'est ainsi — dans la section 5.
- :target: **Le clic n'est pas arrivé.** Si 4 secondes après un clic l'écran n'a pas changé, le bot clique à nouveau : `[VISION] Клик по '...' не зарегистрирован сервером ... Повторяю...`. Ces rares lignes sont normales : le téléphone «réfléchit» parfois.
- :smartphone: **La connexion avec le téléphone par câble a clignoté.** Le bot écrit `[ADB] Постоянное соединение с телефоном оборвалось ... Переподключусь при следующем нажатии` et se reconnecte.
- :send: **Le message dans Telegram n'est pas parti en raison d'Internet.** Le bot le répétera plus tard (section 12) et continuera de fonctionner.

> [!note] Le nombre de fois où le bot s'est bloqué pendant la session est visible dans le bloc `[ИТОГ]` du journal (la ligne contenant le mot «зависания»). Les cas rares ne sont pas graves. S'il y en a beaucoup, cherche la cause dans la section «Cas fréquents» ci-dessous.

### Le bot s'est mis en pause lui-même : que faire

Il s'est arrêté parce qu'il est impossible de continuer sans toi. Procède dans l'ordre :

1. **Regarde l'écran du jeu.** La fenêtre `HeroWarsBot_Arena` montre où le bot est coincé : fenêtre de résultat, combat, menu de pause, champignon de chargement ou quelque chose d'inattendu (autre fenêtre, publicité, demande du jeu).
2. **Lis les dernières lignes du journal.** Ouvre la pilule «Erreurs» et regarde en bas : la raison pour laquelle le bot s'est arrêté y est indiquée (`[СТОРОЖ]`, `[ОТКАТ] ОШИБКА`, `[СЕТЬ]`).
3. **Remets le jeu dans le couloir du Donjon.** Ferme le surplus, attends que le combat se termine ou se charge, et rejoins l'écran avec la porte et le drapeau.
4. **Appuie sur «Continuer».** Le bot refera un état des lieux (démarrage intelligent) et continuera sa route.

> [!note] La pause après une annulation échouée arrive aussi ainsi : le combat manuel a eu le temps de se terminer, le bouton «Encore» sur la fenêtre de résultat n'est plus là, et il est impossible de l'annuler. La fenêtre de résultat reste à l'écran — inutile de tout fermer, après «Continuer», le bot appuiera lui-même sur «OK». Regarde sur cette fenêtre qui a survécu.

> [!tip] Le bot ne se met pas en pause pour chaque détail, mais quand il a essayé et échoué. Par conséquent, avant d'appuyer sur «Continuer», comprends **ce qui** n'a pas fonctionné. Si la cause persiste (pas d'Internet, jeu fermé), le bot se remettra en pause après quelques minutes.

### Cas fréquents : que vérifier et que faire

**Le bot n'appuie sur rien et le journal est silencieux.** Très probablement, il ne voit pas le jeu ou ne peut rien y trouver. Vérifie dans l'ordre :

1. **La fenêtre du jeu est bien là.** Elle s'appelle `HeroWarsBot_Arena`, n'est ni réduite ni fermée. Si la fenêtre n'est pas là, le bot ne l'écrit pas mais la vérifie en silence toutes les demi-secondes. C'est pourquoi le silence dans le journal en cas de fenêtre disparue est courant. Appuie sur «Connecter le téléphone» : la fenêtre s'ouvrira à nouveau.
2. **La taille de la fenêtre n'a pas changé.** Le bot mesure la fenêtre une fois au lancement et utilise cette mesure par la suite. Si tu as étiré, agrandi ou déplacé la fenêtre après le démarrage, arrête le bot (F10), appuie sur «Réinitialiser la taille de la fenêtre du jeu» et à nouveau sur «Lancer le farm». Détails dans la section 3.
3. **Dans le jeu — le couloir du Donjon**, et non le menu, la boutique, un événement tiers ou une fenêtre avec de la publicité.
4. **La langue du programme correspond à la langue du jeu** (deux lettres au bas de la bande de gauche). Sinon, le bot ne reconnaîtra pas les boutons.
5. **Rien ne masque la fenêtre du jeu.** N'importe quelle fenêtre par-dessus le jeu — et le bot attend la mise au point.

**Le bot «voit» et clique, mais rien ne se passe dans le jeu.** Dans le journal, les lignes s'enchaînent : «Клик по ... не зарегистрирован сервером ... Повторяю...». Cela signifie que la commande de clic n'atteint pas le téléphone. Vérifie :

- **Les deux** réglages de débogage sont activés sur le téléphone : «Débogage USB» et «Débogage USB (paramètres de sécurité)». Sans le second, l'image est là mais les clics ne fonctionnent pas (section 2).
- Le téléphone est déverrouillé, le câble est bien branché. Essaie un autre port USB.
- Dans la ligne de commande, `adb devices` affiche `device` à côté du téléphone, et non `unauthorized` ni une liste vide.
- Si cela n'a pas aidé : arrête le bot, appuie sur «Redémarrer scrcpy», puis sur «Lancer le farm».

**Le bot ne clique pas au bon endroit ou confond les titans.** Le plus souvent, la fenêtre du jeu n'a pas la bonne taille ou a été touchée après le démarrage (réinitialisation de la taille comme ci-dessus). Si la taille est correcte mais que le bot manque quand même son coup, enregistre une capture d'écran de ce moment et envoie-la à l'auteur avec le journal (ci-dessous).

**La fenêtre du programme «ne répond pas».** Le programme se surveille lui-même : si la fenêtre ne répond pas pendant 5 secondes, il enregistre dans un fichier à quelle ligne de code il est bloqué. Le fichier se trouve dans `bot_data/debug/` et s'appelle `ui_freeze_<дата>_<время>.txt`. Que faire :

1. **Attends une minute.** Souvent, la fenêtre redevient active d'elle-même : elle est occupée par une tâche lourde.
2. **Le bot fonctionne indépendamment de la fenêtre.** Tu dois l'arrêter alors que les boutons ne répondent pas ? Appuie sur Ctrl+Shift+Q : le bot lui-même écoute cette touche, et non la fenêtre du programme (section 6).
3. **Elle ne redevient pas active — ferme la fenêtre avec la croix.** Si elle ne se ferme pas — via le gestionnaire des tâches (Ctrl+Shift+Esc). Regarde ensuite au même endroit si `HeroWarsBot.exe` ou `python` est resté dans la liste : si oui, ferme-le aussi, sinon le bot continuera à cliquer dans le jeu sans fenêtre.
4. **Envoie le fichier `ui_freeze_...txt` à l'auteur.** Il ne contient que des noms de fichiers et des lignes de code du programme, rien de personnel.

**Le bot s'est arrêté alors que tu ne l'as pas arrêté.** Ouvre la carte «Bilan de session» sur la page principale (bouton «Détails») et regarde la raison :

- «fenêtre scrcpy fermée» — la fenêtre du jeu a été fermée ou a disparu (câble débranché, téléphone verrouillé). Reconnecte le téléphone.
- «le bot s'est arrêté» — le processus s'est terminé sans raison. Si tu as Telegram, le bilan y est arrivé ; sinon, cherche dans le journal la ligne `[ОШИБКА] Бот остановился из-за ошибки:` et le texte en dessous.
- «Пак не найден в правилах» — aucun pack principal n'est défini pour la salle. Ouvre «Maître des règles» → «Base et salles» et définis-le dans les quatre salles (section 7).
- «Ошибка: ...» — le programme a planté. Envoie le journal à l'auteur (ci-dessous).

> [!warning] Après «STOP» (F10), le bot n'a pas le temps d'écrire le bloc `[ИТОГ]` et n'envoie pas le bilan dans Telegram : il est arrêté à la volée (section 6). Ce n'est pas une panne.

**Le téléphone s'est «endormi» ou l'écran s'est éteint.** Le programme lance scrcpy avec le mode «empêcher le téléphone de s'endormir» (`--stay-awake`). Le bouton «Éteindre l'écran du téléphone» n'éteint que **l'écran** : le jeu continue et le bot voit tout. Mais si le téléphone s'est verrouillé ou s'est déconnecté du câble, la fenêtre du jeu affichera l'écran de verrouillage ou du vide, et le bot ne trouvera rien. Déverrouille le téléphone, vérifie le câble et appuie sur «Redémarrer scrcpy».

**Les messages n'arrivent pas dans Telegram.** Très probablement, tu n'as pas appuyé sur «Démarrer» auprès de ton bot ou le token/Chat ID est incorrect — détails dans la section 12. Le bot fonctionne normalement pendant ce temps.

**Le bot ne place pas les bons titans ou ne décide pas comme tu le souhaitais.** Ce n'est pas une panne, mais des règles : consulte les sections 7–11 (packs, seuils, règles, «Le bot décide seul»). La décision du bot se trouve toujours dans le journal sur les lignes `[ТАКТИКА]`.

### Où se trouvent les journaux et les captures d'écran

Le bouton **«Dossier du bot»** sur la page «À propos» ouvre le dossier depuis lequel le programme est lancé. Il содержит les fichiers créés par le bot lui-même. Ce dont tu as besoin se trouve dans le dossier `bot_data` :

- :file-text: `bot_data/logs/bot_log_<дата>_<время>.txt` — **journal complet de chaque lancement du bot.** Le bot l'écrit lui-même, ligne par ligne, il reste donc même après un plantage et la fermeture du programme. C'est le fichier principal d'analyse.
- :gauge: `bot_data/logs/timings_<дата>_<время>.csv` — combien de temps a pris chaque salle (couloir, composition, combat, résultat).
- :swords: `bot_data/logs/battle_log_<дата>_<время>.jsonl` et `battle_log.csv` — historique des combats : salle, ennemis, pack, résultat, PV et énergie des titans.
- :image: `bot_data/debug/` — **captures d'écran pour analyse.** Le nom indique ce qui s'est passé : `stuck_...` — bloqué, `sos_...` — fenêtre SOS, `rollback_wait_...` — a attendu le jeu pendant l'annulation, `rollback_fail_...` — annulation échouée, `start_fail_...` — le combat n'a pas commencé, `result_unreadable_...` — la fenêtre de résultat n'a pas pu être lue. Viennent ensuite le numéro de la salle, l'élément et l'heure (`stuck_комната12_water_2026-10-19_14-03-21.png`). Il y a aussi `ui_freeze_...txt` si la fenêtre du programme a bloqué.

> [!warning] Le bot nettoie lui-même l'ancien contenu : au lancement, 20 nouveaux fichiers de chaque type (`.txt`, `.jsonl`, `timings_*.csv`) restent dans `bot_data/logs/`, et 50 nouvelles captures d'écran restent dans `bot_data/debug/`. Si tu veux conserver les journaux après une nuit problématique, **copie-les ailleurs avant le prochain lancement du bot**. De même, le journal que tu as enregistré avec le bouton «Enregistrer le journal» dans le dossier par défaut est effacé : enregistre-le ailleurs, par exemple sur le bureau.

> [!warning] Ne supprime pas et ne renomme pas `profile.yml` (tes réglages et Telegram) et le dossier `bot_data` : ils contiennent les statistiques, les règles mémorisées par le bot et l'historique des combats. Tu ne peux effacer que `bot_data/debug` et les anciens journaux, et ce uniquement lorsqu'ils ne sont pas nécessaires.

### Comment envoyer le journal à l'auteur

Lorsque le problème n'a pas pu être résolu, le moyen le plus rapide est d'envoyer à l'auteur ce qui s'est passé.

1. **Rappelle-toi quand cela s'est produit.** L'heure et le nombre approximatif de salles (`[СТАТИСТИКА] Комнат: N`) aident à trouver le bon endroit dans le long journal.
2. **Trouve les fichiers.** Le journal est `bot_data/logs/bot_log_...` de cette nuit-là, les captures d'écran proviennent de `bot_data/debug/` avec une heure similaire dans le nom, et en cas de blocage de la fenêtre, il y a aussi `ui_freeze_...txt`.
3. **Appuie sur «Envoyer le journal à l'auteur»** sous le journal sur la page principale. Le programme proposera d'enregistrer ce qui se trouve actuellement dans le journal (le fichier `gui_log_...txt`), puis ouvrira ton logiciel de messagerie avec un e-mail prêt à être envoyé à l'adresse de l'auteur.
4. **Joins toi-même les fichiers à l'e-mail.** Le programme ne sait pas joindre de fichiers à l'e-mail : il ne fait qu'ouvrir le message. Joins `gui_log_...txt` ou `bot_log_...txt`, les captures d'écran et (le cas échéant) `ui_freeze_...txt`.
5. **Décris avec des mots :** ce que tu as fait, ce que tu attendais, ce que tu as vu, quand c'était. Une simple phrase «ça ne marche pas» n'aide pratiquement pas l'auteur.

> [!warning] **Ne joins jamais** `profile.yml` et `bot_data/profile.yml.bak` : ils contiennent le token de ton bot Telegram. Envoie également une capture d'écran de la fenêtre «Réglages Telegram» uniquement avec le token masqué (par des points).

> [!note] L'e-mail ne s'est pas ouvert (logiciel de messagerie non configuré) ? Sur la page «À propos», il y a un bouton «Contacter l'auteur» : si l'e-mail n'a pas pu être ouvert, il place l'adresse dans le presse-papiers et tu pourras écrire depuis n'importe quelle adresse e-mail.

### Si rien n'y fait

Va du plus simple au plus complexe, en vérifiant après chaque étape si le bot est redevenu actif :

1. **«Pause» → remets le jeu dans le couloir → «Continuer».**
2. **«STOP» (F10) → «Lancer le farm».** Le bot commencera par un démarrage intelligent et trouvera lui-même où il se trouve.
3. **Arrête le bot et appuie sur «Redémarrer scrcpy».** Puis à nouveau sur «Lancer le farm».
4. **Ferme le programme et rouvre-le.** Si le téléphone est «coincé», débranche et rebranche le câble.
5. **Redémarre l'ordinateur et le téléphone.** Cela ressemble à une blague, mais cela résout la moitié des problèmes étranges.

Les objectifs de la session (temps, salles, étages, titanite) sont recomptés depuis le début après un redémarrage, tandis que les statistiques, les packs et les règles restent : ils sont stockés dans des fichiers.

> [!done] Tu sais maintenant comment le bot se sauve lui-même, ce qu'il faut faire lorsqu'il s'arrête et comment collecter et envoyer un journal. Il reste une dernière section : à propos du programme et comment soutenir le projet. [Section suivante →](#15)

## À propos et soutien

La dernière page dans le menu de gauche est «À propos». Elle traite du programme lui-même : quelle version tu possèdes, si tout est en place, où écrire à l'auteur et comment dire «merci». Il n'y a rien à configurer dessus, mais deux boutons utiles se trouvent ici : «Rechercher des mises à jour» et «Dossier du bot».

### Ce que contient la page

- :shield-check: **Carte du programme** en haut. Nom «Hero Wars: Knowledge Engine Bot», à côté — **numéro de version** (par exemple `v1.6.1`) et balise `Beta`. «Beta» signifie «en cours de test sur le terrain» : le programme fonctionne, mais l'auteur la perfectionne encore et des erreurs restent possibles. Sous le nom — une courte description. À droite, quatre boutons, détaillés ci-dessous.
- :user: **«Auteur et licence»** : nom de l'auteur, son e-mail et sa licence. Clique sur l'adresse e-mail — un message s'ouvrira.
- :monitor: **«État des composants»** : vérification que tout le nécessaire au fonctionnement est présent sur l'ordinateur. Détails ci-dessous.
- :heart: **«Soutenir le projet»** : moyens de remercier l'auteur. Ce n'est pas obligatoire.

> [!tip] Indique la version à l'auteur lorsque tu écris à propos d'un problème : elle montre immédiatement quel programme tu utilises exactement. La version se trouve dans la carte en haut, à côté du nom.

### Les quatre boutons dans la carte

1. **«Rechercher des mises à jour».** Ouvre dans le navigateur la page des versions du projet sur GitHub (GitHub est le site où l'auteur conserve le programme ; une «version» ou «release» est une version prête à être téléchargée). Compare le numéro le plus récent avec le tien. S'il est plus récent — tu peux mettre à jour, s'il est identique — tu as la version la plus récente.
2. **«Dossier du bot».** Ouvre dans l'explorateur Windows le dossier depuis lequel le programme est lancé : celui-là même où sont stockés tes réglages et tes données. Utile lorsque tu dois copier des fichiers ou trouver un journal.
3. **«Contacter l'auteur».** Ouvre un e-mail à l'adresse de l'auteur dans ton logiciel de messagerie. Si aucun logiciel de messagerie n'est présent sur l'ordinateur, l'e-mail ne s'ouvrira pas. Dans ce cas, le programme placera lui-même l'adresse dans le presse-papiers (la mémoire temporaire depuis laquelle on colle avec Ctrl+V) et l'indiquera en bas de la fenêtre : «Impossible d'ouvrir — copié dans le presse-papiers». Colle l'adresse dans un e-mail depuis n'importe quelle messagerie.
4. **«GitHub du projet».** Ouvre la page principale du projet sur GitHub : le code source et la description s'y trouvent.

> [!note] Le programme **ne va pas lui-même sur Internet pour les mises à jour** : «Rechercher des mises à jour» ne fait qu'ouvrir la page, et c'est toi qui décides. C'est fait exprès pour que rien ne change à ton insu.

### Comment mettre à jour le programme

La mise à jour ne «s'installe pas par-dessus» — tu télécharges la nouvelle version et y transfères tes données. Ainsi, tes packs et tes statistiques ne disparaîtront pas.

1. **Arrête le bot et ferme le programme.** La croix de la fenêtre, si le bot fonctionne, demandera s'il faut l'arrêter.
2. **Télécharge la nouvelle version** sur la page des releases (bouton «Rechercher des mises à jour») et extrait-la dans un nouveau dossier, pas par-dessus l'ancien.
3. **Transfère tes données.** Depuis l'ancien dossier vers le nouveau, copie le fichier `profile.yml` et le dossier `bot_data` dans son ensemble. Sans eux, le nouveau programme repart «de zéro» : des réglages vides et des statistiques vides.
4. **Lance le nouveau programme** et jette un coup d'œil à «À propos» : le numéro de version doit être nouveau et les trois composants doivent être en ordre.
5. **Ne supprime pas l'ancien dossier pour l'instant.** Travaille quelques jours sur la nouvelle version. Si tout va bien — supprime-le alors.

> [!warning] Ne copie pas les fichiers de `bot_data` un par un selon «ce qui est utile», mais transfère le dossier dans son ensemble : les règles que le bot a mémorisées lui-même, l'historique des combats et les statistiques sont liés entre eux et ne peuvent pas être réassemblés à nouveau.

### «État des composants»

Le programme vérifie lui-même la présence de tout ce sans quoi le bot ne peut pas fonctionner. La vérification s'effectue en arrière-plan à chaque arrivée sur la page. Pendant qu'elle s'effectue, on voit «vérification…».

- :smartphone: **ADB** — le service grâce auquel l'ordinateur clique sur le téléphone. Doit être «trouvé».
- :monitor: **scrcpy** — le programme qui affiche l'écran du téléphone dans une fenêtre sur l'ordinateur. Doit être «trouvé».
- :image: **Base de modèles** — les «images modèles» des boutons et des titans grâce auxquelles le bot reconnaît ce qu'il a à l'écran. Doit être «chargée».

Que faire si quelque chose est en rouge :

- **ADB ou scrcpy «introuvable».** Cela signifie que le dossier les contenant n'a pas été ajouté à `PATH` (la liste des emplacements où Windows cherche les programmes). La procédure est décrite dans la section [«Prérequis et installation»](#2). Après avoir modifié `PATH`, ferme le programme et rouvre-le : un programme déjà lancé ne voit pas le nouveau `PATH`.
- **Base de modèles «introuvable».** Des fichiers ont disparu du dossier du programme. Le plus souvent, l'archive n'a pas été entièrement extraite ou l'antivirus a supprimé quelque chose. Extrais à nouveau l'archive dans un nouveau dossier et transfère `profile.yml` et `bot_data` comme lors d'une mise à jour.

### Ce qui se trouve dans le dossier du bot et ce qu'il ne faut pas supprimer

Ouvre-le avec le bouton «Dossier du bot». Il y a beaucoup de fichiers, mais seuls quelques-uns te seront utiles. Le reste est de service et le programme en a besoin pour fonctionner.

- :file-text: `HeroWarsBot.exe` — le programme lui-même. Le bot fonctionne également depuis celui-ci, il n'a pas de fichier séparé. Tous les autres fichiers et dossiers à côté (`guide`, `ui`, bibliothèques, fichiers avec l'extension `.dll` et autres) font partie du programme. **N'en supprime et n'en renomme aucun**, sinon il ne se lancera plus.
- :file-text: `profile.yml` — tes réglages : objectif de la session, seuils, Telegram. **Il contient le token de ton bot Telegram, ne l'envoie donc à personne.** Il apparaît après le premier «Enregistrer les réglages».
- :folder: `bot_data` — tout ce que le programme et le bot ont enregistré eux-mêmes. C'est **ce que tu as de plus précieux**. À l'intérieur :
  - `stats.json` — statistiques (page «Statistiques») ;
  - dossier `rules` — tes packs et règles, y compris ceux mémorisés par le bot ;
  - dossier `logs` — historique des combats et journal du bot (`bot_log_...txt`) ;
  - dossier `debug` — captures d'écran pour analyse (fenêtres SOS, blocages, annulations échouées) ;
  - `titan_state.json` — santé et énergie des titans pour la journée de jeu ;
  - `profile.yml.bak` — copie des réglages. C'est à partir d'elle que fonctionne «Restaurer / Réinitialiser» dans le «Maître des règles». **Elle contient aussi le token Telegram** ;
  - `ui_settings.json` — langue choisie pour la fenêtre ;
  - `sos_info.json`, `temp_sos.png`, `temp_test.png` — petits fichiers de travail pour les messages Telegram.
- :pause: `pause.flag` — «drapeau de pause». Il apparaît lorsque le bot est en pause douce. S'il est resté de la fois précédente, le programme le supprimera lui-même au lancement.

> [!warning] **Ne supprime pas et ne renomme pas** `profile.yml` et `bot_data`. Si tu supprimes `bot_data`, les statistiques, les packs, les règles et tout ce que le bot a appris disparaîtront. Si tu as vraiment besoin de libérer de l'espace, tu peux effacer le contenu de `bot_data/debug` et les anciens journaux dans `bot_data/logs`. Mais le bot ne conserve lui-même que les 20 derniers journaux et les 50 dernières captures d'écran, donc l'espace n'est généralement pas un problème.

> [!tip] **Fais une copie une fois par semaine.** Copie `profile.yml` et le dossier `bot_data` sur une clé USB ou dans le cloud. Si l'ordinateur tombe en panne ou si tu réinstalles Windows, tu téléchargeras à nouveau le programme, et tu restaureras les packs et les statistiques à partir de la copie. Le token Telegram est présent dans la copie — conserve-la chez toi, pas dans un dossier partagé.

### Auteur et licence

Le programme a été écrit et est maintenu par **Platon Petrunin**. Questions, erreurs et idées — bouton «Contacter l'auteur» ou adresse dans la carte «Auteur et licence».

La licence s'appelle **PolyForm Noncommercial 1.0.0**. En mots simples :

- :check: l'utiliser pour soi-même, pour son propre jeu gratuitement est possible — autant que l'on veut ;
- :check: étudier le code et le modifier pour soi-même est également possible ;
- :x: **il est interdit de gagner de l'argent** : vendre le programme ou son `.exe`, le faire passer pour le sien sous un autre nom, l'intégrer à des services payants. Une autorisation écrite de l'auteur est requise pour cela.

> [!note] C'est un résumé succinct, pas un texte juridique. Si ton cas est inhabituel (par exemple, si tu souhaites distribuer le programme à des amis ou à une communauté), écris d'abord à l'auteur. Le texte complet de la licence se trouve dans le fichier `LICENSE` du projet sur GitHub.

### Comment soutenir le projet

Le programme est gratuit et l'auteur le réalise durant son temps libre. S'il te fait gagner du temps et t'évite des soucis, tu peux dire «merci» avec de l'argent. C'est **volontaire** : le bot fonctionne de la même manière que tu aies payé ou non, et il n'y a aucune «fonction payante».

En bas de la page «À propos», trois blocs :

1. **«Cryptomonnaie».** Trois portefeuilles : `USDT · TRC20`, `Bitcoin · BTC` et `Ethereum · ETH`. L'adresse complète est visible dans le champ. Tu peux la copier avec le bouton «Copier» à droite (en bas apparaîtra «Adresse copiée»), en double-cliquant sur le champ (tout sera sélectionné) ou avec le bouton droit de la souris — «Copier».
2. **«Don via Telegram».** Trois lignes — roubles (`RUB`), euros (`EUR`) et dollars (`USD`). Dans chacune, deux boutons : **«Application»** ouvre le paiement dans l'application Telegram, **«Navigateur»** — dans le navigateur si Telegram n'est pas installé. Choisis la devise qui te convient le mieux.
3. **«Virements directs».** Boutons «Soutenir sur Boosty» et «YooMoney (RUB)» : les pages de ces services s'ouvrent, puis le processus se déroule comme pour un paiement habituel.

> [!warning] **Prudence avec les cryptomonnaies.** N'effectue de virement que sur le réseau indiqué à côté du portefeuille : pour le `USDT`, c'est `TRC20`, et non un autre. L'argent envoyé sur le mauvais réseau **ne pourra pas être récupéré**. Ne prends l'adresse que depuis le programme, avec le bouton «Copier» : sur les sites web et dans les messages tiers, elle peut être remplacée. Pour la première fois, envoie une petite somme.

### Foire aux questions

- **Ma version est ancienne — est-ce grave ?** Non. Le programme ne cesse pas de fonctionner parce qu'une nouvelle version est sortie. Mais les nouvelles versions corrigent généralement des erreurs, alors jette un coup d'œil à la page des releases toutes les quelques semaines.
- **«Dossier du bot» ne s'est pas ouvert.** L'inscription «Impossible d'ouvrir le dossier» apparaîtra. Ouvre-le toi-même : explorateur, dossier dans lequel tu as extrait le programme.
- **Pourquoi n'y a-t-il pas de bouton «Mettre à jour» ?** Le programme ne télécharge rien de lui-même afin de ne pas casser tes réglages sans te le demander. Tu te mets à jour toi-même en suivant les étapes ci-dessus.
- **Si je ne soutiens pas le projet, quelque chose changera-t-il ?** Rien. Le bot fonctionne de la même manière pour tout le monde.

> [!done] C'est la dernière section. Tu sais maintenant tout pour lancer le bot, le configurer à ta convenance, comprendre ses décisions et rectifier le tir en cas de problème. Bon jeu ! S'il te reste des questions, le bouton «Contacter l'auteur» se trouve ci-dessous.
