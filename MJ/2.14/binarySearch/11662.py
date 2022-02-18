# 9:40 -> 10:20
# GG
import math
# A1x, A1y, A2x, A2y, B1x, B1y, B2x, B2y = map(int, input().split())


def calDistance(x1, y1, x2, y2):
    return math.sqrt(pow((x2-x1), 2) + pow((y2-y1), 2))


min_distance = 0


# while
# print(calDistance(0, 1, 2, 3))
# print(calDistance(1, 1, 0, 1))
