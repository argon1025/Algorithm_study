# 알고리즘
# 기본 입출력 문제
# boj.kr/2557, 1000, 2558, 10950, 10951, 10952, 10953, 11021, 11022, 11718, 11719, 11720/, 11721, 2741, 2742, /2739, /1924, /8393, /10818, /2438, /2439, /2440, /2441, /2442, /2445, /2522, 2446, 10991, 10992

star = ""
roop = int(input())
for i in range(1,roop):
    for s in range(i):
        star += "*"
    print(star.rjust(roop))
    star = ""
for i in range(roop):
    print("*",end='')
print("")
for i in range(roop-1,0,-1):
    for s in range(i):
        star += "*"
    print(star.rjust(roop))
    star = ""