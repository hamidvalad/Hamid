#https://quera.ir/problemset/contest/91711/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AD%D8%B1%DB%8C%D8%B5%D8%A7%D9%86%D9%87-%D8%B4%D8%A7%D8%B1%DA%98%D8%B1-%D8%AA%D8%A8%D8%A7%D9%87

n, x, y = input().split()
phones = input().split()

charges = [int(phone) for phone in phones]

scr = min(charges)

charges.remove(scr)

for phone in charges:
    if phone < 100 and scr >= int(x):
        while phone < 100 and scr >= int(x):
            scr -= int(x)
            phone += int(y)
    if phone < 100 and scr < int(x):
        print('NO')
        break
else:
    print('YES')
    


