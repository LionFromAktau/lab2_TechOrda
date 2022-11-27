import math
a = input()
sum = 0
count = 0
for i in range(-1, -len(a) - 1, -1):
    if a[i] == '1':
        sum += math.pow(2, count)
    count+=1
print(int(sum))