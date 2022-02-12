import sys
input = sys.stdin.readline

num = int(input())
arr = [[0]*3 for _ in range(26)]

def preorder(a):
    print(a,end="")
    if arr[ord(a)-65][1] != ".":
        preorder(arr[ord(a)-65][1])
    if arr[ord(a) - 65][2] != ".":
        preorder(arr[ord(a) - 65][2])

def inorder(a):
    if arr[ord(a)-65][1] != ".":
        inorder(arr[ord(a)-65][1])
    print(a, end="")
    if arr[ord(a) - 65][2] != ".":
        inorder(arr[ord(a) - 65][2])

def postorder(a):
    if arr[ord(a)-65][1] != ".":
        postorder(arr[ord(a)-65][1])
    if arr[ord(a) - 65][2] != ".":
        postorder(arr[ord(a) - 65][2])
    print(a, end="")


for _ in range(num):
    node,left,right = map(str,input().split())
    arr[ord(node)-65][0],arr[ord(node)-65][1],arr[ord(node)-65][2] = node,left,right


preorder("A")
print()
inorder("A")
print()
postorder("A")