#DNA-READER/GENERATOR
#
#Collects nontemplate DNA strand from user and translates to protein,
#or creates random DNA sequence using random module and generates
#translation of random sequence. Also checks protein for first start
#amino acid (ATG/Met) and displays protein from first stop codon to
#first stop codon (Ochre, Amber, or Opal)

#Created by Sidharth Jain

import random


def main():
    #Collect user input 
    user_seq = input("""Please insert nontemplate strand here (or hit enter for random seq.)
\nNOTE: Please ensure that sequence is in correct format (continuous or codon-length)\n>>> """)

    #Input validation
    while validateUserInput(user_seq) == False:  
        user_seq = input("""Please insert nontemplate strand here (or hit enter for random seq.)
\nNOTE: Please ensure that sequence is in correct format (continuous or codon-length)\n>>> """)
        
    if len(user_seq) >= 1 and len(user_seq) < 3:        #Reject non codon-length DNA.  Return strand.
        print("This sequence can not be translated.")
        print("Your sequence is: ", user_seq)

    #Process user input strand
    elif len(user_seq) >= 3:
        p = processSequence(user_seq)
        while p == False:
            p = processSequence(user_seq)
        print("\nProtein:", p)
        print("Protein length:", len(p)//4, "amino acids")
        scanCheck(user_seq)

    #Generate and process randomly generated strand
    else:
        desired_length = int(input("How long would you like your random nontemplate strand to be? "))
        length = desired_length // 3
        sequence = generateRandomDNA(length)
        print("Randomly generated sequence:")
        print(sequence)                             #Display random sequence
        p = processSequence(sequence)
        while p == False:
            p = processSequence(sequence)
        print("\nProtein:", p)
        print("Protein length:", len(p)//4, "amino acids")
        scanCheck(p)

def validateUserInput(seq):
    if len(seq) < 1:
        return True
    elif seq.find('u') >= 0  or seq.find('U') >= 0:
        print("This is not a DNA sequence.  Please try again. ")
        return False
    elif seq.find('A') < 0 or seq.find('a') < 0:
        print("No A's")
        return True
    else:
        return True

def processSequence(seq):    #Check to see if user wants to translate sequence.
    check = input("Do you want to translate this sequence? [y/n]: ")
    if check == "y" or check == "Y":
        if seq[3] == " " and seq[7] == " ":           #Check if sequence is in codon format or not.
            seq = seq.upper()
            protein = translate(seq)
            return protein
        elif " " not in seq:
            fDNA = formatDNA(seq)
            protein = translate(fDNA)
            print("Sequence:", fDNA)
            return protein
        else:
            print("This is an invalid sequence format.  Try again.")
            
    elif check == "n" or check == "N":
        print("OK, your sequence is", seq)
        return True
    else:
        print("Invalid choice.  Try again.")
        return False

def formatDNA(strand):      #Format continuous sequence to separate out codons.
    strand = strand.upper()
    l = len(strand)
    strand_codons = (l // 3) + 1
    formatted_DNA = ""              #Start with empty str
    for x in range(strand_codons):
        codon = strand[3*x-3:3*x]                   #Add spaces at every multiple of 3 to create codon format
        formatted_DNA = formatted_DNA + codon + " "
    return formatted_DNA

def generateRandomDNA(length):    #If no user input, then generate random strand of length 'length'.  
    sequence = ""
    for m in range(length):
        codon = ""
        for b in range(3):
            x = random.randint(0,3)    #Strand generated using random module.
            if x == 0:
                nucleo = "A"
            if x == 1:
                nucleo = "C"
            if x == 2:
                nucleo = "T"
            if x == 3:
                nucleo = "G"
            codon+=nucleo
        sequence += codon + " "
    return sequence

def translate(x):               #Translate sequence after processing.
    protein = ""
    seqlist = str.split(x)
    for codon in (seqlist):
        #Convert each codon into its corresponding amino acid.
        if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
            amino = 'Stp'
        elif codon == 'TTA' or codon == 'TTG' or codon == 'CTT' or codon == 'CTA' or codon == 'CTC' or codon == 'CTG':
            amino = 'Leu'
        elif codon == 'TTT' or codon == 'TTC':
            amino = 'Phe'
        elif codon == 'ATG':
            amino = 'Met'
        elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA':
            amino = 'Ile'
        elif codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG':
            amino = 'Val'
        elif codon == 'TCT' or codon == 'TCC' or codon == 'TCA' or codon == 'TCG':
            amino = 'Ser'
        elif codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG' or codon == 'AGT' or codon == 'AGC':
            amino = 'Pro'
        elif codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
            amino = 'Thr'
        elif codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
            amino = 'Ala'
        elif codon == 'TAT' or codon == 'TAC':
            amino = 'Tyr'
        elif codon == 'CAT' or codon == 'CAC':
            amino = 'His'
        elif codon == 'CAA' or codon == 'CAG':
            amino = 'Gln'
        elif codon == 'AAT' or codon == 'AAC':
            amino = 'Asn'
        elif codon == 'AAA' or codon == 'AAG':
            amino = 'Lys'
        elif codon == 'GAT' or codon == 'GAC':
            amino = 'Asp'
        elif codon == 'GAA' or codon == 'GAG':
            amino = 'Glu'
        elif codon == 'TGT' or codon == 'TGC':
            amino = 'Cys'
        elif codon == 'TGG':
            amino = 'Trp'
        elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
            amino = 'Arg'
        elif codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
            amino = 'Gly'
        else:
            amino = 'Xxx'
        protein = protein + amino + " "
    return protein

def scanCheck(x):  #Check if protein scanning is desired by user.
    check = input("Do you want to scan the protein (check for start/stop codon?) [y/n]: ")
    if check == "y" or check == "Y":
        scanProtein(x)
    if check == "n" or check == "N":
        print("OK.  Program terminated.")

def scanProtein2(x):
    pass

def scanProtein(x):
    processed_protein = ""  #start with empty string
    seqlist = str.split(x)
    for start in seqlist:
        if start == 'ATG':    #Check for start codon
            amino = 'Met'
            for codon in (seqlist):    #Continue with ordinary translation
                if codon == 'TTA' or codon == 'TTG' or codon == 'CTT' or codon == 'CTA' or codon == 'CTC' or codon == 'CTG':
                    amino = 'Leu'
                elif codon == 'TTT' or codon == 'TTC':
                    amino = 'Phe'
                elif codon == 'ATG':
                    amino = 'Met'
                elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA':
                    amino = 'Ile'
                elif codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG':
                    amino = 'Val'
                elif codon == 'TCT' or codon == 'TCC' or codon == 'TCA' or codon == 'TCG':
                    amino = 'Ser'
                elif codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG' or codon == 'AGT' or codon == 'AGC':
                    amino = 'Pro'
                elif codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
                    amino = 'Thr'
                elif codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
                    amino = 'Ala'
                elif codon == 'TAT' or codon == 'TAC':
                    amino = 'Tyr'
                elif codon == 'CAT' or codon == 'CAC':
                    amino = 'His'
                elif codon == 'CAA' or codon == 'CAG':
                    amino = 'Gln'
                elif codon == 'AAT' or codon == 'AAC':
                    amino = 'Asn'
                elif codon == 'AAA' or codon == 'AAG':
                    amino = 'Lys'
                elif codon == 'GAT' or codon == 'GAC':
                    amino = 'Asp'
                elif codon == 'GAA' or codon == 'GAG':
                    amino = 'Glu'
                elif codon == 'TGT' or codon == 'TGC':
                    amino = 'Cys'
                elif codon == 'TGG':
                    amino = 'Trp'
                elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
                    amino = 'Arg'
                elif codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
                    amino = 'Gly'
                elif codon == 'UGA' or codon == 'UAA' or codon == 'UAG':
                    amino = '***'
                    break
                else:
                    break               #End loop if stop codon is detected.
                processed_protein = processed_protein + amino + " "
        else:
            pass
    

main()


