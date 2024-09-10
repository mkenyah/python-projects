

# r = random.randrange(40)
# to generate 40 included
# r = random.randint(40)

# print(r)

# my nyc trial

import random

top_of_range = input("Please type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
    else:
        print("You've entered a valid number.")
else:
    print("Please type a valid number next time.")
    quit()

random_number = random.randint(0, 5)
print("Random number:", random_number)
guesses = 0
    
while True:
   
    guesses += 1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
        if user_guess == random_number:
            print("You got it!")
            break
        else:
            print("You've got it wrong! 😥")
    else:
        print("Please enter a valid number 😅.")
        
print("you got it in ",  guesses , " guesses ")
