N = int(input())
card = [4, 3, 2, 1]
for _ in range(N):
    A, *Alst = map(int, input().split())
    B, *Blst = map(int, input().split())
    winner = 'D'
    for i in range(4):
        if Alst.count(card[i]) > Blst.count(card[i]):
            winner = 'A'
            break
        elif Alst.count(card[i]) < Blst.count(card[i]):
            winner = 'B'
            break
        else:
            continue
    print(winner)