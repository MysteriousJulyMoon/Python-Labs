with open("two_input.txt", "r") as f:
    a = f.read().splitlines()
    a.sort(key=lambda x: sum(map(int, x)))
with open("two_output.txt", "w") as w:
    for num in a:
        w.write(str(num) + "\n")

