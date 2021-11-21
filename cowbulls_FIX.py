import random

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
print (number)
bull = 0
cow = 0

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")
print()

while playing:
    user_guess = input("Give me your best guess! ")
    if user_guess == "exit":
        print()
        print("Until next time cowboy")
        break
    guesses+=1

    if user_guess == number[0]:
        bull+=1
        print("Hey you got one! NICE!")
    elif user_guess == number[1]:
        bull+=1
        print("Hey you got one! NICE!")
    elif user_guess == number[2]:
        bull+=1
        print("Hey you got one! NICE!")
    elif user_guess == number[3]:
        bull+=1
        print("Hey you got one! NICE!")
    else:
        cow+=1
        print("Your guess isn't quite right, try again.")

    print("You have " + str(cow) + " cows, and " + str(bull) + " bulls.")

    if bull == 4:
        playing = False
        print()
        print("You win the game after " + str(guesses) + "guesses! The number was "+str(number))
        break #redundant exit
