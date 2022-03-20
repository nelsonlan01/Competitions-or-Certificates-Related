def check_div_9(new_num):
    if new_num % 9 == 0:
        return True
    return False

def clear_queue():
    queue9.clear()
    sorted_queue.clear()

queue9 = []
sorted_queue = []

T = int(input())

for t in range(T):
    num = input()
    for pre in range(0,10):
        new_num_max = int(str(num) + str(pre))  #add to rear
        if (check_div_9(new_num_max)) == True:
            queue9.append(new_num_max)
        new_num_min = int(str(pre) + str(num))  #add to front
        if (check_div_9(new_num_min)) == True:
            queue9.append(new_num_min)
    sorted_queue = sorted(queue9)
    print("Case #%d: %d" % (t + 1, sorted_queue[0]))
    clear_queue()
