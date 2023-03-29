changes = int(input())

coin = [10, 40, 60]

Min = 21e8
def abc(level, changes):
    global Min
    if changes < 0:  # 거스름돈이 음수가 되면 되돌아가기
        return
    if changes == 0:  # 거스름돈이 0일 경우 최소값 갱신
        Min = min(level, Min)
        return
    for i in range(3):
        abc(level+1, changes-coin[i])

abc(0, changes)
print(Min)