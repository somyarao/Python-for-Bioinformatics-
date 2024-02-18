# Function for comparing two DNA sequences of equal length and calculating their percentage identity.
def compare_dna_seq(seq1, seq2):
 if len(seq1) != len(seq2):
     return None

 matching_nucleotides = 0
 total_nucleotides = len(seq1)

 for i in range(total_nucleotides):
     if seq1[i] == seq2[i]:
         matching_nucleotides += 1

 if total_nucleotides > 0:
     percentage_identity: float = (matching_nucleotides / total_nucleotides) * 100
 else:
     percentage_identity = 0

 return percentage_identity

#usage:
seq1 = "ATGCTGCATAGCGATAA"
seq2 = "ATGCTCGTATAGCGTAA"
identity = compare_dna_seq(seq1, seq2)

if identity is not None:
 print("Percentage Identity:", f"{identity:.2f}%")
else:
 print("Sequences have different lengths and cannot be compared.")