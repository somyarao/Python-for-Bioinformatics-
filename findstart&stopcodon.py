# Functions to find the start codon and stop codon
# defining_function_for_start_codon
def find_start_codon(rna_seq):
    start_codon = "AUG"
    start_index = rna_seq.find(start_codon)
    return start_index


# defining_function_for_stop_codon
def find_stop_codon(rna_seq):
    stop_codons = ["UAA", "UAG", "UGA"]
    for stop_codon in stop_codons:
        stop_index = rna_seq.find(stop_codon)
    if stop_index != -1:
        return stop_index
    return -1


# usage_Input_mRNA_sequence
rna_seq = "AUGGUACCUUAAAGGGCUAGAGTCGAAAUAGCGUAGUCG"
start_index = find_start_codon(rna_seq)
stop_index = find_stop_codon(rna_seq)

if start_index != -1:
    print(f"Start codon found at index {start_index}")
else:
    print("Start codon not found in the sequence")

if stop_index != -1:
    print(f"Stop codon found at index {stop_index}")
else:
    print("Stop codon not found in the sequence")
