n = int(input())
cnt = 1
for i in range(1,n+1):
    if n/i > 1:
        n /= i
        cnt +=1
    else:
        break
print(cnt+1)