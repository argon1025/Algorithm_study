# 알고리즘
# 기본 입출력 문제
# boj.kr/2557, 1000, 2558, 10950, 10951, 10952, 10953, 11021, 11022, 11718, 11719, 11720/, 11721, 2741, 2742, /2739, /1924, /8393, /10818, /2438, /2439, /2440, /2441, /2442, /2445, /2522, /2446, 10991, 10992

roop = int(input())

for i in range(roop,1,-1):
    for space in range(roop-i):
        print(" ",end='')
    for star in range(i*2-1):
        print("*",end='')
    print("")
for i in range(1,roop+1):
    for space in range(roop-i):
        print(" ",end='')
    for star in range(i*2-1):
        print("*",end='')
    print("")