e,s,m = map(int,input().split())

_e,_s,_m,cnt = 1,1,1,1

while True:
    if _e == e and _s == s and _m == m:
        break
    _e+=1
    _s+=1
    _m+=1
    cnt+=1
    if _e >= 16:
        _e-=15
    if _s >= 29:
        _s-=28
    if _m >= 20:
        _m-=19