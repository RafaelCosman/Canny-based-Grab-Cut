import numpy as np
import matplotlib.pyplot as plt
import cv2

import directories
from visualization import *

def greyscale(img):
    return np.average(img, 2)

def threshold(arr, threshold):
    arr[arr<threshold] = 0
    arr[arr != 0] = 255

def main():
    output = directories.loadImagesInFolder(directories.output)
    output = np.asarray(output)
    
    groundTruth = directories.loadImagesInFolder(directories.groundTruth)
    groundTruth = np.asarray(groundTruth)
    
    print("")
    print("Name\t\tYour dif")
    
    l = []
    for outputImage in output:
        #Find the corresponding groundTruth image
        fname = outputImage[1]
        groundTruthImage = groundTruth[groundTruth[:, 1] == fname][0][0]
        
        #Now compare the output with the ground truth
        groundTruthImage = greyscale(groundTruthImage)
        pixelsTotal = groundTruthImage.size
        
        outputImage = np.asarray(outputImage[0])
        outputImage = greyscale(outputImage)
        threshold(outputImage, 150)

        assert groundTruthImage.shape == outputImage.shape
        
        pixelsDifferent = np.count_nonzero(outputImage != groundTruthImage)
        fractionDifferent = float(pixelsDifferent)/pixelsTotal
        #pixels2Different = np.count_nonzero(output2Image != groundTruthImage)
        
        #print(fname + ":   \t" + "{:.0%}".format(fractionDifferent))# + ":   \t\t" + "{:.0%}".format(float(pixels2Different)/pixelsTotal))
        
        #visualize(outputImage - groundTruthImage)
        l.append((fractionDifferent, fname))
        
    for fractionDifferent, fname in sorted(l):
        print(fname + ":   \t" + "{:.1%}".format(fractionDifferent))# + ":   \t\t" + "{:.0%}".format(float(pixels2Different)/pixelsTotal))
        
    return l
        
if __name__ == "__main__":
    main()