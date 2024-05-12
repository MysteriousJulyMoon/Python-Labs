import numpy as np

# Загрузка файла iris.data из локальной директории
data = np.genfromtxt('iris.data.txt', delimiter=',', dtype='object')

# Получение уникальных значений и их количество в столбце 'species'
unique_species, counts = np.unique(data[:, 4], return_counts=True)

# Вывод уникальных значений и их количество
for species, count in zip(unique_species, counts):
    print(f'Species: {species}, Count: {count}')