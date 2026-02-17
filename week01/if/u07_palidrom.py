word = input("Give me a word >> ")

palindrom = " not "

if word == word[::-1]:
    palindrom = " "

print(f"The word, '{word}', is{palindrom}a palindrom")