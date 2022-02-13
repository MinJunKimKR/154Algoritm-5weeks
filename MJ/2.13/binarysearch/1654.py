# 5:30 -> 6:00
# 5:55 [Success]
K, N = map(int, input().split())

lan_lines = []
for _ in range(K):
    lan_lines.append(int(input()))
max_size = 0


def search_line(start, end):
    if start > end:
        return
    global max_size
    line_cnt = 0
    mid = int((start+end)/2)
    for line in lan_lines:
        line_cnt += line//mid
    if line_cnt >= N:
        max_size = max(max_size, mid)
        search_line(mid+1, end)
    else:
        search_line(start, mid-1)


search_line(1, max(lan_lines))
print(max_size)
# while True:

#     for line in lan_lines:
#     if line_cnt > N:
