#web scraping code
import requests
from bs4 import BeautifulSoup
'''
it is not taking 'tshirt' as the query to show the porper result
Thus have to use 't shirt' as the query for the url

We are using Google Shopping tab to search the product from sellers all across the web

'''




'''
OG url:
https://www.google.com/search?nord=1&output=search&tbm=shop&psb=1&q=blue+shirt
&ved=0ahUKEwjotoKnwLHqAhVQbysKHbNQDbgQ-LwECB8&oq=&gs_lcp=Cg5tb2JpbGUtc2gtc2VycB
ABGAAyBwgjEOoCECcyBwgjEOoCECcyBwgjEOoCECcyBwgjEOoCECcyBwgjEOoCECcyBwgjEOoCECdQA
FgAYKO6AWgAcAB4AIAB0AGIAdABkgEDMi0xmAEAqgESbW9iaWxlLXNoLXdpei1zZXJwsAEG&sclient=
mobile-sh-serp



short url:

https://www.google.com/search?tbm=shop&q=blue+t+shirt

'''



r = requests.get("https://www.google.com/search?tbm=shop&q=blue+t+shirt")
soup = BeautifulSoup(r.content)
soup.find("div", {"class": "sh-dgr__thumbnail"})
for i in soup.find("div", {"class": "sh-dgr__thumbnail"})[:16]):
    print(a[i])
