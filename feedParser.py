import re

class CItem:
    def __init__(self, title, date, category, guid,
                    comments, link, description):
        self.title = title
        self.date = date
        self.category = category
        self.guid = guid
        self.comments = comments
        self.link = link
        self.description = description

def separateChannels(data):
    # 16 is the flag for the dot matching newlines.
    return re.findall("<channel>.*?</channel>", data, 16)

def separateItems(data):
    return re.findall("<item>(.*?)</item>", data, 16)

def getTitle(item):
    return "".join(re.findall("<title><!\[CDATA\[(.*)\]\]></title>", item, 16))
def getDate(item):
    return "".join(re.findall("<pubDate>(.*)</pubDate>", item, 16))
def getCategory(item):
    return "".join(re.findall("<category>(.*)</category>", item, 16))
def getGUID(item):
    return "".join(re.findall("<guid>(.*)</guid>", item, 16))
def getComments(item):
    return "".join(re.findall("<comments><!\[CDATA\[(.*)\]\]></comments>", item, 16))
def getLink(item):
    return "".join(re.findall("<link><!\[CDATA\[(.*)\]\]></link>", item, 16))
def getDescription(item):
    return "".join(re.findall("<description><!\[CDATA\[\[(.*)\]\]></description>", item, 16))

def createItemContainers(itemList):
    itemContainers = []
    for item in itemList:
        tmpItem = CItem(getTitle(item), getDate(item), getCategory(item),
                        getGUID(item), getComments(item), getLink(item),
                        getDescription(item))
        itemContainers.append(tmpItem)
    return itemContainers

if __name__ == "__main__":
    dataFile = open("testFeed.xml", "r")
    data = dataFile.read()
    dataFile.close()

    channels = separateChannels(data)
    if channels:
        itemStrings = separateItems(channels[0])
        itemContainers = createItemContainers(itemStrings)
        for item in itemContainers:
            print(item.title)
            print(item.date)
            print(item.category)
            print(item.guid)
            print(item.comments)
            print(item.link)
