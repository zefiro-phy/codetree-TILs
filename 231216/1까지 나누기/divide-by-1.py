n = int(input())
for i in range(1,n+1):
    if n/i > 1:
        n /= i
    else:
        break
print(i)