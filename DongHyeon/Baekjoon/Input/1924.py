day_list = ['SUN','MON','TUE', 'WED', 'THU', 'FRI', 'SAT']
month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Day = 0

x, y = map(int, input().split())

for i in range(x-1):
    Day = Day + month_list[i]
Day = (Day + y) % 7
    
print(day_list[Day])