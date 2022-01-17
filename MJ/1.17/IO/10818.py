N = int(input())
nums = map(int,input().split())

nums = sorted(nums)

print(f'{nums[0]} {nums[len(nums)-1]}')