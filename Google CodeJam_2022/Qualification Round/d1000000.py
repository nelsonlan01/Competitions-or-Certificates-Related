def convert_int_dice(dice):
    for i in range(len(dice)):
        int_dice.append(int(dice[i]))
    return int_dice

def check_straight(int_dice):
    if len(int_dice) == 1:
        return 1
    straight = 1
    for i in range(len(int_dice)):
        if int_dice[i] >= straight:
            int_dice[i] = straight
            straight += 1
        elif int_dice[i] < straight:
            continue
    int_dice = list(set(int_dice))
    return len(int_dice)

T = int(input())

for t in range(T):
    n = input()
    n = int(n)
    dice = []*n
    int_dice = []*n
    temp_dice = input().split()
    int_dice = convert_int_dice(sorted(temp_dice, key=int))
    print("Case #%d: %d" % (t + 1, check_straight(int_dice)))
