#!/usr/bin/env python3
"""Jeu de la vie en ligne de commande."""

import argparse
import os
import random
import sys

from lib import write_grid


def positive_int(value):
    """Entier strictement positif (pour argparse)."""
    raise NotImplementedError


def non_negative_int(value):
    """Entier positif ou nul (pour argparse)."""
    raise NotImplementedError


def parse_args(argv=None):
    """Lit les arguments de la ligne de commande."""
    raise NotImplementedError


def random_grid(size, seed):
    """Grille aléatoire reproductible."""
    raise NotImplementedError


def parse_grid(text):
    """Convertit le texte de STDIN en grille."""
    raise NotImplementedError


def read_stdin_grid():
    """Renvoie la grille lue sur STDIN, ou None."""
    raise NotImplementedError


def count_neighbors(grid, row, col, periodic):
    """Compte les voisines vivantes d'une cellule."""
    raise NotImplementedError


def next_cell(alive, neighbors):
    """Applique les règles à une cellule."""
    raise NotImplementedError


def next_generation(grid, periodic):
    """Calcule la génération suivante."""
    raise NotImplementedError


def compute_generations(grid, max_iterations, periodic):
    """Produit les grilles des itérations 0 à max_iterations."""
    raise NotImplementedError


def write_images(generations, directory):
    """Écrit une image par génération."""
    raise NotImplementedError


def write_text(generations, max_iterations):
    """Écrit la dernière itération sur STDOUT."""
    raise NotImplementedError


def main():
    """Point d'entrée du programme."""
    raise NotImplementedError


if __name__ == "__main__":
    sys.exit(main())
