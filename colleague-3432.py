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