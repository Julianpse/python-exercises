string = "hello how are you."
"""
#1. Uppercase a String
print(string.upper())

#2. Capitalize a string
print(string.capitalize())

#3. Reverse a string
print(string[::-1])
"""
#4. Leetspeak not done
def leet_translator():
    leet_dictionary = {"a": 4, "e" : 3, "g" : 6, "i" : 1, "o": 0, "s": 5, "t" : 7}
    user_input = input("Enter your string here: ").split()
    out = [ ]
    
    for letters in user_input:
        if letters in leet_dictionary:
            print (leet_dictionary[letters])
        else:
            while leet_dictionary[letters] == False:
                out = out.append(letters)
        print(out)

leet_translator()       
        
"""


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

"""