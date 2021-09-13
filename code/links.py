import requests
from bs4 import BeautifulSoup


def getOutBoundURLs(anchors):
    '''http://www.w3.org/TR/html5/text-level-semantics.html#the-a-element
    anchors contains all \<a\> tag elements from the HTML content.
    Iterate through the list of anchors and build list containing
    the href addresses whenever it is available.

    @author kgashok

    '''
    addressList = []
    for anchor in anchors:
        try:
            linkaddress = anchor.attrs['href']
            addressList.append(linkaddress)
        except BaseException:
            print("Ignoring", anchor)
    return addressList


def getOutBoundHttpURLs(alist):
    return [address for address in alist if address.startswith("https:")]


def generateBanner(url, anchorCount, outBoundCount, linkCount):
    return '''
#############################
---- Outbound links for {0} ({1}, {2}, https: {3})
#############################
'''.format(url, str(anchorCount), str(outBoundCount), str(linkCount))


def printURLs(url, anchors, f=None):
    '''
    Print only those addresses that start with 'https' from valid anchors
    if 'f'ilename is valid, write extracted URLs to file as well
    '''
    outBoundURLs = getOutBoundURLs(anchors)
    hhrefs = getOutBoundHttpURLs(outBoundURLs)

    banner = generateBanner(url, len(anchors), len(outBoundURLs), len(hhrefs))
    print(banner)
    if f:
        f.write(banner)

    for linkaddress in hhrefs:
        print(linkaddress)
        if f:
            f.write(url + " -> " + linkaddress + "\n")


urls = ["http://www.python.org", "http://www.facebook.com", "http://www.kct.ac.in", "http://www.psgtech.edu", "http://www.kgkite.ac.in"        # , "http://www.kghospital.com"
        # , "http://www.kgisl.com"
        , "http://www.sece.ac.in", "http://www.siet.ac.in", "http://www.bennett.edu.in"
        ]

dataFile = open("data.txt", "w")

for url in urls:
    html = requests.get(url)
    soup = BeautifulSoup(html.text)
    anchors = soup.find_all("a")
    # equivalent one-liner
    # anchors = BeautifulSoup(requests.get("http://www.python.org").text).find_all('a')
    printURLs(url, anchors, dataFile)

dataFile.close()
