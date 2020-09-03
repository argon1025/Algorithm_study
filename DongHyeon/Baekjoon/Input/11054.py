n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
dp_re = [0] * n
res = []
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)


for i in range(n -1, -1, -1):
    dp_re[i] = 1
    for j in range(i, n):
        if a[j] < a[i]:
            dp_re[i] = max(dp_re[i], dp_re[j] + 1)

for i in range(n):
    res.append(dp[i] + dp_re[i] - 1)

print(max(res))