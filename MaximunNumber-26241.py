m, s = input().split()

m = int(m)
s = int(s)


minimum = ''

def get_min(m,s):
    global minimum
    if s < 1:
        minimum = -1
    else:
        number_of_9 = s//9
        if number_of_9 == m:
            minimum = number_of_9*'9' 
        elif s <= 9:
            if m > 1:
                minimum = '1' + (m-2)*'0' + str(s-1) + minimum
            else:
                minimum = str(s) + minimum
        else:
            minimum = '9' + minimum
            get_min(m-1,s-9)

if s > m*9 or s == 0:
    print(-1, -1)

else:
    number_of_9 = s//9
    number_of_other = m - s//9
    maximum = number_of_9*'9'
    if number_of_other > 1:
        maximum += str(s%9) + (m - s//9 -1)*'0'
    elif number_of_other == 1:
        maximum += str(s%9)
    
    get_min(m,s)
    
    print(minimum, maximum)