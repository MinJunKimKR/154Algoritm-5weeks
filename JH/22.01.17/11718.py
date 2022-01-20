'''while True:
  try:
    print(input())
  except EOFError:
    break'''
# 입력값이 몇 번 주어지는지 모른다.
# 입력 값이 여러줄로 입력된다. -> input(): 엔터 단위
# 입력 값은 그대로 출력된다. -> 입력되자마자 바로 출력!
# 입력값이 안 들어온 상태라면 -> EOFError (End of File)

import sys
print(sys.stdin.read())

# sys.stdin.read(): 전체를 다 읽어 출력
# readline(): 줄 단위로 읽기