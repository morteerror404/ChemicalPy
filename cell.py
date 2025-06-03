import AminoAcids, protein

class Cell:
    def __init__(self, name, protein):
        self.name = name
        self.protein = protein

def create_cells_from_file(file_path, AminoAcids, protein):
    cells = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                name = data[0]
                protein_names = data[1:]
                cell_protein = [protein for protein in protein if protein.name in protein_names]
                cell = Cell(name, cell_protein)
                cells.append(cell)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return cells

file_path = 'cells.csv'
cells = create_cells_from_file(file_path, AminoAcids, protein)

def calculate_cell_protein_mass(cell, AminoAcids):
    total_mass = 0
    for protein in cell.proteins:  # Assuming it's 'proteins' not 'protein'
        total_mass += sum(amino_acid.molecular_weight 
                         for amino_acid in AminoAcids 
                         if amino_acid.name in protein.amino_acid_composition)
    return total_mass