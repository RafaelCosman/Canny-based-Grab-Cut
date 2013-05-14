"""
Makes the output of the grabCut algorithm more useful by actually applying the masks that it generates to the images in question.
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

import directories
from visualization import *
from scoreOutput import greyscale

def main():
    output = directories.loadImagesInFolder(directories.output)
    output = np.asarray(output)

    groundTruth = directories.loadImagesInFolder(directories.groundTruth)
    groundTruth = np.asarray(groundTruth)

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

        img = directories.loadImageByName(directories.data + fname + ".bmp")

        if img is None:
          img = directories.loadImageByName(directories.data + fname + ".jpg")

        assert img is not None

        img[outputImage ==  0] = 0

        cv2.cv.SaveImage("maskedImages/" + fname + ".jpg", cv2.cv.fromarray(np.asarray(img, dtype="int")))

    print("Done")

if __name__ == "__main__":
    main()