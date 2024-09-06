from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import logging



#========= list items in menu ==========#
logger = logging.getLogger()
link = 'https://tiki.vn/'
html = urlopen(link)
all_list = []

bs = BeautifulSoup(html, 'html.parser')
menu_list = bs.find_all("div", attrs={"class":re.compile('StyledItemV2')})

for menu in menu_list:

    menu_item = menu.find_all('a', href = True)
    all_list.append(menu_item[0]['href'])

# print(all_list)
print(bs)

#========== list product id ==============
