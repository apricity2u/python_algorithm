# 리스트
# 1. append
numbers = [1, 2, 3]
numbers.append(4)

print(numbers) # [1, 2, 3, 4]

# 2. pop
# 원소를 제거하고 반환함
numbers = [1, 2, 3]
number = numbers.pop()
print(numbers) # [1, 2]
print(number) # 3

# 시간복잡도 O(N)
numbers = [1, 2, 3]
number = numbers.pop(0)
print(numbers) # [2, 3]
print(number) # 1

# 3. count
# 시간복잡도 O(N)
numbers = [1, 2, 3]
counts = numbers.count(2)
print(counts)

# 4. sort
numbers = [4, -1, 0, 2, 100]
numbers.sort # 리스트는 변경 가능한 자료형이기 때문에 원본이 바뀜
print(numbers) # [-1, 0, 2, 4, 100] 오름차순 정렬

numbers.sort(reverse=True)
print(numbers) # [100, 4, 2, 0, -1] 내림차순 정렬


