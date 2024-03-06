# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0] * len(id_list)

    # 인덱스 찾기 위한 딕셔너리
    id_dic = {x: idx for idx, x in enumerate(id_list)}

    # 신고 횟수
    reports = {x : 0 for x in id_list}

    # 신고 횟수 중복 제거
    report_set = set(report)

    # 신고 횟수 저장
    for r in report_set:
        a, b = r.split()
        reports[b] += 1

    for r in report_set:
        a, b = r.split()
        # 신고 당한 횟수가 k를 넘어서는 경우
        if reports[b] >= k:
            # 신고자의 메일 받는 횟수 증가
            answer[id_dic[a]] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))