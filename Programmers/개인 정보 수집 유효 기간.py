def solution(today, terms, privacies):
    answer = []
    terms_dic = {}

    # 딕셔너리에 약관 종류별 유효기간 저장
    for term in terms:
        kind, period = term.split()
        terms_dic[kind] = int(period) * 28

    # 문자열 날짜를 day 수로 바꾸는 함수
    def format_date(date):
        year, month, day = date.split('.')
        return int(year)*12*28 + int(month)*28 + int(day)

    # 오늘 날짜
    today = format_date(today)

    for idx, privacy in enumerate(privacies):
        date, kind = privacy.split()

        # 만약 유효기간이 넘은 정보라면 삭제 리스트에 추가
        if terms_dic[kind] <= today - format_date(date):
            answer.append(idx + 1)

    return sorted(answer)

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))