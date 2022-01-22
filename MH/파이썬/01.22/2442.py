#별찍기 -5

num = int(input())

for i in range(1,num+1):
    print(" "*(num-i)+"*"*(2*i-1))
    #print(" "*(num-i)+"*"*(2*i-1)+" "*(num-i))
    #빈칸을 뒤에 출력하면 안되나부다

