word = input()
arr = []
for i in range(len(word)):
    arr.append(word[i:])
arr.sort()
for i in arr:
    print(i)