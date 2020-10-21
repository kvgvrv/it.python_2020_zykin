import pygame
from pygame.draw import *
from random import randint, random


# После импорта библиотеки, необходимо её инициализировать:
pygame.init()

FPS = 60

# И создать окно:

screen = pygame.display.set_mode((600, 800))

# здесь будут рисоваться фигуры
cat_color = (180,82,45)
def room():
    rect(screen, (200, 200, 57), (0, 400, 600, 400))
    rect(screen, (170, 131, 57), (0, 0, 600, 400))
def window():
    rect(screen, (230, 230, 240), (320, 20, 270, 360))
    rect(screen, (150, 150, 200), (340, 40, 110, 80))
    rect(screen, (150, 150, 200), (460, 40, 110, 80))
    rect(screen, (150, 150, 200), (340, 140, 110, 220))
    rect(screen, (150, 150, 200), (460, 140, 110, 220))
def tail():
    surface = pygame.Surface((251, 121))
    surface.fill((200, 200, 57))
    ellipse(surface, cat_color, (0, 0, 250, 100))
    ellipse(surface, (0,0,0), (0, 0, 250, 100), 2)
    surface2 = pygame.transform.rotate(surface, -25)
    screen.blit(surface2, (400,450))
def body():
    ellipse(screen, cat_color, (50, 420, 460, 200))
    ellipse(screen, (0,0,0), (50, 420, 460, 200), 2)
def lapki():
    ellipse(screen, cat_color, (25, 480, 50, 100))
    ellipse(screen, cat_color, (75, 570, 100, 50))
    ellipse(screen, (0,0,0), (25,480, 50, 100), 2)
    ellipse(screen, (0,0,0), (75, 570, 100, 50), 2)
def leg():
    ellipse(screen, cat_color, (400, 520, 120, 120))
    ellipse(screen, (0,0,0), (400, 520, 120, 120), 2)
    ellipse(screen, cat_color, (495, 590, 40, 100))
    ellipse(screen, (0,0,0), (495, 590, 40, 100), 2)
def head():
    circle(screen, cat_color, (80, 500), 70)
    circle(screen, (0,0,0), (80,500), 70, 2)
pink = (255,192,203)
def ears():
    #left ear
    polygon(screen, cat_color, ((18, 430), (20, 465), (50, 437)))
    polygon(screen, (0,0,0), ((18, 430), (20, 465), (50, 437)), 2)
    polygon(screen, pink, ((22, 433), (24, 458), (44, 441)))
    polygon(screen, (0,0,0), ((22, 433), (24, 458), (44, 441)), 1)
    #right ear
    polygon(screen, cat_color, ((107, 437), (132.5, 456), (135, 427)))
    polygon(screen, (0,0,0), ((107, 437), (132.5,460), (135, 427)), 2)
    polygon(screen, pink, ((114,439), (128.8, 451.5), (132.3,432.5)))
    polygon(screen, (0,0,0), ((114,439), (128.8, 451.5), (132.3,432.5)), 1)
def eyes():
    eye = pygame.Surface((41,41))
    eye.fill(cat_color)
    circle(eye, (150, 255, 50), (20, 20), 20)
    blik = pygame.Surface((10, 20))
    blik.fill((150, 255, 50))
    ellipse(blik, (255, 255, 255), (0, 0, 10, 20))
    blik2 = pygame.transform.rotate(blik, 45)
    eye.blit(blik2, (6, 5))
    circle(eye, (0, 0, 0), (19, 20), 20, 1)
    circle(eye, (0, 0, 0), (20, 20), 20, 1)
    ellipse(eye,(0,0,0), (25, 7, 7, 28))
    screen.blit(eye, (25, 470))
    screen.blit(eye, (85, 470))
def face():
    polygon(screen, pink, ((73, 520), (87, 520), (80, 528)))
    polygon(screen, (0,0,0), ((73, 520), (87, 520), (80, 528)), 1)
    polygon(screen, (0,0,0), ((72, 520), (87, 520), (80, 528)), 1)
    line(screen, (0,0,0), (80, 528), (80, 540), 2)
    arc(screen, (0, 0, 0), (70, 535, 10, 10), 3.14, 2 * 3.14, 2)
    arc(screen, (0,0,0), (80, 535, 10, 10),  3.14, 2 * 3.14, 2)
def moustache():
    h = 7
    for i in range(0, 3):
        aalines(screen, (0,0,0), False, [(70,528 +h*i), (68,525+h*i), (65, 523 +h*i), (60, 521+h*i), (55,517+h*i), (50,515+h*i), (45,516+h*i), (40, 519+h*i), (35, 522+h*i), (30, 524+h*i), (25, 527+h*i)], 1)
        aalines(screen, (0,0,0), False, [(90,528 +h*i), (92,525+h*i), (95, 523 +h*i), (100, 521+h*i), (105,517+h*i), (110,515+h*i), (115,516+h*i), (120, 519+h*i), (125, 522+h*i), (130, 524+h*i), (135, 527+h*i)], 1)
def ball():
    nitka = []
    nitka.append((150,750))
    for i in range(1, 40):
        nitka.append((150+i*5, nitka[i - 1][1] + randint(-5, 5)))
    aalines(screen,(100,100,100), False, nitka, 4)
    circle(screen, (160, 160, 160), (350,700), 70)
    circle(screen, (0,0,0), (350,700), 70, 2)
    l = 10
    for i in range(3):
        aalines(screen, (0,0,0), False, [(330+l*i, 750),(332+l*i,730),(335+l*i, 720),(350+l*i,710),(360+l*i,705)], 2)
        aalines(screen, (0,0,0), False, [(325,660+l*i),(345,665+l*i),(365,670+l*i),(375,675+l*i),(380,680+l*i),(385,685+l*i),(390,690+l*i),(395,695+l*i)],2)
room()
window()
tail()
body()
lapki()
leg()
head()
ears()
eyes()
face()
moustache()
ball()

#------------------------------------------------------------------------------------------------
pygame.display.update()
clock = pygame.time.Clock()
finished = False
# после чего, чтобы они отобразились на экране, экран нужно обновить:

pygame.display.update()

# Эту же команду нужно будет повторять, если на экране происходят изменения.

clock = pygame.time.Clock()
finished = False
# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
