T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))

    def game(player):
        player = sorted(player)
        for i in range(len(player)):
            if player.count(player[i]) >= 3:
                return 1
            if (player[i]+1) in player and (player[i]+2) in player:
                return 1
        return 0

    player1 = []
    player2 = []

    for i in range(12):
        if i % 2 == 0:
            player1.append(arr[i])
        else:
            player2.append(arr[i])

        p1 = game(player1)
        p2 = game(player2)
        if p1 > p2:
            result = 1
            break
        elif p1 < p2:
            result = 2
            break
        else:
            result = 0

    print(f'#{test_case} {result}')

