#https://it-college-diary.tistory.com/entry/%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1783%EB%B2%88-%EB%B3%91%EB%93%A0-%EB%82%98%EC%9D%B4%ED%8A%B8
n,m = map(int,input().split())
if n == 1: #이동가능한 칸이 없다
    count = 1
elif n == 2:
    # 4는 최대횟수 -> 시작칸 + 최대 3번 움직일 수 있다.
    count = min(4,(m-1)//2+1)
elif m < 7:
    count = min(4,m)
else:
    count = (2+(m-5)) + 1
print(count)