length = int(input("What is the length of the square >> "))
width = int(input("What is the width of the square >> "))

print(f"The area of a {"square" if length == width else "rectangle"} with the sides '{length}' and '{width}' is '{length * width}'.")