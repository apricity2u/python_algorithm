# 내가 원하는 기준으로 정렬
# 1. 기본적인 방법을 이용한 커스텀 정렬
words = ["hello", "abc", "z"]
print(sorted(words)) # ['abc', 'hello', 'z']

# "z", "abc", "hello"

def length(word):
    return len(word)

sorted_words = sorted(words, key=length)
print(sorted_words) # ['z', 'abc', 'hello']

words.sort(key=length)
print(words) # ['z', 'abc', 'hello']

# 2. 리스트를 원소로 갖는 리스트 커스텀 정렬
numbers = [[1, 13], [2, 7], [1, 7], [5, 10], [4, 20]]
print(sorted(numbers)) # [[1, 7], [1, 13], [2, 7], [4, 20], [5, 10]]

# 두 번째 원소를 기준으로 오름차순 정렬
# [[2, 7], [1, 7], [5, 10], [1, 13], [4, 20]]
def sort_key(unit):
    return unit[1]

sorted_numbers = sorted(numbers, key=sort_key)
print(sorted_numbers) # [[2, 7], [1, 7], [5, 10], [1, 13], [4, 20]]


# 두 번째 원소를 기준,
# 만약 두 번째 원소가 같다면, 첫 번째 원소를 기준으로
# 오름차순 정렬
def sort_key(unit):
    return unit[1], unit[0]

sorted_numbers = sorted(numbers, key=sort_key)
print(sorted_numbers) # [[1, 7], [2, 7], [5, 10], [1, 13], [4, 20]]


# 3. Lambda 활용하기
# "lambda 매개변수: 리턴값"
sorted_numbers = sorted(numbers, key=lambda unit: (unit[1], unit[0]))
print(sorted_numbers) # [[1, 7], [2, 7], [5, 10], [1, 13], [4, 20]]


# "z", "abc", "hello"
words = ["hello", "abc", "z"]

def length(word):
    return len(word)
sorted_words = sorted(words, key=length)

sorted_words = sorted(words, key=lambda word: len(word))

sorted_words = sorted(words, key=len)

print(sorted_words) # ['z', 'abc', 'hello']
