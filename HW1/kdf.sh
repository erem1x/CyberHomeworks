#!/bin/bash
psw=$1

if [ -e result/results.txt ] ; then
  truncate -s 0 result/results.txt
fi

if [ -e result/strong_results.txt ] ; then
  truncate -s 0 result/strong_results.txt
fi

if [ -e keys/bytes ] ; then
  rm keys/bytes
fi

if [ -e keys/strong_bytes ] ; then
  rm keys/strong_bytes
fi

if [ -e keys/key.txt ] ; then
  truncate -s 0 keys/key.txt
  #echo "Key file emptied!"
fi

if [ -e keys/bin_key.txt ] ; then
  truncate -s 0 keys/bin_key.txt
  #echo "Bin key file emptied!"
fi

if [ -e keys/strong_key.txt ] ; then
  truncate -s 0 keys/strong_key.txt
  #echo "Strong key file emptied!"
fi

if [ -e keys/bin_strong_key.txt ] ; then
  truncate -s 0 keys/bin_strong_key.txt
  #echo "Strong key file emptied!"
fi

#Generating 200 "standard" keys
for ((i=0; i<200; i++)); do
  openssl enc -aes-256-cbc -k $psw -P -md SHA256 2>/dev/null | grep key | cut --complement -d "=" -f1 >> keys/key.txt
done
python3 hextobin.py keys/key.txt keys/bin_key.txt keys/bytes
echo "200 standard keys generated"

for ((i=0; i<200; i++)); do
  openssl kdf -keylen 32 -kdfopt digest:SHA256 -kdfopt pass:$psw -kdfopt salt:$(date +%s%N | sha256sum | head -c 10) -kdfopt iter:10000 PBKDF2 | sed 's/://g' >> keys/strong_key.txt
done
python3 hextobin.py keys/strong_key.txt keys/bin_strong_key.txt keys/strong_bytes
echo "200 PBKDF2 keys generated"
echo ""

echo "Analisys on standard openssl kdf keys"
python3 counter.py keys/bin_key.txt
echo ""

echo "Analisys on PBKDF2 keys"
python3 counter.py keys/bin_strong_key.txt

echo""
echo "Executing NIST-SP-800-22 tests"
python3 sp800_22_tests/sp800_22_tests.py keys/bytes >> result/results.txt
python3 sp800_22_tests/sp800_22_tests.py keys/strong_bytes >> result/strong_results.txt

echo "Analisys terminated successfully!"
