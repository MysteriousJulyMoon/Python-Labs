import numpy as np

# Создаем двумерный массив а
a = np.arange(16).reshape(4, 4)
print("Исходный массив a:")
print(a)

# Меняем местами строки 1 и 3
a[1], a[3] = a[3], a[1].copy()

print("\nМассив a после замены строк 1 и 3:")
print(a)