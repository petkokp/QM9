from pathlib import Path
import numpy as np
import random
import pandas as pd
import tqdm
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

def parse_xyz_file(file_path):
    properties = {}

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            # 1 row: number of atoms
            n_atoms = lines[0].strip().split()
            properties['filename'] = Path(file_path).stem
            properties['n_atoms'] = int(n_atoms[0])

            # 2 row: the line of the properties
            properties_line = lines[1].strip().split()

            # Extract properties into the dictionary
            properties['index'] = int(properties_line[1])
            properties['A'] = float(properties_line[2])
            properties['B'] = float(properties_line[3])
            properties['C'] = float(properties_line[4])
            properties['mu'] = float(properties_line[5])
            properties['alpha'] = float(properties_line[6])
            properties['homo'] = float(properties_line[7])
            properties['lumo'] = float(properties_line[8])
            properties['gap'] = float(properties_line[9])
            properties['R2'] = float(properties_line[10])
            properties['zpve'] = float(properties_line[11])
            properties['U0'] = float(properties_line[12])
            properties['U'] = float(properties_line[13])
            properties['H'] = float(properties_line[14])
            properties['G'] = float(properties_line[15])
            properties['Cv'] = float(properties_line[16])
    except Exception as e:
        print(f"Error processing xyz file {file_path}: {e}")
        return None

    return properties

def create_dataframe_from_xyz(folder_path, subset_size=None):
    folder_path = Path(folder_path)
    all_files = list(folder_path.glob('*.xyz'))

    if subset_size and subset_size < len(all_files):
        subset_files = random.sample(all_files, subset_size)
    else:
        subset_files = all_files

    data = []
    for file_path in tqdm(subset_files):
        properties = parse_xyz_file(file_path)
        if properties is not None:
            data.append(properties)

    df = pd.DataFrame(data)
    return df
