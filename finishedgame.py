#Turtle graphics game
import turtle
import random
import math
from playsound import playsound
import pygame

#Music
playsound('C:/Users/callu/Documents/Python/VOLUME_01 A Night Of Dizzy Spells.wav', False)
#Set up screen
wn = turtle.Screen()
wn.bgcolor("blue")
wn.tracer(2)
wn.bgpic("underwater.gif")

#Draw border
mypen = turtle.Turtle()
mypenp2 = turtle.Turtle()
mypen.penup()
mypen.speed(0) 
mypen.setpos(-300, -300)
mypen.pendown()
mypen.pensize(5)
for side in range(4):
	mypen.forward(600)
	mypen.left(90)
mypen.hideturtle()

#Create players
player = turtle.Turtle()
player.color("gold")
player.shape("turtle")
player.penup()
player.speed(0)
player.setpos(random.randint(-300,300), random.randint(-300,300))

player2 = turtle.Turtle()
player2.color("limegreen")
player2.shape("turtle")
player2.penup()
player2.speed(0)
player2.setpos(random.randint(-300,300), random.randint(-300,300))

#Create score variable
score = 0
scorep2 = 0

#Create goals
maxGoals = 10
goals = []

for count in range(maxGoals):
	goals.append(turtle.Turtle())
	goals[count].speed(9)
	goals[count].color("red")
	goals[count].shape("turtle")
	goals[count].penup()
	goals[count].setpos(random.randint(-300,300), random.randint(-300,300))

#Set speed variable
speed = 1

#Define functions
def p1turnleft():
	player.left(30)
def p1turnright():
	player.right(30)
def p2turnleft():
	player2.left(30)
def p2turnright():
	player2.right(30)
def increasespeed():
	global speed
	speed += 1
def decreasespeed():
	global speed
	speed -= 1

def isCollision(t1, t2):
	d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
	if d < 20:
		return True
	else: 
		return False

#Set bindings
turtle.listen()
turtle.onkey(p1turnleft, "Left")
turtle.onkey(p1turnright, "Right")
turtle.onkey(p2turnleft, "a")
turtle.onkey(p2turnright, "d")
turtle.onkey(p2turnleft, "A")
turtle.onkey(p2turnright, "D")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")
turtle.onkey(increasespeed, "w")
turtle.onkey(decreasespeed, "s")
turtle.onkey(increasespeed, "W")
turtle.onkey(decreasespeed, "S")

while True:
	player.forward(speed)
	player2.forward(speed)

	#Player boundary checking
	if player.xcor() > 300 or player.xcor() < -300:
		player.right(180)
		playsound('C:/Users/callu/Documents/Python/Hit 5.wav')
	if player.ycor() > 300 or player.ycor() < -300:
		player.right(180)
		playsound('C:/Users/callu/Documents/Python/Hit 5.wav')
	if player2.xcor() > 300 or player2.xcor() < -300:
		player2.right(180)
		playsound('C:/Users/callu/Documents/Python/Hit 5.wav')
	if player2.ycor() > 300 or player2.ycor() < -300:
		player2.right(180)
		playsound('C:/Users/callu/Documents/Python/Hit 5.wav')
	
	#Move the goals
	for count in range(maxGoals):
		goals[count].forward(3)

		#Goal boundary checking
		if goals[count].xcor() > 300 or goals[count].xcor() < -300:
			goals[count].right(180)
		if goals[count].ycor() > 300 or goals[count].ycor() < -300:
			goals[count].right(180)

		#Collision checking
		if isCollision(player, goals[count]):
			goals[count].setpos(random.randint(-290, 290), random.randint(-290, 290))
			goals[count].right(random.randint(0,360))
			playsound('C:/Users/callu/Documents/Python/Powerup 3.wav')
			score += 1
			mypen.undo()
			mypen.penup()
			mypen.hideturtle()
			mypen.setposition(-385, 280)
			scorestring = "Score: %s" %score
			mypen.color("white")
			mypen.write(scorestring, False, align="left", font=("Arial",14, "normal"))
		if isCollision(player2, player):
			player.setpos(random.randint(-290, 290), random.randint(-290, 290))
			player.right(random.randint(0,360))
			playsound('C:/Users/callu/Documents/Python/Powerup 2.wav')
			score -=1
			mypen.undo()
			mypen.penup()
			mypen.hideturtle()
			mypen.setposition(-385, 280)
			scorestring = "Score: %s" %score
			mypen.color("white")
			mypen.write(scorestring, False, align="left", font=("Arial",14, "normal"))
			scorep2 += 1
			mypenp2.undo()
			mypenp2.penup()
			mypenp2.hideturtle()
			mypenp2.setposition(310, 280)
			scorestring = "Score: %s" %scorep2
			mypenp2.color("white")
			mypenp2.write(scorestring, False, align="left", font=("Arial",14, "normal"))
		#Game over screen
		if score > 14:
			player.hideturtle()
			player2.hideturtle()
			goals[count].hideturtle()
			player.forward(0)
			player2.forward(0)
			goals[count].forward(0)
			mypen.penup()
			mypen.hideturtle()
			mypen.setposition(-205, 0)
			gameoverstring = "GAME OVER"
			p1winstring = "Player 1 wins!"
			mypen.color("black")
			mypen.write(gameoverstring, False, align="left", font=("Arial",52, "normal"))
			mypen.setposition(-200, 0)
			mypen.color("white")
			mypen.write(gameoverstring, False, align="left", font=("Arial",50, "normal"))
			mypen.setposition(-205, -75)
			mypen.color("black")
			mypen.write(p1winstring, False, align="left", font=("Arial",52, "normal"))
			mypen.setposition(-200, -75)
			mypen.color("white")
			mypen.write(p1winstring, False, align="left", font=("Arial",50, "normal"))
		if scorep2 > 14:
			player.hideturtle()
			player2.hideturtle()
			goals[count].hideturtle()
			player.forward(0)
			player2.forward(0)
			goals[count].forward(0)
			mypen.penup()
			mypen.hideturtle()
			mypen.setposition(-205, 0)
			gameoverstring = "GAME OVER"
			p2winstring = "Player 2 wins!"
			mypen.color("black")
			mypen.write(gameoverstring, False, align="left", font=("Arial",52, "normal"))
			mypen.setposition(-200, 0)
			mypen.color("white")
			mypen.write(gameoverstring, False, align="left", font=("Arial",50, "normal"))
			mypen.setposition(-205, -75)
			mypen.color("black")
			mypen.write(p2winstring, False, align="left", font=("Arial",52, "normal"))
			mypen.setposition(-200, -75)
			mypen.color("white")
			mypen.write(p2winstring, False, align="left", font=("Arial",50, "normal"))
