word = '2three45sixseven'

dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
def find_number(word, start):
    idx = start + 1
    while True:
        new_word = word[start:idx]
        if new_word in dic:
            return [dic[new_word], len(new_word)]
        else:
            idx += 1
def solution(word):
    N = len(word)
    answer = ''
    i = 0
    while i < N:
        if word[i].isdigit():
            answer += word[i]
            i += 1
        else:
            num, idx = find_number(word, i)
            answer += num
            i += idx

    return int(answer)


print(solution(word))