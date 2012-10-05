import feedParser
import autoDownloads

dataFile = open("testFeed.xml", "r")
data = dataFile.read()
dataFile.close()

channels = feedParser.separateChannels(data)
if channels:
    itemStrings = feedParser.separateItems(channels[0])
    itemContainers = feedParser.createItemContainers(itemStrings)

    autoList = autoDownloads.getAutoDownloads()
    for autoItem in autoList:
        for item in itemContainers:
            if autoItem.matchRegex(item):
                print("Match found:", autoItem.name, autoItem.regex,
                        item.title, sep = "\t")

