# View matris
def print_matrix(m):
    
    for row in m:
        for n in row:
            print(n, " ", end="", sep="")
            
        print()

# [[1,2,3], [4,5,6], [7,8,9]]
# [[7,4,1], [8,5,2], [9,6,3]]

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print_matrix(matrix)

# Spin 90 degree
for col in range(0, 3):
    new_row = []
    
    for row in range(2, -1, -1):
        
        new_row.append(matrix[row][col])
        
    matrix.append(new_row)

matrix.pop(0)
matrix.pop(0)
matrix.pop(0)

print()
print_matrix(matrix)