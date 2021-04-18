p, d = input().split()

p = int(p)
d = int(d)
i = 1
while True:
    if i*d % p <= p/2:
        print(i*d)
        break
    i+=1