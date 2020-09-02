N = int(input())
tmp = 1

for i in range(1, N+1):
    print(' '*(N-i), end='')
    for j in range(i*2):
        if tmp == 1:
            print('*', end='')
            tmp = 0
        else:
            print(' ', end='')
            tmp = 1
    print('')