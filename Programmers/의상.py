def solution(clothes):
    answer = 1

    closet = {}
    for clothe, kind in clothes:
        closet.setdefault(kind, [])
        closet[kind].append(clothe)

    for k in closet:
        answer *= len(closet[k]) + 1

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))