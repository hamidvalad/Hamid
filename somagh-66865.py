#https://quera.ir/problemset/university/66865/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B7-%D8%B3%D9%85%D8%A7%D9%82%D9%81%D8%A7%D8%B1%D9%85

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