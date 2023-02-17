import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split(" ")))
ownershipList = {}
for card in cards:
    ownershipList[card] = ownershipList.get(card, 0) + 1

M = int(input())
checkList = list(map(int, input().split(" ")))
howManyList = []
for check in checkList:
    howManyList.append(ownershipList.get(check, 0))

print(" ".join(map(str, howManyList)))
