# print
print("1")

# 1. 여러 인자를 넣으면 공백을 기준으로 출력
print("1", "2", "3")

# 2. 맨 끝의 개행을 다른 문자로 바꿀 수 있다. (end)
# - 개행 대신에 "$"로 바꿨기 때문에, hello$python으로 출력됨
print("hello", end="$")
print("python")

# 3. 구분자를 다른 문자로 바꿀 수 있다. (sep)
# - 1$2$3
print("1", "2", "3", sep="$")
# - 알고리즘할 때 많이 사용할 예정
# - 1
#   2
#   3
print("1", "2", "3", sep="\n")

# 4. f-string
name = "kyle"
print(name)  # kyle
print("안녕하세요! " + name)  # 안녕하세요! kyle
print(f"안녕하세요! {name}")  # 안녕하세요! kyle

age = 40
# 문자열 포맷팅에는 표현식이 들어올 수 있음
print(f"안녕하세요! {name}, 나이는 {age+10} 입니다.")

# A+B-7
import sys

input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    a, b = map(int, input().split())

    print(f"Case #{t}: {a+b}")

# A+B-8
import sys

input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    a, b = map(int, input().split())

    print(f"Case #{t}: {a} + {b} = {a+b}")
