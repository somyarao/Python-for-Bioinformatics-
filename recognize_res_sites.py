# Function for recognizing restriction sites in a DNA sequence.
#define_the_function_for_recognizing_restriction_site
def find_recognition_sites(dna_seq, recognition_site):
 sites = []
 site_length = len(recognition_site)

 for i in range(len(dna_seq) - site_length + 1):
     if dna_seq[i:i + site_length] != recognition_site:
         pass
     else:
         sites.append(i)

 return sites

#usage:
dna_seq = "AATGCTAGCTAGCTGCTAGCTGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"
recognition_site = "GCTAGC"

site_positions = find_recognition_sites(dna_seq, recognition_site)

if site_positions:
 print(f"Recognition site '{recognition_site}' found at positions: {', '.join(map(str, site_positions))}")
else:
 print(f"Recognition site '{recognition_site}' not found in the sequence.")