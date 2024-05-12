
# Считываем матрицу из файла
with open('input.txt', 'r') as file:
    matrix = []
    for line in file:
        row = list(map(int, line.strip().split(',')))
        matrix.append(row)

# Находим сумму всех элементов
sum_matrix = sum(sum(row) for row in matrix)

# Находим максимальный и минимальный элементы
flattened_matrix = [element for row in matrix for element in row]
max_element = max(flattened_matrix)
min_element = min(flattened_matrix)

print(f"Matrix:")
for row in matrix:
    print(row)

print(f"The sum of all the elements: {sum_matrix}")  #Сумма всех элементов
print(f"Maximum element: {max_element}")       #Максимальный элемент
print(f"Minimum element: {min_element}")        #Минимальный элемент