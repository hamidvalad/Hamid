'''print 2 lozenge with size of n'''

n = int(input())

space = int((n-1)/2)

for i in range(space+1):
    print((space-i)*' ' + (2*i+1)*'*' + (2*(space-i))*' ' + (2*i+1)*'*' + (space-i)*' ')

for i in range(space)[::-1]:
    print((space-i)*' ' + (2*i+1)*'*' + (2*(space-i))*' ' + (2*i+1)*'*' + (space-i)*' ')