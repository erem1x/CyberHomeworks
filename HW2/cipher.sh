#!/bin/bash
#List of ciphers to be used

#e1b1="aes-128-cbc"
#e1b2="aes-128-ofb"
#e2b1="camellia-128-cbc"
#e2b2="camellia-128-ofb"
#e3b1="aria-128-cbc"
#e3b2="aria-128-ofb"
#e4b1="seed-cbc"
#e4b2="seed-ofb"

#$1 = cipher, $2 = enc/dec, $3 = password
file_in="text.txt"
file_out="text.enc"

if [ $2 == "d" ] ; then
  file_in="text.enc"
  file_out="textd.txt"
  if [ -e textd.txt ] ; then
    rm textd.txt
  fi
fi

if [ $2 == "e" ] ; then
  if [ -e text.enc ] ; then
    rm text.enc
  fi
fi



time openssl enc -$1 -$2 -pbkdf2 -in $file_in -out $file_out -pass pass:$3 2> >(grep "real" | awk '{print $2}' >&2) 


