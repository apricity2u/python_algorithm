# 딕셔너리

# 1. get
users = {"kyle": 20, "alex": 30, "jun": 40}
print(users["kyle"]) # 없는 키 값에 접근 시 에러
print(users.get("kyle")) # 없는 키 값에 접근하면 None

# justin이 있으면 그의 숫자를 춧자를 출력하고, 없으면 0을 출력
if "justin" in users:
    print(users["justin"])
else:
    print(0)

# 없으면 2번째 인자로 적은 값을 출력함
print(users.get("justin", 0)) # 0

# 2. keys, values, items
users = {"kyle": 20, "alex": 30, "jun": 40}

for name in users:
    print(name) # keys가 생략되어 key만 출력

for value in users.values():
    print(value) # value만 출력

for name, value in users.items():
    print(name, value) # key와 value를 한꺼번에 출력