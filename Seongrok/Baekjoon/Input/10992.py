# 알고리즘
# 기본 입출력 문제
# boj.kr/2557, 1000, 2558, 10950, 10951, 10952, 10953, 11021, 11022, 11718, 11719, 11720/, 11721, 2741, 2742, /2739, /1924, /8393, /10818, /2438, /2439, /2440, /2441, /2442, /2445, /2522, /2446, /10991, /10992

value = int(input())

if value == 1:
    print("*")
elif value == 2:
    print(" *")
    print("***")
else:
    for line in range(1,value):
        for space in range(value-line):
            print(" ",end='')
        for star in range(line*2-1):
            if max(range(line*2-1))==star:
                print("*",end='')
            elif min(range(line*2-1))==star:
                print("*",end='')
            else:
                print(" ",end='')
        print("")
    for laststar in range(value*2-1):
        print("*",end='')
    print("")

