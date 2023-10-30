import sys

key_file = sys.argv[1]
bin_file = sys.argv[2]
byte_file = sys.argv[3]

scale = 16 
num_of_bits = 256

#Opening source, binary dest and bytes dest
key = open(key_file, "r")
bin_key = open(bin_file, "w")
byte_key = open(byte_file, "wb")

try:
	line = key.readline()
	while line!="": #EOF
		if(line!="\n"):
			byte_key.write(bytes.fromhex(line)) 
			bin_key.write(bin(int(line, scale))[2:].zfill(num_of_bits) + "\n") #converting hex to bin
		line=key.readline()
finally:
	key.close()
	bin_key.close()
	byte_key.close()

