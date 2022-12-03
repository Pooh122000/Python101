def has23(nums):
    for i in range(len(nums)):
        if nums[i] == 2 or nums[i] == 3:
            return True

    else:
        return False


print(has23([4, 3]))
has23([7, 3])
has23([3, 7])
has23([4, 2])
has23([5, 2])
has23([6, 7])
