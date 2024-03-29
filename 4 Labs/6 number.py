from collections import Counter


def sort_words_by_frequency(text):
    # Разбиваем текст на слова, приводим к нижнему регистру и создаем счетчик
    words = text.lower().split()
    word_counts = Counter(words)

    # Сортируем слова сначала по убыванию количества появления, затем по алфавиту
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    # Выводим отсортированные слова
    for word, count in sorted_words:
        print(word)


# Ввод текста
text = input("Enter the text: ")

# Вызов функции и вывод отсортированных слов
sort_words_by_frequency(text)