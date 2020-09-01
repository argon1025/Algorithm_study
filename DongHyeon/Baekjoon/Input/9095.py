T = int(input())
sum_123 = [0,1,2,4] + [0] * 7

for i in range(4, 11):
    sum_123[i] = sum_123[i-1] + sum_123[i-2] + sum_123[i-3]

for i in range(T):
    n = int(input())
    print(sum_123[n])