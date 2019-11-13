from binary_mult import *
from keygen_extras import *
from random import *

def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)
#
def main():

    mlen = 512
    rlen = 512
    leng = 512

    m = rand_bin(leng)
    m =two_com(m,mlen)

    while prime_check(binary2dec(m) ) != True :
        m = rand_bin(leng)
        m =two_com(m,leng)

    r = rand_bin(leng)
    r = two_com(r,leng)

    while prime_check(binary2dec(m) ) != True :
        r = rand_bin(leng)
        r =two_com(m,mlen)

    print('m is = '+str(m))
    print('r is = '+str(r))
    ilen = mlen + rlen + 1                  #The common length of internal variables
    a = m + GenZeroStr(rlen + 1)            #A: place M in leftmost position. Fill the left bits with 0.
    s = TwoComp(m) + GenZeroStr(rlen + 1)   #S: place negative M in leftmost position.
    p = GenZeroStr(mlen) + r + "0"          #P: place R by rightmost 0.

    for i in range(rlen):

        op = p[-2:]
        if   op == "10":
            p = BitAdd(p, s, len(p))
        elif op == "01":
            p = BitAdd(p, a, len(p))
        p = BitShift(p, 1)

    p = p[:-1]
    print("The answer is: " + str(binary2dec(p)) )

def prime_check(n,k=5):
    r =randint(2, n)
    if hcfnaive(n,r) != 1 :
        return False
    else:
        if n < 2: return False
        for p in [2,3,5,7,11,13,17,19,23,29]:
            if n % p == 0: return n == p
        s, d = 0, n-1
        while d % 2 == 0:
            s, d = s+1, d/2
        for i in range(k):
            x = pow(randint(2, n-1), d)
            if x == 1 or x == n-1: continue
            for r in range(1, s):
                x = (x * x) % n
                if x == 1: return False
                if x == n-1: break
            else: return False
        return True



if __name__ == "__main__":

    main()
