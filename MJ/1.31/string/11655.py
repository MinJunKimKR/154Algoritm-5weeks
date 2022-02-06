# 1:16 -> 1:36
# 1:35 [Success]
code_a = ord('a')
code_z = ord('z')
code_A = ord('A')
code_Z = ord('Z')
code_1 = ord('1')
code_9 = ord('9')


rot = []
S = list(input())

for s in S:
    code_s = ord(s)
    if code_s <= code_Z and code_s >= code_A:
        code = code_s+13
        if code > code_Z:
            code -= 26
        rot.append(chr(code))
        continue
    if code_s <= code_z and code_s >= code_a:
        code = code_s+13
        if code > code_z:
            code -= 26
        rot.append(chr(code))
        continue
    rot.append(s)
for s in rot:
    print(s, end='')
