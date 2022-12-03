list1 = []


def insert(n):

    for i in range(n):
        a = input("enter the number: ")
        if a != "":
            list1.append(a)
            print(list1)
        else:
            print("Invalid input")

    remove(list1)


def remove(list1):
    for i in range(len(list1)):
        list1.pop()
        print(list1)
    check(list1)


def check(list1):
    if not list1:
        print("Empty")
    else:
        print(len(list1))


insert(5)
