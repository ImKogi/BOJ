s = input()
list1 = list(s)

last_list = [-1] * 26
for a in list1:
    index = ord(a) - ord('a')
    last_list[index] = list1.index(a)
print(" ".join(map(str,last_list)))