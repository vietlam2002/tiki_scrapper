from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import logging

logger = logging.getLogger()

all_list = []

def menu_extract(link):

    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')
