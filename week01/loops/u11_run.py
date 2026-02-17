letters = input("Give me a string of letters >> ").upper()

APPROVED_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

compressed = ""
previous_letter = ""
previous_value = 0

for letter in letters:

    if letter in APPROVED_LETTERS:
        
        if letter != previous_letter and previous_value > 0:
            compressed += str(previous_value) +previous_letter
            previous_value = 0
            previous_letter = ""
        
        if letter != previous_letter and previous_value == 0:
            previous_letter = letter
            previous_value = 1
            
        elif letter == previous_letter and previous_value > 0:
            previous_value += 1

else:
    
    if previous_value > 0:
        compressed += str(previous_value) +previous_letter
        
    elif letter in APPROVED_LETTERS:
        compressed += "1" +letter

print(letters, "::",  compressed)





