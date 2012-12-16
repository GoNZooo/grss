import os
import re
import pathcfg

class CAutoDLItem:
    def __init__(self, name, regex, notPatterns = ""):
        self.name = name
        self.regex = regex
        self.notPatterns = notPatterns

    def matchRegex(self, feedItem):
        if re.match(self.regex, feedItem.title, 16):
            if self.notPatterns:
                for pattern in self.notPatterns:
                    if re.match(pattern, feedItem.title, 16):
                        return False
            return True
        else:
            return False

# Reading the autodl.cfg (or any other given file)
# and the data necessary for a AutoDL item.
def getAutoDownloads(filename = "autodl.cfg"):
    inFile = open(filename, "r")
    autoDownloads = []
    for line in inFile:
        splitLine = line.strip("\n").split(";")
        tmpName = splitLine[0]
        tmpRegex = splitLine[1]
        tmpNotPatterns = ""
        if len(splitLine) > 2:
            tmpNotPatterns = splitLine[2:]
        autoDownloads.append(CAutoDLItem(tmpName, tmpRegex, tmpNotPatterns))
    inFile.close()

    return autoDownloads

if __name__ == "__main__":
    autoList = getAutoDownloads()
    for item in autoList:
        print(item.name, item.regex, sep = "\t")
        if item.notPatterns:
            for pattern in item.notPatterns:
                print("NOT", pattern, sep = "\t")
        print("")

