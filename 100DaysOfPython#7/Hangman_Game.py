import random
import Hangman_art
import Hangman_words

word_list = Hangman_words.word_list
stages = Hangman_art.stages
displayed = []
answer = random.choice(word_list)
temp = answer
lives = 7
cnt = 0
for i in range(len(answer)):
    displayed.append("_")
print(Hangman_art.logo)

while True:
    cnt = 0
    user_answer = input("Guess a letter: ").lower()
    for k in range(len(answer)):
        letter = answer[k] # index of answer
        if letter == user_answer :
            print("Right")
            displayed[k] = letter
        else:
            print("Wrong")
            cnt += 1
    if cnt == len(answer): # 글자가 일치하는게 하나도 없을 때.
        cnt = 0
        print(stages[lives-8])
        lives -= 1
        print("It is not in the word.")
        print("Your left lives : {}\n".format(lives))

    if "_" not in displayed:
        print("You Win.\n")
        break  
    elif lives == 0:
        print("You Lose.")
        print("The answer is {0}\n".format(answer))
        break
    print("{0}\n\n".format(displayed))