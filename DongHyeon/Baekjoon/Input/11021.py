import sys
T = int(sys.stdin.readline())
for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1}".format(i, a+b))