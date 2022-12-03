marks = int(input("Enter the marks \n"))

if(marks >= 25 and marks < 80):
    print("In range")

elif(marks >= 0 and marks < 25):
    print("fail")

elif(marks >= 80):
    print("Pass")

else:
    print("incorrect input")
