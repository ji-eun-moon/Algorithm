def solution(relation):

    y = len(relation)
    x = len(relation[0])

    idx_lst = []  # 후보키인지 확인할 컬럼 인덱스 조합
    path = []
    def combi_idx(level, start, N):
        if level == N:
            idx_lst.append(tuple(path[:]))
            return
        for i in range(start, x):
            path.append(i)
            combi_idx(level+1, i+1, N)
            path.pop()

    for i in range(1, x+1):
        combi_idx(0, 0, i)

    # 만들어진 인덱스 조합으로 후보키 만들기
    combinations = []
    for idx in idx_lst:
        part = []
        for item in relation:
            temp = tuple(item[i] for i in idx)
            part.append(tuple(temp))
        combinations.append(tuple(part))

    unique = []
    for combi in combinations:
        temp = list(set(tuple(row) for row in combi))
        if len(set(temp)) == y:
            unique.append(temp)

    # # 유일성 확인
    # unique = []
    # for idx in idx_lst:
    #     # 인덱스 리스트로 후보키 리스트를 생성
    #     part = []
    #     for r in relation:
    #         temp = tuple(r[key] for key in idx)
    #         part.append(temp)
    #     if len(set(part)) == y:
    #         unique.append(idx)

    # 최소성 확인
    answer = list(set(tuple(row) for row in unique))
    N = len(unique)
    for i in range(N):
        for j in range(i+1, N):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)

print(solution(relation=[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
