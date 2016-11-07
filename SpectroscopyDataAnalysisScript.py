# Genral Remarks: be ware of whicht spacing!!

import numpy as n
import time
import spc
import matplotlib.pyplot as plt
import os

###from .spc file import data and convert to .txt file
def DataExtrating (directory, filname):
    specdata = spc.File(directory + 'spcFiles/' + filname + '.spc')

    specdata.data_txt()
    specdata.write_file( directory + 'txtFiles/' + filname + '.txt')
    return specdata.data_txt()

###plot Spectrum with data from .spc file    
def PlotData(directory, filname): 
    specdata = spc.File(directory + 'spcFiles/' + filname + '.spc')
    
    Plot = specdata.plot(filname) 
    Plot.savefig(directory + "pngFiles/" + filname + '.png')

    print 'specdata:', type(specdata)


#Extract, convert und plot Spectroskopy Data from a whole directory
def DoStuffQuicker(Dirname):  
	filenamelist = os.listdir(Dirname + "spcFiles")
	
	for i in range(len(filenamelist)):
		filenamelist[i] = filenamelist[i].split(".")[0]

	for j in range(len(filenamelist)):
		DataExtrating(Dirname, filenamelist[j])
		PlotData(Dirname, filenamelist[j])

### class in order to make polts with multible spectra in it
class ComparisonPlot:

	def __init__(self, directory, filename, name, log = False):
		self.directory = directory + "txtFiles/"
		self.filename = filename 
		self.name = name
		self.data = []
		self.log = log
	
	### from .txt file get spectroscopy data	
	def GetData(self):
		
		for i in range(len(self.filename)):
			with open(self.directory + self.filename[i] + ".txt") as fil:
				fil.readline()
				i = 1
				x = []
				y = []
				
				while (i <= 1024):
					c = fil.readline()
					wl, cou = c.split()
					
					x.append(float(wl))
					y.append(float(cou))
					
					i += 1 
				self.data.append([x,y])
	
	###plot data			
	def Plot(self):
		
		for i in range(len(self.data)):
			fig = plt.plot(
			          self.data[i][0][:len(self.data[i][0])], 
				      self.data[i][1][:len(self.data[i][1])],
				      label = self.filename[i])
				      
		if self.log:
			plt.yscale("log")
			
		plt.legend(self.filename)#loc = (0,1))
		plt.xlabel("Wavelength [nm]")
		plt.ylabel("Counts")
		plt.title(self.name)
		plt.savefig(self.directory + self.name + ".png")

	###	use class funktions in one go
	def make(self):
		self.GetData()
		self.Plot()


###Examples on how to use this code

#Analyiong data sets
'''
DoStuffQuicker(
	"/home/iwsatlas1/kraetzsc/Documents/Spectroscopy/MeasurementSeries1/")
DoStuffQuicker(
	"/home/iwsatlas1/kraetzsc/Documents/Spectroscopy/MeasurementSeries2/")
'''

#Extrakt Data and plot it
'''
DataExtrating(
	"/home/iwsatlas1/kraetzsc/Documents/Spectroscopy/UVlamp/", 
    "UVlamp22-9-16")
PlotData(
	"/home/iwsatlas1/kraetzsc/Documents/Spectroscopy/UVlamp/", 
    "UVlamp22-9-16")
'''

#Make a combined Plot
'''     
Filenames = ["BC408-5mmMS2", 
             "BC408-064MS2"]

cp = ComparisonPlot(
    "/home/iwsatlas1/kraetzsc/Documents/Spectroscopy/MeasurementSeries2/", 
    Filenames, 
    "BC405_5mm_vs_BC408_3mm-logarithmic", 
    log = True)
cp.make()
'''
