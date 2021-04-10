#importing module to use functions
import DNA_toolbox as DT

#taking filename as input
fn =('Enter filename:')

#opening file and counting bases from imported function
with open(fn,'r') as fh:
    ref = DT.base_refine(fh.read())
    A = DT.base_count(ref,'A')
    C = DT.base_count(ref,'C')
    G = DT.base_count(ref,'G')
    T = DT.base_count(ref,'T')
    
    #printing the result
    print(A,C,G,T, end ='')
