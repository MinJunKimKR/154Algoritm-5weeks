# 2:02 -> 2:32
# 2:09 [Success]
import sys
sys_input = sys.stdin.readline
N = int(input())
arr = []
words = []
for _ in range(N):
    word = sys_input().strip()
    if word in words:
        continue
    words.append(word)
    arr.append((len(word), word))

result_arr = sorted(arr, key=lambda x: [x[0], x[1]])
for i in result_arr:
    print(i[1])
