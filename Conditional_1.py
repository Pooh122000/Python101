num_1 = int(input("Enter the first number: \n"))
num_2 = int(input("Enter the second number: \n"))

print("1.Add \n 2.Sub \n  3.multi \n 4.Div \n 5.Power")
option = input("Enter the option needed \n")


if(option == "Add"):
    print(num_1 + num_2)

elif(option == "Sub"):
    print(num_1 - num_2)

elif(option == "multi"):
    print(num_1 * num_2)

elif(option == "Div"):
    print(num_1/num_2)

elif(option == "Power"):
    print(num_1 ** num_2)

else:
    print("Wrrong option selected")
