from pathlib import Path
import numpy as np
from .periodic_table import PERIODIC_TABLE

def read_xyz(filename: Path):
    periodic_table = PERIODIC_TABLE

    with open(str(filename), "r") as f:
        lines = f.readlines()
        num_atoms = int(lines[0].strip())
        atom_data = lines[2 : 2 + num_atoms]

    atomic_numbers = []
    coordinates = []

    for line in atom_data:
        parts = line.split()
        element = parts[0]
        x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
        atomic_numbers.append(periodic_table[element])
        coordinates.append([x, y, z])

    return np.array(atomic_numbers), np.array(coordinates)