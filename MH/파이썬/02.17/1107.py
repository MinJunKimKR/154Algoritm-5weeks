n = int(input())
min_count = abs(100-n) # ++ or --로 이동할 경우
m = int(input())

if m:
    broken = list(input().split())
else:
    broken = []

for nums in range(1000001): #채널은 무한대이므로
    nums = str(nums)
    for index,j in enumerate(nums):
        #각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if j in broken:
            break
        #고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif index == len(nums) - 1:
            min_count = min(min_count,abs(int(nums)-n) + len(nums))

print(min_count)
#https://seongonion.tistory.com/99?category=852500
