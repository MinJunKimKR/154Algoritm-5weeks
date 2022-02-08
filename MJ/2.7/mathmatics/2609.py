# 4:10 -> 4:40
# FAIL
A, B = list(map(int, input().split()))

A, B = max(A, B), min(A, B)

x, y = A, B

while x % y != 0:
    x, y = y, x % y

gcd = y
print(gcd)

print(A*B//gcd)
