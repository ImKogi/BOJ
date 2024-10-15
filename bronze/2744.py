sentence = input()
L = list()

for ch in sentence:
    if 65 <= ord(ch) <= 90:
        ch = chr(ord(ch)+32)
    else:
        ch = chr(ord(ch)-32)
    L.append(ch)

print("".join(map(str,L)))