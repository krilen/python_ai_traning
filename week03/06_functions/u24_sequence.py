def sequence(number: int=0) -> list | None:
    
    if not isinstance(number, int):
        return None
    
    if number < 1:
        return None
    
    result = {}
    
    for i in range(1, number +1):
        
        if not i % 2:
            result[i] = "even"
            
        else:
            result[i] = "odd"
            
    return result

print(f"{sequence("hello")=}")
print(f"{sequence()=}")
print(f"{sequence(3)=}")
print(f"{sequence(37)=}")


