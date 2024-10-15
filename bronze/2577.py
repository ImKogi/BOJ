a = int(input())
b = int(input())
c = int(input())
result = a * b * c
resultlist = [0 for _ in range(10)]

L = list(str(result))
for re in L:
    re = int(re)
    resultlist[re] += 1

for last in resultlist:
    print(last)




"""# 세 수의 곱 계산
a = int(input())
b = int(input())
c = int(input())
result = a * b * c

# 딕셔너리 초기화
result_counts = {}

# 결과를 문자열로 변환
result_str = str(result)

# 각 숫자의 개수 세기
for char in result_str:
    # dict.get()을 사용하여 카운팅
    result_counts[char] = result_counts.get(char, 0) + 1

# 출력
for digit in range(10):  # 0부터 9까지 출력
    print(result_counts.get(str(digit), 0))  # 딕셔너리에서 값을 가져오고 없으면 0을 반환
"""