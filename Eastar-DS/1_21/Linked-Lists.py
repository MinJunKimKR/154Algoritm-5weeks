#Linked-Lists


import sys,collections
a = sys.stdin.readline()

#1406
#스트링으로 하니까 시간초과.
import sys
string = sys.stdin.readline()[:-1]
num = int(sys.stdin.readline())
cursor = len(string)

for i in range(num):
    order = sys.stdin.readline()
    if(order[0]== 'L'):
        if cursor > 0:
            cursor -= 1
        else: continue
    elif(order[0]== 'D'):
        if(cursor < len(string)):
            cursor += 1
        else: continue
    elif(order[0]== 'B'):
        if(cursor > 0):
            string,cursor = string[:cursor-1] + string[cursor:], cursor-1
        else: continue
    else:
        string,cursor = string[:cursor] + order[2] + string[cursor:],cursor+1
print(string)

#stack사용, s2는 방향이 거꾸로되어있음.
import sys
s1 = list(sys.stdin.readline()[:-1])
s2 = []
num = int(sys.stdin.readline())
for i in range(num):
    order = sys.stdin.readline()
    if(order[0]== 'L'):
        if s1:
            s2.append(s1.pop())
        else: continue
    elif(order[0]== 'D'):
        if s2:
            s1.append(s2.pop())
        else: continue
    elif(order[0]== 'B'):
        if s1 : 
            s1.pop()
        else : continue        
    else:
        s1.append(order[2])
print(''.join(s1 + s2[::-1]))


#테스트속도 측정하는법 찾았다 개꿀
# import time 
# li = [1,2,3,4,5,6,7,8,9,0] * 60000 
# st = '1234567890' * 60000 
# start = time.time() 
# st = st[:1000] + '1' + st[1000:] 
# print(time.time() - start) 

# start = time.time() 
# li = li[:1000] + [1] + li[1000:] 
# print(time.time() - start) 

# start = time.time() 
# li.insert(1000, 1) 
# print(time.time() - start)

# b = 30000
# a = '1234567890'*60000
# start = time.time()
# print(start)
# a,b = a[:b-1] + a[b:], b-1
# print(round(time.time() - start,7))


#1158 deque의 rotate를알게된 문제였을뻔했는데 내풀이가 더빠름

import sys
n,k = map(int,sys.stdin.readline().split())
k -= 1
nums,output = list(range(1,n+1)),'<'
K = 0
while(nums):
    K += k
    if(K >= len(nums)):
        K %= len(nums)
    output += (str(nums.pop(K)) + ', ')    
sys.stdout.write(output[:-2] + '>')
print(output[:-2] + '>')


#1168 세그먼트트리



























