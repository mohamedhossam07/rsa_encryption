from binary_mult import *
from keygen_extras import *

def main():
    what = input('[1]Encrypt or [2]Decrypt or [3]Check : ')
    if what == '1':
        n=input('Enter your n : ')
        e=input('Enter your Private "d" : ')
        m=input('Enter your Message : ')
        o = karatsubaMultiplication(int(m),int(e))
        o = o % int(n)
        print(o)
    elif what == '2':
        n=input('Enter your n : ')
        d=input('Enter your Public "e" : ')
        m=input('Enter your encrypted data : ')
        o =karatsubaMultiplication (int(m),int(d))
        o = o % int(n)
        print(o)
    elif what == '3':
        n=input('Enter your n : ')
        d=input('Enter your Public : ')
        m=input('Enter your private : ')
        o = (int(m)*int(d))
        o = o % int(n)
        print(o)
    else:
        print('Enter 1 or 2 !!!')


main()
