import sys
m, n = map(int,sys.stdin.readline().split())

# 소수 구하는 함수 
# m이상 n이하의 소수를 구한다.
def prime(m, n):
    nums = [False, False] + (n-1)*[True]
    primes = []
    for i in range(2, n+1):
        if nums[i]:
            # 만약 해당 소수가 m이상일 경우 출력
            if i >= m:
                print(i)
            for j in range(2*i, n+1, i):
                nums[j] = False

# 함수 실행
prime(m,n)


