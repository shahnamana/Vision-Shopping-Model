from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url="https://www.amazon.in/s?k=blue+shirt"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

print(page_soup)

with open('sc2.html','w') as f:
    f.write(page_soup)

#
# containers = page_soup.findAll("div", { "class": "IIdQZO"})
# #print(len(containers))
#
# #print(soup.prettify(containers[0]))
#
# container = containers[0]
# #print(container.div.img["alt"])
#
# price = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
# #print(price[0].text)
#
#
# ratings = container.findAll("div", {"class": "_1vC4OE"})
# #rint(ratings[0].text)
#
# filename = "products.csv"
# f = open(filename, "w")
#
# headers = "Product_Name, Pricing, Ratings \n"
# f.write(headers)
# product_price = []
# product_name = []
# img_url = []
#
for container in containers:
    for i in container.findAll('div',{'class':'_1vC4OE'}):
        product_price.append(i.text)

    for j in container.findAll('a', {'class':'_2mylT6'}):
        product_name.append(j.text)

    # img_url.append(container.find('div',{'class':'_3ZJShS _31bMyl'}))
    #
    #
    #     # for jj in k.find_all('img'):


#     # for j in container.findAll('div')
# #
# #     product_name = container.div.img["alt"]
# #     price_container = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
# #     price = price_container[0].text.strip()
# #
# #     rating_container = container.findAll("div", {"class": "niH0FQ"})
# #     rating = rating_container[0].text
# #
# #    #rint("Product_Name:"+ product_name)
# #    #print("Price: " + price)
# #    #print("Ratings:" + rating)
# #
# #     #String parsing
# #     trim_price=''.join(price.split(','))
# #     rm_rupee = trim_price.split('₹')
# #     add_rs_price = "Rs."+rm_rupee[1]
# #     split_price = add_rs_price.split('E')
# #     final_price = split_price[0]
# #
# #     split_rating = rating.split(" ")
# #     final_rating = split_rating[0]
# #
# #     print(product_name.replace("," ,"|") +"," + final_price +"," + final_rating + "\n")
# #     f.write(product_name.replace("," ,"|") +"," + final_price +"," + final_rating + "\n")
# # f.close()
#
#
print(product_price)

print()
print()
print(product_name)

#
# for i in range(len(img_url)):
#     print(img_url[i])
#     print()
