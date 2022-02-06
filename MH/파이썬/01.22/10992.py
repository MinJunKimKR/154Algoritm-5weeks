#별찍기 -17

num = int(input())
for i in range(1,num+1):
    if i == num:
        print("*"*(num*2-1))
    elif i == 1:
        print(" "*(num-i),"*",sep="")
    else:
        print(" "*(num-i),"*"," "*(2*i-3),"*",sep="")

