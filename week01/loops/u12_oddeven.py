
def my_sort(nums):
    
    nums_length = len(nums)
    
    if nums_length > 1:
        done = False
        
        while True:
            
            for i in range(1, nums_length):
                
                if i < nums_length:
                    
                    print(nums[i], nums[i-1])
                    # There is no break!!!!!!!!!
                    if nums[i -1] < nums[i]:
                        print("ok")
                        continue
                    
                    nums[i -1], nums[i] = nums[i], nums[i -1]
                    print("flip")
                
                else:
                    done = True
                    break
        
            if done:
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


print(numbers_odd)
numbers_odd = my_sort(numbers_odd)



print(numbers, numbers_odd, numbers_even)
