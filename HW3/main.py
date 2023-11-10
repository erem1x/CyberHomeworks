import subprocess

#Defining the list command to put into subprocess.run
def defineBuf(sys, mode):
	buf=["./exec.sh", mode] #$1
	#Signing with private key
	if(mode=="sign"): 
		buf.append("priv"+sys+".pem") #$2
		buf.extend(["out", sys+".sign"]) #$3 and $4
	
	#Verifying with public key
	elif(mode=="verify"):
		buf.append("pub"+sys+".pem")
		buf.extend(["signature", sys+".sign"])
	
	else: return -1
	
	return buf
			

#Parser of return time
def getTime(a):
	l=a.split("\n")
	l=l[1].split("\t")
	l=l[1].split("m")
	l=l[1].split("s")
	
	return float(l[0])
	
	
def measureTime(buf1, buf2):
	a = subprocess.run(buf1, stderr=subprocess.PIPE).stderr.decode()
	b = subprocess.run(buf2, stderr=subprocess.PIPE).stderr.decode()
	a = getTime(a)
	b = getTime(b)
	
	return [a, b]


def printData(l, fp):
	x=0
	for i in range(0, len(l)):
		if(i%2==0 and i!=0):
				fp.write("\n")
				x = x+0.5
		fp.write(str(x)+" "+l[i]+"\n")
		x=x+0.5
	

#Round and stringfy + space (GNUPLOT)
def strR(i):
	return str(round(i, 3))+" "

#Number of iterations as input
def main(i):
	print("Signing and verifying", i, "times")
	f=open("data/diff.dat", "w")
	#Defining all 4 commands to be executed
	RSA_sign=defineBuf("RSA", "sign")
	RSA_verify=defineBuf("RSA", "verify")
	DSA_sign=defineBuf("DSA", "sign")
	DSA_verify=defineBuf("DSA", "verify")
	DSA_s=0
	RSA_s=0
	DSA_v=0
	RSA_v=0
	
	diff_s=0
	diff_v=0
	
	for x in range(0, i):
	
		tmp = measureTime(RSA_sign, DSA_sign)
		tmp2 = measureTime(RSA_verify, DSA_verify)
		RSA_s = RSA_s + tmp[0]
		DSA_s = DSA_s + tmp[1]
		RSA_v = RSA_v + tmp2[0]
		DSA_v = DSA_v + tmp2[1]
		
		diff_s = diff_s + (tmp[0] - tmp[1])
		diff_v = diff_v + (tmp2[0] - tmp2[1])
		
		f.write(str(x)+" "+str(tmp[0]-tmp[1])+" "+str(tmp2[0]-tmp2[1])+"\n")
		
	
	f.close()
	avgRSA_s = str(round(RSA_s/i, 5))+" "
	avgDSA_s = str(round(DSA_s/i, 5))+" "
	avgRSA_v = str(round(RSA_v/i, 5))+" "
	avgDSA_v = str(round(DSA_v/i, 5))+" "
	print("Averages: "+avgRSA_s+avgDSA_s+avgRSA_v+avgDSA_v)	
	print("\nRSA_sign:", round(RSA_s, 3), "\nDSA_sign:", round(DSA_s, 3))
	print("\nRSA_verify:", round(RSA_v, 3), "\nDSA_verify:", round(DSA_v, 3))
	print("\nDiff_s", round(diff_s, 3), "\nDiff_v", round(diff_v, 3))
	
	with open("data/data.dat", "w") as data, open("data/avg_data.dat", "w") as avg_data:
		printData([strR(RSA_s), strR(DSA_s), strR(RSA_v), strR(DSA_v)], data)
		printData([avgRSA_s, avgDSA_s, avgRSA_v, avgDSA_v],avg_data)
	
main(10000)
	
