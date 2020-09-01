A = input().split('-')
nums = []
for i in A:
    tmp = 0
    num = i.split('+')
    for j in num:
        tmp += int(j)
    nums.append(tmp)
print(nums)
answer = int(nums[0]) - sum(nums[1:])
print(answer)