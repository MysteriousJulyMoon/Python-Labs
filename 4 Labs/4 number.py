k = input("Enter the string: ").split()
m = ""
count = 0
for i in range(len(k)):
    for j in range(i):
        if k[i] == k[j]:
            count += 1
    m += str(count) + " "
    count = 0
print(m, sep = " ")