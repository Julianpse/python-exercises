#1 Basics

class Person:
    def __init__(self, name, email, phone, friends, greeting_count):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greeting_count = greeting_count
        

    def greet(self, other_person):
        self.greeting_count += 1
        
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        
    def print_contact_info(self):
        print("{}'s email: {}, {}'s phone number: {}".format(self.name, self.email, self.name, self.phone))
    
    #need to check     
    def add_friend(self, other_person):
        return self.friends.append(other_person.name)
        
    def num_friends(self):
        print(len(self.friends))
        
    def count_greetings(self):
        print(self.greeting_count)
        
    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)
        
        

sonny = Person('Sonny','sonny@hotmail.com','482-485-4948', [ ], 0)
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', [ ], 0)

sonny.greet(jordan)
jordan.greet(sonny)
jordan.greet(sonny)

jordan.add_friend(sonny)
print(jordan.friends)

sonny.print_contact_info()

print(sonny.name, sonny.email, sonny.phone, sonny.friends, sonny.greeting_count)
print(jordan.name, jordan.email, jordan.phone, jordan.friends, jordan.greeting_count)

print(jordan)

#2 Make your own class

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print('{} {} {}'.format(self.year, self.make, self.model))
        
    
    

car = Vehicle('Nissan', 'Leaf', 2015)
car.print_info()
