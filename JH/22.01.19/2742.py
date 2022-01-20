#a = list(range(1, int(input())+1))
#a.sort(reverse=True)

a = range(int(input()), 0, -1)
print('\n'.join(map(str, a)))


## range 사용법
# start, end, 간격 설정 (음수도 가능하다.)