#https://quera.ir/problemset/contest/6581/%D8%B3%D8%A4%D8%A7%D9%84-%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C%D8%A7%D8%AA-%D8%B5%D8%AF%D9%81-%D9%81%D9%84%D8%B2%DB%8C

t, w = input().split()

res = 0

for i in range(int(w)):
    res += 1*(0.5**i)    

print(format(int(t)/res, '.4f'))