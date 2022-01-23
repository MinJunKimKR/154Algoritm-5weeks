import heapq
import sys

input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):

    j = int(input().rstrip())
    if j < 0:
        k = (abs(j), "minus")
    else:
        k = (j, "plus")

    if j == 0:
        if len(heap) == 0:
            print(0)
        else:
            num = heapq.heappop(heap)
            if num[1] == "minus":
                print(-num[0])
            else:
                print(num[0])

    else:
        heapq.heappush(heap, k)