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
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()




while not at_goal():
    if wall_in_front():
        movement_bot()

    elif front_is_clear():
        move()

    else:
        print("WE run aground!")

#While something_is_true():
# then do this