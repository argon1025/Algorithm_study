import time
start_time = time.time()

# 지수표현
print(1e9)
print(int(1025e-2))

#실수표현
a = 0.1+0.2
print(a)
if(a==0.3):
    print('true')
else:
    print('false')

#실수표현 문제해결 round함수
if(round(a,1)==0.3):
    print('true')
else:
    print('false')

# 연산자
a = 7
b = 3

print(a / b) # 나누기 실수부 까지 전부
print(a % b) # 나머지
print (a // b) # 몫


end_time = time.time()
print("time : ",end_time - start_time)