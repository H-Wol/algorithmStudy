import sys
import re
input = sys.stdin.readline

S = input().rstrip()
pattern = r"(<|>|&&|\|\||\(|\)|\s)"

tokens = re.split(pattern, S)
tokens = [t for t in tokens if t not in ["", " "]]
print(" ".join(map(str, tokens)))
