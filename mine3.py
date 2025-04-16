import random

n = random.randint(0, 255)

for x in range(n):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    znamenko = random.randint(1, 2)
    znamenko_1 = random.randint(3, 4)

    if znamenko == 1:
        print(f"{a} * {b} = {a*b}")
    else:
        print(f"{a} / {b} = {a/b}")
    if znamenko_1 == 3:
        print(f"{a} + {b} = {a+b}")
    else:
        print(f"{a} - {b} = {a-b}")