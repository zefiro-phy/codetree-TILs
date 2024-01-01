cnt = 1
for i in range(1,20):
    for j in range(1,20):
        print(f"{i} * {j} = {i*j}", end = " ")
        if cnt % 2 == 1 and j < 19:
            print("/", end=" ")
            cnt += 1
        else:
            print()
            cnt -= 1
    cnt =1