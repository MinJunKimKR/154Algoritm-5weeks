#Sorting

#2751
import sys
N = int(sys.stdin.readline())
sequence = []
for _ in range(N):
    sequence.append(int(sys.stdin.readline()))
sequence.sort()
for num in sequence:
    print(num)

#solution
print(''.join(sorted(sys.stdin.readlines()[1:], key=int)))


#11650
import sys
N = int(sys.stdin.readline())
sequence = []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    sequence.append([x,y])
sequence.sort(key=lambda x: (x[0],x[1]))
for x,y in sequence:
    print(f'{x} {y}')

#11651
import sys
N = int(sys.stdin.readline())
sequence = []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    sequence.append([x,y])
sequence.sort(key=lambda x: (x[1],x[0]))
for x,y in sequence:
    print(f'{x} {y}')


#10814
import sys
N = int(sys.stdin.readline())
sequence = []
for i in range(N):
    age,name = sys.stdin.readline().split()
    sequence.append((int(age),name,i))
sequence.sort(key=lambda x: (x[0],x[2]))
for age,name,i in sequence:
    print(age, name)


#10825
import sys
N = int(sys.stdin.readline())
sequence = []
for i in range(N):
    name,k,e,m = sys.stdin.readline().split()
    sequence.append([name,int(k),int(e),int(m)])
sequence.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for person in sequence:
    print(person[0])


#10989
import sys
N = int(sys.stdin.readline())
sequence = [0]*10000
for i in range(N):
    num = int(sys.stdin.readline())
    sequence[num-1] += 1

for i,num in enumerate(sequence):
    for j in range(num):
        print(i+1)


#11652
import sys
from collections import defaultdict
N = int(sys.stdin.readline())
dic = defaultdict(int)
for i in range(N):
    dic[int(sys.stdin.readline())] += 1

sequence = sorted(list(dic.items()),key=lambda x: (-x[1],x[0]))
print(sequence[0][0])


#11004
import sys
N,K = map(int,sys.stdin.readline().split())
seq = list(map(int,sys.stdin.readline().split()))
seq.sort()
print(seq[K-1])







