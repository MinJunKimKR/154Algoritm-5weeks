# 4:08 -> 4:38
# 4:21 [Success]
M, N = map(int, input().split())

eratos = [True] * (N+1)
eratos[0], eratos[1] = False, False
harf = int(N/2)
for i in range(2, harf+1):
    if eratos[i] == False:
        continue
    for j in range(i+i, N+1, i):
        eratos[j] = False
for i in range(M, N+1):
    if eratos[i]:
        print(i)
