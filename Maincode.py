import JustCodes
import gettest
import registerval
import Ainstruct
import Cinstruct

f = open("Max.asm","r")
L1=f.readlines()
Binary_codes = []
f.close()

L=JustCodes.remove_lines(L1)
D=gettest.getindex(L)
D=registerval.Binarycode(D)


for i in L:
    if i[0]=="@":
        val=Ainstruct.convert(i,D)+'\n'
        Binary_codes.append(val)
    elif i[0]!='(':
        val = Cinstruct.convert(i)+'\n'
        Binary_codes.extend(val)

f=open("Max.hack","w")
f.writelines(Binary_codes)
f.close()


