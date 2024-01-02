# n*n 2차원 배열을 시계방향으로 90*d 도 회전시키는 함수
def rotate(array, d):
    N = len(array)
    ret = [[0] * N for _ in range(N)]
    if d % 4 == 1:  # 90 도
        for i in range(N):
            for j in range(N):
                ret[j][N - 1 - i] = array[i][j]
    elif d % 4 == 2:  # 180 도
        for i in range(N):
            for j in range(N):
                ret[N - 1 - i][N - 1 - j] = array[i][j]
    elif d % 4 == 3:  # 270 도
        for i in range(N):
            for j in range(N):
                ret[N - 1 - j][i] = array[i][j]
    else:  # 360도
        for i in range(N):
            for j in range(N):
                ret[i][j] = array[i][j]

    return ret

# 자물쇠 중간 부분이 모두 1인지 확인
def check(array):
    N = len(array) // 3
    for i in range(N, N*2):
        for j in range(N, N*2):
            if array[i][j] != 1:
                return False
    return True
def solution(key, lock):
    M = len(key)
    N = len(lock)

    # 자물쇠보다 3배 큰 배열 생성
    new_lock = [[0]*(N*3) for _ in range(N*3)]
    # 가운데에 자물쇠 넣기
    for i in range(N):
        for j in range(N):
            new_lock[N+i][N+j] = lock[i][j]

    # 열쇠를 넣는 모든 경우의 수 확인
    for i in range(0, 2*N):
        for j in range(0, 2*N):
            # 열쇠를 4방향으로 회전
            for d in range(4):
                rotate_key = rotate(key, d)
                # 열쇠 맞추기 전 배열 백업 해두기 - 깊은 복사
                back_up = [lst[:] for lst in new_lock]
                # 열쇠 맞추기
                for y in range(M):
                    for x in range(M):
                        new_lock[i+y][j+x] += rotate_key[y][x]
                # 열쇠 맞는지 확인
                if check(new_lock):
                    return True
                # 다시 열쇠 맞추기 전으로 돌리기
                new_lock = [lst[:] for lst in back_up]

    # 끝까지 True 를 반환하지 못하면 실패
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# solve 2
def rotate_by_zip(array, d):
    ret = array
    for i in range(d):
        ret = list(map(list, zip(*array[::-1])))
        array = ret
    return ret

# 자물쇠 중간 부분이 모두 1인지 확인
def check(array):
    N = len(array) // 3
    for i in range(N, N*2):
        for j in range(N, N*2):
            if array[i][j] != 1:
                return False
    return True

def solution(key, lock):
    M = len(key)
    N = len(lock)

    # 자물쇠보다 3배 큰 배열 생성
    new_lock = [[0]*(N*3) for _ in range(N*3)]
    # 가운데에 자물쇠 넣기
    for i in range(N):
        for j in range(N):
            new_lock[N+i][N+j] = lock[i][j]

    # 열쇠를 넣는 모든 경우의 수 확인
    for i in range(0, 2*N):
        for j in range(0, 2*N):
            # 열쇠를 4방향으로 회전
            for d in range(4):
                rotate_key = rotate_by_zip(key, d)
                # 열쇠 맞추기 전 배열 백업 해두기 - 깊은 복사
                back_up = [lst[:] for lst in new_lock]
                # 열쇠 맞추기
                for y in range(M):
                    for x in range(M):
                        new_lock[i+y][j+x] += rotate_key[y][x]
                # 열쇠 맞는지 확인
                if check(new_lock):
                    return True
                # 다시 열쇠 맞추기 전으로 돌리기
                new_lock = [lst[:] for lst in back_up]

    # 끝까지 True 를 반환하지 못하면 실패
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))