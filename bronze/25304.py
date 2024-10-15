recip = int(input())
T = int(input())

sum = 0
for _ in range(T):
    i,m = map(int, input().split())
    sum += i * m

if sum == recip:
    print("Yes")
else:
    print("No")