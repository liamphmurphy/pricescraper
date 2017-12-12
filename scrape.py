from lxml import html
import requests
import time
import gc

class Scrape:

    def run_scrape(service_name,userquery):
        #userquery = input("Enter the name of the product: ")
        if(service_name == "amazon"):
            page = requests.get("https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="+userquery)
            tree = html.fromstring(page.content)

            productname = tree.xpath('//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]/text()')
            price = tree.xpath('//span[@class="a-offscreen"]/text()')

            if len(productname) == 0:
                print("If you see this message, Amazon is not playing nicely. Attempting to run again.")
                Scrape.amazon_scrape(userquery)

        if(service_name == "newegg"):
            page = requests.get("https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description="+userquery+"&N=-1&isNodeId=1")
            tree = html.fromstring(page.content)

            productname = tree.xpath('//a[@title="View Details"]/text()')
            price = tree.xpath('//span[@style="display: none"]/text()')

        if(service_name == "ebay"):
            page = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR11.TRC1.A0.H0.Xr7+170.TRS0&_nkw="+userquery+"&_sacat=0")
            tree = html.fromstring(page.content)

            productname = tree.xpath('//a[@class="vip"]/text()')
            price = tree.xpath('//span[@class="bold"]/text()')

        productname = productname[:5]
        print(productname)
       # print(price)

    def amazon_scrape(userquery):
        service_name = "amazon"
        Scrape.run_scrape(service_name,userquery)

    def newegg_scrape(userquery):
        service_name = "newegg"
        Scrape.run_scrape(service_name,userquery)

    def ebay_scrape(userquery):
        service_name = "ebay"
        Scrape.run_scrape(service_name,userquery)
