# RSA Encryption
RSA asymmetric encryption implementation using python,
for more informations check: https://en.wikipedia.org/wiki/RSA_(cryptosystem)


### How to run it?

You will need : 
python 2.7 


## Usage

1- You will need to generate n, private key and public key,

```sh
$ python keygen.py
```
The output will be 3 large integers,

2- To encrypt your data, you will need to run "rsa.py" and enter "n" which is generated by keygen.py, your private key and your message.
The output will be a large integer representing the encrypted message.

```sh
$ python rsa.py
```

3- To decrypt your cipher, you will need to run "rsa.py" and enter "n" which is generated by keygen.py, your public key and your cipher.
The output will be your message.


## License

MIT


**Free Software, Hell Yeah!**
