# 10820. 문자열 분석

import sys

while True:
    
    line = sys.stdin.readline().rstrip('\n') # sys.stdin.readline()[:-1]
    up, lo, sp, nu = 0, 0, 0, 0

    if not line:
        break
    
    for i in line:
            
        if i.islower():
            lo += 1
                
        elif i.isupper():
            up += 1

        elif i.isdigit():
            nu += 1

        elif i.isspace():
            sp += 1

    
    print(lo, up, nu, sp)
