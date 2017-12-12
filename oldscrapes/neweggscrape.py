from lxml import html
import requests

#Grab the default template search URL from newegg than append userquery for the keyword.
userquery = input("What would you like to search for?: ")

page = requests.get("https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=r7+1700"+userquery+"&N=-1&isNodeId=1")
#page = requests.get(userquery)
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
