def big_diff(nums):
   max1= nums[0]
   min1=nums[0]
   for i in nums:
     if max1 < i:
       max1=i

     elif min1 > i:
       min1=i
   print("MAX: ",max1)
   print("MIN: ",min1)    
   return (max1 - min1)

print(big_diff([10, 3, 5, 6]))
print(big_diff([7, 2, 10, 9]))
print(big_diff([2, 10, 7, 2]))
