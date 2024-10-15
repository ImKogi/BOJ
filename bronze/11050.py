import sys

def p(n):
    if n == 0:
        return 1
    a=n-1
    while a > 0:
        n *=a
        a -=1
    return int(n)

N,K = map(int,sys.stdin.readline().rstrip().split())
sys.stdout.write(f"{p(N)//(p(K) * p(N-K))}")