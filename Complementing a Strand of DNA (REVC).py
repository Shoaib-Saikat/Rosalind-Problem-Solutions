#importing module to use functions
import DNA_toolbox as DT

#taking filename as input
fn =('Enter filename:')

#opening file and counting bases from imported function
with open(fn,'r') as fh:
    #reifining DNA bases
    ref = DT.base_refine(fh.read())
    #creating variable to accumulate DNA bases
    rcDNA =''
    #reversed list like iterable object
    rcDNA_it = reversed(cDNA)
    #accumulating reversed bases
    for n in rcDNA_it:
        rcDNA += n
    #printing the result
    print(rcDNA)
