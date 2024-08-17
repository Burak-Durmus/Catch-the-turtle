import turtle
import random
import time


# screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Turtle Click Game")


# turtle
tosbaga = turtle.Turtle()
tosbaga.shapesize(3)
tosbaga.shape("turtle")
tosbaga.color("green")
tosbaga.penup()


# score
tiklama_sayisi = 0
score = turtle.Turtle()
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0,250)
score.write(f"score : {tiklama_sayisi}",move=False,align="center",font=("Arial",24,"normal"))


# functıon
def cliker(x,y):
    global tiklama_sayisi
    score.goto(0,250)
    turtle_x,turtle_y = tosbaga.pos()
    mesafe = tosbaga.distance(x,y)
    if mesafe <=20.0:
        tiklama_sayisi +=1
        score.clear()
        score.write(f"score : {tiklama_sayisi}",move=False,align="center",font=("Arial",24,"normal"))
        
         
# click starter
screen.onclick(cliker)


# time 
start = 15.0  
sayac = turtle.Turtle()
sayac.hideturtle()
sayac.color("red")
sayac.penup()
sayac.teleport(0,200)


# teleport & timer
for i in range(30):
    x = random.randint(-250,250)
    y = random.randint(-250,250)
    tosbaga.teleport(x=x,y=y)
    time.sleep(0.50)
    sayac.clear()
    sayac.write(f"Time: {start}",move=False,align="center",font=("Arial",24,"normal"))
    start -= 0.5
    if start == 0:
        sayac.clear()
        sayac.goto(0,0)
        sayac.write("Game Over",move=False,align="center",font=("Arial",50,"normal"))
        break


turtle.mainloop()