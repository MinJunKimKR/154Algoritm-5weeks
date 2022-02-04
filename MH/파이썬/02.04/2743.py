word = input()
ans = 0
for i in word:
    if i.isupper() or i.islower():
        ans+=1
print(ans)
