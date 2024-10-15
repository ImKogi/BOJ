import sys

n,x = map(int,sys.stdin.readline().rstrip().split())
a = input()
L = []

for ch in a.split():
    ch = int(ch)
    if ch < x:
        L.append(ch)


print(" ".join(map(str,L)))