T = int(input())

for t in range(T):
    bag, kids = input().split()
    bag = int(bag)
    kids = int(kids)
    candy_tray = []
    candy_tray = input().split()
    candy = 0
    for i in range(bag):
        candy += int(candy_tray[i])
    print("Case #%d: %d" % (t + 1, (candy % kids)))


