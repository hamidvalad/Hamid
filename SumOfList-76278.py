#https://quera.ir/problemset/technology/76278/%D8%B3%D8%A4%D8%A7%D9%84-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D8%A7%D9%85%D8%AA%D8%A7%DB%8C%DB%8C%D9%87%D8%A7

def calculator(n, m, li):
    res = []
    for i in range((n//m)+1):
        res.append(sum(li[i*m:i*m+m]))
    total = 0
    for i in range(1,len(res)+1):
        total += (-1)**(i+1)*res[i-1]
    return total
