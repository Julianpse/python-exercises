string = "hello how are you."

#1. Uppercase a String
print(string.upper())

#2. Capitalize a string
print(string.capitalize())

#3. Reverse a string
print(string[::-1])

#4. Leetspeak
input_string = input("Enter your string here: ").upper()
output_string = " "

for letter in input_string:
   output_letter = letter
   if output_letter == 'A':
       output_letter = '4'
   if output_letter == 'E':
       output_letter = '3'
   if output_letter =='G':
       output_letter = '6'
   if output_letter == 'I':
       output_letter = '1'
   if output_letter =='O':
       output_letter = '0'
   if output_letter =='S':
       output_letter = '5'
   if output_letter =='T':
       output_letter = '7'
   output_string += output_letter

print(output_string)
       


#5. Long Vowels
def replace_vowels():
    
    replace = {"aa" : "aaaaa", "ee" : "eeeee", "ii" : "iiiii", "oo" : "ooooo","uu" : "uuuuu"}
    
    word = input("input word: ").lower()
    
    for i, j in replace.items():
        word = word.replace(i,j)
        
    print(word)
    
replace_vowels()           
         
#6  Caesar Cipher
import codecs
secret_message = ""

def caesar_cipher(secret_message):
    secret_message = codecs.encode("{}".format(secret_message), 'rot_13')
    print(secret_message)    
  
   
caesar_cipher("lbh zhfg hayrnea jung lbh unir yrnearq")
