# repeatedSpeckleInspector
Run the Fiji or ImageJ speckle inspector with the same settings for a folder filled with subfolders containing image pairings. 
Your file structure should be as follows 
  Fiji.app/images/demo
   * capture1
     * ch1.tif
     * ch2.tif
   * capture2
     * ch1.tif
     * ch2.tif
      ...
    ...
<br />


<br />
Note) You can record a macro in Fiji that will track your manual execution of the speckle inspector. Look at the format string in the macro after you run it.
It looks something like "primary=[yourFileName.TIF]..." you can replace the inspectorInput with that but replace the 
file names with brackets '{}'. to change your settings. Or message me and I may help!

Instructions to use “SmootherSpecklingUpdate.py”

In a single run, this code will convert 16-bit TIFs into binary 8-bit TIFs at custom set thresholds, then run the BioVoxxel Speckle Inspector for each of the binary pairs, and save the results in combined spreadsheets.  

You can set your own lower threshold for each of two channels to optimize signal-to-noise for your assay. **You should manually adjust images (using command t in ImageJ) to get a sense of where your threshold should be.** This will vary by assay and should be determined by testing for the highest (most sensitive) lower threshold that doesn’t lead to high background. The goal is to detect true signal without losing foci. You can also customize your minimum primary image size. 

Before you begin: 

1.	Exposure times for your protein of interest should be the same for all of your images. 
2.	You will need to start with single channel 16-bit TIFs in individual folders. 16-bit images contain far more information than 8-bit images. You can do this when you export images from the AxioVision:
a.	Make sure “Create project folder” is checked (under the top file panel)
b.	Do not generate merged images
c.	Use channel names
d.	Uncheck “Convert to 8-bit” (left)
e.	Export as TIF (middle)
3.	Download (Fiji is Just) ImageJ if you haven’t already
a.	https://imagej.net/Fiji/Downloads
4.	Install the BioVoxxel Toolbox for ImageJ if you haven’t already
a.	https://imagej.net/BioVoxxel_Toolbox
5.	Download SmootherSpeckling.py from: https://github.com/kyleButler9/repeatedSpeckleInspector
a.	Click the green “Code” button on the home screen
b.	Then click “Download ZIP”
c.	Unzip the file
6.	Save SmootherSpeckling.py to the “scripts” folder in the Fiji application
a.	Copy the .py file
b.	Go to Applications in your file explorer (Finder)
c.	Open the app’s files by right clicking it and then clicking “open package contents”
7.	Save your images in a folder within Fiji’s “images” folder

Set up and run the script: 

8.	Open Fiji. Go to File  Open  Fiji  scripts  SmootherSpeckling.py
9.	Edit the code for your experiment in the last line (keep the quotation marks):
a.	Change demo to the name of your folder of images in the Fiji app’s images folder
b.	Change ch1 to DAPI. Change ch2 to GFP or dsRed (whichever channel you used for the protein of interest). If you forgot to check “Use channel names” in AxioVision, use the channel label in your image title names.
c.	Change 500 to any number of pixels you want to be the minimum primary size during the speckle inspection. 3000 is a good number. It is optimized to exclude micronuclei but does not ignore full nuclei. 
d.	The next number after 500 is the lower threshold for your DAPI (primary) image. The default is 15, but you should test some images to make sure it works for your DAPI staining. The goal is to cover the entire nucleus. A bit of background is actually fine (only for DAPI), as long as it doesn’t merge signals from your nuclei. 
e.	The last number is the lower threshold for your secondary image (your protein of interest). How to determine this number is explained above (**).
10.	 Name the output data folder yourself: go to line 151 in the code that reads: self.downloadsFolder = join(IJ.getDir("downloads"),"SpeckleResults" + elapsedTimeStr[:-3])
a.	Delete the elapsedTimeStr[:-3]
b.	Put in quotation marks the name you want for your results folder. Note: it will be saved in your downloads folder.
11.	It is recommended that you save (command s) this edited code for the next time you use it.
12.	Click run and watch the data run.
13.	It is done when it says “script completed successfully” in the console.

Troubleshooting:
•	For the error “incompatible files” try breaking the data into two separate folders and runs. 

After running SmootherSpeckling.py:

14.	Go to your downloads folder
15.	Open the SpeckleResults folder (or whatever you named it)
a.	Check that all is there: 
b.	AnalysisOutput.csv
i.	This is the compiled ROI data for each speckle
c.	speckleOutput.csv
i.	This is the compiled list of the number of speckles per nucleus
d.	speckleInspectorImage0 for each image
i.	This is the binary image of the speckle protein signal
e.	speckleInspectorImage1 for each image
i.	This is the binary image of DAPI signal
f.	logs.txt for each image
g.	InspectorOutput.tif for each image
i.	This counts the nuclei and shows the number of speckles counted per nucleus. The nuclei are pink. The ignored DAPI signal is black.
16.	Save the SpeckleResults folder somewhere on your computer.
17.	Open all of the InspectorOutput files. Scroll through for quality control of each image. 

Clean up the data and tables

18.	Make a list of each “bad” image’s number or name. You will delete this data from each of the two results csvs. I suggest you save this list to your computer for record keeping. Likewise, it is recommended that you list the reason for deleting the data. Examples of data to delete:
a.	A micronucleus that is counted as a nucleus (primary object) (pink with a number of speckles listed in white).
b.	Multiple nuclei counted as a single nucleus (because they are too close together).
c.	Any aberrant DAPI staining counted as an individual nucleus (pink).
d.	Some things that are okay:
i.	Black DAPI signal in the background. As long as it’s not counted as a nucleus (pink), then it won’t affect your data analysis.
ii.	Black DAPI signal that was not counted because it was on the edge of the image. The program is set to run to ignore primary objects on the edges so that you don’t get an incomplete readout of a nucleus.
iii.	Pink blobs connected to a nucleus. I believe these are micronuclei that are close to the nucleus, and should not affect your analysis. The speckle analysis does not depend on nucleus size.
e.	Save your list. 
19.	Save speckleOutput.csv and AnalysisOutput.csv with an identifying name for the experiment. For each run, the code will always be directed to a csv with the default name. 





