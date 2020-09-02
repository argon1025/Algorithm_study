N = int(input())
star = '*'
null = ' '
a = 0
for i in range(1, (2*N-1)+1):
    if N > i:
        print(star*(i) + null*(N*2-i*2) + star*(i))
    else:
        print(star*(i-a) + null*(a) + star*(i-a))
        a +=2
        