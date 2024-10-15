numbers = input()
k=0
for a in numbers.split():
    a= int(a)
    k+=a**2
print(k%10)