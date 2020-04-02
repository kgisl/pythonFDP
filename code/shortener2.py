#!/usr/bin/env python

# Import the modules

import requests
import bitly
import sys

# https://dev.bitly.com/links.html#
# https://dev.bitly.com/user_info.html
# http://code.activestate.com/recipes/578263-url-shortner-using-bitly-api/

# Define your API information

API_USER = "o_1e3c72ka8t"
API_KEY = "1ef1315a2efebd7557de137f776602276d833cb9"

'''
b = bitly.Bitly(API_USER, API_KEY)

# Define how to use the program

usage = """Usage: python shortener.py [url]
e.g python shortener.py http://www.google.com"""

if len(sys.argv) != 2:
    print (usage)
    sys.exit(0)

longurl = sys.argv[1]

response = b.shorten(longUrl=longurl)

print (response['url'])
'''


bURL = "https://api-ssl.bitly.com/v3/user/link_history?access_token=" + API_KEY
#bURL = "https://api-ssl.bitly.com/v3/user/link_history"
r = requests.get(bURL)

print("Request status", r.status_code)

# print(r.json())


linkcount = r.json()['data']['result_count']

errorlist = []
validlist = []


def printlist(alist):
    for x in alist:
        print(x)


token_to_find = 'prezi'
links_to_visit = 5000
#links_to_visit = linkcount

i = 0
for offset in range(0, links_to_visit, 100):
    offsetURL = bURL + "&limit=100&offset=" + str(offset)
    r = requests.get(offsetURL)
    if r.status_code != 200:
        print("Error", bURL)
        break
    link_history = r.json()['data']['link_history']
    for link in link_history:
        linkurl = link['long_url']
        if linkurl.find(token_to_find) != -1:
            try:
                keywordurl = link['keyword_link']
            except BaseException:
                keywordurl = "NA"
            linkobj = {"long_url": linkurl, "keyword_link": keywordurl}
            print(i, linkobj)
            try:
                rr = requests.get(linkurl)
                if rr.status_code == 200:
                    validlist.append(linkobj)
                else:
                    errorlist.append(linkobj)
            except BaseException:
                print("Error in requests:", linkurl)
        i += 1

print("********** RESULTS {0} + {1} / {2} ***********".format(
    len(validlist), len(errorlist), links_to_visit)
)

print(
    "Found",
    len(validlist),
    "valid long_urls with {0}".format(token_to_find))
printlist(validlist)
print(
    "Found",
    len(errorlist),
    "error long_urls with {0}".format(token_to_find))
printlist(errorlist)


'''

rawgits = [
    'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgisl/cs8251/554ffb6d/workshop/june30.html', 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/e7d4c152918d544ccd12ae317a33163a/raw/847c895e8bb2f1960456e99925b05898200653c8/keywordComparison.md#comparing-python-and-c-through-keywords', 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/e90ec33f0c335aecbdcd01abf07eccc0a4429d4e/kishorePan.md.html#refactor-9', 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/310070689603bdd392bc9b566fe0ba233e1068ea/kishorePan.md.html#refactor-9', 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/2aab52c6940c05da1c42021c22edea485da06798/kishorePan.md.html#refactor-8', 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/2aab52c6940c05da1c42021c22edea485da06798/kishorePan.md.html', 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/adfb6d27ec068708bfbef7eb5c61bbfaa7cb7225/kishorePan.md.html#the-partial-pangram-check', 'https://cdn.rawgit.com/kgisl/cs8251/396da5e8/notes/understanding-the-concept-of-recursion1.pdf', 'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/076fa3f382fa039d6bd4eb3c7290008cab4a8fef/replace.html#refactor-2', 'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/ea924bfcf7ec2487f2ae845ccbc601909bed91f3/replace.html#refactor-2', 'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/ea924bfcf7ec2487f2ae845ccbc601909bed91f3/replace.html#refactor-3', 'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/ea924bfcf7ec2487f2ae845ccbc601909bed91f3/replace.html', 'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/7dff9f67ea1fae8ce9d642f2dd86e7a9767543b1/replace.html', 'https://cdn.rawgit.com/kgashok/44e023fc8319f095e4149b208e0dee72/raw/3cba90c7c2110bc5bd0275441fbb9c04ce6cfd0c/importantTopics.html#types-and-their-attributes-aka-methods-unit-3', 'https://cdn.rawgit.com/kgashok/project-ideas/master/elm/curiosityGenius.png', 'https://rawgit.com/kgashok/d18feb3d92e37a128ab8de77597634b2/raw/4e9b1e1a705e6cfc84bcc348dc4d3cab509f98e1/reflectionsGeniusPPT.html', 'https://rawgit.com/kgashok/d18feb3d92e37a128ab8de77597634b2/raw/1740192da0a69604d25a1ad432eecc682e631870/reflectionsGeniusPPT.html', 'https://cdn.rawgit.com/kgashok/7cc416be04fd59c01a2f44f4448c4ebe/raw/30d598747189aca3509d4ba9647e592cdba9dc45/recursiveDirect.html', 'https://rawgit.com/kgashok/7cc416be04fd59c01a2f44f4448c4ebe/raw/e82a86f7df0fc86e1de5020db2ac170f8cffa758/recursiveDirect.html', 'https://rawgit.com/kgashok/7cc416be04fd59c01a2f44f4448c4ebe/raw/f65116557a5adedc6e4232221edab1dd90ccea98/recursiveDirect.html', 'https://rawgit.com/kgashok/66056350fed26bc1708f5a7b11b0e046/raw/f25cf8256dded0b1e7636774ecfa1f341cb56905/recursive.html', 'https://rawgit.com/kgashok/b7ce940e098fb3a6e69b9dc9dbb8dc13/raw/d360bdc343919bf235fdaf18a4c7908bb8899e30/sizeof3.html#pointer-snippet', 'https://rawgit.com/kgashok/7c6b5a51b6c41635f229f0d273ddc8fd/raw/ead6e5e8ae27a5f532f09ead84a74a603c2f8ece/sizeof2.html#check-odd-or-even']

for link in rawgits:
    print ("'"+link+"'", end=",\n")


rlinks = [
    'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgisl/cs8251/554ffb6d/workshop/june30.html',
    'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/e7d4c152918d544ccd12ae317a33163a/raw/847c895e8bb2f1960456e99925b05898200653c8/keywordComparison.md#comparing-python-and-c-through-keywords',
    'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/e90ec33f0c335aecbdcd01abf07eccc0a4429d4e/kishorePan.md.html#refactor-9',
    'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/310070689603bdd392bc9b566fe0ba233e1068ea/kishorePan.md.html#refactor-9',
    'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/2aab52c6940c05da1c42021c22edea485da06798/kishorePan.md.html#refactor-8',
    'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/2aab52c6940c05da1c42021c22edea485da06798/kishorePan.md.html',
    'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/adfb6d27ec068708bfbef7eb5c61bbfaa7cb7225/kishorePan.md.html#the-partial-pangram-check',
    'https://cdn.rawgit.com/kgisl/cs8251/396da5e8/notes/understanding-the-concept-of-recursion1.pdf',
    'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/076fa3f382fa039d6bd4eb3c7290008cab4a8fef/replace.html#refactor-2',
    'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/ea924bfcf7ec2487f2ae845ccbc601909bed91f3/replace.html#refactor-2',
    'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/ea924bfcf7ec2487f2ae845ccbc601909bed91f3/replace.html#refactor-3',
    'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/ea924bfcf7ec2487f2ae845ccbc601909bed91f3/replace.html',
    'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/7dff9f67ea1fae8ce9d642f2dd86e7a9767543b1/replace.html',
    'https://cdn.rawgit.com/kgashok/44e023fc8319f095e4149b208e0dee72/raw/3cba90c7c2110bc5bd0275441fbb9c04ce6cfd0c/importantTopics.html#types-and-their-attributes-aka-methods-unit-3',
    'https://cdn.rawgit.com/kgashok/project-ideas/master/elm/curiosityGenius.png',
    'https://rawgit.com/kgashok/d18feb3d92e37a128ab8de77597634b2/raw/4e9b1e1a705e6cfc84bcc348dc4d3cab509f98e1/reflectionsGeniusPPT.html',
    'https://rawgit.com/kgashok/d18feb3d92e37a128ab8de77597634b2/raw/1740192da0a69604d25a1ad432eecc682e631870/reflectionsGeniusPPT.html',
    'https://cdn.rawgit.com/kgashok/7cc416be04fd59c01a2f44f4448c4ebe/raw/30d598747189aca3509d4ba9647e592cdba9dc45/recursiveDirect.html',
    'https://rawgit.com/kgashok/7cc416be04fd59c01a2f44f4448c4ebe/raw/e82a86f7df0fc86e1de5020db2ac170f8cffa758/recursiveDirect.html',
    'https://rawgit.com/kgashok/7cc416be04fd59c01a2f44f4448c4ebe/raw/f65116557a5adedc6e4232221edab1dd90ccea98/recursiveDirect.html',
    'https://rawgit.com/kgashok/66056350fed26bc1708f5a7b11b0e046/raw/f25cf8256dded0b1e7636774ecfa1f341cb56905/recursive.html',
    'https://rawgit.com/kgashok/b7ce940e098fb3a6e69b9dc9dbb8dc13/raw/d360bdc343919bf235fdaf18a4c7908bb8899e30/sizeof3.html#pointer-snippet',
    'https://rawgit.com/kgashok/7c6b5a51b6c41635f229f0d273ddc8fd/raw/ead6e5e8ae27a5f532f09ead84a74a603c2f8ece/sizeof2.html#check-odd-or-even'
]

bitlyapi = "https://api-ssl.bitly.com"
lookup =  "/v3/user/link_lookup?access_token={0}&url={1}"
lURL = bitlyapi + lookup
errorlist = []
validlist = []
for link in rlinks:
    r = requests.get(link)
    if r.status_code == 403:
        print ("error reading", link)
        errorlist.append(link)
    else:
        print("valid:", link)

        validlist.append(link)

print(len(rlinks))
'''

validl = [
    {'keyword_link': 'http://j.mp/agendaJune30', 'long_url': 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgisl/cs8251/554ffb6d/workshop/june30.html'},
    {'keyword_link': 'http://j.mp/pythonToC', 'long_url': 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/e7d4c152918d544ccd12ae317a33163a/raw/847c895e8bb2f1960456e99925b05898200653c8/keywordComparison.md#comparing-python-and-c-through-keywords'},
    {'keyword_link': 'http://bit.ly/finalCompare', 'long_url': 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/e90ec33f0c335aecbdcd01abf07eccc0a4429d4e/kishorePan.md.html#refactor-9'},
    {'keyword_link': 'http://j.mp/panCompare', 'long_url': 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/310070689603bdd392bc9b566fe0ba233e1068ea/kishorePan.md.html#refactor-9'},
    {'keyword_link': 'http://j.mp/kishoreRefactor8', 'long_url': 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/2aab52c6940c05da1c42021c22edea485da06798/kishorePan.md.html#refactor-8'},
    {'keyword_link': 'http://j.mp/kishoreFinal', 'long_url': 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/2aab52c6940c05da1c42021c22edea485da06798/kishorePan.md.html'},
    {'keyword_link': 'http://j.mp/kishorePartial', 'long_url': 'https://htmlpreview.github.io/?https://cdn.rawgit.com/kgashok/8842262e09e89a849ca628f4692a5d9d/raw/adfb6d27ec068708bfbef7eb5c61bbfaa7cb7225/kishorePan.md.html#the-partial-pangram-check'},
    {'keyword_link': 'http://j.mp/recursionGrok', 'long_url': 'https://cdn.rawgit.com/kgisl/cs8251/396da5e8/notes/understanding-the-concept-of-recursion1.pdf'},
    {'keyword_link': 'http://bit.ly/curiousGenius', 'long_url': 'https://cdn.rawgit.com/kgashok/project-ideas/master/elm/curiosityGenius.png'},
    {'keyword_link': 'http://j.mp/oddOrEven', 'long_url': 'https://rawgit.com/kgashok/7c6b5a51b6c41635f229f0d273ddc8fd/raw/ead6e5e8ae27a5f532f09ead84a74a603c2f8ece/sizeof2.html#check-odd-or-even'}
]

# ******* ERROR *******
errorl = [
    {'keyword_link': 'http://bit.ly/refactorReplace2', 'long_url': 'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/076fa3f382fa039d6bd4eb3c7290008cab4a8fef/replace.html#refactor-2'},
    {'keyword_link': 'http://j.mp/refactorReplace3', 'long_url': 'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/ea924bfcf7ec2487f2ae845ccbc601909bed91f3/replace.html#refactor-2'},
    {'keyword_link': 'http://bit.ly/finalRefactorReplace3', 'long_url': 'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/ea924bfcf7ec2487f2ae845ccbc601909bed91f3/replace.html#refactor-3'},
    {'keyword_link': 'http://bit.ly/replaceRefactor3', 'long_url': 'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/ea924bfcf7ec2487f2ae845ccbc601909bed91f3/replace.html'},
    {'keyword_link': 'http://bit.ly/refactorReplace', 'long_url': 'https://cdn.rawgit.com/kgashok/6a9beb95e0c97d6eb0ea46ecb6ba4295/raw/7dff9f67ea1fae8ce9d642f2dd86e7a9767543b1/replace.html'},
    {'keyword_link': 'http://j.mp/pythonMethods3003', 'long_url': 'https://cdn.rawgit.com/kgashok/44e023fc8319f095e4149b208e0dee72/raw/3cba90c7c2110bc5bd0275441fbb9c04ce6cfd0c/importantTopics.html#types-and-their-attributes-aka-methods-unit-3'},
    {'keyword_link': 'http://j.mp/reflectPPT', 'long_url': 'https://rawgit.com/kgashok/d18feb3d92e37a128ab8de77597634b2/raw/4e9b1e1a705e6cfc84bcc348dc4d3cab509f98e1/reflectionsGeniusPPT.html'},
    {'keyword_link': 'http://j.mp/reflectionsPPT', 'long_url': 'https://rawgit.com/kgashok/d18feb3d92e37a128ab8de77597634b2/raw/1740192da0a69604d25a1ad432eecc682e631870/reflectionsGeniusPPT.html'},
    {'keyword_link': 'http://j.mp/rHTML', 'long_url': 'https://cdn.rawgit.com/kgashok/7cc416be04fd59c01a2f44f4448c4ebe/raw/30d598747189aca3509d4ba9647e592cdba9dc45/recursiveDirect.html'},
    {'keyword_link': 'http://j.mp/recursiveKeys3', 'long_url': 'https://rawgit.com/kgashok/7cc416be04fd59c01a2f44f4448c4ebe/raw/e82a86f7df0fc86e1de5020db2ac170f8cffa758/recursiveDirect.html'},
    {'keyword_link': 'http://j.mp/recursiveKeys2', 'long_url': 'https://rawgit.com/kgashok/7cc416be04fd59c01a2f44f4448c4ebe/raw/f65116557a5adedc6e4232221edab1dd90ccea98/recursiveDirect.html'},
    {'keyword_link': 'http://j.mp/recursiveKeys', 'long_url': 'https://rawgit.com/kgashok/66056350fed26bc1708f5a7b11b0e046/raw/f25cf8256dded0b1e7636774ecfa1f341cb56905/recursive.html'},
    {'keyword_link': 'http://j.mp/pointerS', 'long_url': 'https://rawgit.com/kgashok/b7ce940e098fb3a6e69b9dc9dbb8dc13/raw/d360bdc343919bf235fdaf18a4c7908bb8899e30/sizeof3.html#pointer-snippet'}
]
