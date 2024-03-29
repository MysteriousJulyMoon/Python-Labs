
text = input()   # вводим строку
first = text[0]
count = 0           # заводим счетчик
result = ''
for letter in text:
   if letter == first:   # если символ совпадает с уже сохраненным,
        count += 1     # то увеличиваем счетчик
   else:
        result += first + str(count)   # иначе - записываем в результат
        first = letter                   # обновляем сохраненный символ с его счетчиком
        count = 1
result += first + str(count)          # добавляем в результат последний символ
print(result)