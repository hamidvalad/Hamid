a = int(input())
b = int(input())

if b >= a:
    print('wrong order!')
elif (a-b)%2 != 0:
    print('wrong difference!')
else:
    width = int((a-b)/2)
    for i in range(width):
        print(a*'* ')
    for i in range(b):
        print(width*'* ' + b*'  ' + width*'* ')    
    for i in range(width):
        print(a*'* ')