"""
These are the (default) settings for the grabcut algorithm.
grabcut.py uses these values directly, but note that runTests.py changes these values at runtime.
"""

#General settings
sizeRatio = 10 #scale the images down by this factor before executing GrabCut

#Unary edge settings
bias = 0

#Canny settings
apertureSizes = [3, 5]

#GMM settings
numGMMs = 3
numComponents = 10
alpha = .002
covType = 'full'

#Binary edge settings
binaryEdgeStrength = 20.0
diagonal = True