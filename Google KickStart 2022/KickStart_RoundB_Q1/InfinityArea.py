import math

T = int(input())

for t in range(T):
    r, a, b = input().split()
    r = int(r)
    a = int(a)
    b = int(b)
    result = 0.0
    accumulate = 0.0
    draw_left_circle = r * a
    temp = []
    temp.append(r)  # initial radius
    temp.append(draw_left_circle)
    flag = True
    temp_cal = math.floor(draw_left_circle / b)
    while flag == True:
        if temp_cal == 0:
            break
        if draw_left_circle <= b:
            temp.append(draw_left_circle)
            flag = False
            break
        elif temp_cal > 0:
            temp.append(temp_cal) # draw right
            draw_left_circle = temp_cal * 2
    for i in range(len(temp)):
        accumulate += math.pi * temp[i] * temp[i]

    print("Case #%d: %f" % ((t + 1), accumulate))
