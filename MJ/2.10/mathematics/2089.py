# 9:55 -> 모르겠음
N = int(input())
result = ""

while N != 0:
    div = N // -2
    if N % -2 < 0:
        div += 1
    result += str(N - (div*-2))
    N = div

if result:
    print(result[::-1])
else:
    print(0)
