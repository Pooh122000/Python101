def evenodd(list1):
    list2 = []
    list3 = []
    for i in list1:
        if i % 2 == 0:

            list2.append(i)

        else:
            list3.append(i)

    print(list2)
    print(list3)

    print(len(list2))
    print(len(list3))


evenodd([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 44, 66, 55, 77, 5, 7])
