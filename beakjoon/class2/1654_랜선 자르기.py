import sys
sys.setrecursionlimit(10**6)
K, N = map(int, sys.stdin.readline().split())


def final(min, max):
    if sum(i//max for i in lanLengths) >= N:
        return max
    else:
        return min


def binarySearch(min, max):
    if max == min:
        return min
    if max-1 == min:
        return final(min, max)
    mid = (min + max) // 2

    res = sum(i//mid for i in lanLengths)
    if res >= N:
        return binarySearch(mid, max)
    else:
        return binarySearch(min, mid)


total = 0
lanLengths = []
for i in range(K):
    lan = int(sys.stdin.readline())
    lanLengths.append(lan)
    total += lan

maxLanLength = total // N

print(int(binarySearch(1, maxLanLength)))
