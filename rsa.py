def main():
    what = input('[1]Encrypt or [2]Decrypt : ')
    if what == 1:
        n=input('Enter your phi : ')
        e=input('Enter your Private : ')
        m=input('Enter your Message :')
        o = (m**e)
        o = o % n
        print(o)
    elif what ==2:
        n=input('Enter your phi : ')
        d=input('Enter your Public : ')
        m=input('Enter your encrypted data :')
        o = (m**d)
        o = o % n
        print(o)
    else:
        print('Enter e or d !!!')


main()
