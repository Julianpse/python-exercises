#Uncomment Each Question to Run 

#1 Hello
"""
def hello(name):
    print("Hello {}.".format(name))

hello("Julian")  

"""

#2 y = x + 1
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plot

def f(x):
    return x + 1

xs = list(range(-3, 4))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
plot.savefig('y=x+1.png')
plot.close

"""
#3 Square of X 
"""

import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot

def f(x):
    return (x**2)
    
f_output = []

x_list = list(range(-100,100))

for x in x_list:
    f_output.append(f(x))
    
pyplot.plot(x_list,f_output)
pyplot.savefig('squareofx.png')
pyplot.close

"""
#4. Odd or Even
"""
import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot

def f(x):
    if x % 2 != 0:
        return 1 
    else:
        return -1
        
f_output = []

x_list = list(range(-5,6))

for x in x_list:
    f_output.append(f(x))
    
pyplot.bar(x_list, f_output)
pyplot.savefig('odd_or_even.png')
pyplot.close

"""

#5. Sine 
"""
import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot
from math import sin 

def f(x):
    return sin(x)

f_output = []

x_list = list(range(-5,6))

for x in x_list:
    f_output.append(f(x))

pyplot.plot(x_list, f_output)
pyplot.savefig('sine.png')
pyplot.close

"""

#6. Sine 2
"""
import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot
from math import sin
from numpy import arange

def f(x):
    return sin(x)

f_output = []

x_list = list(arange(-5, 6, 0.1))

for x in x_list:
    f_output.append(f(x))

pyplot.plot(x_list, f_output)
pyplot.savefig('sine2.png')
pyplot.close
"""

#7 Degree Conversion
"""

import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot

def c_to_f(x):
   return x * 1.8 + 32
    
f_output = [] 

c_list = list(range(-50,100))

for x in c_list:
    f_output.append(c_to_f(x))

pyplot.plot(c_list, f_output)
pyplot.savefig('degree_conversion.png')
pyplot.close

"""

#8 Play Again
"""
def play_again():
    answer = (input("Do you want to play again? (Y/N) ")).upper()
    if answer == "Y":
        print("True")
        return True
    else:
        print("False")
        return False

play_again()
"""

#9 Play Again Twice

def play_again():
    answer = (input("Do you want to play again? (Y/N) ")).upper()
    if answer == "Y":
        print("True")
        return True
    else:
        print("False")
        return False

play_again()


