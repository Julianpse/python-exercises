import pickle

phonebook_dict = {
    "Ellen" : "281-555-5555",
    "Johnny" : "832-999-5555",
    "Mike" : "281-330-8004",
    "Christopher" : "713-330-8004",
    "Avinash" : "281-888-9999",
    "Riley" : "222-222-1102",
    "Pizza" : "281-999-5555"
}

not_valid = "That is not a valid selection"

#Looks up an entry from the phonebook and prints their phone number
def look_up_entry():
    entry_name = input("Who are you looking for? ")
    print(entry_name)
    print(phonebook_dict[entry_name])



#Adds a new phonebook entry    
def set_entry():
    new_entry = input("Enter the person's name: ")
    new_value = input("Enter their phone number: ")
    phonebook_dict[new_entry] = new_value
    print("Your entry has been stored")
    
    

#Removes an entry from the phonebook    
def delete_entry():
    delete_person = input("Who would you like to remove? ")
    del phonebook_dict[delete_person]
    print("{} has been removed from your phonebook".format(delete_person))
    
    


#lists all entries of the phonebook 
def print_all():
    for(key, value) in phonebook_dict.items():
        print("{}:{}".format(key,value))



#Saves entries
def save_entries():
# open the file in write mode (wb)
    myfile = open('phonebook.pickle', 'wb')
# dump the contents of the phonebook_dict into myfile - the open file
    pickle.dump(phonebook_dict, myfile)
# close myfile
    myfile.close()
    print("Your entries have been saved")
    

#Restors Entries
def load_entries():
# open the file in read mode (rb)
    myfile = open('phonebook.pickle', 'rb')  
# loads contents from file and stores in the phonebook_dict variable
    phonebook_dict = pickle.load(myfile)
    
#Starts the phonebook app    
def open_phonebook():
    
    print("    Electronic Phone Book\n\
    =====================\n\
    1. Look up an entry\n\
    2. Set an entry\n\
    3. Delete an entry\n\
    4. List all entries\n\
    5. Quit\n\
    6. Save Entries\n\
    7. Restore Saved Entries")

    user_selection = int(input("Pick a number: "))
  
    if user_selection == 1:
        look_up_entry()
        open_phonebook()
    elif user_selection == 2:
        set_entry()
        open_phonebook()
    elif user_selection == 3:
        delete_entry()
        open_phonebook()
    elif user_selection == 4:
        print_all()
        open_phonebook()
    elif user_selection == 5:
        exit_app()
    elif user_selection == 6:
        save_entries()
        open_phonebook()
    elif user_selection == 7:
        load_entries()
        open_phonebook()
    else:
        print(not_valid)
        open_phonebook()
        
        
#prompts user if they want to exit the app     
def exit_app():
    exit_prompt = input("Are you sure you want to exit (y/n)? ").upper()
    print(exit_prompt)
    if exit_prompt == "Y":
        exit()
    elif exit_prompt == "N":
        open_phonebook()
    else:
        print(not_valid)
        open_phonebook()
        

open_phonebook()

    
    


