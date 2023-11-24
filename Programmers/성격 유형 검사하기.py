survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

test = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
def solution(survey, choices):
    N = len(survey)
    result = dict()
    for i in range(N):
        disagree = survey[i][0]
        agree = survey[i][1]
        score = choices[i]
        if 1 <= score <= 3:  # 비동의할 경우
            result.setdefault(disagree, 0)
            result[disagree] += (score - 4)*(-1)
        elif score > 4:  # 동의할 경우
            result.setdefault(agree, 0)
            result[agree] += (score - 4)

    answer = ''
    for t in test:
        result.setdefault(t[0], 0)
        result.setdefault(t[1], 0)
        if result[t[0]] > result[t[1]]:
            answer += t[0]
        elif result[t[0]] < result[t[1]]:
            answer += t[1]
        else:
            answer += min(t[0], t[1])

    return answer

print(solution(survey, choices))