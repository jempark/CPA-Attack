# Basic Cryptography - AES and RSA
AES and RSA for secure network communications

## 1 Overview
Use AES and RSA for secure network communications. These two cryptographic algorithms are used in our daily life (e.g. HTTPS protocol). 
We will analyze the performance of OpenSSL implementations of both algorithms, and then we will use them to set up secure communication between the client and the server to obtain a secret.

## 3 Lab Module 1: Performance of Ciphers 
The OpenSSL library has the following APIs for RSA
1. RSA public encrypt
2. RSA public decrypt
3. RSA private decrypt
4. RSA private encrypt

and for AES

1. AES encrypt
2. AES decrypt

First understand how to use these ciphers, and write the programs to measure the performance of RSA public encrypt and AES encrypt functions. Use and time these functions to encrypt a 16-byte data.
Collect one million timing samples for each function. You will need to look up the appropriate timer and also the parameters for AES encrypt() and RSA public encrypt().

The pseudo code for measuring AES is:
```
for (i = 0; i < 1000000; i++){
t1 = timer_start()
AES_encrypt()
t2 = timer_stop()
timearray[i] = t2 - t1
}
plot_distribution(timearray);
```

The pseudo code for measuring RSA public key implementation is:
```
for (i = 0; i < 1000000; i++){
t1 = timer_start()
RSA_public_encrypt()
t2 = timer_stop()
timearray[i] = t2 - t1}
plot_distribution(timearray);
```

To allow your programs to use these cryptographic functions included in the OpenSSL library, you can
refer to the following Makefile example for header files inclusion and static library linking. Note to update
OPENSSL setting to the directory of your downloaded OpenSSL:
``
CC=gcc
OPENSSL=../../openssl
INCLUDE=$(OPENSSL)/include/
CFLAGS=-c -I$(INCLUDE)
all: program
program: program.c
$(CC) program.c -I$(INCLUDE) -o program $(OPENSSL)/libcrypto.a -ldl -lpthread
clean:
rm -rf program
```

Plot timing distributions of these samples and find the mean for each function.

## 4 Lab Module 2: AES Encryption Mode
There are several operation modes of AES. In this section, you will explore two of them: ECB and CBC.
Using each of these two modes to encrypt an image file and report your findings.

To simplify the experiment, we will be using an image in the PPM format. First, separate the header
and body sections of the image:
```
$ head -n 4 penguin.PPM > header.txt
$ tail -n +5 penguin.PPM > body.bin
```

Encrypt the body sections and reconstruct the image using the header and encrypted body sections.
```
$ openssl enc -aes-128-ecb -nosalt -pass pass:"A" -in body.bin -out enc_body.bin
$ cat header.txt enc_body.bin > ecb_penguin.ppm
```

## Lab Module 3: Secure Communication
You will need to use both AES and RSA to communicate with a service we host on 10.75.11.176 at port
12000 and obtain a 16-byte secret. This address cannot be accessed from the public Internet.

The following is the communication protocol:
```
server -> [size of server’s public key] -> client
server -> [server’s public key] -> client
server <- [size of the client’s AES key encrypted using server’s public key] <- client
server <- [encrypted client’s AES key <- client
server -> [encrypted secret message using client’s AES key] -> client
connection close
```