
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