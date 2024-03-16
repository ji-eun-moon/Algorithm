def solution(n, t, m, timetable):
    # 09:00 부터 총 n회 t분 간격으로 역에 도착
    # 하나의 셔틀에는 최대 m명의 승객이 탈 수 있음
    # 콘이 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 도착 시간?
    # 콘은 같은 시각 도착한 크루 중에서 대기열에서 가장 늦게 선다.

    answer = 0
    # 모든 시간을 분으로 환산해서 생각
    # 크루 도착 시각 리스트
    crewTime = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    crewTime.sort()  # 먼저 온 크루가 앞에 오도록 정렬
    # 버스 도착 시각 리스트
    busTime = [9 * 60 + t * i for i in range(n)]

    i = 0  # 다음에 버스에 오를 크루의 인덱스
    for time in busTime:
        cnt = 0  # 버스에 타는 크루 수
        # 버스에 자리가 남아있고, 탑승할 크루가 남아있고, 해당 크루가 버스 도착 시간 전에 도착했을 경우
        while cnt < m and i < len(crewTime) and crewTime[i] <= time:
            i += 1
            cnt += 1
        # 버스에 자리가 남았을 경우
        if cnt < m:
            answer = time
        # 버스에 자리가 없는 경우 맨 마지막 크루보다 1분 먼저 도착
        else:
            answer = crewTime[i - 1] - 1

    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))