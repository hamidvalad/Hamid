#https://quera.ir/problemset/contest/26109/%D8%B3%D8%A4%D8%A7%D9%84-icpc

p1, s1 = input().split()

s2, p2 = input().split()

s1 = int(s1)
s2 = int(s2)
p1 = int(p1)
p2 = int(p2)

if p1 + p2 == s1 + s2:
    if p2 > s1:
        print('Persepolis')
    elif s1 > p2:
        print('Esteghlal')
    elif s1 == p2:
        print('Penalty')
elif p1 + p2 > s1 + s2:
    print('Persepolis')
elif s1 + s2 > p1 + p2:
    print('Esteghlal')