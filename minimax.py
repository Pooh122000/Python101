# nums=[1,2,3,4]
def big_diff(nums):

    max1 = ''
    min1 = ''
    for i in nums:
        if nums[0] < i:
            max1 = i
        else:
            min1 = i
    print(max1)
    print(min1)
    # print("diff is:", int(max1)-int(min1))


big_diff([10, 3, 5, 6])
big_diff([7, 2, 10, 9])
big_diff([2, 10, 7, 2])


# ***********************
# def big_diff(nums):
#   max1= nums[0]
#   min1=nums[0]
#   for i in nums:
#     if max1 < i:
#       max1=i

#     elif min1 > i:
#       min1=i
#   return (max1 - min1)
