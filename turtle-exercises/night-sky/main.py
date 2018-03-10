# Can be viewed at 
# https://trinket.io/library/trinkets/bd6fa07584

from turtle import *
from shapes import *

if __name__ == "__main__":
  
  #Canvas Setup 
  canvas = Screen()
  canvas.setup(1000,500)
  canvas.bgcolor(25,25,112)
  turtle = Turtle()
  turtle.color(25,25,112)
  turtle.pensize(5)
  speed("fast")
  penup()
  
  goto(0,100)
  big_star()
  goto(100,150)
  tiny_star()
  goto(100,10)
  medium_star()
  goto(500,5)
  tiny_star()
  goto(-200,100)
  small_star()
  goto(-300,200)
  tiny_star()
  goto(-325,5)
  small_star()
  goto(300, 50)
  medium_star()
  

