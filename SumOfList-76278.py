def calculator(n, m, li):
    res = []
    for i in range((n//m)+1):
        res.append(sum(li[i*m:i*m+m]))
    total = 0
    for i in range(1,len(res)+1):
        total += (-1)**(i+1)*res[i-1]
    return total
