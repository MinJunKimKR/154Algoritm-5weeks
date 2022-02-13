# 7:00 -> 7:40 + 0:20 -> 8:00
# GG
import sys
sys_input = sys.stdin.readline

N, C = map(int, input().split())


max_distance = 0
homes = []
for _ in range(N):
    homes.append(int(sys_input()))
homes.sort()
full_distance = homes[len(homes)-1]-homes[0]


def binary_search(start, end, homes):
    while start <= end:
        mid = (start+end)//2
        cnt_wifi = 1
        pre_home = homes[0]
        for i in range(1, len(homes)):
            if homes[i] >= mid+pre_home:
                cnt_wifi += 1
                pre_home = homes[i]
        if cnt_wifi >= C:
            global max_distance
            max_distance = max(max_distance, mid)
            start = mid+1
        else:
            end = mid-1


binary_search(1, full_distance, homes)
print(max_distance)
