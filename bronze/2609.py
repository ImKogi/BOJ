def GCD(n, m):
    gcd = 1
    for num in range(2, min(n, m) + 1):
        if (n % num == 0) and (m % num == 0):
            gcd = num
    return gcd

def LCM(n, m):
    gcd_value = GCD(n, m)
    return (n * m) // gcd_value

n, m = map(int, input().split())
print(GCD(n, m))
print(LCM(n, m))