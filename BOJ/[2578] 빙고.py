cheolsu = [list(map(int, input().split())) for _ in range(5)]
game = []
for _ in range(5):
    game += list(map(int, input().split()))

def bingo():

    bingo = 0
    # 가로 확인
    for i in range(5):
        flag = 0
        for j in range(5):
            if cheolsu[i][j] == 0:
                flag += 1
        if flag == 5:
            bingo += 1

    # 세로 확인
    for i in range(5):
        flag = 0
        for j in range(5):
            if cheolsu[j][i] == 0:
                flag += 1
        if flag == 5:
            bingo += 1
    # 대각선 확인 1
    flag = 0
    for i in range(5):
        if cheolsu[i][i] == 0:
            flag += 1
    if flag == 5:
        bingo += 1
    # 대각선 확인 2
    flag = 0
    for i in range(5):
        if cheolsu[i][4-i] == 0:
            flag += 1
    if flag == 5:
        bingo += 1

    return bingo


for n in range(25):
    for i in range(5):
        for j in range(5):
            if game[n] == cheolsu[i][j]:
                cheolsu[i][j] = 0
    if bingo() >= 3:
        print(n+1)
        break

