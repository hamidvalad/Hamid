#https://quera.ir/problemset/contest/3432/%D8%B3%D8%A4%D8%A7%D9%84-%D9%87%D9%85%DA%A9%D8%A7%D8%B1%DB%8C-%D9%BE%D8%B1-%D8%AF%D8%B1%D8%AF%D8%B3%D8%B1

n, m = input().split()

mj = set(input().split())

ms = set(input().split())

if mj == ms:
    print('Both')
elif mj < ms:
    print('Mohammad Javad')
elif mj > ms:
    print('Mostafa')
else:
    print('None')