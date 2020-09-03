n = int(input())
num_list = list(map(int,input().split()))

ans = [num_list[0]]


for i in range(n-1):
    # 이전까지의 누적 값 + 현재값 vs 현재 값 더 큰 값을 선택  
    ans.append(max(ans[i] + num_list[i+1],num_list[i+1]))
print(ans)
print(max(ans))