T = int(input())

for t in range(T):
    ans = 0
    n = int(input())
    if n <= 3:
        ans = 1
    if n >= 4:
        ans = (n/2)-1
    print("Case #%d: %d" % (t + 1, ans))