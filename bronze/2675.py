import sys

T = int(input())
for _ in range(T):
    L=[]
    a,b = sys.stdin.readline().rstrip().split()
    list1 = list(b)
    a = int(a)
    for ch in list1:
        L.append(ch*a)
    print("".join(map(str,L)))