from random import randint

def check_unique(numbers: list = []) -> bool | None:
    
    if not len(numbers):
        return None

    if len(numbers) != len(set(numbers)):
        return False
    
    return True
    
    
print(f"{check_unique()=}")
print(f"{check_unique([1])=}")
print(f"{check_unique([1,1])=}")
print(f"{check_unique([1,2,3,4])=}")
print(f"{check_unique([1,2,3,1])=}")

