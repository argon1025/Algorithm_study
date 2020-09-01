import sys
n = int(sys.stdin.readline())
words = []
for i in range(n):
    words.append(str(sys.stdin.readline().rstrip()))
words = list(set(words))

print(words)

