from page_parsing import process_page
from menu_parsing import menu_extract
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import re


request_url = "https://tiki.vn/dien-thoai-may-tinh-bang/c1789?page=2"
html = urlopen(request_url)

bs = BeautifulSoup(html, 'html.parser')
list_product_id = bs.find_all("div", attrs={"class": re.compile('ProductItemContainer')})
print(list_product_id)
# menu_list = bs.find_all("div", attrs={"class": re.compile('StyledItemV2')})
# print(menu_list)