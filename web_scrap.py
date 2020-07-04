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
'''
div with class "MUQY0" is imp it has the img tag

div with class "sh-dgr__thumbnail" is for getting the source link of the seller

span with class "Nr22bf" has the price info




'''


r = requests.get("https://www.google.com/search?tbm=shop&q=blue+t+shirt")
soup = BeautifulSoup(r.content)
soup.find("div", {"class": "sh-dgr__thumbnail"})
soup.find("div", {"class": "sh-dgr__content"})
    print(a[i])
