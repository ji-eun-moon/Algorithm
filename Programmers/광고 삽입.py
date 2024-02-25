def solution(play_time, adv_time, logs):

    # 문자열 시간 -> 초로 바꾸는 함수
    def time_to_second(time):
        h, m, s = time.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    # 초 -> 문자열 시간으로 바꾸는 함수
    def second_to_time(time):
        hour = str(time // 3600).zfill(2)
        minute = str(time % 3600 // 60).zfill(2)
        second = str(time % 3600 % 60).zfill(2)
        return hour + ":" + minute + ":" + second

    play_time = time_to_second(play_time)
    adv_time = time_to_second(adv_time)
    time = [0] * (play_time + 1)

    # 모든 로그들에 대해 시작 시간, 종료 시간 체크
    for log in logs:
        start, end = log.split('-')
        time[time_to_second(start)] += 1
        time[time_to_second(end)] -= 1

    # 각 시간의 시청자 수 구하기
    for i in range(1, play_time):
        time[i] = time[i] + time[i-1]

    # 각 시간의 누적 시청자 수 구하기
    for i in range(1, play_time):
        time[i] = time[i] + time[i-1]

    # 광고를 삽입했을 떄, 누적 시청자 수와 기존 최대 누적 시청자 수 비교
    view = 0
    answer = 0
    for i in range(adv_time-1, play_time):  # 광고 끝 시간을 기준으로 잡음
        if view < time[i] - time[i-adv_time]:  # 같은 경우는 시작 시간이 빠른 경우가 정답이므로
            view = time[i] - time[i-adv_time]
            answer = i - adv_time + 1

    return second_to_time(answer)


print('# 1', solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print('# 2', solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print('# 3', solution("50:00:00", 	"50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))