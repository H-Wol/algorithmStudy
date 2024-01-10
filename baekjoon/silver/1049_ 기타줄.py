from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

packages = []
singles = []

for _ in range(m):
    package, single = map(int, input().split())
    packages.append(package)
    singles.append(single)

min_package = min(packages)
min_single = min(singles)

package_cost = min_package * (n // 6) + min_package * \
    (n % 6 if n % 6 > 0 else 6)

single_cost = min_single * n

mixed_cost = min((n // 6 + 1) * min_package, n * min_single,
                 (n // 6) * min_package + (n % 6) * min_single)

print(min(package_cost, single_cost, mixed_cost))
