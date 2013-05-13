import grabcut
import scoreOutput
import directories
import settings

def main():
    scores = []
    
    for settings.binaryEdgeStrength in [.0001, .0001, .001, .001, .01, .01, .1, .1, 1, 1, 10, 10, 100, 100, 1000, 1000, 10000, 10000]:
        directories.output = "output" + "-" + "binaryEdgeStrength" + "-" + str(settings.binaryEdgeStrength) + "/"
        directories.ensureDir(directories.output)
        
        grabcut.main()
        scores.append(scoreOutput.main())
    """ 
    for settings.binaryEdgeStrength in [.001, .001, .01, .01, .1, .1, 1, 1, 10, 10, 100, 100, 1000, 1000, 10000, 10000]:
        directories.output = "output" + "-" + "binaryEdgeStrength" + "-" + str(settings.binaryEdgeStrength) + "/"
        directories.ensureDir(directories.output)
        
        grabcut.main()
        scores.append(scoreOutput.main())
    """
    print("")
    print("")
    
    for score in scores:
        for fractionDifferent, fname in sorted(score):
            print(fname + ":   \t" + "{:.1%}".format(fractionDifferent))# + ":   \t\t" + "{:.0%}".format(float(pixels2Different)/pixelsTotal))

if __name__ == "__main__":
    main()