rows = int(input("Give me the number of rows >> "))
value = int(input("Give me the starting value >> "))

if value < 1:
    value = 1

triangle = []


for i, _ in enumerate(range(rows), start=1):
    row = []
    
    for _ in range(0, i):
        row.append(0)
    
    triangle.append(row)

triangle[0][0] = value

for row in triangle[1:]:
    row_length = len(row)
    pos_row = row_length -1
    
    for pos_col in range(row_length):
        
        pos_value = 0
        
        if pos_col == 0:
            pos_value += triangle[pos_row -1][0]
            
        elif pos_col == row_length -1:
            pos_value += triangle[pos_row -1][pos_col-1]
            
        else:
            pos_value += triangle[pos_row -1][pos_col-1]
            pos_value += triangle[pos_row -1][pos_col]
            
        triangle[pos_row][pos_col] = pos_value
        

# ChatGPT for the save to make the triangel
width = len(" ".join(map(str, triangle[-1])))

for row in triangle:
    line = " ".join(str(x) for x in row)
    print(line.center(width))

