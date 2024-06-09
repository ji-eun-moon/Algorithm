def solution(bandage, health, attacks):
    t, x, y = bandage

    end_time = attacks[-1][0]
    status = [0] * (end_time + 1)
    status[0] = health

    attack = [0] * (end_time + 1)

    for time, damage in attacks:
        attack[time] = damage

    success = 0
    for i in range(1, end_time + 1):
        if attack[i]:  # 공격 받은 경우
            status[i] = status[i - 1] - attack[i]
            success = 0
            if status[i] <= 0:
                return -1
        else:  # 공격 받지 않은 경우
            status[i] = min(health, status[i - 1] + x)
            success += 1
            if success == t:
                status[i] = min(health, status[i] + y)
                success = 0

    if status[-1] <= 0:
        return -1
    else:
        return status[-1]