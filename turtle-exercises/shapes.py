from turtle import * 

def triangle():
  forward(100)
  right(120)
  forward(100)
  right(120)
  forward(100)
  
  mainloop()

def square():
  t.color('aqua')
  forward(100)
  left(90)
  forward(100)
  left(90)
  forward(100)
  left(90)
  forward(100)
  
  mainloop()
    
def pentagon():
  forward(50)
  left(72)
  forward(50)
  left(72)
  forward(50)
  left(72)
  forward(50)
  left(72)
  forward(50)
  
  mainloop()
    
def hexagon():
  counter = 0
  while counter < 6:
    counter += 1 
    forward(50)
    left(60)
    
def octagon():
  counter = 0
  while counter < 8:
    counter += 1 
    forward(50)
    left(45)

def star():
  counter = 0
  while counter < 5:
    counter += 1
    forward(45)
    left(145)
    forward(50)

    
def draw_circle():
  circle(90,360)
  mainloop()
  
circle(90,360)  
star()
octagon()
hexagon()
pentagon()
triangle()
square()

