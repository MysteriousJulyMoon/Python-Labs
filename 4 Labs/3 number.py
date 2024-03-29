s = int(input("Enter the max number: "))
n = " "
for a in range(s):
    a = input("Enter the city: ").title()
    if a in n:
        print("REPEAT")
    else:
        print("OK")
    n += a

