import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
min = num[0]
max = num[0]
for i in range(N):
    if num[i] > max:
        max = num[i]
    if num[i] < min:
        min = num[i]
print(min, max)