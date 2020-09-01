import sys
n = int(sys.stdin.readline())
count0 = [1,0,1]
count1 = [0,1,1]

def fibo(n):
    l = len(count0)
    if l <= n:
        for i in range(l, n+1):
            count0.append(count0[i-1] + count0[i-2])
            count1.append(count1[i-1] + count1[i-2])
    print('%d %d' %(count0[n], count1[n])) 
for i in range(n):
    a = int(sys.stdin.readline())
    fibo(a)