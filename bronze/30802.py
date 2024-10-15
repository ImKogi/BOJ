N = int(input())
list = list(map(int, input().split()))
T,P = map(int, input().split())

result1 = 0
result2 = N//P
result3 = N%P

for num in list:
    if (num%T==0):
        result1+=(num//T)
    elif num == 0:
        result1+=0
    else:
        result1+=(num//T +1)

print(result1)
print(result2,result3)