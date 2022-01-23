#별찍기 -9

num = int(input())

for i in range(num):
    print(" "*i+"*"*(((num-i)*2)-1))
for i in range(num-2,-1,-1):
    print(" "*i+"*"*(((num-i)*2)-1))