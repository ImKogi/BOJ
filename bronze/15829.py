L = int(input())
string = input()

r = 31
M = 1234567891

hash_value = 0
for i in range(L):
    char_value = ord(string[i]) - ord('a') + 1
    hash_value += char_value*(r**i)
    hash_value %= M

print(hash_value)