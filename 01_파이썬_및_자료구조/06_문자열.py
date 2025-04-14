# 문자열

# 1. join (무조건 문자열 원소들만 가능)
numbers = ["h", "e", "l", "l"]
joined_numbers = "".join(numbers)
print(joined_numbers)  # hell

numbers = ["h", "e", "l", "l"]
joined_numbers = "$".join(numbers)
print(joined_numbers)  # h$e$l$l

numbers = ["h", "e", "l", "l"]
print("\n".join(numbers))

# 2. replace(old, new)
word = "hello python"
new_word = word.replace("python", "java")
print(word)  # hello python
print(new_word)  # hello java

# 3. 슬라이싱 string[start:end:step]
# step을 - 하면 방향이 반대로
word = "hello"
print(word[1:3])  # el
print(word[0:4:2])  # hl
print(word[3:1:-1])  # ll
print(word[::-1])  # 뒤집기
