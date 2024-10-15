n = int(input())
a = input()

list = []
for num in a.split():
    num = int(num)
    list.append(num)

print(min(list), max(list))