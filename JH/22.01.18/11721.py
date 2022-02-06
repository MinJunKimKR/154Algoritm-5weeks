words = input()

'''
start = 0
while 1:
  if start < len(words):
    print(words[start:start+10])
    start = start + 10
  else:
    print(words[start+10:]) #엔터 하나가 더 출력됨
    break
'''
for i in range(0, len(words), 10):
  print(words[i:i+10])

# for문 사용: for(0, len(words), 10) -> 10 간격으로 이동