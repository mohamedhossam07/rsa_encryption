from random import *


def two_com(m,mlen):
    if m < 0:
        m = TwoComp( ("{0:0%db}" % mlen).format(m) )    #Calculate the two's complement number of m
    else:
        m = ("{0:0%db}" % mlen).format(m)   #Convert to bits and assign directly
    return m

def decimal(decimalin):
    decimalin =int(decimalin)
    rest ="" #needed to work
    while True:
        rest += str(decimalin % 2)
        decimalin = decimalin // 2

        if decimalin == 0:
            break

    return rest[::-1]


def size_be_R(key,size):
    if len(key) < size :
        x_key = key.rjust(size,'0')
    elif len(key) > size :
        x_key = key[:size]
    else:
        x_key = key
    return x_key


def binary2dec(binaryin):
    binaryin = str(binaryin)
    i=0
    i = len(binaryin) -1
    binarynum = 0
    binarydecimal = 0
    binaryintra = ""
    while i>= 0:
        binaryintra = binaryintra + binaryin[i]
        i = i -1

    while not binarynum == len(binaryin):
        binarydecimal1=int(binaryintra[binarynum])*2**binarynum
        binarydecimal=binarydecimal+binarydecimal1
        binarynum = binarynum +1

    return binarydecimal


def rand_bin(leng):
    out = ''
    for i in range(0,int(leng/8)):
        new = str(bin(randint(0, 10))) [2:]
        new = size_be_R(new,8)
        out += new
        #print (out)
    out = size_be_R(out,leng)
    return binary2dec(out)
