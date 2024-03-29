def is_subset(set1, set2):
    return set1.issubset(set2)

# Ввод двух множеств чисел
set1 = set(map(int, input("Enter the elements of the first set separated by a space: ").split()))
set2 = set(map(int, input("Enter the elements of the second set separated by a space: ").split()))

# Проверка, является ли set1 подмножеством set2
result = is_subset(set1, set2)

# Вывод результата
print(result)