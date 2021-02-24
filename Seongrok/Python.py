
# 리스트 컴프리헨션

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array_1 = [i for i in range(1,11)]
print(array_1)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
array_2 = [i*i for i in range(1,11)]
print(array_2)


# 2차원 리스트 초기화
n = 4
m = 3
array_3 = [[0]* m for _ in range(n)]
print(array_3)


array_4 = []
# 리스트에 요소 삽입
array_4.append(2)
array_4.append(6)
array_4.append(1)
array_4.append(7)

#리스트요소 오름차순 정렬
array_4.sort()
print(array_4)

#리스트요소 오름차수 정렬 함수 -> 값 복사되어 리턴
print(sorted(array_4))

#리스트 요소 내림차순 정렬
array_4.sort(reverse=True)
print(array_4)

#리스트 원소 뒤집기
array_4.reverse()
print(array_4)

#특정 인덱스에 원소 추가
array_4.insert(0,5)
print(array_4)

#특정 원소 삭제
array_4.remove(5)
print(array_4)

#카운트, 특정값 카운트
print(array_4.count(5))