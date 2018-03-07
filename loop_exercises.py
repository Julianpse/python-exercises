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
for i in range (width):
    for j in range (height):
        print('*' if i in [0, height-1] or j in [0, width-1] else ' ', end=' ')
    print()



#7 & 8 Print a Triangle
def triangle(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
        
print(triangle(7))



#9 Multiplication Table
mult_table_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def times_tables(n):
    for i in mult_table_list:
        print("{} x {} = {}".format(n,i,i*n))


print(times_tables(8))


