def findelement(list1, n):
    for i in list1:
        if n in list1:
            print(list1.index(n))
            break

        else:
            list1.append(n)
            print(list1)


print(findelement(["a", "b", "c"], "g"))
