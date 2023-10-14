#####Sample Passed

T = int(input())
s = "!ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for t in range(T):
    deducted = 0
    break_out_flag = False
    n = int(input())
    while n >= 27:
        if n>=27:
            deducted += 1
            n -= 26

    if (n <= 26 and deducted == 0):
        char = s[n]


    if (n <= 26 and deducted >=1):
        for x in range(1, 27):
            for y in range(0, deducted+1):
                n -= 1
                if n == 0:
                    char = s[x]
                    break_out_flag = True
                    break
                if break_out_flag:
                    break


    print("Case #%d: %s" % (t + 1, char))


    '''
    'A' on position: 

    1
    27 28
    77 78 79
    155 156 157 158
    '''
