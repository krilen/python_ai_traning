
def my_sort(nums):
    """
    A function that takes a list and sorts it in order without using built-in sort
    """
    nums_length = len(nums)
    
    if nums_length > 1:
        while True:
            switch_order = False
            
            for i, _ in enumerate(range(1, nums_length), start=1):
                
                if nums[i] < nums[i -1]:
                    nums[i], nums[i -1] = nums[i -1], nums[i]
                    
                    switch_order = True

            if not switch_order:
                break
            
    return nums


numbers = []

while True:
    user_input = input("Give me a number (negative included), 'q' for quit >> ")
    
    if user_input.casefold() == "q":
        break
    
    try:
        numbers.append(int(user_input))
        
    except ValueError:
        print("Not a number, try again!!")

numbers_even = []
numbers_odd = []

for number in numbers:
    if number % 2 == 0:
        numbers_even.append(number)
        continue
    
    numbers_odd.append(number)

print("Even numbers:", end=" ")
for num in my_sort(numbers_even):
    print(num, end=", ")

print()

print("Odd numbers:", end=" ")
for num in my_sort(numbers_odd):
    print(num, end=", ")

print()