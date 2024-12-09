def create_codon_dict(file_path):
    amino_acid_dict = {} 
    for row in rows:
        row_cells = row.strip().split('\t')
        if len(row_cells) >= 3:
          codon = row_cells[0]
          amino_acid = row_cells[2]
          amino_acid_dict[codon] = amino_acid


