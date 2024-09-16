import turtle
import time
import random
HEIGHT = 500
WIDTH = 500
COLORS = ['red', 'yellow', 'blue', 'grey', 'green', 'purple', 'cyan']



def get_number():
    while True:
        number_of_turtles = input("How many turtles would you watch to race (2-10)?  ")
        if number_of_turtles.isdigit():
            number_of_turtles = int(number_of_turtles)
        else:
             print("You didn't type a number, try again! ")
             continue
        if 2 <= number_of_turtles <=10:
             break
        else: 
             print("You have to type a number between 2 and 10:  ")
    return number_of_turtles

def race(colors):
    turtle = turtles(colors)
    while True:
        for racer in turtle:
            distance = random.randrange(2,15)
            racer.forward(distance)

            x,y = racer.pos()
            if y>= HEIGHT//2-10:
                return colors[turtle.index(racer)]
            






def turtles(colors):
    turtles = []
    spacing = WIDTH // (len(colors)+1)
    for i, value in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape('turtle')
        racer.color(value)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH //2 +(i+1)*spacing, -HEIGHT// 2 + 20)
        racer.pendown
        turtles.append(racer)
    
    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)

number = get_number()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:number]


winner = race(colors)
print(winner)

time.sleep(5)
turtle.done()