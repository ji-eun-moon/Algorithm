def solution(new_id):
    answer = ''

    # 1. 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2. 소문자, 숫자 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    lst = ['-', '_', '.']
    for word in new_id:
        if word.isalpha() or word.isdigit() or word in lst:
            answer += word

    # 3. 마침표(.)가 2번 이상 연속된 부분 하나의 마침표(.)로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4. 마침표(.)가 처음이나 끝에 위치한다면 제거
    if answer:
        if answer[0] == '.':
            answer = answer[1:]

    if answer:
        if answer[-1] == '.':
            answer = answer[:-1]

    # 5. 빈 문자열이라면 a 대입
    if answer == '':
        answer = 'a'

    # 6. 16자 이상이면 첫 15개 문자를 제외한 나머지 문자 제거
    answer = answer[:15]
    # 제거 후 마침표(.)가 끝에 위치한다면 제거
    if answer[-1] == '.':
        answer = answer[:-1]

    # 7. 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(answer) < 3:
        answer += answer[-1]

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

def solution(new_id):
    answer = ''

    # 1. 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2. 소문자, 숫자 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    lst = ['-', '_', '.']
    for word in new_id:
        if word.isalpha() or word.isdigit() or word in lst:
            answer += word

    # 3. 마침표(.)가 2번 이상 연속된 부분 하나의 마침표(.)로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4. 마침표(.)가 처음이나 끝에 위치한다면 제거
    answer = answer.strip('.')

    # 5. 빈 문자열이라면 a 대입
    answer = answer if answer else 'a'

    # 6. 16자 이상이면 첫 15개 문자를 제외한 나머지 문자 제거
    # 제거 후 마침표(.)가 끝에 위치한다면 제거
    answer = answer[:15].rstrip('.')

    # 7. 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(answer) < 3:
        answer += answer[-1]

    return answer