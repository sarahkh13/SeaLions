#Open files
genomic_dna = open("genomic_dna.txt").read()
exons_file = open("exons.txt")

code_file = ""

# go through each line in the exon locations file
for line in exons_file:
    positions = line.split(',')

    start = int(positions[0])
    stop = int(positions[1])

    exon = genomic_dna[start:stop]
    code_file = code_file + exon


#Write to an output file
output = open("code_file.txt", "w")
output.write(code_file)
output.close()
