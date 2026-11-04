
# Jeu de la vie
Ce projet consiste à créer en Python une simulation du [jeu de la vie de Conway](https://fr.wikipedia.org/wiki/Jeu_de_la_vie). Le programme permet de générer une grille aléatoire ou de lire une grille sur l'entrée standard, puis de calculer son évolution avec des conditions aux limites fixes ou périodiques.

- [Introduction](#introduction)
- [Objectifs](#objectifs)
- [Programme à réaliser](#programme-à-réaliser)
  - [Les règles du jeu](#les-règles-du-jeu)
  - [Les conditions aux limites](#les-conditions-aux-limites)
  - [Les arguments du programme](#les-arguments-du-programme)
  - [Entrées du programme](#entrées-du-programme)
  - [Sorties du programme](#sorties-du-programme)
  - [Gestion des erreurs](#gestion-des-erreurs)
  - [Scénarios de vérification](#scénarios-de-vérification)
- [Contraintes techniques et vérification](#contraintes-techniques-et-vérification)
  - [Fichiers fournis](#fichiers-fournis)
  - [Tests automatiques](#tests-automatiques)
  - [Scénario 6 : intégration continue (bonus)](#scénario-6--intégration-continue-bonus)
- [Le travail en groupe](#le-travail-en-groupe)
  - [L'historique Git attendu](#lhistorique-git-attendu)
  - [Les messages de commit](#les-messages-de-commit)
  - [Les Pull Requests](#les-pull-requests)
- [Le rendu](#le-rendu)
- [Le barème](#le-barème)
- [Aides techniques](#aides-techniques)
  - [Préparer son environnement](#préparer-son-environnement)
  - [Lecture des arguments avec argparse](#lecture-des-arguments-avec-argparse)
  - [Le pipe Unix](#le-pipe-unix)
  - [Commandes Git](#commandes-git)
  - [Visualisation de l'historique](#visualisation-de-lhistorique)
  - [Générer une vidéo du jeu de la vie](#générer-une-vidéo-du-jeu-de-la-vie)
  - [Gource](#gource)
  - [Découvrir GitHub Actions](#découvrir-github-actions)
- [Liens utiles](#liens-utiles)

## Introduction

Ce projet sert de support pour l'évaluation du module outils de développement logiciel et doit être réalisé en groupes.

Le développement d'un programme fonctionnel est nécessaire, mais il ne constitue pas le seul objectif du projet. La façon dont le groupe organise le travail, utilise les branches, rédige les commits, réalise les revues et fusionne les *Pull Requests* est au cœur de l'évaluation.

Chaque membre du groupe doit contribuer de manière régulière et sensiblement équivalente au dépôt. Un projet terminé par une seule personne, puis partagé avec le reste du groupe à la fin du travail, ne répond pas à l'objectif de cette évaluation.

Voici la liste des groupes :
 - Groupe 1
   - FAYE Mariama
   - GNING Aliou
   - GUEYE Seynabou
   - AHMED ATTOUMANI Nizar
   - HOUSSENI Elamine
   - ROBERT Erwan 
 - Groupe 2
   - MAILLOT CADET Enzo Amable
   - BOYER John-Lucas
   - PAYET Arthur
   - POUNIANDY Rajan
   - RAVALISON RABOANA Jérémie
 - Groupe 3
   - HASSANALY Sania
   - LOUAFI Maya
   - MONTFORT Raphaël
   - PUTTYAH Danish
 - Groupe 4
   - CADIL Yann
   - GRONDIN Morgan
   - RAYBAUD Marc
   - HOAREAU Hugo
   - OKPEICHA Kolawole Amour Dieudonne
 - Groupe 5
   - ASSADILLAH Ahmed
   - RAMAHENINA Anditiana Stéphane
   - SOILIHI Yakinat
   - KOGOE Essossimna
 - Groupe 6
   - ALI Yanisse
   - MAILLOT Maenice
   - RAZAKAMANANTSOA Herimanantsoa
   - VIRAPIN Dhiessene
 - Groupe 7
   - COUROUNADIN-MOUNY Maxence
   - GONTHIER Raphaël
   - LENDERS Bryan
   - MADI M'HADJI Amal
   - RAKOTONANAHARY Lanja
 - Groupe 8
   - HERINIRINASOA Sariaka
   - PANON Yaël
   - SAID Darsia
   - VONJY Zazirka
 - Groupe 9
   - ANDRIAMANANJARA Ranto Ruannah Mialitiana
   - FANOMEZANTSOA Celio
   - RAKOTOMAHARIVO Miangaly Fitia
   - MBAE CHARIF Mounira
   - SHUM-HUNG RAKOTOMANDIMBY Ludovic
 - Groupe 10
   - ABASSE Wissam
   - ABDOUL HALECK Faïssa
 - Groupe 11
   - ESSOB Alexandre
   - SIMONIN Clément
   - AURE Remy
   - MAILLOT Benoît
 - Groupe 12
   - BROCHARD-VIMBOULY Antoine
   - ABDALLAH Johan
   - ZEGHOUDI Mohamed
 - Groupe 13
   - ISMAEL Fred
   - DJAROUDI Younas
   - GRONDIN Alexandre
   - MOUSTOIFA Aftahou
   - PAYET Alexandre
   - ROBERT Alexandre

Si vous souhaitez avoir une vue d'ensemble du contexte qui fait la renommée du jeu de la vie, je vous conseille vivement de regarder cette vidéo :

[![Voir la vidéo sur le jeu de la vie](https://img.youtube.com/vi/gKgAaZ7a5Bs/hqdefault.jpg)](https://youtu.be/gKgAaZ7a5Bs)

## Objectifs

Le groupe démontrera sa capacité à :

- répartir un projet en tâches indépendantes ;
- manipuler des branches Git ;
- produire des commits courts, cohérents et correctement décrits ;
- synchroniser une branche de travail à l'aide d'un *rebase* ;
- créer, relire et fusionner des *Pull Requests* sur GitHub ;
- résoudre les éventuels conflits rencontrés ;
- réaliser en Python un programme utilisable depuis un terminal ;
- composer ce programme avec d'autres commandes grâce au pipe Unix ;
- produire une vidéo du jeu de la vie et une vidéo de l'historique du dépôt.

## Programme à réaliser

Le programme à réaliser est le fichier `main.py`, placé à la racine du dépôt. Il doit être exécutable avec Python 3 de la façon suivante :

```bash
python3 main.py
```

### Les règles du jeu

Le jeu de la vie se déroule sur une grille de cellules. Chaque cellule est soit morte, représentée par `0`, soit vivante, représentée par `1`. Pour calculer la génération suivante, on compte les huit cellules voisines de chaque cellule : horizontalement, verticalement et en diagonale.

Les règles sont les suivantes :

- une cellule morte qui possède exactement 3 voisines vivantes devient vivante : c'est une naissance ;
- une cellule vivante qui possède 2 ou 3 voisines vivantes reste vivante : elle survit ;
- dans tous les autres cas, la cellule est morte à la génération suivante.

Le calcul d'une génération ne doit pas modifier la génération en cours pendant son parcours. Toutes les cellules de la génération suivante sont calculées à partir de la même grille initiale.

La grille utilisée dans ce projet est carrée : elle possède autant de lignes que de colonnes.

### Les conditions aux limites

Le programme doit gérer deux comportements pour les cellules situées sur les bords de la grille.

Par défaut, tout ce qui se trouve à l'extérieur de la grille est considéré comme mort. Par exemple, une cellule placée dans un coin ne possède que trois voisines dans la grille.

Lorsque l'option `-p` ou `--periodic` est utilisée, la grille devient périodique. Le bord gauche est relié au bord droit et le bord supérieur est relié au bord inférieur. On peut se représenter cette grille comme la surface d'un tore : une cellule qui sort d'un côté revient du côté opposé.

### Les arguments du programme

Le programme doit accepter les options suivantes, sous leur forme courte et leur forme longue :

| Option courte | Option longue | Description | Valeur par défaut |
|---|---|---|---|
| `-n N` | `--nb_cells N` | nombre de cellules par côté pour une grille aléatoire | `10` |
| `-m N` | `--max_iterations N` | numéro de la dernière itération à calculer | `20` |
| `-s N` | `--seed N` | graine du générateur de nombres aléatoires | `42` |
| `-o DOSSIER` | `--output_directory DOSSIER` | dossier dans lequel écrire les images | `outputs` |
| `-t TYPE` | `--output_type TYPE` | type de sortie : `image` ou `text` | `image` |
| `-p` | `--periodic` | active les conditions aux limites périodiques | désactivée |
| `-h` | `--help` | affiche l'aide du programme | — |

La génération initiale porte le numéro `0`. Ainsi, une simulation demandée avec `-m 20` comporte 21 générations, de `0` à `20` incluses.

La valeur de `--max_iterations` doit être un entier positif ou nul. La valeur de `--nb_cells` doit être un entier strictement positif. La valeur de `--seed` doit être un entier ; les valeurs négatives, nulles et positives sont acceptées.

Pour vous aider à implémenter ces options, consultez l'aide [Lecture des arguments avec argparse](#lecture-des-arguments-avec-argparse).

### Entrées du programme

#### Génération d'une grille aléatoire

Lorsqu'aucune grille n'est fournie sur l'entrée standard, le programme génère une grille aléatoire. L'option `--nb_cells` définit le nombre de cellules par côté et `--seed` fixe la graine du générateur.

Pour une même graine et une même taille, la grille aléatoire générée doit toujours être identique. Pour cela, vous pouvez créer votre propre générateur avec `random.Random(seed)`.

#### Lecture d'une grille sur STDIN

Le programme doit également pouvoir lire une grille depuis l'entrée standard, `STDIN`. Lorsqu'une grille est reçue de cette façon, elle est utilisée comme génération initiale à la place d'une grille aléatoire. Les options `--nb_cells` et `--seed` n'ont alors pas d'effet sur la grille utilisée.

Les scénarios 3 et 4 utilisent un pipe Unix ; son fonctionnement et la lecture de `STDIN` en Python sont expliqués dans l'aide [Le pipe Unix](#le-pipe-unix).

##### Format d'une grille en entrée

La première ligne contient la taille de la grille. Elle est suivie des lignes de la matrice, dont les cellules sont séparées par des espaces. Voici le contenu de `tests/matrix3/input.txt`, utilisé dans les scénarios 3 et 4 :

```text
3
1 0 1
0 0 1
1 0 1
```

Cette entrée décrit une grille de 3 lignes et 3 colonnes à la génération initiale.

### Sorties du programme

Le choix du type de sortie est indépendant de l'origine de la grille : une grille aléatoire comme une grille lue sur `STDIN` peut produire une sortie image ou texte.

#### Sortie image

Avec `-t image` (ou lorsque `-t` est omis), le programme écrit un fichier PNG par génération, de la génération initiale `0` à la dernière itération demandée incluse. Le dossier de destination est `outputs` par défaut ; l'option `-o DOSSIER` permet de le changer.

Le nom d'une image respecte obligatoirement le format `grid_XXXX.png`, où `XXXX` est le numéro de l'itération écrit sur quatre chiffres. L'image de la génération initiale se nomme donc `grid_0000.png`.

La fonction `write_grid` fournie dans `lib.py` permet de transformer une matrice carrée de `0` et de `1` en une image PNG. Vous ne devez pas modifier le comportement de cette fonction.

#### Sortie texte

Avec `-t text`, aucun fichier image n'est généré : seule la dernière itération demandée est écrite sur la sortie standard, `STDOUT`. La sortie commence par `iteration: N`, où `N` est le numéro de cette itération, puis présente les lignes de la grille, avec des cellules séparées par des espaces.

Aucun autre message ne doit être écrit sur `STDOUT`, car il empêcherait la comparaison automatique du résultat.

### Gestion des erreurs

La gestion des erreurs fait partie intégrante du travail du développeur·se. Le programme doit notamment refuser une grille vide ou mal formée, une cellule différente de `0` ou `1`, une taille non positive, une itération négative et un type de sortie différent de `image` ou `text`.

Lorsqu'une erreur est rencontrée, un message explicite doit être écrit sur la sortie d'erreur, `STDERR`, et le programme doit se terminer avec un code de sortie différent de `0`. Les erreurs d'utilisation des arguments peuvent être prises en charge directement par `argparse`.

### Scénarios de vérification

#### Scénario 1 : exécution sans options

Sans option, le programme utilise les [valeurs par défaut](#les-arguments-du-programme) et crée **21 images dans `outputs`**, de `grid_0000.png` à `grid_0020.png` :

```bash
$ python3 main.py
Generation of 21 images in directory outputs
$ echo $?
0
$ ls -p1 outputs | wc -l
     21
```

Le programme annonce le nombre d'images produites et leur dossier de destination. La commande `echo $?` affiche le code de sortie : `0` indique que l'exécution s'est terminée normalement.

La commande `ls -p1 outputs | wc -l` compte les entrées non cachées du dossier. Pour vérifier le nombre d'images dans les scénarios 1 et 2, ce dossier ne doit contenir aucune autre entrée non cachée avant l'exécution. Le fichier caché `.keep` n'est pas compté.

#### Scénario 2 : génération d'images

Cet exemple utilise une grille de 50 cellules par côté, la graine `4200` et une dernière génération numérotée `200`. Il produit donc 201 images, de `grid_0000.png` à `grid_0200.png` :

```bash
$ python3 main.py -n 50 -m 200 -s 4200
Generation of 201 images in directory outputs
$ echo $?
0
$ ls -p1 outputs | wc -l
    201
```

#### Scénario 3 : évolution d'une grille

À partir de la grille présentée dans [Format d'une grille en entrée](#format-dune-grille-en-entrée), `-m 1` demande une seule évolution, avec les conditions aux limites fixes utilisées par défaut :

```bash
$ cat tests/matrix3/input.txt | python3 main.py -m 1 -t text
iteration: 1
0 1 0
0 0 1
0 1 0
$ echo $?
0
```

#### Scénario 4 : grille périodique

L'ajout de `-p` active les conditions aux limites périodiques et donne un résultat différent pour la même grille :

```bash
$ cat tests/matrix3/input.txt | python3 main.py -m 1 -p -t text
iteration: 1
0 0 0
0 0 0
0 0 0
$ echo $?
0
```

#### Scénario 5 : génération d'une vidéo

Les images produites par `main.py` servent à créer une vidéo de l'évolution du jeu de la vie. Générez les images avec votre programme, puis assemblez-les dans l'ordre des générations pour produire un fichier MP4 avec `ffmpeg`. L'assemblage est réalisé par une commande séparée : `main.py` doit produire les images, mais n'a pas à lancer `ffmpeg`.

Pour ce scénario, l'évaluation porte sur la production des images et leur assemblage en une vidéo MP4 lisible. La publication de cette vidéo sur YouTube est évaluée séparément, selon les exigences de la section [Le rendu](#le-rendu).

Le caractère déterministe attendu concerne la grille initiale et son évolution. Vous pouvez ajuster la taille de la grille, la graine, le nombre d'itérations ou la cadence pour votre vidéo finale.

Consultez le tutoriel [Générer une vidéo du jeu de la vie](#générer-une-vidéo-du-jeu-de-la-vie) pour les commandes et la section [Le rendu](#le-rendu) pour les exigences de publication et de documentation.

## Contraintes techniques et vérification

Le projet doit être réalisé avec Python 3 en utilisant uniquement des bibliothèques standards et le fichier `lib.py` fourni. Aucune bibliothèque Python externe n'est nécessaire.

Votre code doit être lisible et décomposé en fonctions ayant chacune une responsabilité claire. Évitez de placer la totalité du programme dans une seule fonction `main`. Il est notamment conseillé de séparer la lecture des arguments, la création de la grille initiale, le calcul d'une génération et les écritures aux formats texte et image.

### Fichiers fournis

Au début du projet, votre dépôt contient les éléments suivants :

```text
.
├── check_script_options.sh
├── check_tests.sh
├── lib.py
├── main.py
├── outputs/
│   └── .keep
├── README-consigne.md
└── tests/
    ├── matrix3/
    ├── matrix4/
    ├── matrix5/
    └── matrix6/
```

- `main.py` contient le point de départ du programme. Il doit être complété par le groupe.
- `lib.py` fournit la fonction `write_grid` utilisée pour générer les images PNG.
- `check_script_options.sh` vérifie la présence et le comportement des six options du programme.
- `check_tests.sh` exécute tous les cas de test fournis et compare les sorties texte.
- `outputs/.keep` permet de conserver dans Git le dossier destiné aux images, même lorsqu'il est vide.
- `README-consigne.md` est le présent sujet.
- `tests/` contient des grilles d'entrée et les sorties attendues pour plusieurs itérations.

Les fichiers de référence contenus dans `tests/`, les scripts de vérification et la fonction fournie dans `lib.py` ne doivent pas être modifiés dans le but de faire passer une implémentation incorrecte.

### Tests automatiques

Afin de vérifier l'implémentation correcte de votre projet, les scripts de test `check_script_options.sh` et `check_tests.sh` sont fournis. Les scripts de test doivent être exécutés depuis la racine du dépôt, dans un terminal Unix :

```bash
./check_script_options.sh
./check_tests.sh
```

Les deux scripts utilisent `sh`. Si le droit d'exécution des fichiers n'est pas disponible, vous pouvez les lancer explicitement avec cet interpréteur :

```bash
sh check_script_options.sh
sh check_tests.sh
```

Le script `check_script_options.sh` vérifie les formes courtes et longues des options. Le script `check_tests.sh` envoie chaque grille de test au programme, demande une itération précise puis utilise `diff` pour comparer la sortie obtenue à la sortie attendue.

Par défaut, ces scripts s'attendent à trouver un script Python `main.py` dans le répertoire courant du terminal qui les lance, mais vous pouvez préciser un script Python arbitraire à tester en le passant en argument des scripts de test :

```bash
./check_script_options.sh autre_programme.py
./check_tests.sh autre_programme.py
```

La réussite des tests fournis est nécessaire, mais elle ne garantit pas que tous les cas limites sont correctement gérés. D'autres grilles pourront être utilisées lors de l'évaluation.

### Scénario 6 : intégration continue (bonus)

Ce scénario est **facultatif** et permet d'obtenir **1 point de bonus**. Il concerne l'automatisation des tests du projet sur GitHub, sans ajouter d'option au programme `main.py`.

Une aide pour [découvrir GitHub Actions](#découvrir-github-actions) est disponible en annexe.

Créez un workflow GitHub Actions dans un fichier YAML du dossier `.github/workflows/`. Ce workflow doit :

- se déclencher automatiquement lors des envois de commits (`push`) et des *Pull Requests* (`pull_request`) ;
- récupérer le contenu du dépôt et disposer de Python 3 dans un environnement Linux ;
- exécuter, depuis la racine du dépôt, `sh check_script_options.sh` et `sh check_tests.sh` pour tester `main.py` ;
- signaler un échec si l'un des scripts se termine avec un code de sortie différent de `0`.

Comme les autres contributions, la mise en place du workflow doit passer par une *Pull Request* relue par un autre membre du groupe. Les éléments à fournir pour valider le bonus sont précisés dans [Le rendu](#le-rendu).

## Le travail en groupe

Le but principal de ce projet est d'évaluer votre capacité à travailler à plusieurs avec Git et GitHub. Vous devez donc conserver une trace visible de ce travail collectif pendant toute la durée du projet.

Avant de commencer à programmer, répartissez le travail en tâches. Par exemple : calcul d'une génération, gestion des conditions périodiques, lecture de la matrice, interface en ligne de commande, sorties texte, génération des images, documentation et tests supplémentaires.

Cette liste est uniquement un exemple. La répartition choisie doit permettre à tous les membres du groupe de produire des contributions utiles et identifiables.

### L'historique Git attendu

Votre historique final est évalué selon les exigences décrites dans cette section. L'[historique final du workshop 3](https://github.com/frozar/git-workshop-3/blob/main/img/historique-final.png) illustre l'organisation attendue des branches et des fusions ; vous n'avez pas à reproduire exactement son nombre de branches ou de commits, ni la disposition de son graphe.

On doit pouvoir observer dans le graphe Git :

- une branche principale `main` ;
- plusieurs branches de développement correspondant au travail des membres du groupe ;
- des commits réalisés par chaque membre ;
- des ponts représentant les fusions des *Pull Requests* ;
- un historique compréhensible, obtenu en rebasant les branches de développement lorsque cela est nécessaire.

Pour chaque nouvelle tâche, créez une branche à partir de votre branche `main` locale à jour par rapport à la branche `main` distante. Réalisez des commits cohérents, puis propagez la branche sur GitHub. Avant la fusion de votre *Pull Request*, mettez à jour vos références et rebasez votre travail si la branche `main` a avancé.

Les commandes correspondantes et la procédure de résolution des conflits sont regroupées dans l'aide [Commandes Git](#commandes-git).

> [!IMPORTANT]
> Sur GitHub, utilisez une fusion qui crée un commit de merge. N'utilisez pas **Squash and merge** ni **Rebase and merge** pour les *Pull Requests* de ce projet : le graphe final doit conserver les ponts représentant le travail réalisé sur les branches.

Ne supprimez pas les branches distantes après leur fusion avant l'évaluation. Elles doivent rester visibles dans l'historique final.

### Les messages de commit

Les règles suivantes adaptent l'article [Bien nommer ses commits de Buzut](https://buzut.net/cours/versioning-avec-git/bien-nommer-ses-commits) à ce projet. Chaque message doit décrire précisément le travail réalisé dans le commit.

La première ligne doit respecter le format `type(portée): sujet`. La portée est facultative : `type: sujet` est également accepté.

- **Longueur** : la première ligne complète, préfixe compris, doit compter **moins de 70 caractères**. Visez environ 50 caractères lorsque cela reste explicite.
- **Type** : choisissez celui qui correspond au changement dans le tableau ci-dessous.
- **Portée** : indiquez, si utile, la partie concernée, par exemple `grille`, `cli` ou `image`.
- **Sujet** : décrivez une action précise, sans majuscule initiale ni point final. Pour ce projet, utilisez l'infinitif en français (`ajouter`, `corriger`) ou l'impératif en anglais (`add`, `fix`). Gardez la même langue dans le groupe. Les messages vagues comme `update`, `corrections` ou `travail terminé` sont insuffisants.
- **Corps** : si le sujet ne suffit pas, ajoutez une ligne vide puis expliquez le changement, sa raison et la différence avec le comportement précédent. Évitez de paraphraser le code.
- **Pied de message facultatif** : référencez une issue associée ou signalez une incompatibilité introduite.

| Type | Usage |
|---|---|
| `feat` | Nouvelle fonctionnalité |
| `fix` | Correction d'un défaut |
| `docs` | Documentation |
| `test` | Tests |
| `refactor` | Réorganisation du code sans changement de comportement |
| `style` | Mise en forme du code |
| `perf` | Optimisation des performances |
| `ci` | Intégration continue |
| `build` | Construction du projet ou dépendances |

Exemple de message court :

```text
feat(cli): ajouter la lecture de la grille depuis stdin
```

Exemple avec un corps :

```text
fix(grille): corriger les voisins aux limites fixes

Les indices négatifs reliaient les bords opposés de la grille.
Ignorer les positions hors grille lorsque le mode périodique
est désactivé afin de respecter les conditions aux limites fixes.
```

Pour les commits de fusion créés par GitHub, conservez le message de fusion généré et veillez à ce que le titre de la *Pull Request* décrive clairement la tâche fusionnée.

### Les Pull Requests

Chaque progression significative doit passer par une *Pull Request* sur GitHub. Un envoi direct de tout le projet sur `main` à la fin du travail ne permet pas d'évaluer la collaboration.

Une progression significative correspond à une tâche cohérente pouvant être relue et vérifiée : par exemple, ajouter la lecture d'une grille, implémenter les conditions périodiques, ajouter des tests ou rédiger une section du `README.md`. Une *Pull Request* peut regrouper plusieurs commits nécessaires à cette tâche. Créez les *Pull Requests* au fil du travail, à mesure que les tâches sont prêtes à être relues.

Une *Pull Request* doit :

- porter un titre explicite ;
- décrire le problème traité et la solution proposée ;
- indiquer comment vérifier le changement ;
- être relue par au moins un autre membre du groupe ;
- prendre en compte les remarques de la revue avant sa fusion ;
- être fusionnée uniquement lorsque les tests passent.

Les contributions et la participation doivent être sensiblement équilibrées entre les membres du groupe. L'évaluation prend en compte la régularité, l'importance et la qualité des changements, les revues et la participation à la résolution des conflits lorsqu'ils se présentent. Un nombre identique de commits par membre n'est pas exigé et ne suffit pas à démontrer cet équilibre.

## Le rendu

Utilisez ce dépôt, `frozar/git-evaluation-jeu-de-la-vie`, comme *template* pour initialiser le dépôt de travail de votre groupe avec le bouton `Use this template` sur la page d'accueil GitHub.

Une seule personne crée le dépôt du groupe, puis ajoute les autres membres comme collaborateurs. Le dépôt rendu doit être public afin que son code, ses branches, ses *Pull Requests* et son historique puissent être consultés. Le nom de votre dépôt devra avoir la forme `git-evaluation-jeu-de-la-vie_groupe-<numéro>` en fonction de votre numéro de groupe. Par exemple pour le groupe 3, le nom du dépôt est `git-evaluation-jeu-de-la-vie_groupe-3`.

Vous devez rédiger un fichier `README.md` destiné aux utilisateur·ices de votre programme. Il doit au minimum contenir les sections suivantes :

- **Installation** : Ce qu'il faut faire pour pouvoir lancer votre programme et générer les vidéos. Si des logiciels tiers sont nécessaires, les procédures d'installation doivent être décrites ici ;
- **Exécution** : Plusieurs exemples d'utilisation de votre programme et les sorties attendues, comme ce qui est fait dans ce document ;
- **Arguments** : La description des options disponibles sur votre programme ;
- **Vidéos** : Les liens YouTube vers les deux vidéos publiques à produire :
  - au moins une vidéo de simulation du jeu de la vie produite avec votre programme `main.py`, à générer et publier à la fin de la partie implémentation du projet. Indiquez les commandes exactes de génération des images et de la vidéo, ainsi que la graine effectivement utilisée ;
  - une vidéo Gource représentant l'évolution de votre dépôt et reflétant un véritable travail de groupe ;
- **Auteurs** : La liste des membres du groupe. Vous devez fournir les nom, prénom et numéro étudiant de chaque membre du groupe ;
- **Liens utiles** : Une liste de ressources en ligne qui vous a été utile pour réaliser ce projet. Cette liste doit être sous la même forme que la section [Liens utiles](#liens-utiles) de ce document.

Le dépôt final doit notamment contenir le programme terminé dans `main.py`, le fichier `lib.py`, les scripts et les données de test fournis sans altération, ainsi que le fichier `README.md` rédigé par le groupe. Si vous réalisez le scénario 6, le workflow doit être versionné dans `.github/workflows/`. Une exécution réussie des deux scripts doit être consultable dans l'onglet **Actions** de GitHub et son lien doit figurer dans votre `README.md`.

Les images et les vidéos générées peuvent être volumineuses. Elles ne doivent pas être versionnées dans Git, y compris le fichier intermédiaire `gource.ppm` si vous l'utilisez. Pour exclure ces fichiers, vous pouvez utiliser le fichier `.gitignore`.

Assurez-vous que le dépôt et les vidéos sont accessibles en public, et non uniquement par les membres du groupe. Pour réaliser les vidéos, consultez les tutoriels [Jeu de la vie](#générer-une-vidéo-du-jeu-de-la-vie) et [Gource](#gource).

**Date de rendu du projet :** Vous devez m'envoyer un mail contenant l'adresse URL de votre dépôt public GitHub avant mardi 24 novembre 2026, 23h59. Vous perdrez un point par jour de retard.

Mon adresse mail : fabien.rozar@gmail.com

<ins>Remarque :</ins> Je vous encourage vivement de mettre vos collègues en copie du mail de rendu.

## Le barème

L'évaluation prendra notamment en compte :

 - La rédaction du `README.md` conforme à la consigne : 1 point,
 - Respect des noms du dépôt et du programme pour les travaux réalisés : 1 point,
 - Exécution sans erreur du script `check_script_options.sh` : 1 point,
 - Exécution sans erreur du script `check_tests.sh` : 1 point,
 - Réalisation correcte des scénarios 1 à 5 : exécution du programme pour les scénarios 1 à 4, puis production des images et assemblage en une vidéo MP4 lisible avec `ffmpeg` pour le [scénario 5](#scénario-5--génération-dune-vidéo) : 1 point,
 - Exécution correcte de votre programme sur des scénarios non exposés dans ce document : 3 points,
 - Mise en place de l'intégration continue conforme au [scénario 6](#scénario-6--intégration-continue-bonus) : 1 point **(bonus facultatif)**,
 - Respect des contraintes décrites dans [Les messages de commit](#les-messages-de-commit) : 2 points,
 - Équilibre des contributions et de la participation entre les membres du groupe, selon les critères décrits dans [Le travail en groupe](#le-travail-en-groupe) : 1 point,
 - Respect des exigences de la section [L'historique Git attendu](#lhistorique-git-attendu) : branche `main`, branches de développement, commits de chaque membre, fusions visibles et historique compréhensible avec rebase lorsque nécessaire : 4 points,
 - Pour chaque progression, utilisation d'une *Pull Request* sur GitHub respectant les exigences de la section [Les Pull Requests](#les-pull-requests), notamment la description, la vérification et la revue par un autre membre : 3 points,
 - Publication sur YouTube de la vidéo générée par l'utilitaire [gource](https://gource.io/) correspondante à votre activité sur ce dépôt, accessible en public et liée depuis le `README.md` conformément à la section [Le rendu](#le-rendu) : 1 point,
 - Publication sur YouTube de la vidéo de simulation produite au [scénario 5](#scénario-5--génération-dune-vidéo), accessible en public et liée depuis le `README.md` conformément à la section [Le rendu](#le-rendu) : 1 point.

Un programme correct accompagné d'un historique qui ne montre pas un travail collectif ne peut pas obtenir la note maximale. À l'inverse, un bel historique Git ne remplace pas un programme fonctionnel : le fond et la méthode de travail sont tous les deux évalués.

## Aides techniques

Ces aides regroupent les procédures et les exemples de commandes à consulter au fil du travail. Les exigences du projet et les éléments à rendre sont décrits dans les sections précédentes.

### Préparer son environnement

Les scripts fournis utilisent `sh` ainsi que des commandes Unix comme `cat`, `diff`, `find` et `mktemp`. Les vidéos nécessitent `ffmpeg` et Gource.

#### Ubuntu ou Debian

Installez les outils nécessaires :

```bash
sudo apt update
sudo apt install python3 git gource ffmpeg
```

#### macOS

Pour les vidéos, installez Gource et `ffmpeg` avec [Homebrew](https://brew.sh/) :

```bash
brew install gource ffmpeg
```

#### Windows

Pour les utilisateur·ices de Windows, je vous recommande d'installer [WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install) afin d'avoir accès à un terminal similaire à un terminal Unix.

Depuis un terminal PowerShell ouvert en tant qu'administrateur :

```powershell
wsl --install
```

Redémarrez l'ordinateur si cela vous est demandé, ouvrez ensuite la distribution Ubuntu, puis exécutez les commandes de la section [Ubuntu ou Debian](#ubuntu-ou-debian) dans le terminal WSL. Une installation récente de Windows 11 avec WSLg permet normalement d'afficher la fenêtre de prévisualisation de Gource.

Depuis WSL, les disques Windows sont montés dans `/mnt`. Par exemple, le dossier Windows `C:\Users\Alice\projet` est accessible avec :

```bash
cd /mnt/c/Users/Alice/projet
```

#### Vérifier les outils vidéo

```bash
gource --version
ffmpeg -version
```

### Lecture des arguments avec argparse

Le module [`argparse`](https://docs.python.org/fr/3/library/argparse.html), inclus dans la bibliothèque standard de Python, facilite la lecture des paramètres passés en ligne de commande. Son utilisation est **fortement conseillée** pour ce projet : il permet de déclarer les options courtes et longues, de convertir leurs valeurs, de définir les valeurs par défaut et de générer automatiquement un message d'aide.

Une fois que la lecture des arguments est configurée avec `argparse`, vous pouvez vérifier l'aide produite par votre programme avec :

```bash
python3 main.py --help
```

Toutes les options décrites dans la section [Les arguments du programme](#les-arguments-du-programme) doivent être implémentées. Avec `argparse`, `type=int` vérifie qu'une valeur est entière ; vous devez également vérifier les contraintes de signe imposées à `--nb_cells` et à `--max_iterations`.

### Le pipe Unix

Dans [la tradition d'Unix](https://fr.wikipedia.org/wiki/Philosophie_d%27Unix), tout programme devrait présenter une interface *texte*, l'interface universelle, lui permettant de recevoir ses entrées depuis la sortie d'un autre programme sous forme de chaînes de caractères. Ainsi, le programme peut être composé avec d'autres programmes pour en fabriquer de nouveaux.

Pour composer deux programmes, il faut utiliser [un pipe (ou tube)](https://en.wikipedia.org/wiki/Pipeline_(Unix)), représenté par le caractère `|`. Par exemple :

```bash
programme1 | programme2 | programme3
```

`programme3` lit son entrée depuis la sortie de `programme2`, et `programme2` lit son entrée depuis la sortie de `programme1`. On peut dire que `programme1 | programme2 | programme3` est un nouveau programme, *composé* à partir de trois autres programmes.

Les scénarios 3 et 4 utilisent `cat tests/matrix3/input.txt |` pour envoyer le contenu du fichier sur l'entrée standard du programme Python. Le pipe du scénario 3 peut aussi être remplacé par une redirection :

```bash
python3 main.py -m 1 -t text < tests/matrix3/input.txt
```

En Python, `sys.stdin.isatty()` permet de savoir si l'entrée standard est reliée au terminal. La valeur est généralement `False` lorsqu'une entrée est fournie avec un pipe ou une redirection. Vous pouvez alors lire l'ensemble du flux avec `sys.stdin.read()`.

### Commandes Git

Pour chaque nouvelle tâche, créez une branche à partir d'une branche `main` à jour :

```bash
git switch main
git pull
git switch -c prenom-nom/nom-de-la-tache
```

Réalisez ensuite des commits cohérents, puis propagez la branche sur GitHub :

```bash
git push -u origin prenom-nom/nom-de-la-tache
```

Avant la fusion de votre *Pull Request*, mettez à jour vos références et rebasez votre travail si la branche `main` a avancé :

```bash
git fetch origin
git switch prenom-nom/nom-de-la-tache
git rebase origin/main
git push --force-with-lease
```

L'option `--force-with-lease` est nécessaire après un *rebase*, car les identifiants des commits ont changé. Elle est préférable à `--force`, car elle refuse d'écraser un travail distant que vous n'auriez pas récupéré.

En cas de conflit pendant un *rebase* :

```bash
git status
# Modifiez les fichiers en conflit.
git add <fichier-resolu>
git rebase --continue
```

La commande `git rebase --abort` permet d'annuler le *rebase* et de revenir à la situation précédente si nécessaire.

### Visualisation de l'historique

Visualisez régulièrement votre historique, et pas uniquement la veille du rendu. Pour cela, utilisez l'extension **Git Graph** de **Visual Studio Code**, que vous avez tous installée et que nous avons largement utilisée pendant le cours.

Ouvrez le dossier contenant votre dépôt dans VSCode, puis affichez son historique avec Git Graph. Le graphe permet de suivre les branches, les commits et les fusions. Vérifiez au fur et à mesure que vos contributions et les ponts de fusion attendus sont visibles, en vous appuyant sur l'organisation présentée dans le [workshop 3](https://github.com/frozar/git-workshop-3).

### Générer une vidéo du jeu de la vie

Après avoir [installé les outils vidéo](#préparer-son-environnement), vous pouvez suivre cet exemple pour le scénario 5.

Depuis la racine du dépôt, dans un terminal sans pipe ni redirection de l'entrée standard, exécutez les commandes suivantes après avoir implémenté `main.py` :

```bash
mkdir -p outputs/video-seed-4200
python3 main.py --nb_cells 50 --max_iterations 2000 --seed 4200 \
  --output_type image --output_directory outputs/video-seed-4200
ffmpeg -y -framerate 20 -start_number 0 \
  -i outputs/video-seed-4200/grid_%04d.png -frames:v 2001 \
  -c:v libx264 -pix_fmt yuv420p -movflags +faststart \
  outputs/video-seed-4200/game-of-life.mp4
```

- `mkdir -p` crée le dossier de destination s'il n'existe pas.
- `--nb_cells 50` fixe une grille de 50 cellules par côté et `--seed 4200` fixe explicitement la graine aléatoire. L'option `--periodic` est omise : les conditions aux limites sont fixes. Avec la même implémentation et ces mêmes paramètres, la simulation doit reproduire les mêmes générations à chaque exécution.
- `--max_iterations 2000` produit **2001 images**, de `grid_0000.png` à `grid_2000.png`, génération initiale comprise. Le programme doit annoncer `Generation of 2001 images in directory outputs/video-seed-4200`.
- `-start_number 0` commence à la génération initiale et le motif `%04d` lit les numéros sur quatre chiffres dans l'ordre. `-frames:v 2001` limite la vidéo aux 2001 images attendues, même si le dossier contient des images d'une exécution plus longue.
- `-framerate 20` fixe la cadence à **20 images par seconde**, soit une durée de **100,05 secondes** (1 minute et 40,05 secondes).
- `-c:v libx264` encode en H.264 et `-pix_fmt yuv420p` choisit le format de pixels. `-movflags +faststart` place les informations de lecture au début du MP4. `-y` autorise le remplacement de la vidéo existante lors d'une nouvelle exécution.

Ouvrez `outputs/video-seed-4200/game-of-life.mp4` dans un lecteur vidéo pour vérifier le résultat. Les exigences de publication et les informations à reporter dans le `README.md` figurent dans [Le rendu](#le-rendu).

### Gource

[`Gource`](https://gource.io/) représente l'historique d'un dépôt sous la forme d'une animation. Les fichiers apparaissent dans un arbre, tandis que les contributeur·ices sont représenté·es autour du projet. L'activité visible dans cette animation doit refléter un véritable travail de groupe.

Les instructions d’installation sont regroupées dans [Préparer son environnement](#préparer-son-environnement).

Pour prévisualiser l'historique, placez-vous à la racine du dépôt puis lancez `gource`. La touche `Espace` permet de mettre l'animation en pause et la touche `Échap` permet de quitter.

Pour générer directement une vidéo MP4, la sortie de Gource peut être envoyée à `ffmpeg` avec un pipe Unix :

```bash
gource -s 2 -r 60 --file-font-size 8 \
  --title 'Jeu de la vie' --filename-time 2 \
  --stop-at-end --hide date,usernames -o - | \
ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i - \
  -vcodec libx264 -preset medium -pix_fmt yuv420p \
  -crf 18 -threads 0 -bf 0 gource.mp4
```

Dans cette commande, Gource écrit les images au format PPM sur `STDOUT`. Le caractère `|` transmet ce flux à `ffmpeg`, qui le lit sur `STDIN` grâce à `-i -` et produit le fichier `gource.mp4`.

Si votre ordinateur ne parvient pas à produire la vidéo en temps réel, vous pouvez passer par un fichier intermédiaire :

```bash
gource -s 2 -r 60 --file-font-size 8 \
  --title 'Jeu de la vie' --filename-time 2 \
  --stop-at-end --hide date,usernames -o gource.ppm

ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i gource.ppm \
  -vcodec libx264 -preset medium -pix_fmt yuv420p \
  -crf 18 -threads 0 -bf 0 gource.mp4
```

Le fichier `gource.ppm` peut être très volumineux : supprimez-le après avoir vérifié la vidéo MP4. Les exigences de publication et les fichiers à exclure de Git sont précisés dans [Le rendu](#le-rendu).

### Découvrir GitHub Actions

Pour découvrir GitHub Actions, vous pouvez suivre le [module de formation sur Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/github-actions-automate-tasks/) et son [exercice de création et d'exécution d'un workflow](https://learn.microsoft.com/en-us/training/modules/github-actions-automate-tasks/3-exercise-create-container-action). Ces ressources servent de préparation ; le bonus porte sur l'intégration continue mise en place dans le dépôt de votre groupe.

## Liens utiles

- [Workshop 3 : rebase et historique final](https://github.com/frozar/git-workshop-3) : décrit l'organisation Git attendue pour ce projet,
- [Historique final du workshop 3](https://github.com/frozar/git-workshop-3/blob/main/img/historique-final.png) : exemple du graphe à obtenir,
- [Jeu de la vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie) : présentation des règles du jeu de Conway,
- [Documentation argparse](https://docs.python.org/fr/3/library/argparse.html) : analyse des arguments d'un script Python,
- [Documentation random](https://docs.python.org/fr/3/library/random.html) : génération de grilles aléatoires reproductibles,
- [Philosophie d'Unix](https://fr.wikipedia.org/wiki/Philosophie_d%27Unix) : description de la philosophie Unix,
- [Pipeline (Unix)](https://en.wikipedia.org/wiki/Pipeline_(Unix)) : description du pipe,
- [Installation de WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install) : procédure officielle pour Windows,
- [Documentation ffmpeg](https://ffmpeg.org/documentation.html) : installation et utilisation de `ffmpeg`,
- [Site officiel de Gource](https://gource.io/) : présentation et téléchargement de Gource,
- [My Gource video production pipeline](https://dev.to/voieducode/my-gource-video-production-pipeline-5eb0) : exemple de création d'une vidéo Gource,
- [Documentation officielle de git rebase](https://git-scm.com/book/fr/v2/Les-branches-avec-Git-Rebaser-Rebasing) : fonctionnement du *rebase*.
