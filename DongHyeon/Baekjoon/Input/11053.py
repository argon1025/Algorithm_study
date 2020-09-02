A = int(input())
seq = list(map(int,input().split()))

ans = [1]*A

for i in range(1,A):
    for j in range(i):
        if seq[j] < seq[i]:
            ans[i] = max(ans[i], ans[j]+1)
print(max(ans))        