N,M = map(int,input().split())

def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

five_count = count_number(N, 5) - count_number(M, 5) - count_number(N - M, 5)
two_count = count_number(N, 2) - count_number(M, 2) - count_number(N - M, 2)

answer = min(five_count, two_count)
print(answer)