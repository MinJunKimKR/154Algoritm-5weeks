#쇠막대기

p = input()
arr = []
answer = 0
for i in range(len(p)):
    if p[i] == "(":
        arr.append("(")
    else:
        if p[i-1] == "(":
            arr.pop()
            answer+=len(arr)
        else:
            arr.pop()
            answer+=1
print(answer)



