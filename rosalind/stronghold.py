"""
"""

sample_dataset = 'rosalind_revc.txt'
sample_output = 'ACCGGGTTTT'

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
    
    nucs = {'a': 0, 't': 0, 'c': 0, 'g': 0}
    
    for char in dna_string:
        if char != '\n':
            nucs[char.lower()] += 1
        else:
            break
    
    
    print(f"{nucs['a']} {nucs['c']} {nucs['g']} {nucs['t']}")
    
    return nucs['a'], nucs['c'], nucs['g'], nucs['t']


def rna(dna_string: str, file=False) -> str:
    """Function make rna transcription from a DNA string.

    Args:
        dna_string (str): a string of DNA sequence (A, T, C, G).
        file (bool): True if dna_string is a file.
                    (default) False: dna_string is a string of nucleotides.

    Returns:
        str: String of the corresponding transcripted rna.
    """
    if file:
        with open(dna_string, 'r') as dna_file:
            dna_string = str(dna_file.read())

    if len(dna_string) > 1000:
        print(f"This DNA string is too long. This function deals with\
              1000 caracters at most.")
    
    rna = ''.join([char.replace('T', 'U') for char in dna_string])[::-1]
    
    print(f"{rna}")
    return rna


def revc(dna_string: str, file=False) -> str:
    """Function the reverse complementary of a DNA string.

    Args:
        dna_string (str): a string of DNA sequence (A, T, C, G).
        file (bool): True if dna_string is a file.
                    (default) False: dna_string is a string of nucleotides.

    Returns:
        str: String of the corresponding reverse complementary revc.
    """
    if file:
        with open(dna_string, 'r') as dna_file:
            dna_string = str(dna_file.read())

    if len(dna_string) > 1000:
        print(f"This DNA string is too long. This function deals with\
              1000 caracters at most.")
    
    pairs = {'a': 'T', 't': 'A', 'c': 'G', 'g': 'C'}
    
    revc = ''.join([pairs[char.lower()]\
                  for char in dna_string\
                  if char.lower() not in {'\n', 'u'}][::-1])
    
    print(f"{revc}")
    return revc


def fib():
    pass
revc(sample_dataset, True)