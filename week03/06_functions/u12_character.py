count_character = lambda character, text: sum(1 for char in text if char == character)  

print(count_character("l", "hello"))
print(count_character("", "hello"))
print(count_character("e", "hello to you all and have a nice evening"))
print(count_character("l", ""))