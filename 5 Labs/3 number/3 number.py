
# Создаем текстовый файл с данными о детях
with open('three_input.txt', 'w') as file:
    file.write('Иванов Иван 6\n')
    file.write('Петров Федор 4\n')
    file.write('Сидоров Артур 5\n')
    file.write('Морская Марина 3\n')
    file.write('Смирнова Ольга 2\n')
# Читаем данные из файла и находим самого старшего и самого младшего ребенка
with open('three_input.txt', 'r') as file:
    lines = file.readlines()
    max_age = 0
    min_age = 100
    oldest_child = ''
    youngest_child = ''
for line in lines:
    parts = line.split()
    age = int(parts[2])
    if age > max_age:
        max_age = age
        oldest_child = line
    if age < min_age:
        min_age = age
        youngest_child = line

# Записываем данные о самом старшем и самом младшем ребенке в отдельные файлы
with open('3_older_output.txt', 'w') as file:
    file.write(oldest_child)

with open('3_junior_output.txt', 'w') as file:
    file.write(youngest_child)