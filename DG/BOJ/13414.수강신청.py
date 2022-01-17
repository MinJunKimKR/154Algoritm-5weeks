import sys

k, l = map(int, input().split())
input = sys.stdin.readline

data = {}

for i in range(l):
    student = input().rstrip()

    data[student] = i

count = 0
for i in sorted(data.items(), key=lambda x: x[1]):
    count += 1
    if count > k:
        break
    print(i[0])
