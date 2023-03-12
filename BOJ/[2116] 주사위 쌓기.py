N = int(input())  # 주사위 개수
dice = [list(map(int, input().split())) for _ in range(N)]  # 주사위 정보
match = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}  # 짝 찾는 딕셔너리

Max = 0  # 최댓값
for i in range(6):  # 첫 번째 주사위 고르기 (1~6까지 전부 확인하기)
    answer = 0
    temp = [1, 2, 3, 4, 5, 6]
    bottom = dice[0][i]  # 밑에 오는 숫자
    top = dice[0][match[i]]  # 위에 오는 숫자
    temp.remove(bottom)  # bottom, top 제거
    temp.remove(top)
    answer += max(temp)  # 남는 것들 중에 가장 큰 숫자 더하기
    for j in range(1, N):  # 두번째 주사위부터 마지막 주사위까지 확인
        temp = [1, 2, 3, 4, 5, 6]
        bottom = top  # 이전 top 숫자가 bottom
        temp.remove(bottom)
        top = dice[j][match[dice[j].index(bottom)]]  # bottom에 맞는 top 찾기
        temp.remove(top)
        answer += max(temp)  # bottom, top 제거하고 남는 것들 중에 가장 큰 숫자 더하기
    if answer > Max:  # answer 최댓값 구하기
        Max = answer

print(Max)
