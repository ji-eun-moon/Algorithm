def solution(m, k):
    answer = ''
    message, key = 0, 0

    while message < len(m):

        # 암호 문자열 전부 확인했으면 나머지 문자열 정답 문자열에 합치고 반복문 종료
        if key >= len(k):
            answer += m[message:]
            break

        # 암호 문자열에 포함되어 있는 문자열이면 다음 문자열로 넘어감
        if m[message] == k[key]:
            message += 1
            key += 1
        # 포함되지 않는 문자열이면 정답 문자열에 추가
        else:
            answer += m[message]
            message += 1

    return answer

print(solution("kkaxbycyz", "abc"))
print(solution("acbbcdc", "abc"))