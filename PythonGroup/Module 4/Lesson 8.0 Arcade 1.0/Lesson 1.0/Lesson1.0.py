# Подключить нужные модули
from random import randint 
import pygame 
from os import path
pygame.init() 
# во время игры пишем надписи размера 72
 

# Глобальные переменные (настройки)


# цвета: 


# Классы
# класс для цели (стоит и ничего не делает)

  # конструктор класса
   
      # Вызываем конструктор класса (Sprite):
       

      # каждый спрайт должен хранить свойство image - изображение 

      # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан 

#класс для главного героя     
 
        # картинка загружается из файла и умещается в прямоугольник нужных размеров:
         
                    # используем convert_alpha, нам надо сохранять прозрачность

        # каждый спрайт должен хранить свойство rect - прямоугольник. Это свойство нужно для определения касаний спрайтов. 
        
        # ставим персонажа в переданную точку (x, y):
         
        # создаем свойства, запоминаем переданные значения:
         
        # добавим свойство stands_on - это та платформа, на которой стоит персонаж
        
        # если ни на какой не стоит, то значение - False
    #функция для падения (гравитация)  


    #функция для прыжка

    #функция апдейт для данного спрайта. так как спрайт будет премещаться. Самая веселая часть ) 
     

#класс для стены. Делали точно такой же в проекте Лабиринт :))) 
    #конструктор

#класс врага 
    #конструктор 

    # функция апдейт с рандомным перемещением 


# Запуск игры 


# список всех персонажей игры:


# список препятствий:

# список врагов:

# список мин:


# создаем персонажа, добавляем его в список всех спрайтов:

# создаем стены, добавляем их:




# создаем врагов, добавляем их:


# создаем мины, добавляем их:
            
            # в список всех спрайтов бомбы не добавляем, будем рисовать их отдельной командой
            # так легко сможем подрывать бомбы, а также делаем их неподвижными, update() не вызывается

# создаем финальный спрайт, добавляем его: 

# Основной цикл игры: 
 
    # Обработка событий
      
        # Перемещение игровых объектов  

        # дальше проверки правил игры
        # проверяем касание с бомбами: 
                # если бомба коснулась спрайта, то она убирается из списка бомб, а спрайт - из all_sprites!

        # проверяем касание героя с врагами: 
           # robin.kill() # метод kill убирает спрайт из всех групп, в которых он числится

        # проверяем границы экрана: 
             # при выходе влево или вправо переносим изменение в сдвиг экрана 
            # перемещаем на общий сдвиг все спрайты (и отдельно бомбы, они ж в другом списке): 
                        # сам robin тоже в этом списке, поэтому его перемещение визуально отменится
            

        # Отрисовка
        # рисуем фон со сдвигом
        

        # нарисуем все спрайты на экранной поверхности до проверки на выигрыш/проигрыш
        # если в этой итерации цикла игра закончилась, то новый фон отрисуется поверх персонажей
         
        # группу бомб рисуем отдельно - так бомба, которая ушла из своей группы, автоматически перестанет быть видимой
       

        # проверка на выигрыш и на проигрыш:
        

        # проверка на проигрыш:
         
            # пишем текст на экране
             

     

    # Пауза 