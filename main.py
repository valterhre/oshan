from bs4 import BeautifulSoup
import requests

url = 'https://auchan.zakaz.ua/ru/categories/frozen-for-gourmet-auchan/'

def find_(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pd=soup.find_all('div', 'ProductsBox__listItem')
    p=0
    bs=soup.find('span', 'Price__value_caption')
    bs1 = soup.find('span', 'ProductTile__title')
    while p<(len(pd)-1):
        ps=''
        bs=bs.find_next('span', 'Price__value_caption')
        bs1=bs1.find_next('span', 'ProductTile__title')
        k = pd[p].find('div', 'ProductTile__unavailable')
        p = p + 1
        if k != None:
            ps='not avaliable'
        print(bs1.string,bs.string, ps)
find_(url)
