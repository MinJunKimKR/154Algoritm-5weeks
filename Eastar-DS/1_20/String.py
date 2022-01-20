#String
import sys,collections
a = sys.stdin.readline()

#10808
string = input()
num_of_alpha,dic,output = [0]*26, {}, ''
for i,alpha in enumerate('abcdefghijklmnopqrstuvwxyz'):
    dic[alpha] = i
for s in string:
    num_of_alpha[dic[s]] += 1
for num in num_of_alpha:
    output += f'{num} '
print(output)

#10809
string = input()
num_of_alpha,dic,output = [-1]*26, {}, ''
for i,alpha in enumerate('abcdefghijklmnopqrstuvwxyz'):
    dic[alpha] = i
for i,s in enumerate(string):
    if(num_of_alpha[dic[s]] == -1):
        num_of_alpha[dic[s]] = i
for num in num_of_alpha:
    output += f'{num} '
print(output)


#10820 다시풀면 rstrip() stdout활용하자.
import sys
string = sys.stdin.readline()
while(string):
    lower,upper,digit,space = 0,0,0,0
    for s in string:
        if(s.islower()):
            lower += 1
        elif(s.isupper()):
            upper += 1
        elif(s.isdigit()):
            digit += 1
        elif(s == ' '):
            space += 1    
    print(f'{lower} {upper} {digit} {space}')
    string = ''
    string = sys.stdin.readline()


#2743
string = input()
print(len(string))

#11655
table = [['a', 'A'],
 ['b', 'B'],
 ['c', 'C'],
 ['d', 'D'],
 ['e', 'E'],
 ['f', 'F'],
 ['g', 'G'],
 ['h', 'H'],
 ['i', 'I'],
 ['j', 'J'],
 ['k', 'K'],
 ['l', 'L'],
 ['m', 'M'],
 ['n', 'N'],
 ['o', 'O'],
 ['p', 'P'],
 ['q', 'Q'],
 ['r', 'R'],
 ['s', 'S'],
 ['t', 'T'],
 ['u', 'U'],
 ['v', 'V'],
 ['w', 'W'],
 ['x', 'X'],
 ['y', 'Y'],
 ['z', 'Z']]
dic = {'a': 0,
 'A': 0,
 'b': 1,
 'B': 1,
 'c': 2,
 'C': 2,
 'd': 3,
 'D': 3,
 'e': 4,
 'E': 4,
 'f': 5,
 'F': 5,
 'g': 6,
 'G': 6,
 'h': 7,
 'H': 7,
 'i': 8,
 'I': 8,
 'j': 9,
 'J': 9,
 'k': 10,
 'K': 10,
 'l': 11,
 'L': 11,
 'm': 12,
 'M': 12,
 'n': 13,
 'N': 13,
 'o': 14,
 'O': 14,
 'p': 15,
 'P': 15,
 'q': 16,
 'Q': 16,
 'r': 17,
 'R': 17,
 's': 18,
 'S': 18,
 't': 19,
 'T': 19,
 'u': 20,
 'U': 20,
 'v': 21,
 'V': 21,
 'w': 22,
 'W': 22,
 'x': 23,
 'X': 23,
 'y': 24,
 'Y': 24,
 'z': 25,
 'Z': 25}
string = input()
output = ''
for s in string:
    if(s.isupper()):
        output += table[(dic[s]+13)%26][1]
    elif(s == ' ' or s.isdigit()):
        output += s
    else:
        output += table[(dic[s]+13)%26][0]
print(output)


#10824
nums = input().split()
print(int(nums[0]+nums[1])+int(nums[2]+nums[3]))

#11656
string = input()
subs = []
for i in range(len(string)):
    subs.append(string[i:])
subs.sort()
for sub in subs:
    print(sub)




















