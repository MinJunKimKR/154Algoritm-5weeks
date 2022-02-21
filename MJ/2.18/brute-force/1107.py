# 12:56 -> 1:36
# 1:40 [Fail]
# 1:50 -> 2:18 [Success]
N = int(input())
M = int(input())
broken = []
if M > 0:
    broken = input().split()
ch_num = 100
cnt_click = abs(N-ch_num)


for num in range(1000001):
    str_num = str(num)
    for i in range(len(str_num)):
        if str_num[i] in broken:
            break
        elif i == len(str_num)-1:
            cnt_click = min(cnt_click, abs(int(str_num) - N) + len(str_num))

print(cnt_click)
