import time
import os
import sys
import autoDownloads
import feedParser
import pathcfg

running = True
downloaded = []

if pathcfg.rssURL == "http://PUT/RSS/URL/HERE":
    running = False
    print("Default feed URL detected.")
    print("You need to configure your RSS URL in the pathcfg.py file.")

if len(sys.argv) > 1:
    sleepTime = int(sys.argv[1])
else:
    sleepTime = 5 * 60

while running:
    if not os.system(pathcfg.wget + " " + pathcfg.rssURL +  " -O current.xml"):
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
                        if item.link not in downloaded:
                            print("Downloading:", autoItem.name,
                                autoItem.regex, item.title, sep = "\t")
                            item.download()
                            downloaded.append(item.link)
    time.sleep(sleepTime)
