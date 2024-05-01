def solution(participant, completion):
    answer = ''
    participant_dict = {}

    for p in participant:
        participant_dict.setdefault(p, 0)
        participant_dict[p] += 1

    for c in completion:
        participant_dict[c] -= 1

    for p in participant_dict:
        if participant_dict[p] == 1:
            answer = p

    return answer