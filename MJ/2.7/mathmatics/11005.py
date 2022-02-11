# 10:12 -> 10:42
# 10:25 [Success]
n, b = map(int, input().split())

zinsu = [str(x) for x in range(10)] + [chr(x)
                                       for x in range(ord('A'), ord('Z')+1)]

nums = []
while n > 0:
    nums.append(zinsu[(n % b)])
    n = n // b
print(''.join(nums[::-1]))
