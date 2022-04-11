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
        if should_start == "n":
            break
        more_card = input("Type 'y' to get another card, type 'n' to pass:")
        if more_card == "n":
            should_start = "n"
            result()
            break
