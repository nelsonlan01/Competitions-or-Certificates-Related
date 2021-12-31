import random


def moonbrellas_main():
    x_cost = [0] * 999
    y_cost = [0] * 999
    str_arg = [""] * 999
    adjusted_cost = [0]*999
    test_cases = int(input())
    case_no = 1

    for i in range(test_cases):
        x, y, s = input().split()
        x_cost[i] = int(x)
        y_cost[i] = int(y)
        str_arg[i] = str(s)
        # insert "?" replacement function (call) here
        adjusted_cost[i] = replace_questionmark(x_cost[i], y_cost[i], str_arg[i])


    for i in range(test_cases):
        calculate_cost(x_cost[i], y_cost[i], str_arg[i], case_no, adjusted_cost[i])
        case_no += 1


def replace_questionmark(x, y, s):  # CJ?CC?  C?J
    adjusted_cost = 0
    cheaper = "y" if y < x else "x"
    for i in range(len(s)):  # CJ = x   JC = y
        if s[i] == "?":
            if s[0] == "?" and s[1] == "C":
                adjusted_cost += 0 # insert C
            if s[0] == "?" and s[1] == "J":
                adjusted_cost += 0  # insert J
            if s[len(s)-1] == "?" and s[len(s)-2] == "C":
                adjusted_cost += 0 # insert C
            if s[len(s)-1] == "?" and s[len(s)-2] == "J":
                adjusted_cost += 0  # insert J
            if i < len(s)-2:
              if s[i - 1] == "J" and s[i + 1] == "J":
                adjusted_cost += 0
              elif s[i - 1] == "C" and s[i + 1] == "C":
                adjusted_cost += 0
              elif s[i - 1] == "J" and s[i + 1] == "C":
                adjusted_cost += y   # insert C
              elif s[i - 1] == "C" and s[i + 1] == "J":
                adjusted_cost += x   # insert J

    return adjusted_cost


def calculate_cost(x, y, s, case_no, adjusted_cost):
    cost = 0 + adjusted_cost[i]
    for i in range(len(s) - 1):
        if s[i] == "C" and s[i + 1] == "J":
            cost += x
        elif s[i] == "J" and s[i + 1] == "C":
            cost += y
    print("Case #", case_no, ": ", cost)


moonbrellas_main()
