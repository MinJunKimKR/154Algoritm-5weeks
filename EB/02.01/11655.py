# 11655. ROT13

import sys

line = list(sys.stdin.readline().rstrip('\n'))  # 개행 문자 제

for i in range(len(line)):
    
    if line[i].isupper():
        
        if ord(line[i]) + 13 <= 90:
            line[i] = chr(ord(line[i]) + 13)

        else:
            line[i] = chr(ord(line[i]) - 13)

    elif line[i].islower():

        if ord(line[i]) + 13 <= 122:
            line[i] = chr(ord(line[i]) + 13)

        else:
            line[i] = chr(ord(line[i]) - 13)

for c in line:
    print(c, end="")
