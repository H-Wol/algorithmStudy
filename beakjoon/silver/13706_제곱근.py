N = int(input())


def sqrt(x):
    if x < 2:
        return x
    start = 0
    end = x // 2
    while start <= end:
        mid = (start + end) // 2
        sqr = mid * mid
        if sqr == x:
            return mid
        if sqr < x:
            start = mid + 1
        else:
            end = mid - 1


print(sqrt(N))
