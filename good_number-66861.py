k = int(input())

i = 1
num = 0

while True:
    num += i
    i += 1
    count = 1
    for d in range(1, num):
        if num % d == 0:
            count += 1
    if count >= k:
        print(num)
        break