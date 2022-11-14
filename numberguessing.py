import random
#random is a module installed on pythong for choosing a random nimber

top_of_range = input ( "Type a number: ")
# we use .isdigit to check if it is a number before changing it to an integer
if top_of_range.isdigit ():
    top_of_range = int (top_of_range)

    if top_of_range <= 0:
        print ("please type a number larger than 0 next time ")
        quit()

else:
    print ("please type a number next time.")
    quit()
# random.randrange selects a random number in a range without the top value. random.randint selects a random number with the top value
random_number = random.randrange (0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input ("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time.")
        quit()
        continue

    if user_guess == random_number:
        print ("You got it!")
        break
    elif user_guess > random_number:
            print ("You were above the number!")
    else:
            print ("You were below the number!")

print ("You got it in", guesses, "guesses")