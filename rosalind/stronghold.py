"""
"""

sample_dataset = 'rosalind_rna.txt'
#sample_output = 'GAUGGAACUUGACUACGUAAAUU'

def dna(dna_string: str, file=False) -> tuple[int]:
    """Function to count nucleotides in a DNA string.

    Args:
        dna_string (str): a string of DNA sequence (A, T, C, G).
        file (bool): True if dna_string is a file.
                    (default) False: dna_string is a string of nucleotides.

    Returns:
        tuple[int]: number of nucleotides in the order (A, T, C, G).
    """
    if file:
        with open(dna_string, 'r') as dna_file:
            dna_string = str(dna_file.read())
    
    if len(dna_string) > 1000:
        print(f"This DNA string is too long. This function deals with\
              1000 caracters at most.")
    
    a, t, c, g = 0, 0, 0, 0
    
    for char in dna_string:
        if char.lower() == 'a': a+=1
        elif char.lower() == 't': t+=1
        elif char.lower() == 'c': c+=1
        elif char.lower() == 'g': g+=1

    
    
    print(f"{a} {c} {g} {t}")
    
    return a, c, g, t


def rna(dna_string: str, file=False) -> str:
    """Function make RNA transcription from a DNA string.

    Args:
        dna_string (str): a string of DNA sequence (A, T, C, G).
        file (bool): True if dna_string is a file.
                    (default) False: dna_string is a string of nucleotides.

    Returns:
        str: String of the corresponding transcripted RNA.
    """
    if file:
        with open(dna_string, 'r') as dna_file:
            dna_string = str(dna_file.read())

    if len(dna_string) > 1000:
        print(f"This DNA string is too long. This function deals with\
              1000 caracters at most.")
    
    rna = []
    
    for char in dna_string:
        rna.append('U') if char.lower() == 't' else rna.append(char)
    
    rna = ''.join(rna)
    
    print(f"{rna}")
    
    return rna


rna(sample_dataset, True)