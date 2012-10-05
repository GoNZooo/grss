import re

# Conversion table for translation of human readable units.
conversions = {
                "m": 60,
                "h": 60 * 60,
                "d": 60 * 60 * 24,
                "w": 60 * 60 * 24 * 7
                }

class CAutoDLItem:
    def __init__(self, name, regex, interval):
        self.name = name
        self.regex = regex
        self.interval = interval

    # Function to single out a given subterm and calculate the
    # total time of that one unit.
    def findHumanReadable(self, term, key):
        pos = term.find(key)
        if pos != -1:
            coefficient = int(term[: pos])
            return coefficient * conversions[key]
        else:
            return 0
    
    # Function to translate the human readable formats
    # in the interval specification to seconds.
    def translateHumanReadable(self, term):
        totalTime = 0
        totalTime += self.findHumanReadable(term, "w")
        term = term[(term.find("w") + 1): ]
        
        totalTime += self.findHumanReadable(term, "d")
        term = term[(term.find("d") + 1): ]
        
        totalTime += self.findHumanReadable(term, "h")
        term = term[(term.find("h") + 1): ]
        
        totalTime += self.findHumanReadable(term, "m")
        
        return totalTime

    def matchRegex(self, feedItem):
        if re.match(self.regex, feedItem.title, 16):
            return True
        else:
            return False

# Reading the autodl.cfg (or any other given file)
# and the data necessary for a AutoDL item.
def getAutoDownloads(filename = "autodl.cfg"):
    inFile = open(filename, "r")
    autoDownloads = []
    for line in inFile:
        splitLine = line.split(";")
        tmpName = splitLine[0]
        tmpRegex = splitLine[1]
        tmpInterval = splitLine[2].strip("\n")
        autoDownloads.append(CAutoDLItem(tmpName, tmpRegex, tmpInterval))
    inFile.close()

    return autoDownloads

if __name__ == "__main__":
    autoList = getAutoDownloads()
    for item in autoList:
        print(item.name, item.regex, item.interval,
                item.translateHumanReadable(item.interval), sep="\t")

