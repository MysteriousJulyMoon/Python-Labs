import numpy as np

# Генерация массива случайных чисел нормального распределения размера 10х4
arr = np.random.randn(10, 4)

# Нахождение минимального значения
min_value = np.min(arr)

# Нахождение максимального значения
max_value = np.max(arr)

# Нахождение среднего значения
mean_value = np.mean(arr)

# Нахождение стандартного отклонения
std_deviation = np.std(arr)

# Сохранение первых 5 строк в отдельную переменную
first_five_rows = arr[:5, :]

print("Сгенерированный массив:")
print(arr)
print("\nМинимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Среднее значение:", mean_value)
print("Стандартное отклонение:", std_deviation)
print("\nПервые 5 строк:")
print(first_five_rows)