from lxml import html
import requests
import sys

class Scrape:

    def run_scrape(service_name,userquery):
        if(service_name == "amazon"):
            page = requests.get("https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="+userquery)
            tree = html.fromstring(page.content)

            productname = tree.xpath('//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]/text()')
            price = tree.xpath('//span[@class="a-offscreen"]/text()')
            if len(productname) == 0:
                service_name = "amazon"
                Program.amazon_rerun(userquery,service_name)

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
        #print(productname)

        if not productname:
            del productname # If Amazon returns a 503 response in run_scrape, meaning list is empty, delete the list.
        else:
            print(productname) # If list has stuff in it, let it print!

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


class Program:
    def main(userquery):
        print("---------------AMAZON---------------\n")
        Scrape.amazon_scrape(userquery)
        print("\n")
        print("---------------NEWGG---------------\n")
        Scrape.newegg_scrape(userquery)
        print("\n")
        print("---------------EBAY---------------\n")
        Scrape.ebay_scrape(userquery)
        sys.exit()


    def amazon_rerun(userquery,service_name):
        Scrape.amazon_scrape(userquery)
