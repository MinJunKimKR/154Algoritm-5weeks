word = input()

arr = [-1]*26
for i in word:
    arr[ord(i)-97] = word.index(i)

for i in arr:
    print(i,end=" ")