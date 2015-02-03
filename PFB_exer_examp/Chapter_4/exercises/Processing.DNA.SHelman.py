#Open input file
file = open("input.txt")

#Open output file
output = open("trim.txt", "w")

#Remove adaptor loop:
for dna in file:
    trim_dna = dna[14:]    #trim 1st 14 bits
    trim_length = len(trim_dna) - 1    #length of sequence
    output.write(trim_dna)    #write to file
    print("processed sequence with length " + str(trim_length))
