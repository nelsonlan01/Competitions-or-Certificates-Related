def get_ruler(kingdom):
    vowel = ['a', 'e', 'i', 'o', 'u']
    ruler = ""
    if kingdom[-1] == "y":
        ruler = "nobody"
    elif kingdom[-1] in vowel:
        ruler = "Alice"
    else:
        ruler = "Bob"
    return ruler

T = int(input())

for t in range(T):
    kingdom = input()
    king1 = kingdom[0].capitalize()
    king2 = kingdom[1:].lower()
    kingdom = ''
    kingdom = king1+king2
    print("Case #%d: %s is ruled by %s." % (t + 1, kingdom, get_ruler(kingdom)))
