n = int(input())

li = []
for i in range(n):
  li.append(int(input()))

for i in range(n):
  for j in range(1, n):
    if li[j-1] > li[j]:
      li[j-1], li[j] = li[j], li[j-1] # list swap

print(li)