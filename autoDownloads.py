import os
import re
import pathcfg

class CAutoDLItem:
    def __init__(self, name, regex):
        self.name = name
        self.regex = regex

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
        splitLine = line.strip("\n").split(";")
        tmpName = splitLine[0]
        tmpRegex = splitLine[1]
        autoDownloads.append(CAutoDLItem(tmpName, tmpRegex))
    inFile.close()

    return autoDownloads

if __name__ == "__main__":
    autoList = getAutoDownloads()
    for item in autoList:
        print(item.name, item.regex, sep="\t")

