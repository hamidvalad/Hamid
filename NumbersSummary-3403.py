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
