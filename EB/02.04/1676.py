# 1676. 팩토리얼 0의 개수

n = int(input())
pec = 1

for i in range(1, n+1):
    pec *= i

pec = str(pec)
idx = 0

for i in pec[::-1]:
    
    if i == '0':
        idx += 1
        
    else:
        break
print(idx)
