def moonbrellas_main():
    x_cost = [0]* 999
    y_cost = [0] * 999
    str_arg = [""] * 999
    test_cases = int(input())
    case_no = 1

    for i in range(test_cases):
        x, y, s = input().split()
        x_cost[i] = int(x)
        y_cost[i] = int(y)
        str_arg[i] = str(s)

        # insert "?" replacement function (call) here

    for i in range(test_cases):
        calculate_cost(x_cost[i], y_cost[i], str_arg[i],case_no)
        case_no+=1

def calculate_cost(x, y, s, case_no):
    x_count = 0
    y_count = 0
    for i in range(len(s) - 1):
        if s[i] == "C" and s[i + 1] == "J":
            x_count += 1
        elif s[i] == "J" and s[i + 1] == "C":
            y_count += 1
    cost = x_count * x + y_count * y
    print("Case #", case_no, ": ", cost)


moonbrellas_main()
