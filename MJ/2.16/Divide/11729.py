# 10:40 -> 11:10
# GG
# 11:55 [Success]
K = int(int(input()))

move = []
cnt = 0


def hanoi(n, from_pos, to_pos, via):
    global cnt
    if n == 0:
        return
    hanoi(n-1, from_pos, via, to_pos)
    move.append([from_pos, to_pos])
    cnt += 1
    hanoi(n-1, via, to_pos, from_pos)


hanoi(K, 1, 3, 2)
print(cnt)
for step in move:
    print(step[0], step[1])
