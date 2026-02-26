# Skipping the function and simply doing a named lambda
even_numbers = lambda nums: [num for num in nums if num % 2 == 0]

print(even_numbers([1,2,3,4,5,6]))
print(even_numbers([1,3,5]))
print(even_numbers([]))
print(even_numbers([2]))


# Remembered filter() after I was done
# But I think this is worse then the list comprehension
even_numbers2 = lambda num: num % 2 == 0

print(list(filter(even_numbers2, [1,2,3,4,5,6])))
print(list(filter(even_numbers2, [1,3,5])))
print(list(filter(even_numbers2, [])))
print(list(filter(even_numbers2, [2])))