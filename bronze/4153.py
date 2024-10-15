"""import sys

while True:
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    if (a==0)and(b==0)and(c==0):
        break
    elif a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")
"""


import sys

while True:
    ling = sys.stdin.readline().rstrip()
    list1 = []
    for ch in ling.split():
        ch = int(ch)
        list1.append(ch)
    list2 = [num for num in list1 if num != max(list1)]
    if (list1[0]==0)and(list1[1]==0)and(list1[2]==0):
        break
    elif list2[0]**2 + list2[1]**2 == max(list1) **2:
        print("right")
    else:
        print("wrong")