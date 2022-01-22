#별찍기 -12

num = int(input())

for i in range(1,num+1):
    print(" "*(num-i)+"*"*i)
for i in range(1,num+1):
    print(" "*i+"*"*(num-i))