n = int(input())

houses = sorted(map(int, input().split()))
print(houses[(n - 1) // 2])