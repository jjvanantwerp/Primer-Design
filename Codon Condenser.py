fin_name = input("In File Name: ")
#fin_name = "Node 93 DNA Seperated with Degenerate Codons.txt"
Final_Primer_Fasta = ""
codon_list=[]
codon_switcher = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TGC':'C', 'TGT':'C',
    'TAA':' stop ', 'TAG':' stop ', 'TGA':' stop ', 'TGG':'W'
    }

AA_switcher_Ecoli = {
    'A':'gcc','R':'cgt','N':'aac','D':'gat','B':'aac',
    'C':'tgc','E':'gaa','Q':'cag','Z':'cag','G':'ggc',
    'H':'cat','I':'att','L':'ctg','K':'aaa','M':'atg',
    'F':'ttt','P':'ccg','S':'agc','T':'acc','W':'tgg',
    'Y':'tat','V':'gtg',' stop ':'taa'
    }

AA_switcher_Human = {
    'A':'gcc','R':'cgg','N':'aac','D':'gac','B':'aac',
    'C':'tgc','E':'gag','Q':'cag','Z':'cag','G':'ggc',
    'H':'cac','I':'atc','L':'ctg','K':'aag','M':'atg',
    'F':'ttc','P':'ccc','S':'agc','T':'acc','W':'tgg',
    'Y':'tac','V':'gtc',' stop ':'tga'
    }

with open(fin_name, 'r') as file:
    raw_primer_list = (file.read()).splitlines()

Final_Primer_Fasta += (raw_primer_list[0] + '\n')
raw_primer_list.pop(0)

for line in raw_primer_list:
    if (line == ''):
        pass
    elif (line.replace(" ", "")).isdigit():
        pass
    else:
        # This is the case we're interested in. This line contains codons.
        codons = line.split()
        for cod in codons:
            codon_list.append(cod)

# Now, for each codon, let's look up the amino acid it codes for,
# and write the most common codon for that amino acid.
count = 0
for codon in codon_list:
    '''
    count+=1
    if count == 20:
        Final_Primer_Fasta += '\n'
        count = 0
    '''
    '''
    # I've removed this functionality because it interfered with degenerate
    # codons when doing error-prone PCR.
    AA=codon_switcher.get(codon.upper())
    if AA != None:
        Final_Primer_Fasta += AA_switcher_Human.get(AA)
    else:
        Final_Primer_Fasta += codon.lower()
        '''
    Final_Primer_Fasta += codon.lower()

with open(f"Mixed-Base {fin_name[0:-4]}.fasta","w+") as fout:
    fout.write(Final_Primer_Fasta)
