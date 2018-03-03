import random

def play_again():
    ask_user_if_wants_to_play_again =  input("Do you want to play again? (y/n)").upper()
    if ask_user_if_wants_to_play_again == "Y":
        guess_a_number()
    else:
        print("Okay bye!")


def guess_a_number():
    secret_number = random.randint(1,10)
    print("I am thinking of a number between 1 and 10")
    
    guess = int(input("What's the number? "))
    guess_counter = 0
    
    
    while guess != secret_number:
        guess_counter += 1
        guesses_left = 5 - guess_counter
        if guess < secret_number and guess_counter < 5:
            guess = int(input("Sorry, try again. Your guess is too low. You have {} guesses remaining. What's the number? ".format(guesses_left)))
        elif guess > secret_number and guess_counter < 5:
            guess = int(input("Sorry, try again. Your guess is too high. You have {} guesses reamaining. What's the number? ".format(guesses_left)))
        else:
            print("Sorry you ran out of guesses!")
            play_again()
            break
    else:
        print("You got it!")
        play_again()
    

guess_a_number()

        

    
    