import random

def numbers():
    return [random.randint(1, 10) for _ in range(15)]

numbers1 = numbers()
numbers2 = numbers()

numbers1.extend(numbers2)

print(numbers1)
numbers1 = list(set(numbers1))
print(numbers1)
