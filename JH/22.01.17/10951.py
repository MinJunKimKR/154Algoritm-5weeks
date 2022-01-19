'''while True:
  try:
    a, b = map(int, input().split())
    print(a+b)
  except:
    break'''

import sys

for line in sys.stdin:
  try:
    print(sum(map(int, line.split())))
  except:
    break

# try~except 문을 처음 써봄
# 입력을 멈추고 싶으면 예외 입력 값이 들어왔을 때 중단하도록 하면 된다.

# input() -> sys.stdin 으로 바꾸니까 속도가 8ms 빨라짐. (76 ->68)