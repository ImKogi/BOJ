ns = int(input())
num = input()

sum = 0
k=1
while k <= ns:
    sum += int(num[k-1])
    k+=1
print(sum)