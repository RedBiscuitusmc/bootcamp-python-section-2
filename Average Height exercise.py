########################################################
#Coding BootCamp Challenge Udemy
#Section 5
#Average Height exercise
#Jacob A. Merlin
########################################################
#########################################################
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
#########################################################
#########################################################
#total_height = sum(student_heights)
#Creating our own sum function
#########################################################
#Varible for sum function
total_height = 0

#For Loop for sum function
for height in student_heights:
    total_height = total_height + height

#########################################################
#number_of_students = len(student_heights)
#Creating our own len function
#########################################################
#Varible for len function
total_students = 0
#For Loop for len function
for number_of_students in student_heights:
    total_students +=  1

#########################################################
#combining statement with round function
average_height = round(total_height / total_students)


print(average_height)