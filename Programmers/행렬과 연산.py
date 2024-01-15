from collections import deque
def solution(rc, operations):
    N = len(rc)
    M = len(rc[0])

    # left, mid, right 로 배열 나누기
    left = deque()
    mid = deque()
    right = deque()
    for i in range(N):
        left.append(rc[i][0])
        mid.append(deque(rc[i][1:-1]))
        right.append(rc[i][-1])

    # 순서대로 연산
    for op in operations:
        if op == 'ShiftRow':
            left.appendleft(left.pop())
            mid.appendleft(mid.pop())
            right.appendleft(right.pop())
        else:
            mid[0].appendleft(left.popleft())
            right.appendleft(mid[0].pop())
            mid[-1].append(right.pop())
            left.append(mid[-1].popleft())

    # 다시 2차원 배열로 만들기
    answer = []
    for i in range(N):
        answer.append([left[i]] + list(mid[i]) + [right[i]])

    return answer

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))