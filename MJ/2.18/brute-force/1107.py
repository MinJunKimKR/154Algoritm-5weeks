# 12:56 -> 1:36
# 1:40 [Fail]
# 1:50 -> 2:18 [Success]
N = int(input())
M = int(input())
if M > 0:
    broken = input().split()
else:
    print(len(str(N)))
    exit(0)
ch_num = 100
cnt_click = abs(N-ch_num)

# if N == 100:
#     print(0)
#     exit(0)
# if (N >= 98 and N <= 103) or M == 10:
#     print(cnt_click)
#     exit(0)
# if M == 0:
#     print(len(N))
#     exit(0)


for num in range(1000001):
    str_num = str(num)
    for i in range(len(str_num)):
        if str_num[i] in broken:
            break
        elif i == len(str_num)-1:
            cnt_click = min(cnt_click, abs(int(str_num) - N) + len(str_num))

print(cnt_click)
