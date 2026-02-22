string = input("Provide a string >> ").lower()

string_unique = set(string)

if " " in string_unique:
    string_unique.remove(" ")

print(f"The string '{string}' has '{len(string_unique)}' unique letters.")