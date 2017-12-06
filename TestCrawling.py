from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import datetime
import random

# html = urlopen("https://nba.hupu.com/teams/warriors")
pages = set()
random.seed(datetime.datetime.now())


# get innerlinks
def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    internalLinks = []
    # get links of head with "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                if link.attrs["href"].startWith("/"):
                    internalLinks.append(includeUrl + link.attrs["href"])
                else:
                    internalLinks.append(link.attrs["href"])
    return internalLinks


# ger outer links
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(http|https|www)((?!" + excludeUrl + ").)*$")):
        if link is not None:
            if link not in externalLinks:
                externalLinks.append(link.attrs["href"])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts
