from lxml import html
import requests

#userquery has to be in the form of an Amazon URL (with the keyword), to be worked on in the future.
userquery = input("Enter the URL: ")

page = requests.get(userquery)
tree = html.fromstring(page.content)

# Currently, the program only searches Amazon. More sites to come later!
productname = tree.xpath('//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]/text()')
price = tree.xpath('//span[@class="a-offscreen"]/text()')

# Cut down the list gathered by the scrape to just 5 results, mainly for testing and reducing load times.
productname = productname[:5]
price = price[:5]

if (5 > 4):
    print("Hi!")

print(productname)
print(price)

print(page)
