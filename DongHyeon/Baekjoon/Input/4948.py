def prime(s,e):
    check = [False, False] + [True] * e
    primes = []
    for i in range(2, e+1):
        if check[i]:
            if i > s:
                primes.append(i)
            for j in range(2*i, e+1, i):
                check[j] = False

    return len(primes)

while True:
    n = int(input())
    if n == 0:
        break
    print(prime(n, n*2))

