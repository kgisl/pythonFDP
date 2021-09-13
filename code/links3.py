import requests
from bs4 import BeautifulSoup

'''
http://www.w3.org/TR/html5/text-level-semantics.html#the-a-element

anchors contains \<a\> tag elements from the HTML content.
Iterate through the list of anchors and extract 'href' property value
that start with 'https:'
'''
# http://j.mp/linktagPythonCode - borrowed code from this example


def getOutBoundURLs(a_tags):
    urls = []
    for x in a_tags:
        if x.has_attr('href'):
            href = x.get('href').strip("/")
            if href.startswith("http:") or href.startswith("https:"):
                if href not in urls:
                    urls.append(href)
    return urls


def generateBanner(url, anchorCount, linkCount):
    return '''
#############################
---- Outbound links for {0} ({1}, {2}, https: {3})
#############################
'''.format(url, str(anchorCount), str(linkCount))


def printURLs(url, anchors, f=None):
    # outBoundURLs = getOutBoundURLs(anchors)
    # hhrefs       = getOutBoundHttpURLs(outBoundURLs)
    # banner = generateBanner(url, len(anchors), len(outBoundURLs), len(hhrefs))
    hhrefs = getOutBoundURLs(anchors)
    banner = generateBanner(url, len(anchors), len(hhrefs))
    print(banner)
    if f:
        f.write(banner)

    for linkaddress in hhrefs:
        print("  -", linkaddress)
        if f:
            f.write(url + " -> " + linkaddress + "\n")


urls = ["https://www.reddit.com/r/learnprogramming/comments/6tvjsw/stepbystep_guide_from_beginner_to_worthy_of_a_job/", "https://gitter.im/kgisl/campsite?utm_source=share-link&utm_medium=link&utm_campaign=share-link"
        # , "http://sijinjoseph.com/programmer-competency-matrix/"
        # , "http://pydanny.blogspot.in/2011/08/github-is-my-resume.html"
        # , "http://www.python.org", "http://www.facebook.com", "http://www.kct.ac.in"
        # , "http://www.psgtech.edu", "http://www.kgkite.ac.in", "http://www.sece.ac.in"
        # , "http://www.siet.ac.in", "http://www.bennett.edu.in" ]
        ]

dataFile = open("data.txt", "w")
for url in urls:
    html = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    print(html)
    soup = BeautifulSoup(html.text)
    anchors = soup.find_all("a")
    printURLs(url, anchors, dataFile)
dataFile.close()


####### legacy ###################
def getOutBoundURLs2(anchors):
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
