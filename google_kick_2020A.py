house = [0] * 99999

test_case = int(input())
bought_house = 0

for i in range(test_case):
    n, b = input().split()
    n = int(n)
    b = int(b)
    nth_house_price = input().split()
    nth_house_price.sort()
    print(nth_house_price)
    while b >= nth_house_price[0] :
        bought_house += 1
        nth_house_price.pop(0)
    print(nth_house_price)
