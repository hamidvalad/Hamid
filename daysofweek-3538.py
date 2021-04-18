#https://quera.ir/problemset/contest/3538/%D8%B3%D8%A4%D8%A7%D9%84-%D8%A2%D8%AE-%D8%AC%D9%88%D9%86-%D8%B7%D8%B1%D9%81-%D9%86%DB%8C%D8%B3%D8%AA

total_days = {'shanbe' ,'1shanbe','2shanbe','3shanbe','4shanbe','5shanbe','jome'}
full = set()

for i in range(1,7):
    if i % 2 == 1:
        n = int(input())
    else:
        days = input()
        lst = days.split()
        for item in lst:
            full.add(item)

print(len(total_days-full))