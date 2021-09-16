'''
генератор рандомных поролей


https://www.youtube.com/watch?v=7bHYCesBgXo&t=145s

программа создает тхт файл в папке с кодом 
'''
import random

chars = '+-/*!&$#?=@<>abcdefghijk1234567890'

number = int(input('количество поролей '))
lenght = int(input('длинна строки '))

for x in range( number):
    password = ''

    for i in range(lenght):
        password += random.choice( chars )


    print( password )

    file = open('password.txt', 'a') #имя файла 
    file.write( '\n' + password )
    file.close()
