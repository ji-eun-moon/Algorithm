from heapq import heappush, heappop

words = list(input())
def heap_sort(words):
    heap = []
    # 모든 원소를 차례대로 힙에 삽입
    for word in words:
        heappush(heap, (-ord(word), word))

    result = []
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    while heap:
        result.append(heappop(heap)[1])
    return result

answer = heap_sort(words)
for a in answer:
    print(a, end='')