res=[]
for n in range(1,1000):
    x=bin(n) [2:]
    if n % 2 != 0:
        x = x+"11"
    else:
        x = x+"00"
    r = int(x,2)
    if r > 177:
        res.append(r)
print(min(res))
