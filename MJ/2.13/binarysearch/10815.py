# 10:11 -> 10:41
# 10:35[Success]
import sys
sys_input = sys.stdin.readline

N = int(input())
n_card = list(map(int, sys_input().strip().split()))
n_card.sort()
M = int(input())
m_card = list(map(int, sys_input().strip().split()))


def bi_search(start, end, num):
    if start > end:
        print(0, end=' ')
        return
    mid = (start + end) // 2
    if n_card[mid] == num:
        print(1, end=' ')
        return
    if n_card[mid] > num:
        bi_search(start, mid-1, num)
    else:
        bi_search(mid+1, end, num)


for m in m_card:
    bi_search(0, len(n_card)-1, m)
