import math


def calculate_lhs(n_intergers):
    sum_of_lhs = 0
    for i in range(len(n_intergers)):
        sum_of_lhs += n_intergers[i]
    return pow(sum_of_lhs, 2)


def calculate_rhs(n_intergers):
    sum_of_rhs = 0
    for i in range(len(n_intergers)):
        sum_of_rhs += pow(n_intergers[i], 2)
    return sum_of_rhs


def try_number(n_intergers, lhs, rhs, k):
    inside_l = lhs
    inside_r = rhs

    sqr_of_diff = math.floor(math.sqrt((abs(lhs - rhs))))
    #print(sqr_of_diff)

    if sqr_of_diff == 0:
        return -1000000000000000000

    result = "IMPOSSIBLE"
    for K in range(1, int(k) + 1):
        for loop in range(1, pow(sqr_of_diff,2)):
            n_intergers[-1 + K] = loop
            inside_l = calculate_lhs(n_intergers)
            inside_r = calculate_rhs(n_intergers)
            if inside_l == inside_r:
                result = loop
                break
    return str(result)


def convert_int(temp_intergers, k):
    #if len(temp_intergers) == 1 and temp_intergers[0] != '0':
    for i in range(int(k)):
        n_intergers.append(1)

    for i in range(len(temp_intergers)):
        n_intergers.append(int(temp_intergers[i]))
    #print(n_intergers)
    return n_intergers


T = int(input())

for t in range(T):
    n, k = input().split()
    # n = the number of elements of the initial list and
    # k = the maximum number of elements you may add
    temp_intergers = []
    temp_intergers = input().split()
    n_intergers = []
    n_intergers = convert_int(temp_intergers, k)
    lhs = calculate_lhs(n_intergers)
    rhs = calculate_rhs(n_intergers)
    #print(lhs, rhs)
    result = try_number(n_intergers, lhs, rhs, k)
    print("Case #%d: %s " % (t + 1, result))
