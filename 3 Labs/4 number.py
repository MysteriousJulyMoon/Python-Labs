def count_string_occurrences(strings):
    occurrences = {}
    for string in strings:
        if string in occurrences:
            occurrences[string] += 1
        else:
            occurrences[string] = 1

    return occurrences

# Пример списка строк
strings = ["apple", "orange", "apple", "grape", "orange", "apple"]

# Получаем словарь с количеством повторений каждой строки
occurrences = count_string_occurrences(strings)

# Выводим количество повторений каждой строки
for string, count in occurrences.items():
    print(count)
