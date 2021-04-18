#https://quera.ir/problemset/contest/8838/%D8%B3%D8%A4%D8%A7%D9%84-%DA%A9%D9%85%DA%A9-%D8%A8%D9%87-%DA%A9%D8%A7%D9%BE%DB%8C

n, s = input().split()

res = ''
for _ in range(int(n)):
    res += 'copy of '

print(res+s)