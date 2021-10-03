import time
import datetime
import requests
from bs4 import BeautifulSoup

url = 'https://www.kufar.by/l/r~minsk/noutbuki'
       
print('Начало запроса')
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')
so = soup.find('article')
hh = so.a['class']
print(str(hh) + 'класс блока обявления ')

fh = soup.find('article').a #первая ссылка с содержанием
#print(fh)

hk = so.h3['class']
print(str(hk)+ 'класс названия товара')


fh = so.find('div', class_ ='kf-yNuN-4d8cb')# див в котором лежит span цены 
#print(fh)


jj = fh.span['class']
print(str(jj)+ 'класс цены товара')
