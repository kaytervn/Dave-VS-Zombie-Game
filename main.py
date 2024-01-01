import turtle
import random
import math
import pygame

sc = turtle.Screen()
sc.setup(width=800, height=800)
sc.title("Dave vs Zombie")
sc.addshape("dave.gif")
sc.addshape("dave_rv.gif")
sc.addshape("mower.gif")
sc.addshape("mower_rv.gif")
sc.addshape("yard.gif")
sc.addshape("tomb.gif")
sc.addshape("win.gif")
sc.addshape("gameover.gif")
sc.addshape("taco.gif")
sc.addshape("hotsauce.gif")
sc.addshape("chickenbucket.gif")
sc.addshape("zombie1.gif")
sc.addshape("zombie2.gif")
sc.addshape("zombie3.gif")
sc.addshape("zombie4.gif")
sc.addshape("zombie5.gif")
sc.addshape("zombie6.gif")
sc.addshape("zombie7.gif")
sc.bgpic("yard.gif")


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("dave.gif")
        self.goto(-300, 0)

    def move_up(self):
        if self.ycor() < 180:
            self.goto(self.xcor(), self.ycor() + 90)

    def move_down(self):
        if self.ycor() > -180:
            self.goto(self.xcor(), self.ycor() - 90)

    def move_forward(self):
        self.shape("dave.gif")
        if self.xcor() < 284:
            self.goto(self.xcor() + 73, self.ycor())

    def move_backward(self):
        self.shape("dave_rv.gif")
        if self.xcor() > -300:
            self.goto(self.xcor() - 73, self.ycor())


class Mower(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.goto(900, 900)
        self.speed = 10

    def move(self):
        self.forward(self.speed)

    def collidesZombie(self, zombie):
        d = math.sqrt(
            math.pow(self.xcor() - zombie.xcor(), 2)
            + math.pow(self.ycor() + 50 - zombie.ycor(), 2)
        )
        if d < 20:
            return True
        else:
            return False


class Zombie(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape(random.choice(zom_skins))
        self.goto(400, random.choice(yard_ycors))
        self.setheading(180)
        self.speed = random.randint(1, 4)

    def move(self):
        self.speed = random.randint(1, 4)
        self.forward(self.speed)

    def jump(self):
        self.goto(400, random.choice(yard_ycors))
        self.shape(random.choice(zom_skins))


class Tomb(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.goto(900, 900)
        self.shape("tomb.gif")

    def appear(self, object):
        self.goto(object.xcor(), object.ycor())


class Item(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape(random.choice(item_skins))
        self.goto(random.choice(yard_xcors) + 20, random.choice(yard_ycors) - 40)

    def appear(self):
        self.shape(random.choice(item_skins))
        self.goto(random.choice(yard_xcors) + 20, random.choice(yard_ycors) - 40)

    def collidesPlayer(self, player):
        d = math.sqrt(
            math.pow(self.xcor() - 20 - player.xcor(), 2)
            + math.pow(self.ycor() + 40 - player.ycor(), 2)
        )
        if d < 20:
            return True
        else:
            return False


class End(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.goto(900, 900)
        self.state = False

    def appear_win(self):
        self.shape("win.gif")
        self.goto(0, 0)
        self.state = True

    def appear_lose(self):
        self.shape("gameover.gif")
        self.goto(0, 0)
        self.state = True


class Score(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-320, 280)
        self.score = 0
        self.items_collected = 0
        self.update_display()

    def update_display(self):
        self.clear()
        self.write(
            "Score: "
            + str(self.score)
            + "\nItems Collected: "
            + str(self.items_collected),
            align="left",
            font=("Tahoma", 16, "bold"),
        )

    def change_score_by(self, num):
        self.score += num
        self.update_display()

    def change_items_collected_by(self, num):
        self.items_collected += num
        self.update_display()


def place_mower():
    if mower.xcor() < -400 or mower.xcor() > 400:
        if player.shape() == "dave.gif":
            mower.shape("mower.gif")
            mower.setheading(0)
        else:
            mower.shape("mower_rv.gif")
            mower.setheading(180)
        mower.goto(player.xcor(), player.ycor() - 50)


def isCollision(t1, t2):
    d = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)
    )
    if d < 20:
        return True
    else:
        return False


def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)


play_sound("Loonboon.mp3")

yard_ycors = [180, 90, 0, -90, -180]
yard_xcors = [-300, -227, -154, -81, -8, 65, 138, 211, 284]
zom_skins = [
    "zombie1.gif",
    "zombie2.gif",
    "zombie3.gif",
    "zombie4.gif",
    "zombie5.gif",
    "zombie6.gif",
    "zombie7.gif",
]
item_skins = ["chickenbucket.gif", "hotsauce.gif", "taco.gif"]

zombies = [Zombie() for _ in range(4)]
player = Player()
mower = Mower()
tomb = Tomb()
item = Item()
score = Score()
end = End()

turtle.listen()
turtle.onkey(player.move_backward, "Left")
turtle.onkey(player.move_forward, "Right")
turtle.onkey(player.move_up, "Up")
turtle.onkey(player.move_down, "Down")
turtle.onkey(place_mower, "space")

while not end.state:
    mower.move()
    if item.collidesPlayer(player):
        score.change_items_collected_by(1)
        item.appear()
    for zb in zombies:
        zb.move()
        if mower.collidesZombie(zb):
            score.change_score_by(10)
            tomb.appear(zb)
            zb.jump()
        if isCollision(player, zb) or zb.xcor() < -400:
            end.appear_lose()
    if score.score > 150 and score.items_collected > 15:
        end.appear_win()

pygame.mixer.music.stop()
turtle.done()
