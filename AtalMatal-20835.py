#https://quera.ir/problemset/contest/69899/%D8%B3%D8%A4%D8%A7%D9%84-%D9%BE%DB%8C%D8%A7%D8%AF%D9%87-%D8%B3%D8%A7%D8%B2%DB%8C-%D8%A7%D8%AA%D9%84-%D9%85%D8%AA%D9%84-%D8%AA%D9%88%D8%AA%D9%88%D9%84%D9%87

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