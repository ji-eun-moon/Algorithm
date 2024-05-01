def solution(nums):
    answer = 0

    N = len(nums) // 2

    poke = dict()
    for n in nums:
        poke.setdefault(n, 0)
        poke[n] += 1

    if len(poke) >= N:
        answer = N
    else:
        answer = len(poke)

    return answer