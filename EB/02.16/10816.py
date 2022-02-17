# 10816. 숫자 카드2

n = int(input())
cards = list(map(int, input().split(' ')))
cards.sort()

m = int(input())
targets = list(map(int, input().split(' ')))

dic = dict()

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(m):
    if targets[i] in dic:
        print(dic[targets[i]], end=' ')
    else:
        print(0, end=' ')
