n, k = input().split()
n = int(n)
k = int(k)

legs = []
for i in range(1,n+1):
    legs.append(i)
    legs.append(i)
    
index = 0

while True:

    for i in range(k):
        print(legs[index%len(legs)], end=' ')
        index += 1
    print()
    legs.pop((index-1)%len(legs))
    index -= 1
    index = index%(len(legs)+1)

    if len(legs) <= 2:
        if legs.count(legs[0]) > 1:
            print('winner:',end='')
            print(legs[0])
            break
        elif len(legs) == 1:
            print('winner:',end='')
            print(legs[0])
            break