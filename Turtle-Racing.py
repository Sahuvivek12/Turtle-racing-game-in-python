import turtle
import random
import time

WIDTH, HEIGHT = 1280, 720
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'pink', 'brown']

def get_number_of_turtles():
    while True:
        turtles = input("Enter the number of turtles you want to race (2-8): \n")
        if turtles.isdigit():
            turtles = int(turtles)
            if 2 <= turtles <= 8:
                return turtles
            else:
                print("Number not in range (2-8), Try again!")
        else:
            print("Invalid input, please enter a number (2-8)")

def race(turtles):
    finish_line = WIDTH // 2 - 40 
    while True:
        for racer in turtles:
            distance = random.randrange(1, 30)
            racer.forward(distance)
            x, y = racer.pos()
            if x >= finish_line:
                return racer.color()[0]

def create_turtles(colors):
    turtles = []
    spacingy = HEIGHT // (len(colors) + 1)
    for i, color in enumerate(colors):
        racing_turtle = turtle.Turtle()
        racing_turtle.color(color)
        racing_turtle.shape('turtle')
        racing_turtle.penup()
        racing_turtle.setpos(-WIDTH // 2 + 20, -HEIGHT // 2 + (i + 1) * spacingy)
        racing_turtle.pendown()
        turtles.append(racing_turtle)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')
    screen.bgcolor('black')

turtles_count = get_number_of_turtles()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:turtles_count]
turtles = create_turtles(colors)
winner = race(turtles)
print("The winner is the turtle with color:", winner)
time.sleep(3)
