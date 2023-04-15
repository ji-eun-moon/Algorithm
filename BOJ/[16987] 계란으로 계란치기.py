N = int(input())
egg = []
for _ in range(N):
    S, W = map(int, input().split())
    egg.append([S, W])

Max = 0
cnt = 0
def dfs(level):
    global Max, cnt
    if level == N:
        if Max < cnt:
            Max = cnt
        return
    if egg[level][0] <= 0:  # 이미 깨진 계란이면 다음 계란 확인하기
        dfs(level+1)
    else:
        flag = 0
        for i in range(N):
            if level != i and egg[i][0] > 0:  # 다른 계란이고 아직 깨지지 않았으면
                flag = 1
                egg[level][0] -= egg[i][1]  # 내구도 감소하기
                egg[i][0] -= egg[level][1]
                backup = cnt
                if egg[level][0] <= 0:
                    cnt += 1
                if egg[i][0] <= 0:
                    cnt += 1
                dfs(level+1)
                egg[level][0] += egg[i][1]  # 원상 복구
                egg[i][0] += egg[level][1]
                cnt = backup
        if flag == 0:  # 한개도 못깨뜨렸으면 다음 계란 확인
            dfs(level+1)

dfs(0)
print(Max)