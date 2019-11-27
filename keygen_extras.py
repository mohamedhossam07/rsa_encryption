from random import *
from binary_mult import *
from keygen_extras import *


def power(x, y, p):
    #temp = x
    #for i in range(0,y-1):
        #x = karatsubaMultiplication(x,temp)
    return (x ** y )  % p

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



def multiplicative_inverse(a, b):
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oa  # If neg wrap modulo orignal a
    # return a , lx, ly  # Return only positive values
    return lx
