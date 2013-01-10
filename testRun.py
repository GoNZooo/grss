import time
import os
import sys
import autoDownloads
import feedParser
import pathcfg
from optparse import OptionParser



if __name__ == "__main__":
    parser = OptionParser()

    parser.add_option ("-s", "--sleep", action = "store", dest = "sleeptime",
                        default = 5 * 62, type = "int",
                        help = "How long the system should wait between GETs.")
    parser.add_option ("-w", "--wget", action = "store", dest = "wget_path",
                        default = pathcfg.wget, type = "string",
                        help = "Path to wget.")
    parser.add_option ("-r", "--rss", action = "store", dest = "rss_url",
                        default = pathcfg.rssURL, type = "string",
                        help = "URL to RSS feed.")

    (options, args) = parser.parse_args()
    running = True
    downloaded = []

    if pathcfg.rssURL == "http://PUT/RSS/URL/HERE":
        running = False
        print("Default feed URL detected.")
        print("You need to configure your RSS URL in the pathcfg.py file.")

    while running:
        if not os.system(options.wget_path + " " + options.rss_url +  " -O current.xml"):
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
                                print("Match:", autoItem.name,
                                    autoItem.regex, item.title, sep = "\t")
                                item.download()
                                downloaded.append(item.link)
        time.sleep(options.sleeptime)
        loop += 1
        if loop >= 400:
            downloaded = []
            loop = 0

