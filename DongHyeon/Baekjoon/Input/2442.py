N = int(input())
star = '*'
null = ' '
A = 1
for i in range(N):
    print(null*(N-i-1) + star*(A))
    A += 2
