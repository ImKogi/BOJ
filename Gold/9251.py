s = input()
t = input()
counting = 0
for a in s:
    for b in t:
        if a == b:
            counting +=1
print(counting/2)