word = input()
N = len(word)

def wolf(num):
    ret = 'w'*num + 'o'*num + 'l'*num + 'f'*num
    return ret

def solve(word):
    w = word.count('w')
    o = word.count('o')
    l = word.count('l')
    f = word.count('f')

    # 알파벳 수가 같을 때
    if w == o == l == f:
        # 1번 규칙을 만족하면 1 리턴
        if word == wolf(w):
            return 1
        # 2번 규칙을 만족하는지 확인
        else:
            # w를 하나씩 줄여나가면서 1번 규칙을 만족하는 단어를 만들고 그 단어가 포함되어 있는지 확인
            for i in range(1, w):
                # 1번 규칙을 만족하는 단어 만들기
                temp = wolf(w-i)
                # word 안에 있는 temp를 star로 대체
                while temp in word:
                    star = '*' * len(temp)
                    word = word.replace(temp, star)
            # 전부 확인 후 *로 변경되지 않은 단어가 있다면 올바르지 않은 단어
            for w in word:
                if w != '*':
                    return 0
            return 1

    # 알파벳 수가 같지 않으면 0 리턴
    else:
        return 0

print(solve(word))