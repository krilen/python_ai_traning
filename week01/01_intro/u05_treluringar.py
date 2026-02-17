# Simplest way :)
def order(*nums):
    _nums = list(nums)
    _nums.sort(reverse=True)
    
    return ", ".join(map(str, _nums))

print("Skriv in tre heltal!")

num1 = int(input("Skriv tal 1 >> "))
num2 = int(input("Skriv tal 2 >> "))
num3 = int(input("Skriv tal 3 >> "))

print()

print(f"Att '{num1}' är större än '{num2}' är '{num1>num2}'")
print(f"Att '{num2}' är större än '{num3}' är '{num2>num3}'")
print(f"Att '{num3}' är större än '{num1}' är '{num3>num1}'")

print()

print(f"Medelvärdet av '{num1}', '{num2}' och '{num3}' är '{(num1+num2+num3)//3}'")

print()

print(f"Nummer sorterade: '{order(num1, num2, num3)}'")

print()

if num1 < 0 or num2 < 0 or num3 < 0:
    print("Ett av talen var mindre än 0")

print()
    
if num1 == num2 == num3:
    print("Alla talen var lika")

elif num1 == num2:
    print(f"Tal 1 och tal 2 var lika, '{num1}'")
    
elif num1 == num3:
    print(f"Tal 1 och tal 3 var lika, '{num1}'")

elif num2 == num3:
    print(f"Tal 2 och tal 3 var lika, '{num2}'")