''' import Requests and BeautifulSoup from python library '''
import requests
import bs4
BASE_URL = 'http://quotes.toscrape.com/page/{}'
lst = []
i = 1
while i > 0:
    res =  requests.get(BASE_URL.format(i))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    results = soup.select(".author")
    if not results:
        break
    for result in results:
        author = result.text
        if author in lst:
            continue
        lst.append(author)
    i=i+1
print(lst)