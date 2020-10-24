#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Gabriel Santos IS-211 10/24/2020
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as souP


def open_url(url):
    with uReq(url) as response:
        html = response.read()
    return html


def make_soup(response):
    soup = souP(response, features='lxml')
    soup_table = soup.find('table', {'cols': '4'})
    soup_rows = soup_table.find_all('tr')[1:]
    return soup_rows


def displaydata(scrapped_data):
    display = '{:^20} | {:^20} | {:^10}'
    row_list = []
    for game in scrapped_data:
        row_list.append(game.text.splitlines())
    for row in row_list:
        print(row[2], row[4], row[3])
    print('\n')

def main():
    url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'
    url_response = open_url(url)
    stats = make_soup(url_response)
    displaydata(stats)

if __name__ == '__main__':
    main()


# In[ ]:




