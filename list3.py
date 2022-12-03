# find smallest number in a list
def small(list1):
    # return min(list1)

    min1 = list1[0]
    for i in list1:
        if min1 > i:
            min1 = i

    print(min1)


small([4, 5, 6, 7, 7, 8, 3, 2, 1])
