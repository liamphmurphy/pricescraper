from lxml import html
import requests

#userquery has to be in the form of an Amazon URL (with the keyword), to be worked on in the future.
userquery = input("Enter the URL: ")

page = requests.get(userquery)
tree = html.fromstring(page.content)

# Search the resulting Newegg page. Gonna add these all into one program later.
productName = tree.xpath('//a[@title="View Details"]/text()')
price = tree.xpath('//span[@style="display: none"]/text()')

# Cut down the list gathered by the scrape to just 5 results, mainly for testing and reducing load times.
productName = productName[:5]
price = price[:5]


print(productName)
#print(price)

print(page)
