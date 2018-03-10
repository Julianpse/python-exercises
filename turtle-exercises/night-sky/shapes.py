from turtle import * 

def big_star():
  color("yellow")
  fillcolor("yellow")
  pendown()
  begin_fill()
  counter = 0
  while counter < 5:
    counter += 1
    forward(45)
    left(145)
    forward(50)
  end_fill()
  penup()

  
  
def medium_star():
  pendown()
  color("yellow")
  fillcolor("yellow")
  begin_fill()
  counter = 0
  while counter < 5:
    counter += 1
    forward(20)
    left(145)
    forward(50)
  end_fill()
  penup()
  

def small_star():
  color("yellow")
  fillcolor("yellow")
  pendown()
  begin_fill()
  counter = 0
  while counter < 5:
    counter += 1
    forward(10)
    left(145)
    forward(50)
  end_fill()
  penup()
  
  
def tiny_star():
  color("yellow")
  fillcolor("yellow")
  pendown()
  begin_fill()
  counter = 0
  while counter < 5:
    counter += 1
    forward(5)
    left(145)
    forward(50)
  end_fill()
  penup()