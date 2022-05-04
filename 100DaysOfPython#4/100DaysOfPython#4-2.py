import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("What do you choose? Type 0 for Rock, 1 for paper,\
2 for scissors. : ")
me = input()
cases = [rock, paper, scissors]
computer = cases[random.randint(0,2)]

if (me=="0" and computer==cases[1]):
    print(f"{rock}\ncomputer choose:\n{paper}\nYou Lose.")
elif (me=="0" and computer==cases[2]):
    print(f"{rock}\ncomputer choose:\n{scissors}\nYou Win.")
elif (me=="0" and computer==cases[0]):
    print(f"{rock}\ncomputer choose:\n{rock}\nDraw.")
elif (me=="1" and computer==cases[1]):
    print(f"{paper}\ncomputer choose:\n{paper}\nDraw.")
elif (me=="1" and computer==cases[2]):
    print(f"{paper}\ncomputer choose:\n{scissors}\nYou Lose.")
elif (me=="1" and computer==cases[0]):
    print(f"{paper}\ncomputer choose:\n{rock}\nYou Win.")
elif (me=="2" and computer==cases[1]):
    print(f"{scissors}\ncomputer choose:\n{paper}\nYou Win.")
elif (me=="2" and computer==cases[2]):
    print(f"{scissors}\ncomputer choose:\n{scissors}\nDraw.")   
else:
    print(f"{scissors}\ncomputer choose:\n{rock}\nYou Lose.")  
print("rock,paper,scissors game is finished.")