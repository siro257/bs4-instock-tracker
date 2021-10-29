import requests
import re
from bs4 import BeautifulSoup
from mail import send_mail
from time import sleep

URLS = ['https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161',
        'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149',
        'https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324']

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

# URL = 'https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161'

while True:

    for URL in URLS:
        page = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find('div', class_='sku-title').get_text()
        price = soup.find('span', class_=None, text=re.compile(r'^\$')).get_text()

        out_of_stock = soup.find_all('button', {"data-button-state": "SOLD_OUT"})
        in_stock = soup.find_all('button', {"data-button-state": "ADD_TO_CART"})

        if(in_stock):
            print('!'*25+f'{title} ::: INSTOCK!'+'!'*25+'\nSending notification email...')
            send_mail(title, price, URL)
        else:
            print(f'{title} ::: OUT OF STOCK')

        print('-'*100)

    sleep(30)
