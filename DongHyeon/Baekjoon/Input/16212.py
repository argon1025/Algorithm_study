import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
for i in nums:
    print(i, end=" ")
