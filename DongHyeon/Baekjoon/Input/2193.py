n = int(input())
pinaryNum = [0,1,1,2] + [0] * n

for i in range(2, n+1):
    pinaryNum[i] = pinaryNum[i-1] + pinaryNum[i-2]
print(pinaryNum[n])
