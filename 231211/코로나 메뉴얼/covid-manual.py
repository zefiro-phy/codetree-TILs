a =input().split()
b =input().split()
c =input().split()
a_t = int(a[1])
b_t = int(b[1])
c_t = int(c[1])
counting =0
if a[0] =="Y":
     if a_t >= 37:
        counting +=1
if b[0] =="Y":
    if b_t >= 37:
        counting +=1
if c[0] =="Y":
    if c_t >= 37:
        counting +=1

if counting >=2:
    print("E")
else:
    print("N")