# 알고리즘
# DP 문제
# boj.kr/ DP - 1463, 11726, 11727, 9095, 10844, 11057, 2193, 9465, 2156, 11053, 11055, 11722, 11054, 1912, 2579, 1699, 2133, 9461, 2225, 2011, 11052

#귀납법

N = int(input())
count = [0] * (N+1) # 0으로 구성된 배열 N+1 개를 생성

for value in range(2,N+1):
    count[value] = count[value-1] + 1 # 해당 인덱스에서 -1한 값의 계산횟수를 먼저 저장
    if value % 2 == 0 and count[value//2] < count[value]: # 인덱스가 2로 나누어 지고 -1한 계산횟수보다 적을때
        count[value] = count[value//2] + 1
    if value % 3 == 0 and count[value//3] < count[value]: # 인덱스가 3로 나누어 지고 -1한 계산횟수보다 적을때
        count[value] = count[value//3]+1
print(count[N])



