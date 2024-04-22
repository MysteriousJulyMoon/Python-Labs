def numbers_in_string(input_string):
    numbers = [int(num) for num in input_string.split() if num.isdigit()]
    result = 1
    for number in numbers:
        result *= number
    return result

with open('input.txt') as f:
    result = 1
    for line in f:           # перебирает строки в файле
        result *= numbers_in_string(line)      #накапливаем произведение чисел

with open("output.txt", "w") as file:
    file.write(str(result))


