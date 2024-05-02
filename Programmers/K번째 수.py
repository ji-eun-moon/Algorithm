def solution(array, commands):

    answer = []
    for st, ed, target in commands:
        tmp = array[st-1:ed]
        tmp.sort()
        answer.append(tmp[target-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))