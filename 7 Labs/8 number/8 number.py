import numpy as np

arr = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])

nonzero_indices = np.nonzero(arr)[0]

print("Исходный массив:", arr)
print("Индексы ненулевых элементов:", nonzero_indices)