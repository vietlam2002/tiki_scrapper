from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib
import logging

class product_info:
    def __int__(self, category, price, title, discount,rating, total_sales, prod_id):
        self.category = category
        self.price = price
        self.title = title
        self.discount = discount
        self.rating = rating
        self.total_sales = total_sales
        self.prod_id = prod_id

class product_link:
    def __int__(self, image, product):
        self.image = image
        self.product = product

def process_page(website_path, link, i):
    tuple_data = []
    tuple_data_page = []
    request_url = website_path + link + "?page=" + i
    html = urlopen(request_url)

    bs = BeautifulSoup(html, 'html.parser')
    list_product_id = bs.find_all("div", attrs={"class":re.compile('CatalogProducts')})
    return list_product_id