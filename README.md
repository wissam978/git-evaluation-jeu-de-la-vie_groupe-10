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

## Arguments

| Court | Long | Description | Valeur par défaut |
|---|---|---|---|
| -n N | --nb_cells N | nombre de cellules par côté d'une grille aléatoire (entier strictement positif) | 10 |
| -m N | --max_iterations N | numéro de la dernière itération à calculer (entier positif ou nul) | 20 |
| -s N | --seed N | graine du générateur aléatoire (tout entier, y compris négatif ou nul) | 42 |
| -o DOSSIER | --output_directory DOSSIER | dossier dans lequel écrire les images | outputs |
| -t TYPE | --output_type TYPE | type de sortie : image ou text | image |
| -p | --periodic | active les conditions aux limites périodiques | désactivé |
| -h | --help | affiche l'aide du programme | – |

Une grille lue sur l'entrée standard remplace la grille aléatoire : dans ce cas, -n et -s n'ont pas d'effet.

## Auteurs

- ABASSE Wissam, numéro étudiant : 46008160
- ABDOUL HALECK Faissa, numéro étudiant : 46008873

## Liens utiles

- [Jeu de la vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie) : présentation des règles du jeu de Conway,
- [Documentation argparse](https://docs.python.org/fr/3/library/argparse.html) : analyse des arguments d'un script Python,
- [Documentation random](https://docs.python.org/fr/3/library/random.html) : génération de grilles aléatoires reproductibles,
- [Pipeline (Unix)](https://en.wikipedia.org/wiki/Pipeline_(Unix)) : description du pipe,
- [Installation de WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install) : procédure officielle pour Windows,
- [Documentation ffmpeg](https://ffmpeg.org/documentation.html) : installation et utilisation de ffmpeg,
- [Site officiel de Gource](https://gource.io/) : présentation et téléchargement de Gource,
- [Documentation officielle de git rebase](https://git-scm.com/book/fr/v2/Les-branches-avec-Git-Rebaser-Rebasing) : fonctionnement du rebase.
