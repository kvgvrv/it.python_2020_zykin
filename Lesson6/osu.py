import pygame
from pygame.draw import *
from random import randint

pygame.init()
pygame.font.init() #это необходимо для отображения сообщений для игрока

FPS = 60
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
Score = 0
Combo = 0
Live = 5
q = 0       #временной счетчик
BALLS = []  #список мячей находящихся на экране
BOXES = []  #список коробок с сюрпризом

#инициализируем переменные текста
final_score = pygame.font.SysFont('Comic Sans MS', 60) 
stats_info = pygame.font.SysFont('Comic Sans MS', 40)
trolling = pygame.font.SysFont('Comic Sans MS', 55)
start_menu = pygame.font.SysFont('Comic Sans Ms', 60)


class ball:
    '''рисует новый шарик '''
    def __init__(self):
        self.x = randint(100, 1100)
        self.y = randint(100, 800)
        self.r = randint(50, 100)
        self.Vx = randint(-10, 10)
        self.Vy = randint(-10, 10)
        self.color = COLORS[randint(0, 5)]
    #метод отрисовки шарика
    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)
    #сделаем шарик движущимся
    def move(self):
        self.x += self.Vx
        self.y += self.Vy
        if self.x >= 1200:
            self.x = 1200
            self.Vx *= -1
        elif self.x <= 0:
            self.x = 0
            self.Vx *= -1
        if self.y >= 900:
            self.y = 900
            self.Vy *= -1
        elif self.y <= 0:
            self.y = 0
            self.Vy *= -1

class box:
    #новая мишень в форме квадрата О_О
     def __init__(self):
        self.a = randint(100, 100)
        self.x = randint(100, 1100)
        self.y = 0
        self.Vx = 0
        self.Vy = randint(3, 10)
        self.color = WHITE

     def move(self):
        self.y += self.Vy
        self.color = COLORS[randint(0, 5)]

     def draw(self):
        rect(screen, self.color, (self.x, self.y, self.a, self.a))

class bullet(ball):
     #конструктор шариков из коробок
    def __init__(self, x0, Rmax):
        self.x = x0
        self.y = 1050
        self.r = randint (30, Rmax)
        self.Vx = randint (-10, 10)
        self.Vy = randint (-10, 0)
        self.color = COLORS[randint(0, 5)]

def interface():
        #отобразим на экране интерфейс
        live_text = "Live: " + str(Live)
        score_text = 'Score: ' + str(Score)
        combo_text = 'Combo: ' + str(Combo)
        live_info = stats_info.render(live_text, True, (255,255,255))
        score_info = stats_info.render(score_text, True, (255,255,255))
        combo_info = stats_info.render(combo_text, True, (255,255,255))
        screen.blit(live_info, (1050,0))
        screen.blit(score_info, (0, 0))
        screen.blit(combo_info, (0,845))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
game_finished = False
Start_Screen = True

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            catched = False
            #проверка на попадание по шарику
            for i in range(len(BALLS)):
                if (event.pos[0] - BALLS[i].x)**2 + (event.pos[1] - BALLS[i].y)**2 <= BALLS[i].r**2:
                    Score += int (5000 / BALLS[i].r * Combo)
                    Combo += 1
                    if Combo % 5 == 0:
                        if Live < 5:
                            Live += 1
                    print('Got it!')
                    BALLS.pop(i)
                    catched = True
                    break
            #проверка на попадание по коробке
            for i in range(len(BOXES)):
                if BOXES[i].x <= event.pos[0] <= BOXES[i].x + BOXES[i].a:
                    if BOXES[i].y <= event.pos[1] <= BOXES[i].y + BOXES[i].a:
                        Score += int(5000 / BOXES[i].a * Combo)
                        Combo += 1
                        if Combo % 5 == 0:
                            if Live < 5:
                                Live += 1
                        print('Got it!')
                        BOXES.pop(i)
                        catched = True
                        break
            if catched == False:
                Live -= 1
                Combo = 0
                print("Missed!")
    #Стартовое меню
    if Start_Screen == True:
        hello_message = start_menu.render('Press space button', True, WHITE)
        screen.blit(hello_message, (320,420))
        pygame.display.update()

    #конец игры
    if game_finished == True:
        screen.fill(BLACK)
        Score_txt = str(Score)
        final_message = 'Your Score is ' + Score_txt
        final_score_message = final_score.render(final_message, True, (255, 255, 255)) #поверхность с текстом
        screen.blit(final_score_message, (360, 350))                                    #nemnogo trollinga
        if Score < 1000:
            trolling_message = trolling.render('Pathetic', True, (255,255,255))
            screen.blit(trolling_message, (400, 420))
        elif Score < 10000:
            trolling_message = trolling.render('Are you even trying to play?', True, (255,255,255))
            screen.blit(trolling_message,(320, 420))
        elif Score < 30000:
            trolling_message = trolling.render('Better luck next time', True, (255,255,255))
            screen.blit(trolling_message,(350,420))
        elif Score < 50000:
            trolling_message = trolling.render('Nice one', True, (255,255,255))
            screen.blit(trolling_message,(400,420))
        elif Score < 100000:
            trolling_message = trolling.render('You are tough!', True, (255,255,255))
            screen.blit(trolling_message,(380,420))
        elif Score > 100000:
            trolling_message = trolling.render('ARE YOU AN ASIAN!!!???', True, (255,0,0))
            screen.blit(trolling_message, (350,420))
        pygame.display.update()
        #запишем топ скор в файл
        ok = False
        with open('C:\dev\workspace\python_mipt/top_scores.txt', 'r') as file:
            for line in file:
                if Score > int(line):
                    ok = True
        with open('C:\dev\workspace\python_mipt/top_scores.txt', 'w') as file:
            if ok == True:
                file.write(Score_txt)
    #введем клавиши запуска и остановки игры
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            if Start_Screen == True:
                Start_Screen = False
        elif event.key == pygame.K_ESCAPE:
            game_finished = True
    #так же игра остановится если у нас закончатся жизни
    if Live == 0:
        game_finished = True
    #Мы проиграем, если мячей на экране окажется слишком много
    if len(BALLS) > 12:
       game_finished = True
     
                
    if game_finished == False and Start_Screen == False:
        if q % 50 == 0:
            b = ball()
            BALLS.append(b)
            if randint(0,1) == 1:
                s = box()
                BOXES.append(s)
        for element in BOXES:
            element.draw()
            element.move()
            #если коробка с сюрпризом упадет на землю то из нее вылетят шарики
            if element.y >= 1200 - element.a:
                BOXES.pop(BOXES.index(element))
                for i in range (3, randint(3,6)):
                    o = bullet(element.x, element.a)
                    BALLS.append(o)
        for element in BALLS:
            element.draw()
            element.move()
        pygame.display.update()
        screen.fill(BLACK)
        interface()
        q +=1
pygame.quit()