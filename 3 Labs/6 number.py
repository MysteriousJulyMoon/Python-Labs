words = input("Enter the words to create an abbreviation: ")
words_list = words.split()

abbreviation = ""
for word in words_list:
    abbreviation += word[0].upper()

print("Abbreviation:", abbreviation)