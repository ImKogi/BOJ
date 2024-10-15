N = int(input())
s = list(map(int,input().split()))
M = max(s)

sum = 0
for num in s:
    sum += num/M * 100

print(sum/N)