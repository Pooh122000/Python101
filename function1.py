def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def multi(a, b):
    return a*b


def div(a, b):
    return a/b


def power(a, b):
    return a**b


num_1 = int(input("Enter the first number: \n"))
num_2 = int(input("Enter the second number: \n"))

print("1.Add \n 2.Sub \n  3.multi \n 4.Div \n 5.Power")
option = input("Enter the option needed \n")

if(option == "Add"):
    print(add(num_1, num_2))

elif(option == "Sub"):
    print(sub(num_1, num_2))

elif(option == "multi"):
    print(multi(num_1, num_2))

elif(option == "Div"):
    print(div(num_1, num_2))

elif(option == "Power"):
    print(power(num_1, num_2))

else:
    print("Wrrong option selected")
