n = int(input())

levels = input().split()

mode = ''
change = 0

for i in range(n-1):
    if change < 2:
        if int(levels[i+1]) > int(levels[i]):
            if mode != 'ghole':
                change += 1
                mode = 'ghole'
        elif int(levels[i+1]) < int(levels[i]):
            if mode != 'dare':
                change += 1
                mode = 'dare'
        elif int(levels[i+1]) == int(levels[i]):
            pass
    else:
        if int(levels[i+1]) > int(levels[i]):
            if mode != 'ghole':
                change += 1
                mode = 'ghole'
        elif int(levels[i+1]) < int(levels[i]):
            if mode != 'dare':
                change += 1
                mode = 'dare'
        elif int(levels[i+1]) == int(levels[i]):
            change += 1

if change <= 2:
    print('Yes')
else:
    print('No')