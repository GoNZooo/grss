class CAutoDLItem:
    def __init__(self, name, regex):
        self.name = name
        self.regex = regex

def getAutoDownloads():
    inFile = open("autodl.cfg", "r")
    autoDownloads = []
    for line in inFile:
        tmpName = line[: line.find(";")]
        tmpRegex = line[line.find(";") + 1:]
        autoDownloads.append(CAutoDLItem(tmpName, tmpRegex))
        inFile.close()


    return autoDownloads

