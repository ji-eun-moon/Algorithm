import re

while True:
    try:
        n = int(input())
        result = []
        word_dic = {}
        while True:
            word = input()
            if word == 'EndOfText':
                break
            word_list = re.split(r"[^a-zA-Z]", word)  # 문자가 아닌 것을 기준으로 단어 구분
            for w in word_list:  # 딕셔너리 이용해서 단어 개수 세기
                word_dic.setdefault(w.lower(), 0)
                word_dic[w.lower()] += 1

        for key, value in word_dic.items():  # 단어 개수가 n개인 것만 담기
            if value == n:
                result.append(key)

        result.sort()  # 사전 순 정렬
        if result:  # result가 빈배열 아니면 출력
            for r in result:
                print(r)
            print()
        else:
            print('There is no such word.')
            print()
    except:
        break


# sol2

import re

flag = 0
n = int(input())

while True:
    if flag:
        break
    result = []
    word_dic = {}
    while True:
        word = input()
        if word == 'EndOfText':
            try:
                next_n = int(input())
            except:
                flag = 1
            break
        word_list = re.split(r"[^a-zA-Z]", word)  # 문자가 아닌 것을 기준으로 단어 구분
        for w in word_list:  # 딕셔너리 이용해서 단어 개수 세기
            word_dic.setdefault(w.lower(), 0)
            word_dic[w.lower()] += 1

    for key, value in word_dic.items():  # 단어 개수가 n개인 것만 담기
        if value == n:
            result.append(key)

    result.sort()  # 사전 순 정렬
    if result:  # result가 빈배열 아니면 출력
        for r in result:
            print(r)
        print()
    else:
        print('There is no such word.')
        print()

    n = next_n