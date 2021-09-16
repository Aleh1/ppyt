import time
import datetime
import requests
from bs4 import BeautifulSoup
import pygame
'''
Начало запроса
<div class="kf-QFbE-73322"><a class="kf-Qbtw-92065" href="https://www.kufar.by/item/134563189" target="_blank">
'''
url = 'https://www.kufar.by/listings?size=42&sort=lst.d&cur=BYR&cat=17010&rgn=7&pb=5&phm=v.or%3A270%2C265%2C260%2C245%2C250%2C3745%2C3750%2C3740'
url2 ='https://www.kufar.by/l/r~minsk/fotoapparaty?size=42&sort=lst.d&cur=BYR&pcb=v.or:1,11'
link_baner ='kf-LEuA-880a1'

link = 'kf-Qbtw-92065' # 

l= ['']
#print('Начало запроса')
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')
ads = soup.find("a", class_= link_baner)
#print(ads.text)
link_ads = ads['href']
fd = ads.find("a", class_= link)
bb = str(l)
print('СВЕЖЕЕ ОБЪЯВЛЕНИЕ')
print(link_ads)
x = datetime.datetime.now()
print(x.strftime('%X'))

pygame.mixer.init()
pygame.mixer.music.load('iphone.mp3')
pygame.mixer.music.play()

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
link_ads2 = ads2['href']
fd = ads2.find("a", class_= link)
bb = str(l2)
print('СВЕЖЕЕ ОБЪЯВЛЕНИЕ В РУБРИКЕ ФОТО')
print(link_ads2)
x = datetime.datetime.now()
print(x.strftime('%X'))

pygame.mixer.init()
pygame.mixer.music.load('iphone.mp3')
pygame.mixer.music.play()


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
    #print('dffsfvfdvsvdfvs' + str(l[0]))

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
        print(link_ads)
        x = datetime.datetime.now()
        print(x.strftime('%X'))

        pygame.mixer.init()
        pygame.mixer.music.load('iphone.mp3')
        pygame.mixer.music.play()        
       
        
        print('-------------------------')
        l=link_ads

    if l2!=link_ads2:
        print('НОВОЕ ОБЪЯВЛЕНИЕ В РУБРИКЕ ФОТО УРРААА')
        print(link_ads2)
        x = datetime.datetime.now()
        print(x.strftime('%X'))

        pygame.mixer.init()
        pygame.mixer.music.load('iphone.mp3')
        pygame.mixer.music.play()
        
        print('-------------------------')
        l2=link_ads2
    

