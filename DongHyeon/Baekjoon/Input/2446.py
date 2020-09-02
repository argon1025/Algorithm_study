import sys
N = int(sys.stdin.readline())
a = '*'
b = ' '
T = 2*(N-1)
j = 0
for i in range(T+1):
    if i <= T-N+1:
        print('%s%s' % (b*i, a*((N*2)-(i*2)-1)))
    elif i > T-N+1:
        j = j+2
        print('%s%s' % (b*(T-i), a*(j+1)))

