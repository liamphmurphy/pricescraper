from lxml import html
import requests

userquery = input("Enter the URL: ")

page = requests.get(userquery)
tree = html.fromstring(page.content)

productname = tree.xpath('//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]/text()')
price = tree.xpath('//span[@class="a-offscreen"]/text()')

productname = productname[:5]
price = price[:5]


print(productname)
print(price)

print(page)
