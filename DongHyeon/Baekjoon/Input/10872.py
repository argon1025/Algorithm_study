N = int(input())

def fac(N):
    if N == 0:
        return 1
    return N * fac(N-1)

print(fac(N))