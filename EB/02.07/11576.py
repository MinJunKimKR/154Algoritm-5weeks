# 11576 Base Conversion

import math # pow라는 n제곱을 쉽게 해주는 내장함수 이용을 위함

a, b = map(int, input().split())    # a진법의 수를 b진법으로
n = int(input())    # n자리수인 a진법 수
lists = list(map(int, input().split()))
ten = 0	# 10진법으로 만든 수
result = []
fin = ''

for i in range(n):
    ten += int(lists[i] * math.pow(a, n - i - 1))

while ten:
    nam = ten % b
    result.append(str(nam))
    ten = ten // b

result = result[::-1]
fin = ' '.join(result)	# 절 대 띄 어 쓰 기 삽 입 해
print(fin)
