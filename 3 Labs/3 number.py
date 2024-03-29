nums_str = [
    "", "one", "two", "three", "four", "five", "six", "seven",
    "eight", "nine", "ten", "eleven", "twelve",
    "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"
]

tens_str = [
    "", "", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
]

hundreds_str = [
    "", "hundred", "two hundred", "three hundred", "four hundred", "five hundred",
    "six hundreds", "seven hundred", "eight hundred", "nine hundred"
]

num = int(input("Enter the number from 1 to 1000: "))

if num == 1000:
    print("thousand")
else:
    if num >= 100:
        print(hundreds_str[num // 100])
        num %= 100

    if num >= 20:
        print(tens_str[num // 10])
        num %= 10

    if num > 0:
        print(nums_str[num])