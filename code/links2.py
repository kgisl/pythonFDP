import requests
from bs4 import BeautifulSoup

urls = [ "http://www.python.org"
       , "http://www.facebook.com"
       , "http://www.kct.ac.in"
       , "http://www.psgtech.edu"
       , "http://www.kgkite.ac.in"
       #, "http://www.kghospital.com"
       #, "http://www.kgisl.com"
       #, "http://www.sece.ac.in"
       #, "http://www.siet.ac.in"
       #, "http://www.bennett.edu.in"
       ]
       


'''
    http://www.w3.org/TR/html5/text-level-semantics.html#the-a-element

    anchors contains <a> tag elements from the HTML content.
    Iterate through the list of anchors and print hyperlink addresses
    that start with 'http'
'''
def get_addresses (anchors): 
    alist = []
    for anchor in anchors:
        try:
            linkaddress = anchor.attrs['href']
            if linkaddress.startswith("https:"): # or linkaddress.startswith("http:"):
                alist.append(linkaddress)
        #print(linkaddress)
        except:
            print("Ignoring", anchor)
    return alist
        
def printURLs(url, anchors, f=None):
    banner = '''
#############################
---- Outbound links for {0} ({1})
#############################
'''.format(url,str(len(anchors)))

    print(banner)
    if f: f.write(banner)
    
    addresses = get_addresses(anchors)
    print(addresses)
    if f:
        [f.write(url + " -> " + address+"\n") for address in addresses]
        

dataFile = open("data.txt", "w")    

for url in urls:
    html = requests.get(url)
    soup = BeautifulSoup(html.text)
    anchors = soup.find_all("a")
    # anchors = BeautifulSoup(requests.get("http://www.python.org").text).find_all('a')
    printURLs(url, anchors, dataFile)

dataFile.close()




# Need to improve on this 
# https://developers.google.com/custom-search/docs/xml_results#WebSearch_Request_Format
# https://stackoverflow.com/a/22629483/307454
def googleSearch(query):
    with requests.session() as c:
        url = 'https://www.google.com/search'
        query = {'q': query, 'pli':1}
        urllink = requests.get(url, params=query)
        print (urllink.url)
        soup = BeautifulSoup(urllink.content)
        
        anchors = soup.find_all('a')
        printURLs(urllink.url, anchors)

#googleSearch('Dharmaveera Govindaswamy Naidu')
#googlesearch('Python programming')

### Alternative function 
### Needs to be debugged to work 
def googlesearch(searchfor):                                                                                                                                                                                       
    link = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0' #&%s' % searchfor                                                                                                                              
    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}                                                                
    payload = {'q': searchfor}                                                                                                                                                                             
    response = requests.get(link, headers=ua, params=payload)                                                                                                                                                      
    print (response.url)
    soup = BeautifulSoup(response.content)
    
    anchors = soup.find_all('a')
    printURLs(response.url, anchors)
    
    
