import numpy as np

def run_length_encoding(x):
    # Инициализируем переменные для хранения уникальных элементов и их длин серий
    unique_elements = []
    series_lengths = []

    current_element = x[0]
    current_length = 1

    # Проходим по элементам вектора x для выполнения кодирования
    for i in range(1, len(x)):
        if x[i] == current_element:
            current_length += 1
        else:
            unique_elements.append(current_element)
            series_lengths.append(current_length)
            current_element = x[i]
            current_length = 1

    # Добавляем информацию о последней серии элементов
    unique_elements.append(current_element)
    series_lengths.append(current_length)

    return np.array(unique_elements), np.array(series_lengths)

# Заданный вектор x
x = np.array([2, 2, 2, 3, 3, 3, 5])

# Кодируем длины серий вектора x
encoded_values, series_lengths = run_length_encoding(x)

print("Результат кодирования длин серий:")
print("Unique elements:", encoded_values)
print("Series lengths:", series_lengths)