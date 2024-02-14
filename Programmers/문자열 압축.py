def solution(s):
    answer = 1000

    def compress(length):
        word = [s[i:i+length] for i in range(0, len(s), length)]
        word.append('0')  # 마지막 문자까지 처리하기 위해서
        result = ""
        prev = ""
        cnt = 0

        for w in word:
            # 이전 단어와 같다면
            if w == prev:
                cnt += 1
            # 이전 단어와 같지 않다면
            else:
                # 첫 단어 일 때
                if cnt == 0:
                    cnt += 1
                    prev = w
                else:
                    if cnt == 1:
                        result += prev
                    else:
                        result += (str(cnt) + prev)
                    prev = w
                    cnt = 1

        return len(result)

    # if len(s) == 1:
    #     return 1

    for n in range(1, len(s)+1):
        answer = min(compress(n), answer)

    return answer

print(solution("a"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"	))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))