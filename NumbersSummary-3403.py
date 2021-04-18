#https://quera.ir/problemset/contest/3403/%D8%B3%D8%A4%D8%A7%D9%84-%D8%B3%D8%A7%D8%AF%D9%87-%D8%AA%D8%B1

numbers = []

for i in range(4):
    numbers.append(int(input()))
    
print('Sum :',format(sum(numbers),'.6f'))
print('Average :',format(sum(numbers)/len(numbers),'.6f'))
prod = 1
for num in numbers: prod*= num
print('Product :',format(prod,'.6f'))
print('MAX :',format(max(numbers),'.6f'))
print('MIN :',format(min(numbers),'.6f'))
