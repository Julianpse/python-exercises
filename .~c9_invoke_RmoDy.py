"""
#1. 1 to 10
for numbers in range(1,11):
    print(numbers)
    
#2. n to m

n = int(input("Start from #: "))
m = int(input("End at #: "))

for number in range(n,(m+1)):
    print(number)


#3 Odd Numbers
for numbers in range (1,11):
    if numbers % 2 != 0:
        print(numbers)


#4 Print a Square
counter = 0
star = "*"
while counter < 6:
    counter += 1
    print("*" * 5)


#5 Print a Square II
counters = 0 
stars = "*"
how_big = int(input("How big is the square? "))
while counters < how_big:
    counters += 1
    print(stars * how_big)
    


#6 Print a Box
width = int(input("How wide is the box? "))
height = int(input("How tall is the box? "))
sides = "*"
top_bottom = width
middle = height - 2
count = 0

"""

#7 Print a Triangle
a = "*"
counter = 0
while 
