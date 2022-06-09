#Coding BootCamp Challenge Udemy
#Section 4
#Banker Roulette Exercise
#Jacob A. Merlin
########################################################
import random
########################################################

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
########################################################

#converting varible from string into int to be used in name picker randomizer
num_items = len(names)

#random name picker use -1 because scale is 0 - end of list -1 as 0 takes its place
random_choice = random.randint(0, num_items - 1)


#named varible controls logic for name choice based on the number drawn
person_who_pays = names[random_choice]
#output printed to the user
print(f"{person_who_pays} is going to buy the meal today!")