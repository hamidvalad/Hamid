#https://quera.ir/problemset/contest/91713/%D8%B3%D8%A4%D8%A7%D9%84-%D9%BE%DB%8C%D8%A7%D8%AF%D9%87-%D8%B3%D8%A7%D8%B2%DB%8C-%D8%B4%D9%85%D8%A7%D8%B1%D9%87-%D8%B1%D9%86%D8%AF

itr = int(input())

result = []
for i in range(itr):
    number = input()
    if number[::-1] == number:
        result.append('Ronde!')
    else:
        for i in number:
            if number.count(i) >= 4:
                result.append('Ronde!')
                break
            index = number.index(i)
            if number[index:index+3] == i*3:
                result.append('Ronde!')
                break
        else:
            result.append('Rond Nist')

for res in result:
    print(res)