T = int(input())


for t in range(T):
    counter = 0
    i = input()   # need to input
    p = input()   # she typed
    i_ascii = []
    p_ascii = []
    for character in i:
        i_ascii.append(ord(character))
    for character in p:
        p_ascii.append(ord(character))
    print(i_ascii)
    print(p_ascii)
    for character_i in range(len(i)):
        p_ascii.remove(ord(i[character_i]))
    print("Case #%d: %d" % (t + 1, len(p_ascii)))
