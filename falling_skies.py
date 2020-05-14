import turtle
import random

score=0
lives = 3

wn = turtle.Screen()
wn.title("Falling Skies")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)


wn.register_shape("deer-left.gif")
wn.register_shape("deer-right.gif")
wn.register_shape("hunter.gif")
wn.register_shape("nut.gif")

#Player

player = turtle.Turtle()
player.speed(0)
player.shape('deer-right.gif')
player.color('white')
player.penup()
player.goto(0,-250)
player.direction = "stop"

#list of good_guys

good_guys = []

#Good guy

for _ in range(20):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape('nut.gif')
    good_guy.color('blue')
    good_guy.penup()
    good_guy.goto(-100,250)
    good_guy.speed = random.randint(1,4)
    good_guys.append(good_guy)

#list of bad_guys

bad_guys = []

#Bad guy

for _ in range(20):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape('hunter.gif')
    bad_guy.color('red')
    bad_guy.penup()
    bad_guy.goto(100,250)
    bad_guy.speed = random.randint(1,4)
    bad_guys.append(bad_guy)

#Pen

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.goto(0,260)
font = ("Courier",24,'normal')
pen.write("Score: {} Lives: {}".format(score,lives), align='center',font=font)


#function

def go_left():
    player.direction="left"
    player.shape("deer-left.gif")

def go_right():
    player.direction="right"
    player.shape("deer-right.gif")

#keyboard-binding

wn.listen()
wn.onkeypress(go_left,'Left')
wn.onkeypress(go_right,'Right')

#Main game loop

while True:
    
    #Update Screen
    wn.update()

    #Move Player
    
    if player.direction=="left":
        x=player.xcor()
        x-=3
        player.setx(x)

    if player.direction=="right":
        x=player.xcor()
        x+=3
        player.setx(x)

    #Move good_guy
    for good_guy in good_guys:
        y = good_guy.ycor()
        y-= good_guy.speed
        good_guy.sety(y)

        if y<-300:
            x = random.randint(-380,380)
            y = random.randint(300,300)
            good_guy.goto(x,y)

        if good_guy.distance(player)<20:
            x = random.randint(-380,380)
            y = random.randint(300,300)
            good_guy.goto(x,y)
            score += 10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score,lives), align='center',font=font)
    
    #Move bad_guy
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y-= bad_guy.speed
        bad_guy.sety(y)

        if y<-300:
            x = random.randint(-380,380)
            y = random.randint(300,300)
            bad_guy.goto(x,y)

        if bad_guy.distance(player)<20:
            x = random.randint(-380,380)
            y = random.randint(300,300)
            bad_guy.goto(x,y)
            score -= 10
            lives -=1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score,lives), align='center',font=font)


wn.mainloop()
