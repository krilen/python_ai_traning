import random

nums = [random.randint(1,100) for _ in range(10)]

nums_sum = 0

for num in nums:
    nums_sum += num
    
print("The sum of '", *nums, "' is '", nums_sum, "'.")

nums.sort()

print("The largest number is: '", nums[-1], "'.")
print("While the smallest number is: '", nums[0], "'.")