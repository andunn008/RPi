import serial
import time
import csv
import numpy as np
import matplotlib.pyplot as plt

csvfile = "data.csv"
txtfile1 = "humid.txt"
csvfile2 = "temp.csv"
csvfile3 = "soil.csv"

ser = serial.Serial('/dev/ttyACM0',9600)

data = []
humid = []
temp = []
soil = []
timel = []
n = 0

x = []
y = []

csv.register_dialect("data", doublequote = False, escapechar=",")

def readings():
	input1 = ser.readline()
	sinput1 = input1.strip()
	sinput1 = sinput1[2:]
	input2 = ser.readline()
	sinput2 = input2.strip()
	sinput2 = sinput2[2:]
	input3 = ser.readline()
	sinput3 = input3.strip()
	sinput3 = sinput3[2:]
	timec = time.ctime()
	print(sinput1,sinput2,sinput3)
	return sinput1,sinput2,sinput3,timec
	
def createfile(f,i,n):
	with open(("%s.txt" %(n+str(i))), "a")as output:
			output.writelines(','.join(f))

def creategraph(n,i):
	x = np.genfromtxt(("Time%s.txt"%(str(i))),dtype='str',delimiter=',')
	y = np.fromfile(("%s.txt" %(n+str(i))),dtype=float,sep=',')
	
	l = np.arange(len("Time%s.txt"%(str(i)))/5)
	
	plt.figure(i)
	plt.clf
	plt.plot(y)
	plt.xticks(l,x)
	plt.xlabel("Time")
	plt.ylabel(("%s" %n))
	plt.title(("%s vs. Time." %n))
	plt.legend()
	plt.savefig("%s vs. Time." %(n+str(i)))

while (1):
	input =ser.readline()
	if input[0] != 'S':
		continue;
	for i in range(5):
		data.append([])
		humid.append([])
		temp.append([])
		soil.append([])
		timel.append([])
		
		for b in range(10):
			(in1,in2,in3,timec) = readings()
			humid[i].append(in1)
			temp[i].append(in2)
			soil[i].append(in3)
			timel[i].append(timec)
		createfile(timel[i],i,'Time')	
		createfile(humid[i],i,'Humid')
		creategraph('Humid',i)
		createfile(temp[i],i,'Temp')
		creategraph('Temp',i)
		createfile(soil[i],i,'Soil')
		creategraph('Soil',i)
		
		
		
		
		

	
		
			
