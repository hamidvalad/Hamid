t, w = input().split()

res = 0

for i in range(int(w)):
    res += 1*(0.5**i)    

print(format(int(t)/res, '.4f'))