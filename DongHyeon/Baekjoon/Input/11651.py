import sys
n = int(sys.stdin.readline())
location = []
for i in range(n):
    x, y = map(int,sys.stdin.readline().split())
    location.append([x,y])
location = sorted(location, key=lambda x:(x[1], x[0]))
for i in location:
    print(i[0], i[1])