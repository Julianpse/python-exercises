string = "hello how are you."

#1. Uppercase a String
print(string.upper())

#2. Capitalize a string
print(string.capitalize())

#3. Reverse a string
print(string[::-1])

#4. Leetspeak not done
paragraph = "Given a paragraph of text as a string, print the paragraph in leetspeak."


#5. not done
string = "poop"

for letter in string:
    for char in "aeiou":
        if char == letter * 2:
            char * 5
print(string)
            
            
#6  Caesar Cipher
import codecs
secret_message = ""
def caesar_cipher(secret_message):
    secret_message = codecs.encode("{}".format(secret_message), 'rot_13')
    print(secret_message)    
  
   
caesar_cipher("lbh zhfg hayrnea jung lbh unir yrnearq")