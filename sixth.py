import math
a, b = input().split(" ")
a = float(a)
b = int(b)
r = math.pow(a, b)
if(r.is_integer()):
    print(int(r))
else:
    print(r)