# Qualitative Deviations from Consensus Ancestral Sequence for Library Design
# This program parses the information found in a Bali-Phy output, and determines in a 
#   qualatative manner possible dissenting options from concensus  amino acids at ancestral sites.
#   This program is designed to be used with Patrick Finnerans' Sample BAliPhy Nodes program outputs.
# Written by James VanAntwerp in July 2020
# Written for the Woldring Lab, Michigan State University in East Lansing, Michigan, USA.

import Bio
from Bio import SeqIO
import os

if not os.path.isdir("Consensus Deviations"):
    os.mkdir("Consensus Deviations")
AA_key = ['G', 'A', 'V', 'L', 'I', 'W', 'F', 'Y', 'P',  'M', 'C', 'S', 'T', 'N', 'Q', 'D', 'E', 'H', 'K', 'R', 'x', '-']
Percent_Share_Cuttoff = 0.05


def parse_multifasta (f_path):
    with open(f_path) as handle:
        for Seq_Rec_Itr in SeqIO.parse(handle, "fasta"):
            Sequences_list.append(str(Seq_Rec_Itr.seq))
    return Sequences_list

def calculate_data(Sequences_list):
    # For each position,
    for position in range(len(Sequences_list[0])):
        # Make a blank list
        position_aa_distribution = [0]*22
        # And tally each Amino Acid
        for i in range(Num_Sequences):
            AA = Sequences_list[i][position]
            (position_aa_distribution[AA_key.index(AA)])+=1
        # Then add the collumn to the matrix
        AA_Probability_Matrix.append(position_aa_distribution)

def write_output (matrix, name):
    space = "  "
    name = name[0:-26]
    name += "_Non-Concensus_Deviations.txt"
    with open(f"Consensus Deviations/{name}","w+") as fout:
        for position in range(len(matrix)):
            output = f"At position {space}{position+1}, "
            for i in range(len(matrix[position])):
                if ((matrix[position][i] / Num_Sequences) >= Percent_Share_Cuttoff):
                    output += f"{AA_key[i]} apears %{round((matrix[position][i]/Num_Sequences)*100,2) } of the time;  "
            output+="\n"
            fout.write(output)
            output = ""
            if (position==8):
                space=" "
            if (position==98):
                space=""

# For each file in the folder. Each file should be an alignment of possible ancestral sequences.

for Ancestor_Alignment in [x for x in os.listdir('Ancestor_Nodes_Aligned') if x.split('.')[0].split('_')[-1] == 'Aligned']:
    Sequences_list = []
    AA_Probability_Matrix = []
    Num_Sequences = 1
    # Each itteration of this loop is one file.
    parse_multifasta(f"Ancestor_Nodes_Aligned/{Ancestor_Alignment}")
    # We now have the sequences parsed. Let's make a matrix.
    Num_Sequences = len(Sequences_list)
    calculate_data(Sequences_list)
    # Now let's write the output.
    write_output(AA_Probability_Matrix, Ancestor_Alignment)


