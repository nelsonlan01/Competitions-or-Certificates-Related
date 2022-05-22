import re
def final_check(old_pw, Upper, Lower, Digit, Special, char_7):
    new_pw = old_pw
    if (Upper == False):
        new_pw+="A"
    if (Lower == False):
        new_pw+="a"
    if (Digit == False):
        new_pw+="1"
    if (Special == False):
        new_pw+="@"

    char_7 = len(new_pw)
    for x in range(char_7 , 7):
        new_pw+="1"
    return new_pw

T = int(input())

for t in range(T):
    length = int(input())
    old_pw = input()
    old_pw = str(old_pw)

    char_7 = len(old_pw)
    Upper = False
    Lower = False
    Digit = False
    Special = False

    special_list =  re.compile('["#", "@", "*", "&"]')
    lower_List = re.compile('["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]')
    upper_List = re.compile('["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]')
    digit_List = re.compile('["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]')

    if (special_list.search(old_pw) != None):
        #print("String contains specialed")
        Special = True
    if (lower_List.search(old_pw) != None):
        #    print("String contains lower")
            Lower = True
    if (upper_List.search(old_pw) != None):
        #    print("String contains upper")
            Upper = True
    if (digit_List.search(old_pw) != None):
        #   print("String contains dight")
            Digit = True

    new_pw = final_check(old_pw, Upper, Lower, Digit, Special, char_7)

    print("Case #%d: %s " % (t + 1, new_pw))
