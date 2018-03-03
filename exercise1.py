"""
# Exercise 1 Hello, you!
name1 = input("First Name? ")
print("Hey, what's up {}".format(name1))




# Exercise 2 HELLO, YOU!
name2 = input("name: ")
print("HELLO, ", name2.upper())




# Exercise 3 Madlib
name3 = input("What's the person's name? ")
favorite_restaurant = input("What is their favorite restaurant to eat at? ")
print("{}'s favorite restaurant to eat at is {}".format(name3, favorite_restaurant))




# Exercise 4 Day of the week
days_of_week = {0 : "Sunday", 1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday"}

def day_calculator(day):
    day = int(input('Day (0-6)? ')) 
    
    for number, words in days_of_week.items():
        if number == day:
            return words 
        else:
            return "That's not a valid entry!"
            
print (day_calculator(5))
    



# Exercise 5 Work or Sleep In?
def go_to_work():
    day = int(input('Day (0-6)'))
    
    if day == 0 or day == 6:
        print ("Sleep in! You don't have work today!")
    elif day in range (1,5):
        print ("Get up! You have work today!")
    else:
        print ("That's not a valid day!")

go_to_work()




# Exercise 6 Celsius to Fahrenheit
def celsius_to_fahrenheit():
    temp = int(input("Temperature in Celsius: " ))
    temp_fahrenheit = temp * 1.8 + 32
    
    print("The temperature in Fahreneit is {} degrees".format(temp_fahrenheit))
    
celsius_to_fahrenheit() 



# Exercise 7 & 8 Tip Calculators
def tip_calculator():
    tip_levels = {"good" : .20, "fair" : .15, "bad" : .1}
    tip = 0.0
    total = 0.0
    total_rounded_cents = 0.0
    splitting = 0
    
    bill = float(input("Enter Total Bill Amount: "))
    level = input("Enter level of service(good, fair or bad): ")
    

    for levels, percent_tip in tip_levels.items():
        if level == levels: 
            tip = bill * percent_tip
            total = tip + bill
            
            #Rounds to 2 decimal places for cents
            total_rounded_tip = float("{0:.2f}".format(tip))
            total_rounded_cents = float("{0:.2f}".format(total))
            
            
            print("Tip amount: ${} \nTotal Bill: ${}".format(total_rounded_tip,total_rounded_cents))
            
    split = input("Are you splitting the bill today (yes/no)?: ").upper()
            
    if split == "YES":
        splitting = int(input("How many ways?: "))
        print("Each of you will pay: ${}".format(total / splitting))
        
            
tip_calculator() 



#Exercise 9: 1 to 10
counter = 0
while counter < 10:
    counter += 1
    print(counter)
    
"""

#Exercise 10: How many coins? 

def coin_adder():
    coins = 0
    print("You currently have {} coins".format(coins))
    while coins >=  0:
        asking = input("Would you like another (yes/no)? ").upper()
        while asking == "YES":
            coins += 1
            print("You have {} coins".format(coins))
            break
        if asking == "NO":
            print("Okay, I guess you have enough coins! Bye!")
            exit()
            
coin_adder()