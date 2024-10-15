#팰린드롬수

def palindrom(n):
    s = str(n)
    return s == s[::-1]

while True:
    n = int(input())
    if n == 0:
        break
    elif palindrom(n):
        print("yes")
    else:
        print("no")