# 알고리즘
# 기본 입출력 문제
# boj.kr/2557, 1000, 2558, 10950, 10951, 10952, 10953, 11021, 11022, 11718, 11719, 11720/, 11721, 2741, 2742, /2739, /1924, /8393, /10818, 2438, 2439, 2440, 2441, 2442, 2445, 2522, 2446, 10991, 10992

roop = int(input())
value = list(map(int, input().split(" ")))
first = value[0]
Last = value[0]
for i in range(roop):
    if first < value[i]:
        first = value[i]
    else:
        if Last > value[i]:
            Last = value[i]
print("{0} {1}".format(Last,first))



# min max 함수 사용시 빠르게 가능
