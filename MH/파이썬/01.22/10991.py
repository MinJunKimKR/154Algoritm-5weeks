#별찍기 -16

num = int(input())

for i in range(1,num+1):
    print(" "*(num-i), end = "")
    for j in range(i):
        print("*", end = " ")
    print()

#end옵션 : 줄바꿈 안됨.