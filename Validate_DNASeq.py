# Function to validate DNA sequences.
def validate_base_sequence(dna_seq):
    # define_a_set_of_valid_nucleotide_bases
    valid_bases = {'A', 'T', 'G', 'C'}

    # check_if_all_characters_in_the_DNA_sequence_are_in_the_valid_bases_set
    return all(base in valid_bases for base in dna_seq)


# usage:

seq1 = "ATGCTGTAGGTAAGTAAGCG"
seq2 = "ATGXGMGGGTCTA"

if validate_base_sequence(seq1):
    print(f"seq1 is a valid DNA sequence.")
else:
    print(f"seq1 contains invalid bases.")

if validate_base_sequence(seq2):
    print(f"seq2 is a valid DNA sequence.")
else:
    print(f"seq2 contains invalid bases.")
