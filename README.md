# repeatedSpeckleInspector
Run the Fiji or ImageJ speckle inspector with the same settings for a folder filled with subfolders containing image pairings. 
Your structure should be as follows 
  Fiji.app/images/demo
    capture1
      channel1.tif
      channel2.tif
    capture2
      channel1.tif
      channel2.tif
      ...
    ...

At the very bottom, you will see example inputs to replace with yours inside a "dirInputMain()" function.
The function inputs are defined as follows:


Note) You can record a macro in Fiji that will track your manual execution of the speckle inspector. Look at the format string in the macro after you run it.
It looks something like "primary=[yourFileName.TIF]..." you can replace the inspectorInput with that but replace the 
file names with brackets '{}'. to change your settings. Or message me and I may help!



