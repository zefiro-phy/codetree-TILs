while True:
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])
    print(a*b)
    if arr[2] == "C":
        break