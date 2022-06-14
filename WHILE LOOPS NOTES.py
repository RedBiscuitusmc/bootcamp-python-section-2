########################################################
#Coding BootCamp Challenge Udemy
#Section 5
#while loops notes
#Jacob A. Merlin
########################################################
########################################################

def turn_right ():
    turn_left()
    turn_left()
    turn_left()

def movement_bot ():
    move()
    turn_left()

    move()
    turn_right()

    move()
    turn_right()

    move()
    turn_left()


number_Of_movement = 6

while number_Of_movement > 0:
    movement_bot()
    number_Of_movement -= 1
    print(number_Of_movement)


while not at_goal():
    movement_bot()

#While something_is_true():
# then do this