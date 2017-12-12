from lxml import html
import requests
from scrape import Scrape

#service_name = ""
userquery = input("Enter the name of the product: ")

print("---------------AMAZON---------------\n")
Scrape.amazon_scrape(userquery)
print("\n")
print("---------------NEWGG---------------\n")
Scrape.newegg_scrape(userquery)
print("\n")
print("---------------EBAY---------------\n")
Scrape.ebay_scrape(userquery)
