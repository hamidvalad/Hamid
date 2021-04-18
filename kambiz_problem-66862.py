#https://quera.ir/problemset/university/66862/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B7-%D9%85%D8%B5%D8%A7%D8%A6%D8%A8-%DA%A9%D8%A7%D9%85%D8%A8%DB%8C%D8%B2

k = input()

import itertools

nums = [i for i in range(1,len(k))]

res = set()
count = 0

def good_part(part):
    if int(part) > 255 or int(part) < 0:
        return False
    if part.startswith('0') and part != '0':
        return False
    return True

for pos in itertools.combinations(nums,3):
    a = pos[0]
    b = pos[1]
    c = pos[2]
    parts = [k[:a], k[a:b], k[b:c], k[c:]]
    good = 0
    for part in parts:
        if good_part(part):
            good += 1
    if good == 4:
        item = '.'.join(parts)
        res.add(item)

for ip in res:
    print(ip)