"""n = int(input())

for num in range()

a = n//(num+1)
b = n//(num/10 + 1)
c = n//(num/100 + 1)


def find_smallest_decomposition(n):
    # 자리수 수
    digits = len(str(n))
    # 분해합을 계산할 최소 m의 시작점
    start = max(1, n - 9 * digits) # n보다 작고 자연수인 가장 작은 시작점
    smallest = None

    for m in range(start, n):  # m은 n보다 작아야 한다.
        # 자리수의 합 계산
        digit_sum = sum(int(d) for d in str(m))
        if m + digit_sum == n:  # 분해합이 n과 같으면
            smallest = m if smallest is None else min(smallest, m)

    return smallest

n = int(input("정수를 입력하세요: "))
result = find_smallest_decomposition(n)
if result is not None:
    print(f"가장 작은 분해합은: {result}")
else:
    print(0)
"""

n = int(input())
result = 0
for i in range(1, n+1):
    nums = list(map(int, str(i)))
    result = sum(nums) + i 
    if result == n:
        print(i)
        break
    if i == n:
        print(0)