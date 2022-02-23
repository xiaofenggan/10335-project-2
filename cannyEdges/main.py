import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# references:
#	- https://www.askpython.com/python/examples/edge-detection-in-images
#	- https://www.geeksforgeeks.org/python-opencv-cv2-imwrite-method/
 
NEW_FILENAME = "jellyfish"
OLD_DIRECTORY_BAD_NAMING_CONVENTIONS = "jellyfishBadFilenames"
NEW_DIRECTORY_GOOD_NAMING_CONVENTIONS = "jellyfishColor"
CANNY_EDGE_OUTPUT_DIRECTORY = "jellyfishEdge"

def convertImage(originalImg):
	# Converts colored .jpg to greyscale, then to canny edge image
	grayImage = cv2.cvtColor(originalImg, cv2.COLOR_BGR2GRAY)
	edgedImage = cv2.Canny(grayImage, threshold1=30, threshold2=100)
	return edgedImage

def saveImages(originalImg, edgeImage, filename):
	# Saves the original image to a new folder, with better naming convention
	# Also saves the edge image to a different folder
	ogPath = NEW_DIRECTORY_GOOD_NAMING_CONVENTIONS + "/" + filename
	edgePath = CANNY_EDGE_OUTPUT_DIRECTORY + "/" + filename
	cv2.imwrite(ogPath, originalImg)
	cv2.imwrite(edgePath, edgeImage)

rootDir = OLD_DIRECTORY_BAD_NAMING_CONVENTIONS
for dirName, subdirList, fileList in os.walk(rootDir):
	print('Found directory: %s' % dirName)
	counter = 0
	for f in fileList:
		print('\t%s' % f)
		filePath = rootDir + "/" + f
		loadedImage = cv2.imread(filePath)
		loadedImage = cv2.cvtColor(loadedImage, cv2.COLOR_BGR2RGB)
		grayImage = cv2.cvtColor(loadedImage, cv2.COLOR_BGR2GRAY)
		edgeImage = cv2.Canny(grayImage, threshold1=30, threshold2=100)
		newName = NEW_FILENAME + str(counter) + ".jpg"
		saveImages(loadedImage, edgeImage, newName)
		counter += 1







