#Coding BootCamp Challenge Udemy
#Section 4
#Treasure Map Exercise
#Jacob A. Merlin
########################################################
import random
########################################################
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
########################################################
#Grabbing a new varible for position request from user
Loc_0 = position [0]
Loc_1 = position [1]
#Converting str into int
horizonal = int (Loc_0)
vertical = int (Loc_1)
########################################################
#We took a varible (( selected_row)) then wrapped the varible "map" with
# our other varible vertical and created a new result
# we took that combined result under the new varible 'selected_row'
#then added another varible 'horizonal' to equal the placement of our new data 'x'
selected_row = map [vertical - 1 ]
selected_row [horizonal - 1 ] = "x"



########################################################
print(f"{row1}\n{row2}\n{row3}")