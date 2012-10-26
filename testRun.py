import time
import os
import sys
import autoDownloads
import feedParser
import pathcfg

if len(sys.argv) > 1:
    sleepTime = int(sys.argv[1])
else:
    sleepTime = 5 * 60

while running:
    if not os.system(pathcfg.wget + " http://rss.torrentleech.org/545bd4247b6ebdf311b7 -O current.xml"):
        dataFile = open("current.xml", "r")
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
                        print("Downloading:", autoItem.name,
                                autoItem.regex, item.title, sep = "\t")
                        item.download()
    time.sleep(sleepTime)
