# repeatedSpeckleInspector
Run the Fiji or ImageJ speckle inspector with the same settings for a folder filled with subfolders containing image pairings. 
Your structure should be as follows 
  Fiji.app/images/demo
    capture1
      ch1.tif
      ch2.tif
    capture2
      ch1.tif
      ch2.tif
      ...
    ...

At the very bottom, you will see example inputs to replace with yours inside a "dirInputMain()" function.
The function inputs are defined as follows:
  dirInputmain("demo","ch1","ch2","ch1IgnorePhrase","ch2IgnorePhrase",500,15,84)
    1) replace "demo" with the name of your folder in the Fiji.app/images directory
    2) replace "ch1" and "ch2" with a character string thats present in every primary and secondary image in your folders subfolders.
    3) replace "ch1IgnorePhrase" and "ch2IgnorePhrase" with character strings that may be present in images in your folders subfolders that are not your primary and secondary images respectively but that may still contain your equivalents to "ch1" and "ch2" in their names. 
    4) replace 500 with your min primary size specification for the speckle inspector
    5) replace 15 with your Renyi binarization threshold for the primary image
    6) replace 84 with your Renyi binarization threshold for the secondary image
    7) open the .py file in Fiji using "ctrl + o" or access the file dropdown and select open.
    8) run the script, making sure that under the lenguages drop down of the Fiji text editor Python is selected
      **if you cannot find python in the lengauages dropdown, update your version of Fiji. 


Note) You can record a macro in Fiji that will track your manual execution of the speckle inspector. Look at the format string in the macro after you run it.
It looks something like "primary=[yourFileName.TIF]..." you can replace the inspectorInput with that but replace the 
file names with brackets '{}'. to change your settings. Or message me and I may help!



