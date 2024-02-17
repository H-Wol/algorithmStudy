from sys import stdin

input = stdin.readline


def min_time_to_arrive(N, M, times):
    low, high = 0, max(times) * M

    while low < high:
        mid = (low + high) // 2

        # mid 시간 동안 각 직원이 도착하는 횟수
        arrivals = sum(mid // time for time in times)

        if arrivals >= M:
            high = mid
        else:
            low = mid + 1

    return low


N, M = map(int, input().split())
times = list(map(int, input().split()))

result = min_time_to_arrive(N, M, times)
print(result)
