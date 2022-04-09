import itertools

def powerset(s):
  pset = set()
  for n in range(len(s) + 1):
    for sset in itertools.combinations(s, n):
      pset.add(sset)
  return pset



def travel(s):
    out = []
    out.append(s.replace(s[i],s[i]*2,2))
    return out

T = int(input())

for t in range(T):
    double_string = []
    s = input()
    s = str(s.upper())
    for i in range(len(s)):
        double_string.append(travel(s))
    double_string = sorted(double_string)
    first = str(double_string[0])
    temp_powerset = powerset(s)
    print(temp_powerset)
    print("Case #%d: %s" % (t + 1, first))