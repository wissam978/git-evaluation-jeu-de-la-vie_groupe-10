# Jeu de la vie – groupe 10

Simulation du jeu de la vie en Python 3, utilisable depuis un terminal. Le programme `main.py` lit les options en ligne de commande, crée une grille aléatoire ou lit une grille sur l'entrée standard, calcule les générations successives et les écrit sous forme d'images PNG ou de texte.

## Installation

Python 3 est nécessaire. Le programme n'utilise que la bibliothèque standard : aucun paquet Python à installer. Pour générer les vidéos, il faut aussi `ffmpeg` et `gource`.

Sous Ubuntu ou Debian :

    sudo apt update
    sudo apt install python3 git gource ffmpeg

Sous macOS :

    brew install python git gource ffmpeg

Sous Windows, installer WSL (`wsl --install` dans PowerShell lancé en administrateur), redémarrer, ouvrir Ubuntu, puis suivre la procédure Ubuntu.

Récupérer le projet :

    git clone https://github.com/wissam978/git-evaluation-jeu-de-la-vie_groupe-10.git
    cd git-evaluation-jeu-de-la-vie_groupe-10

## Exécution

Simulation avec les valeurs par défaut (grille aléatoire de 10 cellules par côté, 20 itérations, graine 42). Les images grid_0000.png à grid_0020.png sont écrites dans le dossier outputs :

    $ python3 main.py
    Generation of 21 images in directory outputs

Grille de 50 cellules par côté, 200 itérations, graine 4200 :

    $ python3 main.py -n 50 -m 200 -s 4200
    Generation of 201 images in directory outputs

Grille lue sur l'entrée standard, avec une sortie texte (limites fixes) :

    $ cat tests/matrix3/input.txt | python3 main.py -m 1 -t text
    iteration: 1
    0 1 0
    0 0 1
    0 1 0

Même grille avec les conditions aux limites périodiques :

    $ cat tests/matrix3/input.txt | python3 main.py -m 1 -p -t text
    iteration: 1
    0 0 0
    0 0 0
    0 0 0

Format d'une grille en entrée : la première ligne contient la taille N, suivie de N lignes de N cellules (0 ou 1) séparées par des espaces. Exemple (tests/matrix3/input.txt) :

    3
    1 0 1
    0 0 1
    1 0 1

En cas d'erreur (grille vide ou mal formée, cellule autre que 0 ou 1, taille non positive, itération négative, type de sortie invalide), le programme écrit un message sur la sortie d'erreur et se termine avec un code de sortie différent de 0.

Pour vérifier le programme avec les scripts de test fournis :

    sh check_script_options.sh
    sh check_tests.sh
