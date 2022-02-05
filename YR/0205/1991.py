#1991
#실버1


tree={} #딕셔너리 형태로 구성.
n=int(input())
for i in range(n):
    root,left,right=input().strip().split() #입력받기.
    tree[root]=[left,right]
    
def preorder(root): #뿌리를 먼저 방문.
    if root!='.':
        print(root,end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
        
def postorder(root): #하위 트리 모두 방문후 뿌리를 방문
    if root!='.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root,end='')
        
def inorder(root): #왼쪽 하위트리 방문후 뿌리방문
    if root!='.':
        inorder(tree[root][0])
        print(root,end='')
        inorder(tree[root][1])
        
preorder('A')
print()
inorder('A')
print()
postorder('A')       
        
