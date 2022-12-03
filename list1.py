# interchange first and last element in the list

# list1 = [1, 2, 3, 4, 5]
# first = list1[0]
# last = list1[-1]
# first, last = last, first

# list1[0] = first
# list1[-1] = last
# print(list1)

def swap(list1, num1, num2):
    n1 = list1.index(num1)
    n2 = list1.index(num2)
    list1[n1], list1[n2] = list1[n2], list1[n1]
    print(list1)


swap(["a", "b", "c", "d", "e", "f", "g"], "a", "b")
