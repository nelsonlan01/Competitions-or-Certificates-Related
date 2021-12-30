import random


def moonbrellas():
    test_cases = input()

    x, y, s = input().split()
    x = int(x)
    y = int(y)
    s = str(s)
    s_i = [None]*1000
    x_count = 0
    y_count = 0
    print(s)
    for i in range(len(s)):
        if s[i] == "C":
            s_i[i] = 0
        elif s[i] == "J":
            s_i[i] == 1
        elif s[i] == "?":
            choose = "01"
            s_i[i] = random.choice(choose)


    for i in range(len(s)-1):
        if s[i] == "C" and s[i+1] == "J":
            x_count += 1
        elif s[i] == "J" and s[i+1] == "C":
            y_count += 1
    print(x_count,y_count)
    cost = x_count * x + y_count * y
    print("cost ==> ", cost)


moonbrellas()

