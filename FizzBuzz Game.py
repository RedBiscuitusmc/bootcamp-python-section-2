########################################################
#Coding BootCamp Challenge Udemy
#Section 5
#FizzBuzz Coding Exercise
#Jacob A. Merlin
########################################################
#########################################################
# Use the last step first when building if, elif, else statements
#Such as  checking if both numbers are divided by 3 and 5 then divides into 3 then into 5
#Finally following the else statement to act as the catch all.


# #for loop using in range
# for number in range (1, 101):
#   # Using a if statement to check if the list number divides into either 3 and 5
#     if( number % 3==0) and (number % 5==0):
#       print("FizzBuzz")
#       #Checking only if 3 divides into the number varible
#     elif( number % 3==0):
#       print("Fizz")
#       #Checking only if 5 divides into  number varible
#     elif( number % 5==0):
#       print("Buzz")
#       #The catch all
#     else:
#       print(number)

#for loop using in range
for number in range (1, 101):
    if( number % 3==0) and (number % 5==0):
        print("FizzBuzz")
    elif( number % 3==0):
        print("Fizz")
    elif( number % 5==0):
        print("Buzz")
    else:
        print(number)