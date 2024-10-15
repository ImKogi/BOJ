N, M = map(int, input().split())
list = list(map(int,input().split()))

r_result = 0

for num1 in list:
    for num2 in list:
        if num1 != num2:
            for num3 in list:
                if num3 != num1 and num3 != num2:
                    result = num1 + num2 + num3
                    if (result <= M):
                        if result >= r_result:
                            r_result = result

print(r_result)