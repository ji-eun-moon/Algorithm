import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
cards = deque(range(1, N+1))

while len(cards) > 1:
    card1 = cards.popleft()
    if len(cards) == 1:
        break
    card2 = cards.popleft()
    cards.append(card2)

print(cards[0])