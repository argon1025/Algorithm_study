import sys
while True:
    A, B = map(int, sys.stdin.readline().split())
    if A+B != 0:
        print(A+B)
    else:
        break