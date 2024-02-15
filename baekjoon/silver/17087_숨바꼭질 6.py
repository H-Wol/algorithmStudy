from sys import stdin
import math

input = stdin.readline


def find_gcd_of_distances(positions):
    distances = [abs(positions[i] - positions[i+1])
                 for i in range(len(positions)-1)]
    gcd_result = math.gcd(*distances)
    return gcd_result


N, S = map(int, input().split())
positions = list(map(int, input().split()))

positions.append(S)
result = find_gcd_of_distances(positions)
print(result)
