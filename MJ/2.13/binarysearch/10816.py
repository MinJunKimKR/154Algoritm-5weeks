# 10:40 -> 11:10
# 10:50
# 11:02 [Success]
import sys
sys_input = sys.stdin.readline
dic = {}

N = int(input())
n_cards = list(map(int, sys_input().strip().split()))
n_cards.sort()

for n in n_cards:
    if dic.get(n) == None:
        dic[n] = 1
    else:
        dic[n] += 1
M = int(input())
m_cards = list(map(int, sys_input().strip().split()))


def bi_search(start, end, num):
    if start > end:
        print(0, end=' ')
        return
    mid = (start + end)//2
    if n_cards[mid] == num:
        print(dic[num], end=' ')
        return
    if n_cards[mid] > num:
        bi_search(start, mid-1, num)
    else:
        bi_search(mid+1, end, num)


for m in m_cards:
    bi_search(0, N-1, m)

# dic = {
#     1: 1
# }
# print(dic.get(1))
# print(dic.get(2) == None)
