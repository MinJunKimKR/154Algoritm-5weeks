# 11652. 카드

import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for _ in range(n):
    number = int(input())

    if number in dict:
        dict[number] += 1
    else:
        dict[number] = 1

result = sorted(dict.items(), key = lambda x : (-x[1], x[0]))
print(result[0][0])


'''
런타임 에러 
max1 = max(dict.values())

for key, value in dict.items():

    if max1 == value:
        print(key)
        break
'''
