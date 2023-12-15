a = int(input())
for i in range(a+1):
    if (a%2 == 0) and (a%4 != 0):
        continue
    if (a//8)%2 == 0:
        continue
    if a%7 <4:
        continue
    print(i)