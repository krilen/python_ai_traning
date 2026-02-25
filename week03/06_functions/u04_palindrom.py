
def is_palindrome(text: str) -> bool:
    
    if not isinstance(text, str):
        return False
    
    return text == text[::-1]

words = [
    "level",
    "radar",
    "world",
    "madam",
    "python",
    "refer",
    "apple",
    "racecar",
    "house",
    "civic"
]


for word in words:
    print(f"Is the '{word}' a palindrome? {is_palindrome(word)}.")