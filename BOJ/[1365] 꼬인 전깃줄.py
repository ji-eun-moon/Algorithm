import bisect

N = int(input())  # 전봇대의 개수
array = list(map(int, input().split()))  # i 번째 전봇대와 연결된 전봇대 정보

def solution(array):
    n = len(array)
    answer = [array[0]]
    for i in range(1, n):
        target = array[i]
        if answer[-1] < target:
            answer.append(target)
        else:
            idx = bisect.bisect_left(answer, array[i])
            answer[idx] = target
    return len(answer)

longest = solution(array)
print(N - longest)

N = int(input())  # 전봇대의 개수
array = list(map(int, input().split()))  # i 번째 전봇대와 연결된 전봇대 정보

def binary_search(array, target):
    start, end = 0, len(array)-1 # 초기 시작점과 끝점
    while start < end:
        mid = (start + end) // 2 # 중간값

        if array[mid] == target: # 중간값이 타겟과 같다면 중간값의 위치를 반환
            return mid

        # 타겟보다 큰 값 중 가장 작은 값의 위치는
        # 아래와 같이 바로 전 값보다 크면서 바로 현재 값(중앙)보단 작은 위치이다
        elif array[mid-1] < target < array[mid]:
            return mid

        # target이 더 작으면 왼쪽 더 탐색
        elif target < array[mid]:
            end = mid - 1

        # target이 더 크면 오른쪽 더 탐색
        else:
            start = mid + 1

    return start # 만약 시작점과 끝점이 같다면 시작점을 반환

def solution(array):
    n = len(array)
    answer = [array[0]] # A 수열의 첫번째 값
    # A 수열의 두번째 값부터 LIS의 마지막 값과 비교
    for i in range(1,n):
        target = array[i]
        if answer[-1] < target: # 타겟이 더 크다면 LIS 에 추가
            answer.append(target)
        else: # 타겟이 더 작다면 이분탐색을 통해 LIS 갱신
            idx = binary_search(answer, target)
            answer[idx] = target

    return len(answer) # 최종 LIS 길이 반환

longest = solution(array)
print(N - longest)