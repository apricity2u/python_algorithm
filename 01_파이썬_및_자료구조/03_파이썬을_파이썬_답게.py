# 1. List Comprehension (리스트 컴프리헨션)
numbers = []  # [1, 2, 3, 4, 5]

for i in range(1, 6):
    if i % 2 == 0:
        numbers.append(i)

print(numbers)


numbers2 = [i for i in range(1, 6)]
print(numbers2)

numbers3 = [i for i in range(1, 6) if i % 2 == 0]
print(numbers3)

# 2. 다중 할당, 패킹, 언패킹
# 2-1. 다중 할당
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

a, b = b, a
print(a, b)  # 2 1

# 2-2. 패킹(Packing) -> 리스트로 감싼다
a, *b = 1, 2, 3, 4
print(a)  # 1
print(b)  # [2, 3, 4]

*a, b = 1, 2, 3, 4
print(a)  # [1, 2, 3]
print(b)  # 4

# 2-3. 언패킹(Unpacking) -> 감싼 걸 해제한다.
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  # 1 2 3

numbers = [1, 2, 3]

for number in numbers:
    print(number, end=" ")  # 1 2 3

# 가장 간편한 방식
numbers = [1, 2, 3]
print(*numbers)  # 1 2 3

# 3. enumerate
numbers = [8, 2, 5, 3]
# 0번째 원소 : 8
# 1번째 원소 : 2
# ...

for i in range(len(numbers)):
    print(f"{i}번째 원소 : {numbers[i]}")

# enumerate는 튜플의 집합처럼 생겼음
# (인덱스, 원소)
# (0, 8), (1, 2), (2, 5), (3, 3)
# 그 다음 각각 i, number에 다중할당
for i, number in enumerate(numbers):
    print(f"{i}번째 원소 : {number}")

# 인덱스와 원소별 분류도 가능
print(list(zip(*enumerate(numbers))))  # [(0, 1, 2, 3), (8, 2, 5, 3)]

# 4. Counter
numbers = [1, 2, 4, 1, 2, 2, 3, 2, 2]
# numbers의 원소가 각각 몇개 있는지 알고 싶다.

counter = {}

for number in numbers:
    # 만약, 딕셔너리에 이미 있으면 -> + 1
    # if number in counter:
    if counter.get(number):
        counter[number] += 1
    # 만약, 딕셔너링에 없으면 -> 1개로 넣어
    else:
        counter[number] = 1

print(counter)

# 4-2. 카운터 모듈을 이용한 카운팅
from collections import Counter

numbers = [1, 2, 4, 1, 2, 2, 3, 2, 2]
counter = Counter(numbers)  # Counter({2: 5, 1: 2, 4: 1, 3: 1})
print(counter)

# 가장 많이 있는 원소 순으로 정렬
common = counter.most_common()
print(common)  # [(2, 5), (1, 2), (4, 1), (3, 1)]
print(common[0][0])  # 2
