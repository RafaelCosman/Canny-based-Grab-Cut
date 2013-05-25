"""
directories does all of the io for GrabCut
"""

import cv2
import sys
import os
import numpy as np

data = "data_GT/"
bboxes = "ICCV09_new_bounding_boxes/"
groundTruth = "seg_GT/"
output = "output/"
test = "test/"

bboxSuffix = ".txt"

def loadImageByName(filepath):
    return cv2.imread(filepath)

def loadBBoxByName(name):    
    filename = bboxes + name + bboxSuffix
    
    with open(filename) as f:
        return map(float, f)
    
def loadImagesAndBBoxes():
    x = loadImagesInFolder(data)
    
    images = [tup[0] for tup in x]
    filenames = [tup[1] for tup in x]
    
    bboxes = map(loadBBoxByName, filenames)
    
    assert not None in bboxes
    
    return zip(images, bboxes, filenames)

def loadImagesInFolder(folder):
    filenames = os.listdir(folder)
    images = [loadImageByName(folder + filename) for filename in filenames]
    
    assert not None in images
    
    filenames = [fname.split(".")[0] for fname in filenames]
    
    return zip(images, filenames)

def ensureDir(d):
    if not os.path.exists(d):
        os.makedirs(d)
        
def saveArrayAsImage(path, arr):
    arr = np.copy(arr)
    
    arr -= np.min(arr)
    arr *= 255/np.max(arr)
    
    cv2.cv.SaveImage(path, cv2.cv.fromarray(np.asarray(arr,dtype="int")))
    
def clearFolder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e    