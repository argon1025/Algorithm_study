N = int(input())

print(' '*(N-1)+'*')
for i in range(2, N):
    print(' '*(N-i) + '*' + ' '*(i*2-3) + '*')

if N != 1:
    print('*'*(N*2-1))