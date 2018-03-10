#Exercise 1 
# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# print(phonebook_dict['Elizabeth'])
# phonebook_dict['Kareem'] = '938-489-1234'
# del phonebook_dict['Alice']
# print(phonebook_dict)



#Exercise 2
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }


# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'][1])



# Exercise 3 Letter Summary 

# dictionary = {}

# def letter_histogram(word):
  
#   for letters in word:
#     if letters not in dictionary:
#       dictionary[letters] = 1
#     else: 
#       dictionary[letters] += 1 
  
#   print(dictionary)
  
# letter_histogram("poopy")



#Exercise 4 Word Summary

word_tally= {} 
top_3 = []

def word_histogram():
  paragraph = input("Write a sentence: " )
  paragraph = paragraph.split()
  
  for words in paragraph:
    if words not in word_tally:
      word_tally[words] = 1
    else:
      word_tally[words] += 1
  print(word_tally)
  
  
word_histogram()


#Bonus
