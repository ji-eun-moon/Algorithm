'''
1. 작업이 요청되는 시간이 빠른 순서대로 정렬
2. 현재 시간에 처리할 수 있는 작업들 중에서 소요 시간이 가장 적은 작업부터 처리
    1. 현재 시간에서 처리할 수 있는 작업들을 우선순위 큐에 추가 → `[소요시간, 요청시간]` 형태로
    2. 우선 순위 큐를 이용해서 소요시간이 가장 적은 작업을 선택
    3. 현재 시간을 업데이트
'''

# sol 1

def solution(jobs):  # [요청 시간, 소요 시간]
    jobs.sort(key= lambda x: x[0])  # 요청시간이 빠른 순으로 정렬
    now = 0  # 현재 시간
    completed = 0  # 완료한 작업 수
    total = 0  # 총 작업 시간
    N = len(jobs)
    start = -1  # 이전 작업 종료 시간

    heap = []
    # 모든 작업 처리할 때까지 반복문 수행
    while completed < N:

        for i in range(N):
            request, duration = jobs[i]
            # 아직 처리하지 않은 작업이고, 현재 처리할 수 있다면
            if start < request <= now:
                # 우선 순위 큐에 추가
                heapq.heappush(heap, (duration, request))

        # 처리할 작업이 있으면
        if heap:
            start = now  # 이전 작업 종료 시간 갱신
            duration, request = heapq.heappop(heap)  # 소요시간이 가장 적은 작업 선택
            now += duration  #
            total += now - request
            completed += 1
        else:
            now += 1

    return total // N

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[7, 8], [3, 5], [9, 6]]))

# sol 2

def solution(jobs):
    answer = 0
    start = 0
    N = len(jobs)

    # 소요시간을 기준으로 내림차순
    jobs = sorted(jobs, key=lambda x: x[1])

    while jobs:
        for i in range(len(jobs)):  # pop을 사용하므로 N 을 그대로 쓰면 안된다! - 인덱스 에러
            flag = 0
            request, duration = jobs[i]
            # 처리할 수 있는 작업이 있으면
            if request <= start:
                flag = 1
                start += duration  # 시작 시간 갱신
                answer += start - request  # 처리 시간 갱신
                jobs.pop(i)
                break
        # 아무것도 처리하지 못했으면 시작 시간 + 1
        if flag == 0:
            start += 1

    return answer // N

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[7, 8], [3, 5], [9, 6]]))

# sol 3

import heapq

def solution(jobs):
    # 작업이 요청되는 시점이 빠른 순서로 정렬
    jobs.sort()

    # 현재 시간에 처리할 수 있는 작업들 중에서 작업의 소요시간이 가장 적은 작업부터 처리
    heap = []  # 작업을 관리할 힙 초기화

    # 현재 시간, 완료된 작업 수, 총 대기 시간
    current_time, completed_jobs, total_response_time = 0, 0, 0
    jobs_idx = 0  # 현재 처리 중인 jobs 인덱스

    # 모든 작업이 완료될 때까지 반복
    while completed_jobs < len(jobs):
        # 현재 시간에서 처리할 수 있는 작업들을 우선순위 큐에 추가
        while jobs_idx < len(jobs) and jobs[jobs_idx][0] <= current_time:
            start, duration = jobs[jobs_idx]
            heapq.heappush(heap, (duration, start))
            jobs_idx += 1

        # 우선순위 큐를 이용해서 소요시간이 가장 적은 작업을 선택 하여 처리
        if heap:  # 처리할 작업이 있으면 처리
            duration, start = heapq.heappop(heap)
            current_time += duration
            total_response_time += current_time - start
            completed_jobs += 1
        else:  # 처리할 작업이 없다면 현재 시간 증가
            current_time = jobs[jobs_idx][0]

    # 총 대기 시간의 평균을 계산하여 반환
    return total_response_time // completed_jobs