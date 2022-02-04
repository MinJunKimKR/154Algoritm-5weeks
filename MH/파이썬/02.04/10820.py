while 1:
    try:
        word = input()
        up,lo,sp,nu = 0,0,0,0

        for i in word:
            if i.isupper():
                up+=1
            elif i.islower():
                lo+=1
            elif i.isdigit():
                nu+=1
            elif i.isspace():
                sp+=1
        print("{} {} {} {}".format(lo,up,nu,sp))
    except:
        break

# import sys
# while True:
#     line = sys.stdin.readline().rstrip('\n')
#     up, lo, sp, nu = 0, 0, 0, 0
#     if not line:
#         break
#     for l in line:
#         if l.isupper():
#             up += 1
#         elif l.islower():
#             lo += 1
#         elif l.isdigit():
#             nu += 1
#         elif l.isspace():
#             sp += 1
#     sys.stdout.write("{} {} {} {}\n".format(lo, up, nu, sp))

