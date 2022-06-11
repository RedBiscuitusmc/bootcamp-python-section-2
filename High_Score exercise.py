########################################################
#Coding BootCamp Challenge Udemy
#Section 5
#High Score exercise
#Jacob A. Merlin
########################################################
#########################################################
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
#########################################################

#########################################################
#Varible for sum function
highest_Score = 0

#For Loop for max function
for score in student_scores:
    if score > highest_Score:
        highest_Score = score


print(f"The highest score in the class is: {highest_Score}")

#########################################################

#########################################################
#Notes for this exercise

# We use  the list 'student_scores' in a for loop to grab the information stored
# From there we use a if statement to define the list, we say if the value in score is greater than the highest_score varible then set the highest_score varible to  the highest value stored inthe list or in this case 'score'.
#for score in student_scores:
#  if score > highest_Score:
#    highest_Score = score
