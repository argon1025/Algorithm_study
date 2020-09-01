n = int(input())
mod = 10007
fibo = [1,2] + (n-1)*[0]

for i in range(2,n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
    fibo[i] %= mod
print(fibo)
print(fibo[n-1])

# def fibo(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return fibo(n-1) + fibo(n-2)