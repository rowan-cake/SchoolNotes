from turtle import *


    
def left_turn():
    for i in range(10):
        forward(15)
        left(9)
def left_turn(length):
    for i in range(10):
        forward(length/10)
        left(9)
def petal():
    begin_fill()
    left_turn()    
    left(90)       
    left_turn()
    left(90) # Line added 
    end_fill()
def petal(size):
    begin_fill()
    left_turn(size)
    left(90)
    left_turn(size)
    left(90)
    end_fill()
def drawFlower():
    for i in range(5): 
        petal()
        right(360/5)
def drawSprialFlower():   
    # Loop through the "petal spiral" 
    for i in range(0, 200, 10):
        petal(i) # Petal takes an input for size
        right(360/10)
def sprial():
    for i in range(100, 0, -5):
        forward(i)
        left(90)

