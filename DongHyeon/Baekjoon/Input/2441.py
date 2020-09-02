N = int(input())
star = '*'
null = ' '
for i in range(N):
    print(null*i + star*(N-i))