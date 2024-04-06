from sys import stdin
from collections import Counter

input = stdin.readline

def get_hamming_word(words : list):
    return sorted(Counter(words).most_common(),key=lambda x:(-x[1],x[0]))[0]

N,M = map(int, input().split())
DNAs = [list(input().rstrip()) for _ in range(N)]
total_hamming_distance = 0
answer_dna = []

for i in range(M):
    hamming_word , frequency =  get_hamming_word(DNA[i] for DNA in DNAs)
    answer_dna.append(hamming_word)
    total_hamming_distance += N - frequency
print("".join(answer_dna))
print(total_hamming_distance)
