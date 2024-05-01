def solution(phone_book):

    word_dic = {}
    word_len = []

    for p in phone_book:
        word_dic.setdefault(p, True)
        word_len.append(len(p))

    word_len = list(set(word_len))

    for word in word_dic:
        for l in word_len:
            if len(word) <= l:
                continue
            if word[:l] in word_dic:
                return False

    return True
