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


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request


my_url = 'https://www.google.com/search?tbm=shop&q=blue+shirt'
hdr = {'User-Agent': 'Mozilla/5.0'}
request = Request(my_url, headers=hdr)
uClient = uReq(request)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,'html.parser')
# print(page_soup)


'''
the following line provides proper output for img, pricelist, name_prod

'''
containers = page_soup.findAll('div' , {'class' :'u30d4'})

price_lst = []

img_url = []

name_prod = []

initial_url = 'https://www.flipkart.com/'
for container in containers[:10]:

    for j in container.findAll('span', {'class':"HRLxBb"}):
        price_lst.append(j.text)
    for a in container.find_all('a'):
        name_prod.append(a.text)

'''
The next line removes the blank entries got from a tag of images as they don't have any text
'''

import re

if my_url.find('Shoes'):
    name_prod = name_prod[1::2]
else:
    name_prod = name_prod[0::2]
print(price_lst)

print()
print(name_prod)
