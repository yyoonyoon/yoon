############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

#----------------------------------------------------------------------------------------------
import random
from Black_Jack_art import logo

def random_card():
    my_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

def total_score():
    global my_score
    global computer_score
    my_score = sum(my_cards)
    computer_score = sum(computer_cards)

def ace():
    if (my_score > 21):
        if (11 in my_cards):
            my_cards[my_cards.index(11)] = 1
        total_score()
    elif (computer_score > 21):
        if (11 in computer_cards):
            computer_cards[computer_cards.index(11)] = 1
        total_score()

def result():
    if (my_score > 21 or computer_score > 21):
                if (my_score > 21 and computer_score > 21):
                    if (my_score - computer_score > 0):
                        print("\tYour final hand: {0}, Final Score: {1}\
                        \n\tComputer's final hand: {2}, Final score: {3}"\
                        .format(my_cards,my_score,computer_cards,computer_score))
                        print("You went over. You lose😤")
                        should_start = "n"
                    elif (my_score - computer_score < 0):
                        print("\tYour final hand: {0}, Final Score: {1}\
                        \n\tComputer's final hand: {2}, Final score: {3}"\
                        .format(my_cards,my_score,computer_cards,computer_score))
                        print("Congratulations!! You win🥳")
                        should_start = "n"
                    else:
                        print("Draw🤔")
                        should_start = "n"
                elif (my_score > 21):
                    print("\tYour final hand: {0}, Final Score: {1}\
                    \n\tComputer's final hand: {2}, Final score: {3}"\
                    .format(my_cards,my_score,computer_cards,computer_score))
                    print("You went over. You lose😤")
                    should_start = "n"
                elif (computer_score > 21):
                    print("\tYour final hand: {0}, Final Score: {1}\
                    \n\tComputer's final hand: {2}, Final score: {3}"\
                    .format(my_cards,my_score,computer_cards,computer_score))
                    print("Congratulations!! You win🥳")
                    should_start = "n"
    elif (more_card == "n"):
        if (my_score - computer_score > 0):
            print("\tYour final hand: {0}, Final Score: {1}\
            \n\tComputer's final hand: {2}, Final score: {3}"\
            .format(my_cards,my_score,computer_cards,computer_score))
            print("Congratulations!! You win🥳")
            should_start = "n"
        elif (my_score - computer_score < 0):
            print("\tYour final hand: {0}, Final Score: {1}\
            \n\tComputer's final hand: {2}, Final score: {3}"\
            .format(my_cards,my_score,computer_cards,computer_score))
            print("You went over. You lose😤")
            should_start = "n"

my_cards = []
computer_cards = []
my_score = 0
computer_score = 0
more_card = ""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
should_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")
random_card()
total_score()

while should_start == "y":
    print(logo)
    random_card()
    total_score()
    ace()
    print("\tYour Cards: {0}, Current Score: {1}\n\tComputer's first Card: {2}\n"\
        .format(my_cards,my_score,computer_cards[0]))
    more_card = input("Type 'y' to get another card, type 'n' to pass:")
    if more_card == "n":
        should_start = "n"
        result()
        break
    result()

    while (more_card == "y"):
        random_card()
        total_score()
        ace()
        print("\tYour Cards: {0}, Current Score: {1}\n\tComputer's first Card: {2}\n"\
        .format(my_cards,my_score,computer_cards[0]))
        result()
        more_card = input("Type 'y' to get another card, type 'n' to pass:")
        if more_card == "n":
            should_start = "n"
            result()
            break
