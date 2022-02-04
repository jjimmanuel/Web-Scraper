from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312&_nkw=thinkpad&_sacat=175672"


page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

item_title = soup.find_all("div", {"class":"s-item__info clearfix"})
title = item_title[0]
#print(title.a.h3)

item_price = soup.find_all("div", {"class":"s-item__details clearfix"})
price = item_price[0]
#print(price.span)

item_shipping = soup.find_all("span", {"class":"s-item__shipping s-item__logisticsCost"})
shipping = item_shipping[0]
#print(shipping)

title_list = []
for title in item_title:
    print(title.a.h3)


price_list = []
for price in item_price:
    print(price.span)

shipping_list = []
for shipping in item_shipping:
    print(shipping)


    




