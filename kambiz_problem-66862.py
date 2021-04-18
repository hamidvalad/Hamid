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