
# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

classes_held = int(input("Enter the number of classes held: \n"))
classes_attended = int(input("Enter the number of classes attented: \n"))

percent = (classes_attended / classes_held) * 100

if percent >= 75:
    print("You can sit in the Exam...")

else:
    print(" You can't sit in the Exam!!!")
