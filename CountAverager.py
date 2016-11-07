# program which calculates the average of the counts measured for a tile see Grease test for specifics of the setup
import numpy as n
import os

dirnamelist = os.listdir(
	"/home/iwsatlas1/kraetzsc/Documents/GreaseTest/GreasTestData")
print os.listdir(
	"/home/iwsatlas1/kraetzsc/Documents/GreaseTest/GreasTestData")


for j in range(len(dirnamelist)):
	
	dirname = dirnamelist[j]
	greasefile = open("GreasTestData/" + dirname + "/photon-events.dat", 
		"r")
	counts = 0.0
	i = 0
	
	for line in greasefile.readlines():
		counts = counts + float(line.split()[3])
		i += 1

	countsaverage = round(counts/i, 3)
	print dirname + ":", countsaverage
	
