# 2089. -2진수

n = int(input())
result = ""

while n != 0:
    div = n // -2
    if n % -2 < 0:
        div += 1
    result += str(n - (div*-2))
    n = div

if result:
    print(result[::-1])
else:
    print(0)
