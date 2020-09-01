n = int(input())
mod = 10007
fibo = [1,3] + [0] * n

for i in range(2, n):
    fibo[i] = fibo[i-1] + fibo[i-2] *2
    fibo[i] %= mod
print(fibo[n-1])
