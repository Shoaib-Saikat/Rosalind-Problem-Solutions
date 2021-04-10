#importing module to use functions
import DNA_toolbox as DT

#taking filename as input
fn =input('Enter filename:')

#opening file and counting bases from imported function
with open(fn,'r') as fh:
    #reifining DNA bases
    ref = DT.base_refine(fh.read())
    #converting to RNA
    RNAseq = DT.d_to_r(ref)
    #printing RNA sequence
    print(RNAseq)
