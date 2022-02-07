# 5:45 -> 6:15
# 5:48  [Success]
A, B, C = list(map(int, input().split()))

print((A+B) % C)
print(((A % C) + (B % C)) % C)
print((A*B) % C)
print(((A % C) * (B % C)) % C)
