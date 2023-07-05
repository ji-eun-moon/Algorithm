import sys
input = sys.stdin.readline

N, target = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

# 이진 탐색
def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

def solve():
    # 1개 선택 확인
    if binary_search(0, N-1, target):
        return 1

    # 2개 선택 확인
    i, j = 0, N-1
    while i < j:
        Sum = data[i] + data[j]
        if Sum > target:  # 합이 타겟 보다 큰 경우
            j -= 1  # j 인덱스 감소
        elif Sum == target:  # 합이 타겟과 같은 경우
            return 1  # 성공
        else:  # 합이 타겟보다 작은 경우
            new_target = target - Sum  # 3개 선택 확인
            # i, j 인덱스 값은 new_target이 아니어야 함 (물건은 한 번밖에 못쓰므로!!)
            if data[i] != new_target and data[j] != new_target and binary_search(0, N-1, new_target):
                return 1
            i += 1

    return 0

print(solve())