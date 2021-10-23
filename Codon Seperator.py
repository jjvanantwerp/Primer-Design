fin_name = input("In File Name: ")
primer_name = ""
DNA = ""
Modified_DNA=""
with open(fin_name, "r") as fin:
    for line in fin:
        line = line[0:-1]
        if line[0]==">":
            primer_name = line
        else:
            DNA+=line
i = 0
Final_DNA = (primer_name)

for pos in range(len(DNA)):
    # Add a line for numbering codons
    if ((pos%30) == 0):
        Modified_DNA += '\n\n'
        for j in range(10):
            i+=1
            if (i<=9):
                Modified_DNA += str(i)
                Modified_DNA += "    "
            elif (i>9 and i<=99):
                Modified_DNA += str(i)
                Modified_DNA += "   "
            elif (i>99 and i<=len(DNA)/3):
                Modified_DNA += str(i)
                Modified_DNA += "  "
        Modified_DNA += '\n'
    # Write codons, with a break between every three.
    if ((pos+1)%3 == 0):
        Modified_DNA += (DNA[pos]+"  ")
    else:
        Modified_DNA += DNA[pos]
Final_DNA += Modified_DNA
fout_name = fin_name+" Seperated"
with open(fout_name, "w+") as fout:
    fout.write(Final_DNA)
