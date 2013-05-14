"""
These are the settings for the grabcut algorithm
"""

#General settings
sizeRatio = 10 #scale the images down by this factor before executing GrabCut

#Unary edge settings
bias = -.01

#Canny settings
apertureSizes = [3, 5]

#GMM settings
numComponents = 10
alpha = .002
covType = 'full'

#Binary edge settings
binaryEdgeStrength = 20.0