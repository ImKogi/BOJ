def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

gs = input()
nums = input().split()

s = 0
for num in nums:
    num = int(num)
    if is_prime(num):
        s+=1

print(s)