#11729
#분할정복
#실버1

#왜 다시봐도 어렵지.. 실전에서 못풀듯.
import sys
sys.setrecursionlimit(100000000)

def hanoi(start,end,n): #start번 막대에서 end번 막대로 옮길것이라는 뜻.
    if n==1:
        print(start,end)
        return
    
    hanoi(start,6-start-end,n-1)#start+end+이름모를막대의 합=6
    print(start,end)
    hanoi(6-start-end,end,n-1)

n=int(input())
print(2**n-1)
hanoi(1,3,n) 
