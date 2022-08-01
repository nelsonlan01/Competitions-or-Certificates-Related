import math

T = int(input())

for t in range(T):
    mpv = 0
    regions, categories = input().split()
    regions = int(regions)
    categories = int(categories)
    regions_arg = input().split()
    regions_arg.sort()
    int_regions = [int(numeric_string) for numeric_string in regions_arg]

    if categories == 1:
        mpv = int_regions[(math.ceil(len(int_regions) / 2) - 1)]

    if categories > 1:
        fake_mpv = 0
        for i in range(len(int_regions)):
            fake_mpv = int_regions[i] + ((sum(int_regions) - int_regions[i]) / 2)
            if fake_mpv >= mpv:
                mpv = fake_mpv

    print("Case #%d: %.1f" % (t + 1, mpv))
