house = []
global int_house
int_house= []
test_case = int(input())
global bought
bought = 0
bought_arg = []

def convert_house(house):
    for i in range(len(house)):
        int_house.append(int(house[i]))
    return int_house

def initial_var():
    int_house.clear()
    nth_house_price.clear()

def print_result():
    for i in range(len(bought_arg)):
        print("Case #",i+1,":",bought_arg[i])
        
for i in range(test_case):
    n, b = input().split()
    n = int(n)
    b = int(b)
    nth_house_price = input().split()
    nth_house_price.sort()
    int_house = convert_house(nth_house_price)
    bought = 0
    while b >= int_house[0]:
        bought += 1
        b -= int_house[0]
        int_house.pop(0)
    bought_arg.append(bought)
    initial_var()
print_result()
    
