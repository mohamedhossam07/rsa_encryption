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
    eleng = 1024
    m = rand_bin(leng)
    m =two_com(m,mlen)

    while isPrime(binary2dec(m) ) != True :
        m = rand_bin(leng)
        m =two_com(m,leng)

    r = rand_bin(leng)
    r = two_com(r,leng)

    while isPrime(binary2dec(r)) != True :
        r = rand_bin(leng)
        r =two_com(r,eleng)

    e = rand_bin(eleng)
    e = two_com(e,eleng)
    #print(e)
    m = binary2dec(m)
    r = binary2dec(r)
    fi = (m-1)*(r-1)
    g = 5
    e = binary2dec(e)
    while g != 1:
        while isPrime(e) != True :
            e = rand_bin(eleng)
            e =two_com(e,eleng)
            e = binary2dec(e)
        g = gcd(e, fi)

    #g = gcd(e, fi)
    print('m is = '+str(m))
    print('')
    print(isPrime(m))
    print('')
    print('r is = '+str(r))
    print('')
    print(isPrime(r))
    print('')
    print('e is = '+str(e))
    print(isPrime(e))
    print('')


    d = multiplicative_inverse(e, fi)
    print(d)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


def isPrime(n, k=5): # miller-rabin
    from random import randint
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d/2
    for i in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":

    main()
