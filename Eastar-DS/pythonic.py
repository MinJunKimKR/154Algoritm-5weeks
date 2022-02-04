#알고리즘 이용할것들

#90도 회전
def rotate(arr):
    return list(zip(*arr[::-1]))

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [(7, 4, 1)
# (8, 5, 2)
# (9, 6, 3)]

