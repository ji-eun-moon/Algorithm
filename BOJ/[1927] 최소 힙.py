import sys
input = sys.stdin.readline

# 1. 모듈 사용
from heapq import heappush, heappop

heap = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(heap) > 0:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, num)

# 2. 직접 구현
def heappush(heap, data):
    heap.append(data)
    # 추가한 원소의 인덱스를 구한다.
    current = len(heap) - 1
    # 현재 원소가 루트(인덱스 0)에 도달하면 종료
    while current > 0:
        # 추가한 원소의 부모 인덱스를 구한다.
        parent = (current - 1) // 2
        if heap[parent] > heap[current]:
            heap[parent], heap[current] = heap[current], heap[parent]
            # 추가한 원소의 인덱스를 갱신한다.
            current = parent
        else:
            break

def heappop(heap):
    # heap이 비어 있으면 0 반환
    if not heap:
        return 0
    # 루트노드만 있으면 pop한 값 반환
    elif len(heap) == 1:
        return heap.pop()

    # 루트 노드의 값 임시 저장, 루트 노드에는 heap에서 pop한 마지막 값 넣기
    pop_data, heap[0] = heap[0], heap.pop()
    current, child = 0, 1  # 현재 노드, 왼쪽 자식 노드
    # 왼쪽 자식노드가 heap 길이보다 작으면 반복
    while child < len(heap):
        sibling = child + 1  # 오른쪽 자식 노드
        # 왼쪽자식 노드가 오른쪽 자식 노드보다 크면 자식 = 오른쪽 자식 노드
        if sibling < len(heap) and heap[child] > heap[sibling]:
            child = sibling
        # 현재 노드와 작은 자식 노드 비교
        # 현재 노드의 값이 자식 노드의 값보다 크면 swap하고 인덱스 갱신
        if heap[current] > heap[child]:
            heap[current], heap[child] = heap[child], heap[current]
            current = child
            child = current * 2 + 1
        else:
            break
    return pop_data

heap = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        print(heappop(heap))
    else:
        heappush(heap, num)
