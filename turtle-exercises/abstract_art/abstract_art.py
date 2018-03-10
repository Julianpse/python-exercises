#Available at https://trinket.io/library/trinkets/8e5418c91d

from turtle import *
import random

colors  = ["red","green","blue","orange","purple","pink","yellow"]

Screen().setup(500,500)
pensize(1)
speed('fast')

i = 20 
while i > 0:
  i -= 1
  begin_fill()
  color = random.choice(colors)
  fillcolor(color)
  penup()
  setpos(0,-i*20)
  circle(20 * i)
  pendown()
  
  end_fill()
  