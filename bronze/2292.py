"""벌집 문제네요.
시간 제한 2초
메모리 제한 128mb

규칙성; 한바퀴를 돌기위한 집의 갯수가 6의 배수 만큼 증가함
6, 12, 18, 24,...

어떻게 풀 것인가?

입력; 첫째 줄에 1에서 10억까지의 자연수 n값이 주어짐

출력; 지나는 방의 갯수만 출력한다.

입력을 어떻게 받을까요? 하나의 숫자를 받는다.
import sys

N = int(sys, stdin.readline().rstrip())
하나의 값을 받더라도 꼭 rstrip()을 써주자 개행문자 삭제하기 위해 필요함

while문을 일단 사용해 봅시다.
변수는 일단 dan 과 N 2개로 설정합니다.

dan은 일정 규칙을 지날때마다 증가하도록 합니다.
단과 방의 갯수는 연관성을 파악햇을떄 존재한다는 것을 발견할 수 있습니다.

포인트는 N= 1일떄 어떻게 처리할 것인가?
dan의 초기 전역변수 설정값을 몇으로 줄 것인가?

dan = 0 
while 1+ (6*dan) <N:
    dan+=1
로 하면
N =1 일때 1 < 1로 조건이 성립되지 않아
방은 0개로 출력됩니다.

N>=2일떄부터
너무 좋네요

import sys

N= int(sys.stdin.readline().rstrip())

dan = 0 
while 1+(6*dan) < N:
    dan+=1

print(dan)


결과 :  시간 초과?


시간 제한은 2초였다...

while이 안되면
for이나 자료구조를 써봐야겠다는 생각이 듦

N // 1+(6*dan) = ??

단을 먼저 설정하고 범위를 좁혀볼까?

dan = 0
for x in range(1,):
    if x < 1 + (6*dan):
        print(dan)
    dan+=1

range(1,)이라는 건 없다 ㅋㅋ

import sys

N= int(sys.stdin.readline().rstrip())

dan = 0 
while True:
    if 1 + (6*dan) < N:
        dan+=1
    elif 1 + (6*(dan+1)) < N:
        dan+=2
    else:
        print(dan)
        break
print(dan)

결과 시간 초과

도대체 시간 초과 안시킬려면...

import sys

N= int(sys.stdin.readline().rstrip())

dan = 0 
while True:
    if dan <= N <= 1+(6*dan):
        print(dan)
        break
    dan+=1
print(dan)


이것도 시간 초과
"""





import sys

N = int(sys.stdin.readline().rstrip())

dan = 0
num=1
while num < N:
    num +=(6*dan)
    dan+=1
    
print(dan)



N = int(input())
print(round(((N-1)/3)**0.5)+1)