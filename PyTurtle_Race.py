# ----------------------------------------------------------------------------------------------  #
# PyTurtle_Race : Based upon famour turtle and random library
# This script will give you a little glimpse, what you can do with turtle library.
# A cool betting game, bet your turtle as winner :)
# ----------------------------------------------------------------------------------------------  #


import turtle
from random import randint

color_list = ['red', 'green', 'blue', 'cyan','yellow']
turtl = ['red', 'green', 'blue', 'cyan','yellow']
x_quad = [110, 80, 50, 20, -10 ]

def begin_race():

    
    game_screen=turtle.Screen()
    game_screen.title('Turtle Race')
    game_screen.setup(500,480)
    game_screen.bgcolor('#A7E30E')
    mygame=turtle.Turtle()
    
    mygame.penup()
    mygame.goto(-110, 210)
    mygame.write("Python's Turtle Race", align='left', font=('Arial', 14, 'bold'))
    mygame.goto(-110, 190)
    mygame.write('Bet your turtle', align='left', font=('Arial', 8, 'bold'))
    mygame.penup()
    mygame.goto(-130, -130)
    mygame.color('blue')
    mygame.write('Winner : The One touches the 14th Lap first.', align='left', font=('Arial', 10, 'bold'))
    mygame.color('black')
    mygame.penup()
    mygame.goto(-140, 140)
    mygame.speed(500)

    for step in range(15):
        mygame.write(step)
        mygame.right(90)
        mygame.forward(10)

        if step == 14:
            mygame.pendown()
            mygame.forward(190)
            mygame.penup()
            mygame.backward(210)
            mygame.left(90)
            mygame.penup()
            mygame.forward(20)
            mygame.hideturtle()

        else:
            new_step = 0

            while new_step <= 180:
                mygame.pendown()
                mygame.forward(10)
                mygame.penup()
                mygame.forward(10)
                new_step=new_step+20

            mygame.backward(210)
            mygame.left(90)
            mygame.forward(20)



    for i in range(5):
        turtl[i]=turtle.Turtle()
        turtl[i].color(color_list[i])
        turtl[i].shape('turtle')
        turtl[i].penup()
        turtl[i].goto(-160, x_quad[i])
        for val in range(10):
            turtl[i].left(36)
            turtl[i].pendown()

        if i == 4:
            for turn in range(100):
                turtl[0].forward(randint(1,5))
                turtl[1].forward(randint(1,5))
                turtl[2].forward(randint(1,5))
                turtl[3].forward(randint(1,5))
                turtl[4].forward(randint(1,5))


    
    turtle.done()


begin_race()
