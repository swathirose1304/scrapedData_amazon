from bs4 import BeautifulSoup
import requests
import pandas
import numpy

URL = 'https://www.amazon.com/s?k=shoes&crid=2MOBZKDE81CMR&sprefix=shoes%2Caps%2C2161&ref=nb_sb_ss_ts-doa-p_2_5'

# HEADERS FOR REQUEST
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5' })

#HTTP request
webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, 'html.parser')

# Fetch links as List of Tag Objects

links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
link = links[0].get('href')
product_list = "https://amazon.com" + link
# print(product_list)   #produce link for particular product

# ####First scrap data for single product & loop
new_webpage = requests.get(product_list, headers=HEADERS)
# print(new_webpage)

new_soup = BeautifulSoup(new_webpage.content, 'html.parser')
title = new_soup.find('span', attrs={'id':'productTitle'}).text.strip()
# print(title)
rate = new_soup.find('span', attrs={'class':'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'}).find('span', attrs={'class':'a-offscreen'}).text
# print(rate)
# price = new_soup.find('span', attrs={'class':'a-price-whole'}).text
# print(price)
stars = new_soup.find('span', attrs={'class':'a-icon-alt'}).text
# print(stars)
desc = new_soup.find('div', attrs={'class':'a-section a-spacing-medium a-spacing-top-small'}).text
print(desc)