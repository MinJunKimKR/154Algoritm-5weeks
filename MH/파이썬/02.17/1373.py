# import sys
# input = sys.stdin.readline
# n=input().strip()
# n = n[::-1]
#
# ten = 0
# for i in range(len(n)):
#     ten += int(n[i]) * (2**i)
#
# ans = ""
# while ten != 0:
#     ans += str(ten%8)
#     ten = ten//8
#
# print(ans[::-1])

print(oct(int(input(),2))[2:])


