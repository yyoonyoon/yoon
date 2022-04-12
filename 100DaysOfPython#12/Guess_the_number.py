import random
import Guess_the_number_art
should_continue = True
user_guess = 0
computer_guess = 0
lives = 0

def is_correct():
    global lives
    global should_continue
    if user_guess == computer_guess:
        print("You've got number! you win😃")
        should_continue = False
    elif user_guess > computer_guess :
        lives -= 1
        print("Too high.\nGuess again.")
        print("You have {0} attemps remaining to guess number.".format(lives))
    elif user_guess < computer_guess:
        lives -= 1
        print("Too low.\nGuess again.")
        print("You have {0} attemps remaining to guess number.".format(lives))

print(Guess_the_number_art.logo)
print("Welcome to the Number Guessing Game !\n\
    I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard'. :").lower()
print("You have 10 attemps remaining to guess number.".format(lives))

if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

computer_guess = random.randrange(1,101)

for i in range(10):
    user_guess = int(input("Make a guess. :"))
    is_correct()
    if (lives == 0):
        print("You lose😭")
        break
    if should_continue == False:
        break