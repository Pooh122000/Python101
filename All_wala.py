def array123(nums):
    list1 = [1, 2, 3]
    check = all(item in list1 for item in nums)
    if check is True:
        return True

    else:
        return False


print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))
