#Exercise 1
# file_handle = open(input("Enter file name: "), 'r')
# contents = file_handle.read()
# print(contents)
# file_handle.close()


#Exercise 2 
# file_handle = open(input("Enter file name: "), 'w')
# contents = file_handle.write(str(input("Enter file content: ")))
# print(contents)
# file_handle.close()


#Exercise 3 
histogram = {}

file_handle = open(input("Enter File Name: "), 'r')
contents = file_handle.read()

#histogram letters
for letters in contents:
    if letters not in histogram:
        histogram[letters] = 1
    else:
        histogram[letters] += 1 

# histogram words
contents = contents.split()

for words in contents:
    if words not in histogram:
        histogram[words] = 1
    else:
        histogram[words] += 1
        

#Exercise 4
import json

data = histogram
with open('data.json', 'w') as fh:
  json.dump(histogram, fh, indent = 2)
   
with open('data.json', 'r') as fh:
    data = json.load(fh)
    print(data)

file_handle.close()  



#Bonus 
#Crashed after 514 loops with "Killed" error 
# import io 
# counter = 0
# file_handle = io.StringIO()
# while True:
#     counter += 1
#     file_handle.write("hp" * 1024 * 1024)
#     print(counter)
# contents = file_handle.getvalue()
# file_handle = io.StringIO("initial text")
# contents = file_handle.read()
    






        
