test_case = int(input())
temp_stack = []
temp_int_stack = []
global world_stack
world_stack = []
output = []
case_sum = 0


def convert(stack):
    for j in range(len(stack)):
        temp_int_stack.append(int(stack[j]))
    return temp_int_stack


def scan_top_most_beauty():
    most_beauty = 0
    indices = 0
    for nth_stack in range(len(world_stack)):
        world_stack.sort(reverse=True)

        if world_stack[nth_stack] != []:
            if world_stack[nth_stack][0] >= most_beauty:
                most_beauty = world_stack[nth_stack][0]
                indices = nth_stack
                #indices = estimate_remain_disk()
    return indices
'''
def estimate_remain_disk():
    calc_0, calc_1 = 0
    for nth_stack in range(len(world_stack)):
        if nth_stack == len(world_stack):
            break
        if world_stack[nth_stack][0] == world_stack[nth_stack+1][0]:
            for x in range(len(world_stack[nth_stack])):
                calc_0 += world_stack[nth_stack][x]
            for y in range(len(world_stack[nth_stack+1])):
                calc_1 = world_stack[nth_stack+1][y]
        if calc_1 > calc_0:
            return nth_stack+1
        else:
            return nth_stack
'''
def take_disk(indices):
    temp = 0
    temp = world_stack[indices][0]
    world_stack[indices].pop(0)
    #print(world_stack)
    return temp

def initial():
    temp_stack.clear()
    world_stack.clear()


def print_result():
    for i in range (len(output)):
        print("Case #%d: %d" % (i + 1, output[i]))


for i in range(test_case):
    n, k, p = input().split()
    n, k, p = int(n), int(k), int(p)
    for n_stack in range(n):
        case_sum = 0
        temp_stack = convert(input().split())
        world_stack.append(temp_stack[:])
        temp_stack.clear()
    #print(world_stack)

    for take in range(p):
        case_sum += take_disk(scan_top_most_beauty())

    output.append(case_sum)
    initial()

print_result()
