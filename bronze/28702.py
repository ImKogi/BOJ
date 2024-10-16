for i in range(3, 0, -1):
    x = input()
    if x not in ['FizzBuzz', 'Fizz', 'Buzz']:
        n = int(x) + i

if n%3==0 and n%5==0:
    print('FizzBuzz')
elif n%3==0:
    print('Fizz')
elif n%5==0:
    print('Buzz')
else:
    print(n)

"""
for i in range(3, 0, -1):
    x = input()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x) + i
        print('Fizz'*(n % 3 == 0) + 'Buzz'*(n % 5 == 0) or n)
        break
    
"""