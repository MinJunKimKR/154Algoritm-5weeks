# 11:28 -> 12:18
# 12:30 [FAIL]
# 12:32[Success]
N = int(input())
nums = []

if N == 1:
    print(input())
    exit(0)
for _ in range(N):
    nums.append(int(input()))
total = 0

plus_nums = sorted([x for x in nums if x > 0], reverse=True)
mi_nums = sorted([x for x in nums if x < 0])
zero_cnt = nums.count(0)

end = len(plus_nums)
if end % 2 == 1:
    total += plus_nums[end-1]
    end -= 1


for i in range(0, end, 2):
    if i+1 == len(plus_nums):
        total += plus_nums[i]
    elif plus_nums[i] == 1 and plus_nums[i+1] == 1:
        total += 2
    elif plus_nums[i] == 1 or plus_nums[i+1] == 1:
        total += (plus_nums[i]+plus_nums[i+1])
    else:
        total += (plus_nums[i] * plus_nums[i+1])
end = len(mi_nums)
if len(mi_nums) % 2 == 1 and zero_cnt > 0:
    end -= 1

for i in range(0, end, 2):
    if i+1 == end:
        total += mi_nums[i]
    else:
        total += (mi_nums[i] * mi_nums[i+1])
print(total)
