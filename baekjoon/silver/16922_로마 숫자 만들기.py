from sys import stdin

input = stdin.readline


def count_roman_combinations(N):
    romans = [1, 5, 10, 50]
    visited = set()

    def dfs(idx, current_sum, count):
        if count == N:
            visited.add(current_sum)
            return

        for i in range(idx, len(romans)):
            dfs(i, current_sum + romans[i], count + 1)

    dfs(0, 0, 0)
    return len(visited)


N = int(input())
result = count_roman_combinations(N)
print(result)
