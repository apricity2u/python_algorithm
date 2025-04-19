# 오름차순 정렬
# 내장함수 sorted(), 리스트 메서드 .sort()
numbers = [1, 3, -4, 0, 100]
sorted_numbers = sorted(numbers)
print(numbers) # [1, 3, -4, 0, 100]
print(sorted_numbers) # [-4, 0, 1, 3, 100]

numbers = [1, 3, -4, 0, 100]
numbers.sort()
print(numbers) # [-4, 0, 1, 3, 100]


# 내림차순 정렬
numbers = [1, 3, -4, 0, 100]
sorted_numbers = sorted(numbers, reverse=True)
print(numbers) # [1, 3, -4, 0, 100]
print(sorted_numbers) # [100, 3, 1, 0, -4]

numbers = [1, 3, -4, 0, 100]
numbers.sort(reverse=True)
print(numbers) # [100, 3, 1, 0, -4]
