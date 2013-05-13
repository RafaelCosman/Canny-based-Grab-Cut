"""
These are the settings for the grabcut algorithm
"""

#Unary edge settings
bias = -.01

#Canny settings
apertureSizes = [3, 5, 7]

#GMM settings
numComponents = 10
alpha = .002
covType = 'full'

#Binary edge settings
binaryEdgeStrength = 20.0