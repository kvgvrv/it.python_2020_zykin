from random import randrange as rnd, choice
import tkinter as tk
import math
import time


class target():
    def __init__(self, canv):
        """Инициализация мишени."""

        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.new_target(canv)

    def new_target(self, canv):
        """ Инициализация новой цели. """

        x = self.x = rnd(600, 750)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 50)
        self.vx = rnd(5, 15) * choice([-1, 1])
        self.vy = rnd(5, 15) * choice([-1, 1])
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def move(self, canv):
        """Функция описывает движение мишеней.
        1. Функция проверяет, жива ли мишень или нет.
        2. Функция проверяет, не достигла ли мишень какой-либо стенки.
        """

        if self.live == 1:
            if (self.x + self.r >= 800) or (self.x - self.r <= 400):
                self.vx = - self.vx
            if (self.y + self.r >= 600) or (self.y - self.r <= 0):
                self.vy = - self.vy
            self.x += self.vx
            self.y -= self.vy
            self.set_coords(canv)

    def set_coords(self, canv):
        """Функция, устанавливающая координаты объекта мишени."""

        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def hit(self, canv):
        """Попадание шарика в цель."""

        canv.coords(self.id, -10, -10, -10, -10)


class points():
    def __init__(self, canv):
        """Инициализация объекта очки.
        Подсчет очков в левом верхнем углу
        """

        self.points = 0
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')

    def hit(self, canv, points=1):
        """Функция, отвечающая за подсчет очков при попадании."""
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

class ball():
    def __init__(self, canv, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.live = 1
        self.time = 0
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def time_live(self, canv, balls):
        """Функция, которая удаляет шары, выпущенные пушкой.
        Условие удаление шара:
        1.скорость шарика равно 0 по всем направлениям
        2.время существования шарика больше 1 секунды.
        """
        if self.vx == 0 and self.vy == 0 and self.time > 1000:
            canv.delete(self.id)
            balls.remove(self)
        else:
            self.time += 30

    def set_coords(self, canv):
        """Устанавливает координаты, по которым рисуется объект
        координаты задаются с помощью координат центра объекта, а также его радиуса."""
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self, canv):
        """Переместить мяч по прошествии единицы времени.
        Функция описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= 2
        if self.x + self.vx >= 780:
            self.x = 780
        if self.x + self.vx <= 20:
            self.x = 20
        if (self.x >= 780) or (self.x <= 20):
            self.vx = - self.vx
        if self.y - self.vy >= 550:
            self.y = 550
        if self.y >= 550:
            self.vy = - self.vy / 1.5
            self.vx = self.vx / 1.5
        if self.vx ** 2 + self.vy ** 2 < 2:
            self.vy = 0
            self.vx = 0
            self.y = 550
        self.x += self.vx
        self.y -= self.vy
        self.set_coords(canv)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2:
            return True
        else:
            return False


# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)



class gun():
    def __init__(self):
        """Инициализация пушки."""

        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        """Функция, которая описывает начала процесса стрельбы из пушки."""

        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """

        global balls, bullet
        bullet += 1
        new_ball = ball(canv)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""

        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        """Функция, описывающая мощность выстрела из пушки."""

        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


def new_game(event=''):
    """Функция, описывающая игру.
    внутри функции действует цикл, кооторый проверяет, находятся ли сейчас на экране мишени, присутсвуют ли на экране
    шары из пушки.
    Если условие выполняется, то вызывается функция движения мишеней."""

    global gun, t1, t2, screen1, balls, bullet, points
    t1.new_target(canv)
    t2.new_target(canv)
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls:
        t1.move(canv)
        t2.move(canv)
        for b in balls:
            b.move(canv)
            if t1.live and b.hittest(t1):
                t1.live = 0
                t1.hit(canv)
                points.hit(canv)
            if t2.live and b.hittest(t2):
                t2.live = 0
                t2.hit(canv)
                points.hit(canv)
            if t1.live == 0 and t2.live == 0:
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
            b.time_live(canv, balls)
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


t1 = target(canv)
t2 = target(canv)
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
points = points(canv)

new_game(canv)

tk.mainloop()
