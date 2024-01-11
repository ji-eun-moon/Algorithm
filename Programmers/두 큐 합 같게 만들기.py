from collections import deque
def solution(queue1, queue2):

    qSum = sum(queue1) + sum(queue2)

    if qSum % 2:
        return -1

    target = (qSum) // 2

    if max(queue1) > target or max(queue2) > target:
        return -1

    cnt = 0

    q1, q1Sum = deque(queue1), sum(queue1)
    q2, q2Sum = deque(queue2), sum(queue2)

    while q2:
        if q1Sum > target:
            num = q1.popleft()
            q1Sum -= num
            cnt += 1
        elif q1Sum < target:
            num = q2.popleft()
            q1.append(num)
            q1Sum += num
            cnt += 1
        elif q1Sum == target:
            return cnt

    return -1

print('#1', solution([3, 2, 7, 2], [4, 6, 5, 1]))
print('#2', solution([1, 2, 1, 2], [1, 10, 1, 2]))
print('#3', solution([1, 1], [1, 5]))

# 큐
from collections import deque
def solution(queue1, queue2):

    N = len(queue1)
    qSum = sum(queue1) + sum(queue2)

    if qSum % 2:
        return -1

    target = (qSum) // 2
    if max(queue1) > target or max(queue2) > target:
        return -1

    cnt = 0

    q1, q1Sum = deque(queue1), sum(queue1)
    q2, q2Sum = deque(queue2), sum(queue2)

    for i in range(0, 4*N):
        if q1Sum == q2Sum:
            return cnt
        elif q1Sum < q2Sum:
            temp = q2.popleft()
            q1.append(temp)
            q1Sum += temp
            q2Sum -= temp
            cnt += 1
        else:
            temp = q1.popleft()
            q2.append(temp)
            q1Sum -= temp
            q2Sum += temp
            cnt += 1

    return -1

print('#1', solution([3, 2, 7, 2], [4, 6, 5, 1]))
print('#2', solution([1, 2, 1, 2], [1, 10, 1, 2]))
print('#3', solution([1, 1], [1, 5]))

# 투 포인터
def solution(queue1, queue2):

    N = len(queue1)
    q = queue1 + queue2

    qSum = sum(queue1) + sum(queue2)

    if qSum % 2:
        return -1

    target = (qSum) // 2
    if max(queue1) > target or max(queue2) > target:
        return -1

    q1Sum = sum(queue1)

    cnt = 0
    i, j = 0, N

    while True:
        if q1Sum > target:
            q1Sum -= q[i]
            i += 1
            cnt += 1
        elif target > q1Sum:
            q1Sum += q[j]
            j += 1
            cnt += 1
        else:
            return cnt
        if (i == j) or (j == 2*N):
            return -1

    return -1

print('#1', solution([3, 2, 7, 2], [4, 6, 5, 1]))
print('#2', solution([1, 2, 1, 2], [1, 10, 1, 2]))
print('#3', solution([1, 1], [1, 5]))


