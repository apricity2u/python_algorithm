# 이차원 리스트의 조회와 수정
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])  # 1
print(matrix[2][2])  # 9

matrix[2][2] = 0
print(matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# 이차원 리스트의 초기화
matrix = []

for _ in range(3):
    matrix.append([0] * 4)

print(matrix)
# [
#   [0, 0, 0, 0],
#   [0, 0, 0, 0],
#   [0, 0, 0, 0]
# ]

matrix = [[0] * 4 for _ in range(3)]
print(matrix)
# [
#   [0, 0, 0, 0],
#   [0, 0, 0, 0],
#   [0, 0, 0, 0]
# ]

matrix = [[0] * 4] * 3  # 얕은복사
matrix[0][0] = 1
print(matrix)
# [
#   [1, 0, 0, 0],
#   [1, 0, 0, 0],
#   [1, 0, 0, 0]
# ]












