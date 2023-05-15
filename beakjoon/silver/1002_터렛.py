import math
from sys import  stdin
input = stdin.readline 
def calculate_distance(x1, y1, x2, y2):

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def solve_turret(x1, y1, r1, x2, y2, r2):

    distance = calculate_distance(x1, y1, x2, y2)

    if distance == 0 and r1 == r2:

        return -1

    elif distance > r1 + r2 or distance < abs(r1 - r2):

        return 0

    elif distance == r1 + r2 or distance == abs(r1 - r2):

        return 1

    else:

        return 2

test_cases = int(input())

for _ in range(test_cases):

    x1, y1, r1, x2, y2, r2 = map(int, input().rsplit())

    result = solve_turret(x1, y1, r1, x2, y2, r2)

    print(result)
