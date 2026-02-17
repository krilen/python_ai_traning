weeks = int(input("Number of weeks >> "))
days = int(input("Number of days >> "))
hours = int(input("Number of hours >> "))

total_hours = (weeks * 7 * 24) + (days * 24) + hours

print()
print(f"That is a total of '{total_hours}' hours.")
print(f"That is a total of '{total_hours / 24:.1f}' days.")
print(f"That is a total of '{total_hours / (24*7):.1f}' weeks.")
print(f"That is a total of '{total_hours / (24 *365.25):.2f}' years.")