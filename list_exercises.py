list_of_numbers = [-21,1,14,-8,3,7,9,5,2,0,24,12,46]
"""
#1. Sum the Numbers
print(sum(list_of_numbers))

#2. Largest Number
print(max(list_of_numbers))

#3. Smallest Number
print(min(list_of_numbers))

#4. Even Numbers
for numbers in list_of_numbers:
    if (numbers % 2 == 0):
        print(numbers)
        
#5. Positive Numbers
for numbers in list_of_numbers:
    if (numbers > 0):
        print(numbers)

#6. Positive Numbers 2
positive_numbers_list = []

for numbers in list_of_numbers:
    if numbers > 0:
        positive_numbers_list.append(numbers)
       
print(positive_numbers_list)

#7. Multiply a List (factor of 3)
new_list = []
for numbers in list_of_numbers:
    new_list.append(numbers*3)

print(new_list)

#8. Multiply Vectors
list_a = [2,4,6]
list_b = [3,6,9]
list_c = []

for i in range(0, len(list_a)):
    list_c.append(list_a[i] * list_b[i])

print(list_c)

#9. Matrix Addition
m1 = [[1, 2] , [3,4]]
m2 = [[5,6] , [7,8]]

m3 = []

for i in range(len(m1)):
    for j in range(len(m1)):
        m3[i][j] = m1[i][j] + m2[i][j]

for k in m3:
    print(m3)


#10. Matrix Addition II
for i in range(len(matrix1)):
    for j i range(len(matrix2)):
        
"""
#11. De-Dup
a = ["hello", "apple", "banana", "ice cream", "orange", "banana", "kiwi", "hello"]
b = []

a = set(a)
b = list(a)

print(b)


