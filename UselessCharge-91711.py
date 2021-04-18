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
    


