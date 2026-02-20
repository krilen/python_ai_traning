import random

nums = [random.randint(1,100) for _ in range(3)]

print("These are the nunbers in the order that they was appended: '", *nums, "'.")

# Way 1
print()
print("Sorting the list and using the first and last element as the smallest and largest number")

nums1 = nums[:]
nums1.sort()

print(f"Smallest number: {nums1[0]}")
print(f"Largest number: {nums1[-1]}")
print(f"Median for these numbers: {round((nums1[0] + nums1[-1]) /2,1)}")

# Way 2
print()
print("Using max and min functions to get the element as the smallest and largest number")

print(f"Smallest number: {min(nums)}")
print(f"Largest number: {max(nums)}")
print(f"Median for these numbers: {round((min(nums) + max(nums)) /2,1)}")