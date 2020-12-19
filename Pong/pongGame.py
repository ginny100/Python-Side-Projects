#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:05:13 2020

Pong Game

Implementation for Mac

Tutorial by: Christian Thompson
"""

import turtle
import os

wn = turtle.Screen() # Create a frame for the game screen
wn.title("Classic Pong Game") # Add the title of the game to the game screen
wn.bgcolor("pink") # Color of the game screen
wn.setup(width = 800, height = 600) # Demensions of the game screen
wn.tracer(0) # Stops the window from updating

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0) # Speed of animation, not speed of the paddle. It sets the speed to the maximum possible speed
paddleA.shape("square")
paddleA.color("black")
paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
paddleA.penup() # Draw a line while the paddel is moving
paddleA.goto(-350, 0) # The location of the paddle

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0) # Speed of animation, not speed of the paddle. It sets the speed to the maximum possible speed
paddleB.shape("square")
paddleB.color("black")
paddleB.shapesize(stretch_wid = 5, stretch_len = 1)
paddleB.penup() # Draw a line while the paddel is moving
paddleB.goto(350, 0) # The location of the paddle

# Ball
ball = turtle.Turtle()
ball.speed(0) # Speed of animation, not speed of the paddle. It sets the speed to the maximum possible speed
ball.shape("circle")
ball.color("red")
ball.penup() # Draw a line while the ball is moving
ball.goto(0, 0) # The location of the paddle
ball.dx = 1/2 # every time the ball moves,
ball.dy = -1/2 # it moves by 2 pixels

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier", 24, "normal"))

# Move paddle A up
def paddleAUp():
    y = paddleA.ycor() # ycor() is from the turtle module
    y += 20
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor() # ycor() is from the turtle module
    y -= 20
    paddleA.sety(y)  
    
# Move paddle B up
def paddleBUp():
    y = paddleB.ycor() # ycor() is from the turtle module
    y += 20
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor() # ycor() is from the turtle module
    y -= 20
    paddleB.sety(y)  
    
# Keyboard binding
wn.listen()
wn.onkeypress(paddleAUp, "w")
wn.onkeypress(paddleADown, "s")
wn.onkeypress(paddleBUp, "o")
wn.onkeypress(paddleBDown, "k")

# Main game loop (any game needs this)
while True:
    wn.update() # Update the screen every time the loop runs
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    
    # Top and Bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # Reverse the direction
        #os.system("afplay bounce_sound.wav&")
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # Reverse the direction
        #os.system("afplay bounce_sound.wav&")
    
    # Left and Right
    if ball.xcor() > 350:
        scoreA += 1 
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        
    if ball.xcor() < -350:
        scoreB += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        
        
    # Paddle A and Ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1    
        os.system("afplay bounce_sound.wav&")
        
    # Paddle B and Ball collisions
    elif ball.xcor() > 340 and ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce_sound.wav&")