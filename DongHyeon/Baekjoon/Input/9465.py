T = int(input())

for i in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a[1] = b[0] + a[1]
    b[1] = a[0] + b[1]
    for j in range(2, n):
        #  
        a[j] += max(b[j-1], b[j-2])
        b[j] += max(a[j-1], a[j-2])
    print(max(a[n-1], b[n-1]))


