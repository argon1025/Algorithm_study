N = int(input())
words = []
answer = 0
tmp = []
for i in range(N):
    words.append(input())


for word in words:
    tmp_alpha = word[0]
    tmp.append(tmp_alpha)
    for alpha in word[1:]:
        if alpha in tmp:
            if alpha != tmp_alpha:
                answer += 1
                break
            else:
                tmp_alpha = alpha
        else:
            tmp_alpha = alpha
            tmp.append(alpha)
    tmp = []
print(N - answer)