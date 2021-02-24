# 키와 값의 쌍을 데이터로 가지는자료형 입니다
# 해시테이블과 같습니다

# 딕셔너리 선언 1
a = dict()
a['id'] = 1
a['data'] = "apple"

# 딕셔너리 선언 2
b = {
    'id':1,
    'data' : "tomato"
}

#id 라는 키가 존재하는지
if 'id' in a:
    print('true')

# 관련함수
print(a.keys()) # 키값만 리스트로 반환
print(a.values()) #데이터만 리스트로 반환

# 키를 이용해 각 키의 값 출력
for i in a.keys():
    print(a[i])