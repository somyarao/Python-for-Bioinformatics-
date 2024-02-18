# Function to find the overlapping region between two DNA sequences.
def find_overlap(seq1, seq2):
 overlap = 0
 for i in range(1, min(len(seq1), len(seq2)) + 1):
     if seq1[-i:] == seq2[:i]:
         overlap = i
 return overlap

def extract_overlap(seq1, seq2, overlap):
 return seq1 + seq2[overlap:]

#usage
seq1 = "TCGGTCACTTACGAGCGTTAGG"
seq2 = "CGTTAGGCGGTAACCCCTTAAAGTCGG"

overlap = find_overlap(seq1, seq2)
if overlap > 0:
 overlapping_seq = extract_overlap(seq1, seq2, overlap)
 print(f"No of bases that overlap between the two sequences: {overlap} bases")
 print(f"The new overlapping sequence: {overlapping_seq}")
 print(f"Overlapped portion: {seq2[:overlap]}")
else:
 print("No overlap found between the two sequences.")