m = int(input())
n = int(input())

# 소수 구하는 함수
def prime(n):
    nums = [False, False] + (n-1)*[True]
    primes = []
    for i in range(2, n+1):
        if nums[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                nums[j] = False
    return primes

# n까지의 소수 구하기
A = prime(n)
answer = []

# m이상 n이하의 자연수 중 소수 구하기
for i in range(m,n+1):
    if i in A:
        answer.append(i)

# 만약 m이상 n이하의 자연수 중 소수가 없을 경우 -1
if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)
