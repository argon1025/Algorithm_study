Arr = input()
cnt = 0

for i in Arr:
    print(i, end="")
    cnt +=1
    if cnt % 10 == 0:
        print("")
    