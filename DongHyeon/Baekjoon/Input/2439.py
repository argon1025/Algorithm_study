import sys
star = '*'
null = ' '
N = int(sys.stdin.readline())
for i in range(1, N+1):
    print('%s%s' % (null*(N-i), star*i))