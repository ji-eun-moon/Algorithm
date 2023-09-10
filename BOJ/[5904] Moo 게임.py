N = int(input())

# 수열은 left, mid, right로 구성

def recursive(total, mid, N):
    if N <= 3:
        return "moo"[N - 1]

    # 왼쪽 수열 길이 = 가운데를 제외한 절반
    left = (total - mid) // 2

    # 찾으려는 순서가 왼쪽 수열에 있으면, 그 전 수열에서 찾기
    if N <= left:
        return recursive(left, mid-1, N)

    # 찾으려는 순서가 오른쪽 수열에 있으면 왼쪽 수열의 순서로 바꾸고 그 전 수열로 가기
    if N > left + mid:
        return recursive(left, mid-1, N-left-mid)

    # 찾으려는 순서가 가운데 일 때
    # 찾으려는 순서가 가운데의 첫번째이면 m, 아니면 o
    if N - left == 1:
        return 'm'
    else:
        return 'o'

# 몇 번째 수열에 위치하는지 구하기
# 수열의 총 길이 = 이전 수열 * 2 + 추가 되는 수열 길이
#            = 이전 수열 * 2 + (수열의 순서 + 3)
total = 3  # 처음 3글자
k = 0  # 수열 순서
while total < N:
    k += 1
    total = 2 * total + (k + 3)

# 가운데 길이 = 수열 순서 + 3
print(recursive(total, k+3, N))