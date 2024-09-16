import turtle
import time
import random
HEIGHT = 500
WIDTH = 500
COLORS = ['red', 'yellow', 'blue', 'grey', 'green', 'purple', 'cyan']
assignators = ['+', "-", "*" ]
numbers = ['1', '2', '3', '4', '5','6', '7', '8', '9', '10']

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




def verify_input(number):
        if number.isdigit():
            number = int(number)
        
        return number

def race(colors):
    list = turtles(colors)
    while True:
        for racer in list:
            answer = random.choice(numbers) + random.choice(assignators) + random.choice(numbers)
            answer2 = eval(answer)
            response = turtle.textinput("Question for the "+colors[list.index(racer)]+"turtle:", answer+" = ")
            response = verify_input(response)
            if eval(answer) == response:
                print(answer2, response)
                racer.forward(100)
            elif response == "q":
                break
            
             
            x,y = racer.pos()
            if y>= HEIGHT//2-10:
                return colors[list.index(racer)]
            

    
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
turtle.write("The winner is"+ winner)
turtle.done()

