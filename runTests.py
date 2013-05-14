import grabcut
import scoreOutput
import directories
import settings

def main():
    scores = []
    """
    for settings.binaryEdgeStrength in [.0001, .0001, .001, .001, .01, .01, .1, .1, 1, 1, 10, 10, 100, 100, 1000, 1000, 10000, 10000]:
        directories.output = "output" + "-" + "binaryEdgeStrength" + "-" + str(settings.binaryEdgeStrength) + "/"
        directories.ensureDir(directories.output)
        
        grabcut.main()
        scores.append(scoreOutput.main())
    """ 
    """
    for settings.apertureSizes in [[3, 5], [3, 5, 7], [3], [5], [7]]:
        directories.output = "output" + "-" + "apertureSizes" + "-" + str(settings.apertureSizes) + "/"
        directories.ensureDir(directories.output)
        
        grabcut.main()
        scores.append(scoreOutput.main())
    """
    for settings.numGMMs in [1, 2, 3, 4, 5, 6, 7]:
        directories.output = "output" + "-" + "numGMMs" + "-" + str(settings.numGMMs) + "/"
        directories.ensureDir(directories.output)
        
        grabcut.main()
        scores.append(scoreOutput.main())
        
    print("")
    print("")
    
    for score in scores:
        for fractionDifferent, fname in sorted(score):
            print(fname + ":   \t" + "{:.1%}".format(fractionDifferent))# + ":   \t\t" + "{:.0%}".format(float(pixels2Different)/pixelsTotal))

if __name__ == "__main__":
    main()