matrix1 = []
matrix2 = []

a,b = map(int, input().split())

for _ in range(a):
    hang = list(map(int, input().split()))
    matrix1.append(hang)

for _ in range(a):
    hang = list(map(int, input().split()))
    matrix2.append(hang)

result = []
for a1 in range(a):
    sub_result = []
    for b1 in range(b):
        sub_result.append(matrix1[a1][b1]+matrix2[a1][b1])
    result.append(sub_result)

for ch in range(a):
    print(" ".join(map(str,result[ch])))