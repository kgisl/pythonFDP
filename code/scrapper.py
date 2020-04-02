

from bs4 import BeautifulSoup
import requests
url = "https://www.python.org/about/success/#engineering"
url = "https://simpleprogrammer.com/products/careerguide/links/?utm_source=careerguide&utm_medium=book&utm_campaign=chapter-59&utm_content=refactor#chapter-59"
url = "https://hackernoon.com/i-built-a-chatbot-in-2-hours-and-this-is-what-i-learned-f5dbb4ba5fcc"
url = "https://medium.com/personal-growth/how-to-be-yourself-2221085391a3"
url = "https://www.reddit.com/r/Python/comments/29qd6x/ask_recommended_python_books_for_experienced/"
#url = "https://www.programiz.com/c-programming/list-all-keywords-c-language"


html = requests.get(url)
soup = BeautifulSoup(html.text)
anchors = soup.find_all('a')

outbound = []

for anchor in anchors:
    if anchor.has_attr("href"):
        # print(anchor)
        href = anchor.get("href")
        # if href.find("hackernoon") == -1 and href.find("twitter") == -1:
        # print(href)
        if href.startswith("http:") or href.startswith("https:"):
            if href.strip() not in outbound:
                outbound.append(href.strip())

print(url)
for i, link in enumerate(outbound):
    print(str(i) + ".", link, end="\n")
