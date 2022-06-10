#Coding BootCamp Challenge Udemy
#Section 4 Final
#rock, paper, scissors Game
#Jacob A. Merlin
########################################################
import random
########################################################
#Varibles for signs
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
########################################################
#User Input Request
print("Welcome to rock, paper, scissors.Lets play.")
player_Choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
print("=====================================================")
########################################################
#transform user input to ensure the input is captured correctly
p_c = player_Choice.lower()

########################################################
#Player Section
#Varible to transform the str into a int
p_c_final = int(p_c)
#Bug Catch / stop block for invlid numbers
if p_c_final >= 3 or p_c_final <= 0:
    print("You typed a invalid number, you lose!")
########################################################
#list for rock/paper/scissors
r_p_s = [rock, paper, scissors]
########################################################
print("=====================================================")
print("You Picked:")
print("=====================================================")
########################################################
#Player Choice Logic Handler
if p_c_final == 0:
    print(rock)
elif p_c_final == 1:
    print(paper)
elif p_c_final == 2:
    print(scissors)
########################################################
print("=====================================================")
print("The A.I. Picked:")
print("=====================================================")
########################################################
#A.I. Choice Logic Handler
a_I_Choice = random.randint(0, 2)

if a_I_Choice == 0:
    print(rock)
elif a_I_Choice == 1:
    print(paper)
elif a_I_Choice == 2:
    print(scissors)

########################################################
print("=====================================================")
########################################################
#Win Condition Handler or event handler
if p_c_final == 0 and a_I_Choice == 2:
    print("You Win!")
elif p_c_final == 2 and a_I_Choice == 0:
    print("You lose.")
elif p_c_final < a_I_Choice:
    print("You lose.")
elif p_c_final > a_I_Choice:
    print("You Win!")
elif p_c_final == a_I_Choice:
    print("You tied")