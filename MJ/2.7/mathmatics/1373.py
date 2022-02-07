a = input()

a = list(a)[::-1]

total = ''
for i in range(0, len(a), 3):
    nums = list(map(int, a[i:i+3]))
    if len(nums) != 3:
        nums += [0] * (3-len(nums))

    zinsu = nums[0] + (nums[1]*2) + (nums[2]*4)
    total = str(zinsu) + total
print(total)
#     total += int(a[i])*pow(2, i)
# print(total)
