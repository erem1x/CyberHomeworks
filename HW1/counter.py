import sys
from math import sqrt

biggest_series_b=0
biggest_series_w=0
run_tot=0
std_dev=0

def findRun(l):
	global run_tot
	run=0
	last_seen=l[0]
	for x in l[1:]:
		if x!=last_seen:
			run = run + 1
		last_seen=x
	run_tot = run_tot + run
			
		
def stdDeviation(rate):
	global std_dev
	temp = rate*(1-rate)
	temp = sqrt(temp)
	std_dev = std_dev + temp
		


def findSeries_sp(l, i):
	mem=0;
	counter=0;
	for x in l:
		if x==i:
			counter = counter+1
		else:
			if counter > mem: mem=counter
			counter=0;
	return mem

def findSeries(l):
	global biggest_series_b
	global biggest_series_w
	b = findSeries_sp(l, "0");
	w = findSeries_sp(l, "1");
	
	if b > biggest_series_b: biggest_series_b=b
	if w > biggest_series_w: biggest_series_w=w
	
	

bin_file = sys.argv[1]

f = open(bin_file, "r")

b, w=0, 0
lowest_w=9999999999999999;
lowest_b=9999999999999999;
rapp_w=0
rapp_b=0

try:
	line = f.readline()
	while line!="": #EOF
		ch = [x for x in line]
		zero = ch.count("0")
		one = ch.count("1")
		
		#Stats functions
		findSeries(ch)
		findRun(ch)
		stdDeviation(one/(one+zero))
		
		if zero < lowest_b: 
			lowest_b = zero
			rapp_b = zero/256
			
		if one < lowest_w: 
			lowest_w = one
			rapp_w = one/256
					
		b = b + zero
		w = w + one
		
		line= f.readline()
finally:
	f.close()
	tot=b+w
	std_dev2=sqrt((w/tot)*(1-(w/tot)))
	avg_b=b/200
	avg_w=w/200
	exp_runs=((2*avg_b*avg_w)/((avg_b+avg_w)+1))
	
	print("Rate of 0 to 1:", b/w)
	print("Rate of 0 on total:", b/tot)
	print("Rate of 1 on total:", w/tot)
	print("Rate of lowest number of 0:",rapp_b)
	print("Rate of lowest number of 1:",rapp_w)
	print("Longest series of 0:", biggest_series_b)
	print("Longest series of 1:", biggest_series_w)
	print("Average run:", run_tot/200)
	print("Expected runs:", exp_runs)
	print("Standard deviation:", std_dev2)
		
