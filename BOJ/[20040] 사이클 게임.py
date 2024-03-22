'''
사이클을 완성하는 순간 게임 종료
사이클 C : 플레이어가 그린 선분들의 부분집합
사이클이 처음으로 만들어진 차례의 번호를 양의 정수로 출력
사이클 만들어 지지 않으면 0 출력

유니언 파인드 최적화 필요
'''
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, M = map(int, input().split())  # 점의 개수, 진행된 차례의 수
answer = 0
parents = [i for i in range(N)]

# 재귀로 구현
def findparents(child):
    if parents[child] == child:
        return child
    # 1. 경로 압축
    parents[child] = findparents(parents[child])
    return parents[child]

def setunion(a, b):
    fa, fb = findparents(a), findparents(b)
    if fa == fb:
        return 1
    # 2. rank가 더 높은 트리가 부모가 됨
    if parents[a] < parents[b]:
        parents[fa] = fb
    else:
        parents[fb] = fa


# 사이클 확인
for i in range(M):
    a, b = map(int, input().split())
    if setunion(a, b):
        answer = i + 1
        print(answer)
        exit(0)

print(answer)