'''
экран ноута должен быть включенным постаянно


'''
import time
import datetime
import requests
from bs4 import BeautifulSoup
import pyautogui
#import pygame

pyautogui.PAUSE = 2
ut_mob = ['']
ut_foto =['']

url = 'https://www.kufar.by/listings?size=42&sort=lst.d&cur=BYR&cat=17010&rgn=7&pb=5&phm=v.or%3A270%2C265%2C260%2C245%2C250%2C3745%2C3750%2C3740'
url2 ='https://www.kufar.by/l/r~minsk/fotoapparaty?size=42&sort=lst.d&cur=BYR&pcb=v.or:1,11'
link_baner ='kf-ZHei-5e965'

link = 'kf-aGMh-4f4e3,lazyloaded' #

link_price = 1
link_product_name = 1

l= ['']
print('Начало запроса')
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')
ads = soup.find("a", class_= link_baner)
#print(ads.text)


product_name1 = ads.find('h3',class_='kf-ZHpr-420a5')#название
print(product_name1.text)

price1 = ads.find('span',class_='kf-Txnh-e313a')
print(price1.text)

link_ads = ads['href']


print('СВЕЖЕЕ ОБЪЯВЛЕНИЕ')
print(link_ads)
x = datetime.datetime.now()
print(x.strftime('%X'))


ut_mob = link_ads

pyautogui.hotkey('win', '3')
time.sleep(5)
pyautogui.typewrite('ol', interval=0.25)

pyautogui.press('down')
pyautogui.press('enter')

pyautogui.typewrite(ut_mob , interval=0.05)

pyautogui.press('enter')

pyautogui.hotkey('alt', 'F4')


#pygame.mixer.init()
#pygame.mixer.music.load('iphone.mp3')
#pygame.mixer.music.play()

print('-------------------------')
l=link_ads
'''
вторая часть 

'''

l2= ['']
#print('Начало запроса часть вторая ')
request2 = requests.get(url2)
soup2 = BeautifulSoup(request2.text, 'html.parser')
ads2 = soup2.find("a", class_= link_baner)


product_name2 = ads2.find('h3',class_='kf-ZHpr-420a5')#название
print(product_name2.text)

price2 = ads2.find('span',class_='kf-Txnh-e313a')
print(price2.text)

link_ads2 = ads2['href']

print('СВЕЖЕЕ ОБЪЯВЛЕНИЕ В РУБРИКЕ ФОТО')
print(link_ads2)
x = datetime.datetime.now()
print(x.strftime('%X'))


ut_foto = link_ads2

pyautogui.hotkey('win', '3')
time.sleep(5)
pyautogui.typewrite('ol', interval=0.25)

pyautogui.press('down')
pyautogui.press('enter')

pyautogui.typewrite(ut_foto , interval=0.05)

pyautogui.press('enter')

pyautogui.hotkey('alt', 'F4')

#pygame.mixer.init()
#pygame.mixer.music.load('iphone.mp3')
#pygame.mixer.music.play()


print('-------------------------')
l2=link_ads2

while 1>0 :
    time.sleep(20)
    #print('Начало запроса')
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    ads = soup.find("a", class_= link_baner)

    
    

    #print(ads.text)
    link_ads = ads['href']
    #print(link_ads)
    

    fd = ads.find("a", class_= link)
    #print(fd.text)

    
    bb = str(l)
    #print('ссылка сохранилась ' + bb)
    
    #print('Конец запроса')


    

    #print('Начало запроса темы ФОТО ')
    request2 = requests.get(url2)
    soup2 = BeautifulSoup(request2.text, 'html.parser')
    ads2 = soup2.find("a", class_= link_baner)

    #print(ads.text)
    link_ads2 = ads2['href']
    #print(link_ads)
    #print('dffsfvfdvsvdfvs' + str(l[0]))

    fd = ads2.find("a", class_= link)
    #print(fd.text)

    
    bb = str(l)
    #print('ссылка сохранилась ' + bb)
    
    #print('Конец запроса')


    
    if l!=link_ads:
        print('НОВОЕ ОБЪЯВЛЕНИЕ В РУБРИКЕ IPHONE УРРААА')

        product_name1 = ads.find('h3',class_='kf-ZHpr-420a5')#название
        print(product_name1.text)

        price1 = ads.find('span',class_='kf-Txnh-e313a')
        print(price1.text)
        
        print(link_ads)
        
        x = datetime.datetime.now()
        print(x.strftime('%X'))

        ut_mob = link_ads

        pyautogui.hotkey('win', '3')
        time.sleep(5)
        pyautogui.typewrite('ol', interval=0.25)

        pyautogui.press('down')
        pyautogui.press('enter')

        pyautogui.typewrite(ut_mob , interval=0.05)

        pyautogui.press('enter')

        pyautogui.hotkey('alt', 'F4')

        #pygame.mixer.init()
        #pygame.mixer.music.load('iphone.mp3')
        #pygame.mixer.music.play()        
       
        
        print('-------------------------')
        l=link_ads

    if l2!=link_ads2:
        print('НОВОЕ ОБЪЯВЛЕНИЕ В РУБРИКЕ ФОТО УРРААА')


        product_name2 = ads2.find('h3',class_='kf-ZHpr-420a5')#название
        print(product_name2.text)

        price2 = ads2.find('span',class_='kf-Txnh-e313a')
        print(price2.text)
        
        print(link_ads2)

        
        x = datetime.datetime.now()
        print(x.strftime('%X'))


        ut_foto = link_ads2

        pyautogui.hotkey('win', '3')
        time.sleep(5)
        pyautogui.typewrite('ol', interval=0.25)

        pyautogui.press('down')
        pyautogui.press('enter')

        pyautogui.typewrite(ut_foto , interval=0.05)

        pyautogui.press('enter')

        pyautogui.hotkey('alt', 'F4')

        #pygame.mixer.init()
        #pygame.mixer.music.load('iphone.mp3')
        #pygame.mixer.music.play()
        
        print('-------------------------')
        l2=link_ads2
    
