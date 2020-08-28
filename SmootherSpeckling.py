# this is python2. All the info about it is best accessed here:
# https://docs.python.org/2/library/index.html
from ij.measure import ResultsTable
from ij import WindowManager
from ij import IJ
import re
import csv
from os.path import join, exists
import os

class ResultsTableToCSV:
	def __init__(self,channel1,channel2,ignoreString):
		self.toIgnore = ignoreString
		self.channel1 = channel1
		self.channel2 = channel2

	def getImageNames(self):
		try:
			images = WindowManager.getImageTitles()
			for imageName in images:
				#this first if statement will skip images with *ignoreString in their name
				if not re.search(self.toIgnore,imageName):
					if re.search(self.channel1,imageName): 
						primary = imageName
					else:
						if re.search(self.channel2,imageName): 
							secondary = imageName
		except:
			print("can't find images with '{}' and '{}' in their names in Fiji.".format(self.channel1,self.channel2))
			primary = ""
			secondary = ""
			images = set()
		finally:
			return primary,secondary, images
	#roiAnalysisToWrite takes the Roi Analysis table and turns it into a table that
	#python can write to a csv
	def roiAnalysisToWrite(self,roiTableName):
		#I can't figure out the syntax to preallocate memory,
		#this will not scale to many speckles
		try:
			RT = ResultsTable.getResultsTable(roiTableName)
			headings = RT.getHeadings()
			labelCol = RT.getColumnAsVariables(headings[0])
			headers = headings[1:]
			numCols = len(headers)
			numRows = len(labelCol)
			out = []
			for col in range(numCols):
				out.append([])
				column = RT.getColumnAsVariables(headers[col])
				for row in range(numRows):
					out[col].append(column[row].getValue())
			outT = []
			for i in range(numRows):
				lis = []
				lis.append(labelCol[i].getString())
				for j in range(numCols):
					lis.append(out[j][i])
				outT.append(lis)
			return outT
		except:
			print("failed roi read")
			return []
	#readResultsTablesOfNumbers takes the speckle list table and turns it into a table that
	#python can write to a csv
	def readResultsTablesOfNumbers(self,tableName):
		#I can't figure out the syntax to preallocate memory,
		#this will not scale to many speckles
		try:
			RT = ResultsTable.getResultsTable(tableName)
			headers = RT.getHeadings()
			labelCol = RT.getColumnAsVariables(headers[0])
			numCols = len(headers)
			numRows = len(labelCol)
			out = []
			for col in range(numCols):
				out.append([])
				column = RT.getColumnAsVariables(headers[col])
				for row in range(numRows):
					out[col].append(column[row].getValue())
			outT = []
			for i in range(numRows):
				lis = []
				for j in range(numCols):
					lis.append(out[j][i])
				outT.append(lis)
			return outT
		except:
			print("failed speckle read")
			return []
	#this function does operation of adding left hand side column to the table
	def appendColToFront(self,column,matrix):
		try:
			for row in matrix:
				row.insert(0,column)
		except:
			print("failed to append the first entry to the front input"
			+"of the all the entries of the second.")
		finally:
			return matrix
		
class SaveStuff:
	def __init__(self,uniqueFileName):
		self.uniqueID = uniqueFileName[:-4]
		
		self.downloadsFolder = join(IJ.getDir("downloads"),"SpeckleResults")
		if not exists(self.downloadsFolder):
			os.mkdir(self.downloadsFolder)
			
	#this writes a suitably formatted table to a csv
	def table2CSV(self,csvName, writeTable):
		try:
			with open(join(self.downloadsFolder,csvName), 'a') as f:
				writer = csv.writer(f)
				writer.writerows(writeTable)
		except:
			print("failed to write table to csv.")
		finally:
			print("done.")
	#this saves the logs with a name based on what you add in the columns 
	def saveLogs(self):
		try:
			log = IJ.getLog()
			#change the below line to f=open(join(self.downloadsFolder,"logs.txt"),'a') 
			#for one log file to rule them all...it will append all logs to one file.
			f = open(join(self.downloadsFolder,self.uniqueID + " logs.txt"),'w')
			f.write(log)
		except:
			print("no speckles.")
		finally:
			f.close()
			
	def saveNewImages(self,oldImages):
		try:
			#this will extract all the new images generated sence oldImages was created
			#and will save them all to the downloads folder
			newImages = WindowManager.getImageTitles()
			titles2Save = list(set(newImages) - set(oldImages))
			iterID = int(0)
			for image in titles2Save:
				im2Save = WindowManager.getImage(image)
				IJ.save(im2Save, join(self.downloadsFolder,self.uniqueID 
				+ " speckleInspectorOutput{}.tif".format(iterID)))
				iterID = iterID + 1
		except:
			print("failed to save image.")
		finally:
			print("done.")
			
	def saveNewImage(self,oldImages):
		try:
			#this will extract one image
			newImages = WindowManager.getImageTitles()
			title2Save = list(set(newImages) - set(oldImages))
			im2Save = WindowManager.getImage(title2Save[0])
			IJ.save(im2Save, join(self.downloadsFolder,self.uniqueID 
			+ " speckleInspectorOutput{}.tif".format(iterID)))
		except:
			print("failed to save image.")
		finally:
			print("done.")
			
	def saveAllImages(self,oldImages):
		try:
			#this will extract all the new images generated sence oldImages was created
			#and will save them all to the downloads folder
			titles2Save = WindowManager.getImageTitles()
			inspectorOutput = list(set(titles2Save) - set(oldImages))[0]
			im2Save = WindowManager.getImage(inspectorOutput)
			IJ.save(im2Save,join(self.downloadsFolder,"InspectorOutput"+self.uniqueID+".tif"))
			iterID = int(0)
			for image in list(set(titles2Save) - set([inspectorOutput])):
				
				im2Save = WindowManager.getImage(image)
				IJ.save(im2Save, join(self.downloadsFolder,self.uniqueID 
					+ " speckleInspectorImage{}.tif".format(iterID)))
				iterID = iterID + 1
		except:
			print("failed to save image.")
		finally:
			print("finished saving all images.")


def main(channel1,channel2,ignoreString,primarySize):
	def writeTablesToCSV(channel,roiOut,speckleOut):
		try:
			#append your labels to them before they're written
			speckleOut_ = RTC.appendColToFront(channel[:-4], speckleOut)
			roiOut_ = RTC.appendColToFront(channel[:-4], roiOut)
			#save the tables to csvs -- they will append to a currently existing csv 
			#or create a new one
			Saves.table2CSV("speckleOutput.csv",speckleOut_)
			print('here')
			Saves.table2CSV("AnalysisOutput.csv",roiOut_)
		except:
			print("failed to write to csvs.")
		finally:
			print("finished writing tables to csvs.")
			
	#Begin
	RTC = ResultsTableToCSV(channel1,channel2,ignoreString)
	primary,secondary,images = RTC.getImageNames()
	speckleInputs = "primary=[{}] " \
		 "secondary=[{}] " \
		 "redirect=None min_primary_size={} show=secondary " \
		 "exclude speckle statistic secondary_object" 
	IJ.run("Speckle Inspector",speckleInputs.format(primary,secondary,primarySize))

	Saves = SaveStuff(primary)
	Saves.saveLogs()
	Saves.saveAllImages(images)
	
	speckleTableName = "Speckle List " + primary
	roiTableName = "Roi Analysis"
	
	roiOut = RTC.roiAnalysisToWrite(roiTableName)
	speckleOut = RTC.readResultsTablesOfNumbers(speckleTableName)
	WindowManager.closeAllWindows()
	
	writeTablesToCSV(channel1,roiOut,speckleOut)
	#End
	
if __name__ in ['__builtin__','__main__']:
	#these are examples below. Change them to your values
	main("Channel1","Channel2","Inspector",1000)


