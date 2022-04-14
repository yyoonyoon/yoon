import random
import game_data
import Higer_Lower_Game_Art

again = "yes"
should_continue = True
score = 0
user_answer = ""
real_answer = ""
rand_dict_A = game_data.data[random.randint(0,49)]
rand_dict_B = game_data.data[random.randint(0,49)]

def check(user_answer, real_answer): # 정답체크 함수
    global score
    global should_continue
    global again
    global rand_dict_A
    global rand_dict_B
    if (rand_dict_A["follower_count"] > rand_dict_B["follower_count"]):
        real_answer = "A"
        if (user_answer == real_answer): 
            rand_dict_B = game_data.data[random.randint(0,49)]
            score += 1
            print("Your current score is {}\n\n".format(score))
            return rand_dict_B
        else:
            print("Your final score is {0}\n".format(score))
            again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
            if again == "yes":
                should_continue = True
            else :
                should_continue = False
    else:
        real_answer = "B"
        if (user_answer == real_answer):
            rand_dict_A = rand_dict_B
            rand_dict_B = game_data.data[random.randint(0,49)]
            score += 1
            print("Your current score is {}\n\n".format(score))
            return rand_dict_B
        else:
            print("Your final score is {0}\n".format(score))
            again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
            if again == "yes":
                should_continue = True
            else :
                should_continue = False
        

while (again == "yes"):
    print(Higer_Lower_Game_Art.logo)
    print("Welcome to Higher Lower Game 🎮🕹\n")
    while (should_continue == True):
        print("A - Name: {0}, Description: {1}, Country: {2}"\
            .format(rand_dict_A["name"], rand_dict_A["description"], rand_dict_A["country"]))
        print(Higer_Lower_Game_Art.vs)
        while True: # 중복 제거
            if(rand_dict_A == rand_dict_B):
                rand_dict_B = game_data.data[random.randint(0,49)]
            else:
                break
        print("\nB - Name: {0}, Description: {1}, Country: {2}\n"\
            .format(rand_dict_B["name"], rand_dict_B["description"], rand_dict_B["country"]))
        user_answer = input("Type 'A' or 'B' who has more instagram followers you think. :").upper()
        check(user_answer, real_answer)