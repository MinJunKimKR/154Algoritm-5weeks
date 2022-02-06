def merge_sort(array):
  if len(array) <= 1:
    return array

  # Step 1. 배열 분할
  mid = len(array) //2
  left = merge_sort(array[:mid])
  right = merge_sort(array[mid:])

  i, j, k = 0,0,0
  # i: left index
  # j: right index
  # k: array index

  # Step 2. 분할 배열 요소 중 작은 크기대로 새로운 배열에 병합
  while i< len(left) and j < len(right):
    if left[i] < right[j]:
      array[k] = left[i]
      i += 1
    else:
      array[k] = right[j]
      j += 1
    k +=  1

  # Step 3. 나머지 한 배열 비교가 끝난 경우, 남은 배열 값들 다 넣어 주기
  if i == len(left):
    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1
  elif j == len(right):
    while i < len(left):
      array[k] = left[i]
      i += 1
      k += 1
    return array

# 입력
n = int(input())

num = []
for _ in range(n):
  num.append(int(input()))

num_sorted = merge_sort(num)
print(num_sorted)

'''
for i in range(n):
  for j in range(1, n):
    if li[j-1] > li[j]:
      li[j-1], li[j] = li[j], li[j-1]
'''
# N의 범위가 100만이라 시간 초과!!
# O(NlogN)까지 가능 -> 1-^6번 연산 가능
# 병합정렬 (분할정복), 퀵정렬, 힙정렬 만 가능하다. + or 기본정렬
# 파이썬 기본정렬: A.sort(), A.sorted()

# https://assaeunji.github.io/python/2020-05-06-bj2751/