#https://quera.ir/problemset/contest/91712/%D8%B3%D8%A4%D8%A7%D9%84-%D9%BE%DB%8C%D8%A7%D8%AF%D9%87-%D8%B3%D8%A7%D8%B2%DB%8C-%D8%B3%D9%88%D8%B1%D8%A7%D8%AE-%D9%85%D9%88%D8%B4

x , y = input().split()

if int(y) > int(x):
    print('R'*(int(y)-int(x)))
elif int(x) > int(y):
    print('L'*(int(x)-int(y)))
elif x == y:
    print('Saal Noo Mobarak!')
