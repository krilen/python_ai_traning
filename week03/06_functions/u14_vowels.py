VOWELS = "aeiou"

def count_vowels(text: str ="", char: str =VOWELS) -> int | None:
    if not isinstance(text, str) or not isinstance(char, str):
        return None
    
    if not len(text) or not len(char):
        return None   
    
    count_char = 0

    for c in char:
        count_char += text.casefold().count(c.casefold())

    return count_char

print(count_vowels(12))
print(count_vowels("hello"))
print(count_vowels("hello", "l"))
print(count_vowels("hello", 0))
print(count_vowels("hello world and have a nice weekend"))
print(count_vowels("hello world and have a nice weekend", "ae"))