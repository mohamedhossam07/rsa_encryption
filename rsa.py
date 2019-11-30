from binary_mult import *
from keygen_extras import *

def main():
    what = input('[1]Encrypt or [2]Decrypt : ')
    if what == '1':
        n=input('Enter your n : ')
        e=input('Enter your Private "d" : ')
        m=input('Enter your Message : ')
        m = strtoint(m)
        o = karatsubaMultiplication(int(m),int(e))
        o = o % int(n)
        print('The Output is : ')
        print(o)
    elif what == '2':
        n=input('Enter your n : ')
        d=input('Enter your Public "e" : ')
        m=input('Enter your encrypted data : ')
        o =karatsubaMultiplication (int(m),int(d))
        o = o % int(n)
        print('The Output is : ')
        print(inttostr(o))
    else:
        print('Enter 1 or 2 !!!')


def inttostr(a):
    intstr = str(a)
    out = ''
    i = 0
    if int(intstr[0]) > 4 :
        intstr = '0' + intstr
    while i < len(intstr):
        out = out + chr(int(intstr[i:i+3]))
        i += 3
    return out

def strtoint(a):
    out = ''
    ap = ''
    for i in range(0,len(a)):
        ap = ''
        if len(str(ord(a[i]))) == 1 :
            ap = '00'
        elif len(str(ord(a[i]))) == 2 :
            ap = '0'
        elif len(str(ord(a[i]))) == 3:
            ap == ''
        out = out + ap +str(ord(a[i]))
    print ('your int message is : '+str(out))
    return out


main()
