import collections


def convert_int_cake(cake):
    for i in range(len(cake)):
        int_cake.append(int(cake[i]))
    return int_cake


def buy_cake(de_cake):
    global flag
    bought = 0
    last_buy = 0
    same = False
    if len(de_cake) > 0:
        same = de_cake.count(de_cake[0]) == len(de_cake)
    if same == True:
        return len(de_cake)

    for i in range(len(de_cake)):
        if i == 0:
            flag = True
        if flag == True and de_cake[0] >= last_buy:
            last_buy = de_cake[0]
            de_cake.popleft()
            bought += 1
            flag = False
        elif de_cake[len(de_cake) - 1] >= last_buy:
            last_buy = de_cake[-1]
            de_cake.pop()
            bought += 1
            flag = True
    return bought


T = int(input())

for t in range(T):
    cake = input()
    cake = int(cake)
    cake_arg = []
    int_cake = []
    temp_cake = input().split()
    int_cake = convert_int_cake(temp_cake)
    de_cake = collections.deque([])
    for i in range(len(int_cake)):
        de_cake.append(int_cake[i])
    result = buy_cake(de_cake)

    print("Case #%d: %d" % (t + 1, result))
