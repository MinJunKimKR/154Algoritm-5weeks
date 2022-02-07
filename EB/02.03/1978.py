# 1978. 소수 찾기

n = int(input())
lst = list(map(int, input().split()))
result = 0

for i in lst:

    div = 1
    
    if i == 1:
        continue
    
    else:
        for j in range(2, i+1):
            if i % j == 0:
                div += 1

    if div == 2:
        result += 1

print(result)
