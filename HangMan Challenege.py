#########################################################
########################################################
#Coding BootCamp Challenge Udemy
#Section 7
#HangMan Challenge
#Jacob A. Merlin
#########################################################
#########################################################
#Imports
import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list
#########################################################
print(logo)

#########################################################
#Word List

display_list = []

#########################################################
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(chosen_word)

#########################################################
#list build logic
for letter in range (word_length):
    display_list += "_"


print (display_list)

#########################################################
end_of_game = False


while not end_of_game:

    guess = input("Guess a letter:\n").lower()
    #If the user has entered a letter they've already guessed, print the         letter and let them know.
    if guess in display_list:
        print(f"you have already entered {guess}")

    #letter placement logic
    for position in range (word_length):
        letter = chosen_word [position]
        if guess == letter:
            display_list[position] = letter

    #life logic
    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose.")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display_list)}")

    if "_" not in display_list:
        end_of_game = True
        print("you win!")

    print(stages[lives])
#########################################################