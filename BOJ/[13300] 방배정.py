N, K = map(int, input().split())  # 학생 수, 한 방의 최대 인원수

# 학년 별 인원수를 담을 성별 딕셔너리
girl = {}
boy = {}
for _ in range(N):
    S, Y = map(int, input().split())  # 성별(0 여자 1 남자), 학년
    if S == 0:
        girl.setdefault(Y, 0)
        girl[Y] += 1
    elif S == 1:
        boy.setdefault(Y, 0)
        boy[Y] += 1

# 딕셔너리 돌며 필요한 방의 수 계산
room = 0
for value in girl.values():
    temp = value//K + bool(value % K)
    room += temp

for value in boy.values():
    temp = value//K + bool(value % K)
    room += temp

print(room)
