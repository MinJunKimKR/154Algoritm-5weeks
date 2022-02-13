# 3:57 -> 4:27

N = int(input())


for i in range(2, int(N/2)+1):
    if N == 1:
        break
    while N % i == 0:
        print(i)
        N = N//i
if N != 1:
    print(N)
# print(N)
# eratos = [True] * (int(N/2) + 1)
# eratos[0], eratos[1] = False, False
# sosu = []
# for i in range(2, len(eratos)):
#     if eratos[i] == False:
#         continue
#     sosu.append(i)
#     for i in range(i+i, len(eratos), i):
#         eratos[i] = False

# while sosu.count(N) == 0:
#     for su in sosu:
#         if N % su == 0:
#             print(su)
#             N = N//su
#             break
# print(N)
