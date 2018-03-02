# Exercise 1
name1 = input("First Name? ")
print("Hey, what's up {}".format(name1))


# Exercise 2 
name2 = input("name: ")
print("HELLO, ", name2.upper())


# Exercise 3 
name3 = input("What's the person's name? ")
favorite_restaurant = input("What is their favorite restaurant to eat at? ")
print("{}'s favorite restaurant to eat at is {}".format(name3, favorite_restaurant))


# Exercise 4
days_of_week = {0 : "Sunday", 1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday"}

def day_calculator(day):
    day = int(input('Day (0-6)? ')) 
    
    for number, words in days_of_week.items():
        if number == day:
            return words 
        else:
            return "That's not a valid entry!"
            
print (day_calculator(5))
    

# Exercise 5