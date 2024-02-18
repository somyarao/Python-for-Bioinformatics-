#Function to calculate the GC content for any DNA sequence.

# METHOD 01
# defining_a_function_to_calculate_GC_content_in_the_DNA_sequence
def gc_content(base_seq):
    seq = base_seq.upper()
    return (seq.count('G') + seq.count('C')) / len(seq)

# usage:
seq60 = "AATTCCCGGG"
gc_content(seq60)
hashtag  # output
0.6

# METHOD 02
def calculate_gc_content(sequence):
    # Count the number of 'G' and 'C' characters in the sequence
    gc_count = sequence.count('G') + sequence.count('C')

    # Calculate_the_total_length_of_the_sequence
    sequence_length = len(sequence)

    # Calculate_the_GC_content_as_a_percentage
    gc_content = (gc_count / sequence_length) * 100.0

    return gc_content


# usage:
dna_sequence = "ATGCGCTAGCTAGCTGCTAGCTGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCT"
gc_percentage = calculate_gc_content(dna_sequence)
print(f"GC Content: {gc_percentage:.2f}%")