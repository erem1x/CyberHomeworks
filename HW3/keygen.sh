#!/bin/bash

#key for RSA
openssl genrsa -out privRSA.pem 2048

#key for DSA
openssl dsaparam -out dsaparam.pem 2048
openssl gendsa -out privDSA.pem dsaparam.pem


#Separate public key from private key
#RSA
openssl rsa -in privRSA.pem -pubout > pubRSA.pem
#DSA
openssl dsa -in privDSA.pem -pubout > pubDSA.pem

