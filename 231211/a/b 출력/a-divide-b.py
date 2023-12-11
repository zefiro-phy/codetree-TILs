arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = a//b
d = a%b
print(c, end =".")
for _ in range(1,21):
    print(d*10//b, end="")
    d = d*10%b