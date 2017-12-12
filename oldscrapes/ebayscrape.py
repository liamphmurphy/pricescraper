from lxml import html
import requests

#Grab the default template search URL from amazon than append userquery for the keyword.
userquery = input("What would you like to search for?: ")

page = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR11.TRC1.A0.H0.Xr7+170.TRS0&_nkw="+userquery+"&_sacat=0")
tree = html.fromstring(page.content)

# Currently, the program only searches Amazon. More sites to come later!
productname = tree.xpath('//a[@class="vip"]/text()')
price = tree.xpath('//span[@class="bold"]/text()')

# Cut down the list gathered by the scrape to just 5 results, mainly for testing and reducing load times.
productname = productname[:5]
price = price[:5]

print(productname)
print(price)

print(page)
