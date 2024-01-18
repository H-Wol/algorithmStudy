
from sys import stdin

input = stdin.readline

n = int(input())
energy = list(map(int, input().split()))


def max_energy_collection(n, energy):
    if n == 2:
        return 0

    max_energy = 0

    for i in range(1, n - 1):
        current_energy = energy[i - 1] * energy[i + 1]
        new_energy = energy[:i] + energy[i + 1:]
        max_energy = max(max_energy, max_energy_collection(
            n - 1, new_energy) + current_energy)

    return max_energy


result = max_energy_collection(n, energy)
print(result)
