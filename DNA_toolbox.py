''' 1. base_refine() func-(base refiner) -> refines unrefined bases from a long string and returns a refined string, be sure to provide string that contains base in capital letter '''

def base_refine(raw_str):

	ref = (('A', 'T', 'G', 'C','U'))

	refined_file=''

	upper_file = raw_str
	for base in upper_file:

		if base in ref:

			refined_file += base

		else:
		    continue

	return refined_file

	

''' 2. base_count() func-(base counter) -> counts number of total bases from a long string of bases. A second argument can be provided to know the number of specific nucleotide. Second argument takes 'A','T','G','C','U' '''

def base_count(raw_data,nucleotide='total'):

    

    A= 0

    T= 0

    G= 0

    C= 0

    U= 0

    

    for base in raw_data:

        if base == 'A':

            A+=1



        elif base == 'T':

            T+=1

        

        elif base == "G":

            G+=1

        

        elif base == "C":

            C+=1

        

        elif base == "U":

            U+=1
        else:
            continue

    total = A + T + G + C + U    

    if nucleotide == "total":

        return total

        

    elif nucleotide == 'A':

        return A



    elif nucleotide == 'T':

        return T

        

    elif nucleotide == "G":

        return G

        

    elif nucleotide == "C":

        return C

        

    elif nucleotide == "U":

        return U 
    


''' 3. codon_list() func-(str to triplet codon list) -> takes a long string and returns a list of triplets sequentially'''
def codon_list(raw_file):

	cdn_lst = []

	n_index = 0

	for n in raw_file:



		#triplet_addition

		triplet = raw_file[n_index:n_index + 3]

		n_index += 3

		if len(triplet) == 3:

			cdn_lst.append(triplet)

		else:

			break

	return cdn_lst


''' 4. d_to_r() func-(DNA to RNA converter) -> takes a long string of DNA bases and returns a string of RNA bases '''
def d_to_r(d_str):
    r_str=''
    for base in d_str:

        if base == 'A':

            r_str+='A'



        elif base == 'T':

            r_str+='U'

        

        elif base == "G":

            r_str+='G'

        

        elif base == "C":

            r_str+='C'
    return r_str 
    
    
''' 5. d_to_cd() func-(DNA complimentary sequence provider) -> takes a long string of DNA and returns the complimentary sequence of DNA '''
def d_to_cd(d_str):
    cd_str=''
    for base in d_str:

        if base == 'A':

            cd_str+='T'


        elif base == 'T':

            cd_str+='A'

        

        elif base == "G":

            cd_str+='C'

        

        elif base == "C":
            
            cd_str+='G'
    return cd_str
    
''' 6. d_to_mr() func-(mRNA transcript provider) -> takes a DNA long string and returns an mRNA transcript '''
def d_to_mr(d_str):
    mr_str=''
    for base in d_str:

        if base == 'A':

            mr_str+='U'


        elif base == 'T':

            mr_str+='A'

        

        elif base == "G":

            mr_str+='C'

        

        elif base == "C":
            
            mr_str+='G'
    return mr_str
    
	
''' 7. r_to_aa() func-(codon to amino acid interpreter) -> takes a long string of RNA codon and returns a string of amino_acid '''
def r_to_aa(s_str):
    
    s_lst = codon_list(s_str)

    aa=""

    ref_dict = {

        "UUU":"F",

        "UUC":"F",

        "UUA":"L",

        "UUG":"L",

        "UCU":"S",

        "UAU":"Y",

        "UGU":"C",

        "UCC":"S",

        "UAC":"Y",

        "UGC":"C",

        "UCA":"S",

        "UAA":"**terminator**",

        "UGA":"**terminator**",

        "UCG":"S",

        "UAG":"*terminator**",

        "UGG":"W",

        "CUU":"L",

        "CCU":"P",

        "CAU":"H",

        "CGU":"R",

        "CUC":"L",

        "CCC":"P",

        "CAC":"H",

        "CGC":"R",

        "CUA":"L",

        "CCA":"P",

        "CAA":"Q",

        "CGA":"R",

        "CUG":"L",

        "CCG":"P",

        "CAG":"Q",

        "CGG":"R",

        "AUU":"I",

        "ACU":"T",

        "AAU":"N",

        "AGU":"S",

        "AUC":"I",

        "ACC":"T",

        "AAC":"N",

        "AGC":"S",

        "AUA":"I",

        "ACA":"T",

        "AAA":"K",

        "AGA":"R",

        "AUG":"M",

        "ACG":"T",

        "AAG":"K",

        "AGG":"R",

        "GUU":"V",

        "GCU":"A",

        "GAU":"D",

        "GGU":"G",

        "GUC":"V",

        "GCC":"A",

        "GAC":"D",

        "GGC":"G",

        "GUA":"V",

        "GCA":"A",

        "GAA":"E",

        "GGA":"G",

        "GUG":"V",

        "GCG":"A",

        "GAG":"E",

        "GGG":"G"

    }
    for s_str in s_lst:
        
        if s_str in ref_dict:
            aa+=ref_dict[s_str]
            
        else:
            continue

    return aa