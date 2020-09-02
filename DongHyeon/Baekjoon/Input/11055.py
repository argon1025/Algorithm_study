n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
ans = 0
for i in range(n):
    dp[i] += a[i]
    for j in range(i):
        if a[j] < a[i] and dp[i] < dp[j] + a[i]:
            dp[i] = dp[j] + a[i]
    ans = max(ans, dp[i])
print(ans)