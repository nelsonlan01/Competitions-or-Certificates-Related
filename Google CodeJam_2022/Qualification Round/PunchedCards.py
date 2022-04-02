patten_corner_plus = "..+-+-+-+-+-+-+-+-+-"
patten_corner_hole = "..|.|.|.|.|.|.|.|.|."
patten_plus = "+-+-+-+-+-+-+-+-+-+-"
patten_hole = "|.|.|.|.|.|.|.|.|.|."

T = int(input())

for t in range(T):
    r, c = input().split()
    r = int(r)
    c = int(c)
    double_r = r*2+1
    first_row_of_card = True
    result = []
    print("Case #%d:" % (t + 1))
    for i in range(double_r):
        if i == 0:
            print(patten_corner_plus[0:c*2]+"+")
        elif i == 1:
            print(patten_corner_hole[0:c*2] + "|")
        elif i % 2 == 0:
            print(patten_plus[0:c*2] + "+")
        elif i % 2 == 1:
            print(patten_hole[0:c*2] + "|")
