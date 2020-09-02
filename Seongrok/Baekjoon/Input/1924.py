# 알고리즘
# 기본 입출력 문제
# boj.kr/2557, 1000, 2558, 10950, 10951, 10952, 10953, 11021, 11022, 11718, 11719, 11720/, 11721, 2741, 2742, /2739, /1924, 8393, 10818, 2438, 2439, 2440, 2441, 2442, 2445, 2522, 2446, 10991, 10992

month = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month_val,day_val = map(int, input().split(" "))
total_day = 0

for i in range(0,month_val-1,+1):
    total_day += month[i]
total_day += day_val
print(week[total_day%7])