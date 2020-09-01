import sys
N = int(sys.stdin.readline())
meet = []
ans = 0
tmp = 0

for i in range(N):
    A, B = map(int,sys.stdin.readline().split())
    meet.append((A, B))

meet_s = sorted(meet, key=lambda x:x[1])
print(meet_s)
for i in meet_s:
    if tmp <= i[0]:

        ans += 1
        tmp = i[1]

print(ans)