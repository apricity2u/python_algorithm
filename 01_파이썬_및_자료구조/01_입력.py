# input, readline
# 1. input을 이용한 기본 문법
# - input으로 입력받은 값은 문자열로 들어오기 때문에
#   숫자인 경우 형변환을 해줌
n = int(input())
print(n)

# 2. readline을 이용한 빠른 입력
# - input의 경우 개행이 같이 들어가기 때문에
# - 입력을 받다가 시간초과가 발생하여 readline 사용함
import sys

input = sys.stdin.readline

n = int(input())
print(n)

# * 문자열을 리스트로 입력받기
# word = list(input()) # ["h", "e", "l", "l", "o", "/n"]
# - 개행이 들어가기 때문에 rstrip 꼭 필요함!
word = list(input().rstrip())
print(word)

# 3. 한 줄 리스트 입력
import sys

input = sys.stdin.readline

# 입력값 "1 2"
# - split을 사용하면 공백을 기준으로 나눠줌
# - 그리고 map 객체는 list로 변환해줘야 한다.
numbers = list(map(int, input().split()))
print(numbers)

# - 아래와 같이 다중할당 방식으로도 가능
# - 또한 다중할당으로 받는 경우에는 꼭 list를 사용하지 않아도 됨
a, b = list(map(int, input().split()))
print(a + b)

# Q. A+B-2
import sys

input = sys.stdin.readline

a = int(input())
b = int(input())

print(a + b)

# Q. A+B-3
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(a + b)

# Q. A+B-6
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split(","))
    print(a + b)
