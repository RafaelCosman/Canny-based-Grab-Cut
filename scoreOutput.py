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
    output2 = directories.loadImagesInFolder("outputOpenCV100Iteration/")
    groundTruth = directories.loadImagesInFolder(directories.groundTruth)
    
    print("")
    print("Name\t\tYour dif.\tOpenCV dif.")
    
    for outputImage, groundTruthImage in zip(output, groundTruth):
        fname = outputImage[1]

        groundTruthImage = np.asarray(groundTruthImage)[0]
        groundTruthImage = greyscale(groundTruthImage)
        pixelsTotal = groundTruthImage.size
        
        outputImage = np.asarray(outputImage[0])
        outputImage = greyscale(outputImage)
        threshold(outputImage, 150)
        sizeRatio = (groundTruthImage.shape[0]) / (outputImage.shape[0])
        outputImage = np.asarray(np.repeat(np.repeat(outputImage, sizeRatio, axis=0), sizeRatio, axis=1))
        """
        output2Image = np.asarray(output2Image[0])
        output2Image = greyscale(output2Image)
        threshold(output2Image, 150)
        """
        
        if not groundTruthImage.shape == outputImage.shape:
            import pdb; pdb.set_trace()
        
        pixelsDifferent = np.count_nonzero(outputImage != groundTruthImage)
        fractionDifferent = float(pixelsDifferent)/pixelsTotal
        #pixels2Different = np.count_nonzero(output2Image != groundTruthImage)
        
        print(fname + ":   \t" + "{:.0%}".format(fractionDifferent))# + ":   \t\t" + "{:.0%}".format(float(pixels2Different)/pixelsTotal))
        visualize(outputImage - groundTruthImage)
        
if __name__ == "__main__":
    main()