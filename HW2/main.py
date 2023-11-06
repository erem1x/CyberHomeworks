import subprocess


ciphers=["aes-128-cbc", "aes-128-ofb", "aes-256-cbc", "aes-256-ofb", "camellia-128-cbc", "camellia-128-ofb", "aria-128-cbc", "aria-128-ofb"]

#Global variable password (same for all)
result=subprocess.run(["./passgen.sh"], stdout=subprocess.PIPE)
password=(result.stdout.decode())


def getTime(a):
	l=a.split("\n")
	l=l[1].split("\t")
	l=l[1].split("m")
	l=l[1].split("s")
	
	return float(l[0])
	


def measureTime(cipher, psw):
	a = subprocess.run(["./cipher.sh", cipher, "e", psw], stderr=subprocess.PIPE).stderr.decode()
	b = subprocess.run(["./cipher.sh", cipher, "d", psw], stderr=subprocess.PIPE).stderr.decode()
	a = getTime(a)
	b = getTime(b)
	
	return [a, b]

#Aux function (should be called 8 times)
def encDec(cipher):
	time=0
	tmp_e=0
	tmp_d=0
	with open("exp/data/data_"+cipher+".dat", "w") as data, open("exp/avg/data_"+cipher+".dat", "w") as average, open("exp/enc/data_"+cipher+".dat", "w") as enc, open("exp/dec/data_"+cipher+".dat", "w") as dec:
		for i in range(0, 500):
			tmp=measureTime(cipher, password)
			tmp_e=tmp_e+tmp[0]
			tmp_d=tmp_d+tmp[1]
			
			time = time + tmp[0] + tmp[1]
			time= (float(f'{time:.4f}'))
			
			enc.write(str(i)+" "+str(tmp_e)+"\n")
			dec.write(str(i)+" "+str(tmp_d)+"\n")
			average.write(str(i)+" "+str(time/(i+1))+"\n")
			data.write(str(i)+" "+str(time)+"\n")
		
	print(cipher+" completed! Time: "+str(time))

for i in ciphers:
	encDec(i)

	
	

