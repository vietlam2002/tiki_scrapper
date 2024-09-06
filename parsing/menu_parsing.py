from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import logging

logger = logging.getLogger()

all_list = []

def menu_extract(link):

    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')
    menu_list = bs.find_all("div", attrs={"class": re.compile('StyledItemV2')})

    for menu in menu_list:
        menu_item = menu.find_all('a', href=True)
        all_list.append(menu_item[0]['href'])

    return all_list

logger.info("Starting to crawl...")