from lxml import html
import requests
import time

class Scrape:

    def amazon_scrape(userquery):

        # Grab the default template search URL from amazon than append userquery for the keyword.
        page = requests.get("https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="+userquery)
        tree = html.fromstring(page.content)

        # Currently, the program only searches Amazon. More sites to come later!
        productname = tree.xpath('//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]/text()')
        price = tree.xpath('//span[@class="a-offscreen"]/text()')

        # Cut down the list gathered by the scrape to just 5 results, mainly for testing and red$
        productname = productname[:5]
        price = price[:5]


        print(productname)
        print(price)

        print(page)

        if len(productname) == 0:
            print("If you see this message, Amazon is not playing nicely. Attempting to run again.")
            time.sleep(1)
            Scrape.amazon_scrape(userquery)

    def newegg_scrape(userquery):
        #Grab the default template search URL from newegg than append userquery for the keyword.
        #userquery = input("What would you like to search for?: ")

        page = requests.get("https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description="+userquery+"&N=-1&isNodeId=1")
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

    def ebay_scrape(userquery):
        #Grab the default template search URL from amazon than append userquery for the keyword.
        #userquery = input("What would you like to search for?: ")

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
