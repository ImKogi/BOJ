"""N = int(input())
numbers = []

for _ in range(N):
    a = int(input())
    numbers.append(a)

for number in sorted(numbers):
    print(number)
"""
"""
import sys
N = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(N):
    num_list[int(sys.stdin.readline())]+=1

for i in range(10001):
    if num_list[i] !=0:
        for _ in range(num_list[i]):
            sys.stdout.write("{i}\n")
"""

import sys
def main():
    num = int(sys.stdin.readline())

    counting = [0] * 10001

    for i in range(num):
        counting[int(sys.stdin.readline())]+=1

    for i in range(1,10001):
        count = counting[i]
        while count > 0:
            batch = min(count,10000)
            sys.stdout.write(f"{i}\n" * batch)
            count -= batch

if __name__ == "__name__":
    main()

"""한꺼번에 batch를 1만 이상 주게 되면
            과도한 출력으로 성능저하를 유발할 수 있음."""