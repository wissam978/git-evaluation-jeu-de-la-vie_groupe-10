#!/usr/bin/env python3
"""Jeu de la vie en ligne de commande."""

import argparse
import os
import random
import sys

from lib import write_grid


# ---------------------------------------------------------------------------
# Lecture des arguments
# ---------------------------------------------------------------------------

def positive_int(value):
    """Entier strictement positif (pour argparse)."""
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"entier attendu, reçu '{value}'")
    if number <= 0:
        raise argparse.ArgumentTypeError(
            f"l'entier doit être strictement positif, reçu {number}")
    return number


def non_negative_int(value):
    """Entier positif ou nul (pour argparse)."""
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"entier attendu, reçu '{value}'")
    if number < 0:
        raise argparse.ArgumentTypeError(
            f"l'entier doit être positif ou nul, reçu {number}")
    return number


def parse_args(argv=None):
    """Lit les arguments de la ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Simulation du jeu de la vie sur une grille carrée.")
    parser.add_argument("-n", "--nb_cells", type=positive_int, default=10,
                        metavar="N",
                        help="cellules par côté d'une grille aléatoire (défaut : 10)")
    parser.add_argument("-m", "--max_iterations", type=non_negative_int,
                        default=20, metavar="N",
                        help="numéro de la dernière itération (défaut : 20)")
    parser.add_argument("-s", "--seed", type=int, default=42, metavar="N",
                        help="graine du générateur aléatoire (défaut : 42)")
    parser.add_argument("-o", "--output_directory", default="outputs",
                        metavar="DOSSIER",
                        help="dossier des images (défaut : outputs)")
    parser.add_argument("-t", "--output_type", choices=["image", "text"],
                        default="image", metavar="TYPE",
                        help="type de sortie : image ou text (défaut : image)")
    parser.add_argument("-p", "--periodic", action="store_true",
                        help="conditions aux limites périodiques")
    return parser.parse_args(argv)


# ---------------------------------------------------------------------------
# Grille initiale
# ---------------------------------------------------------------------------

def random_grid(size, seed):
    """Grille aléatoire reproductible (même graine, même grille)."""
    rng = random.Random(seed)
    return [[rng.choice([0, 1]) for _ in range(size)] for _ in range(size)]


def parse_grid(text):
    """Convertit le texte reçu sur STDIN en grille. Lève ValueError."""
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        raise ValueError("grille vide")
    try:
        size = int(lines[0].strip())
    except ValueError:
        raise ValueError(f"taille invalide : '{lines[0].strip()}'")
    if size <= 0:
        raise ValueError(f"la taille doit être strictement positive : {size}")
    rows = lines[1:]
    if len(rows) != size:
        raise ValueError(
            f"{size} lignes attendues, {len(rows)} reçues")
    grid = []
    for number, row in enumerate(rows, start=1):
        cells = row.split()
        if len(cells) != size:
            raise ValueError(
                f"ligne {number} : {size} cellules attendues, "
                f"{len(cells)} reçues")
        for cell in cells:
            if cell not in ("0", "1"):
                raise ValueError(
                    f"ligne {number} : cellule invalide '{cell}' "
                    f"(0 ou 1 attendu)")
        grid.append([int(cell) for cell in cells])
    return grid


def read_stdin_grid():
    """Renvoie la grille lue sur STDIN, ou None si rien n'est fourni."""
    if sys.stdin is None or sys.stdin.isatty():
        return None
    text = sys.stdin.read()
    if not text.strip():
        return None
    return parse_grid(text)


# ---------------------------------------------------------------------------
# Calcul d'une génération
# ---------------------------------------------------------------------------

def count_neighbors(grid, row, col, periodic):
    size = len(grid)
    total = 0
    for d_row in (-1, 0, 1):
        for d_col in (-1, 0, 1):
            if d_row == 0 and d_col == 0:
                continue
            r, c = row + d_row, col + d_col
            if periodic:
                r, c = r % size, c % size
            elif not (0 <= r < size and 0 <= c < size):
                continue
            total += grid[r][c]
    return total


def next_cell(alive, neighbors):
    if alive:
        return 1 if neighbors in (2, 3) else 0
    return 1 if neighbors == 3 else 0


def next_generation(grid, periodic):
    """Nouvelle grille calculée à partir de la grille courante (non modifiée)."""
    size = len(grid)
    return [[next_cell(grid[r][c], count_neighbors(grid, r, c, periodic))
             for c in range(size)] for r in range(size)]


def compute_generations(grid, max_iterations, periodic):
    """Génère les grilles des itérations 0 à max_iterations incluses."""
    yield grid
    for _ in range(max_iterations):
        grid = next_generation(grid, periodic)
        yield grid


# ---------------------------------------------------------------------------
# Sorties
# ---------------------------------------------------------------------------

def write_images(generations, directory):
    os.makedirs(directory, exist_ok=True)
    count = 0
    for number, grid in enumerate(generations):
        filename = os.path.join(directory, f"grid_{number:04d}.png")
        write_grid(matrix=grid, filename=filename)
        count = number + 1
    print(f"Generation of {count} images in directory {directory}")


def write_text(generations, max_iterations):
    last = None
    for last in generations:
        pass
    print(f"iteration: {max_iterations}")
    for row in last:
        print(" ".join(str(cell) for cell in row))


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    try:
        grid = read_stdin_grid()
    except ValueError as error:
        print(f"Erreur : {error}", file=sys.stderr)
        return 1
    if grid is None:
        grid = random_grid(args.nb_cells, args.seed)

    generations = compute_generations(grid, args.max_iterations, args.periodic)
    try:
        if args.output_type == "image":
            write_images(generations, args.output_directory)
        else:
            write_text(generations, args.max_iterations)
    except OSError as error:
        print(f"Erreur : {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
