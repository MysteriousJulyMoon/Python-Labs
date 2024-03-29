matrix = \
    [
[10, 20, 30],
[40, 50, 60],
[70, 80, 80]
    ]

det = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) - matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]) + matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])

if det == 0:
    print("The columns of the matrix are linearly dependent")
else:
    print("The columns of the matrix are not linearly dependent")

for i in matrix:
    print(i)