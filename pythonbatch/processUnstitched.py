#!/usr/local/bin/python

# Set default logging handler to avoid "No handler found" warnings.
import glob

import string 

# Here add the path to the default template you want to use...
<<<<<<< HEAD
templateString = open('templates/template-reference.pto', 'r').read()
=======
templateString = open('templates/template-XiaomiMijiaMi.pto', 'r').read()
>>>>>>> origin/master

# Path of the unstitched images - Copy your JPG files in the "files" folder
files = glob.glob("files/*.JPG")

for entry in files:
	filenameImage=entry.replace('files/', '')
	filenamePTOOutput=entry.replace('.JPG', '.pto')

	stringToWrite=templateString
	stringToWrite = string.replace(stringToWrite,'image.jpg',filenameImage)
	
	text_file = open(filenamePTOOutput, "w")
	text_file.write(stringToWrite)
	text_file.close()




	
	
