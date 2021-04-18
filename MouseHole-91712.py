x , y = input().split()

if int(y) > int(x):
    print('R'*(int(y)-int(x)))
elif int(x) > int(y):
    print('L'*(int(x)-int(y)))
elif x == y:
    print('Saal Noo Mobarak!')
