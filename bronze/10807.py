n = input()
lit = list(map(int, input().split()))
check = int(input())
k = 0

for ch in lit:
    if ch == check:
        k+=1

print(k)