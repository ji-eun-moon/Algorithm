N, M = map(int, input().split())  # 과목, 마일리지
lst = []  # 강의를 수강신청하는데 필요한 마일리지

for i in range(N):
    person, limit = map(int, input().split())
    temp = list(map(int, input().split()))  # 각 신청자가 마일리지 넣은 수
    if person >= limit:  # 수강인원이 모자라면
        temp.sort(reverse=True)
        need = temp[limit-1]  # 문닫고 들어간 사람과 같은 마일리지가 필요 (마일리지가 같다면 성준이에게 우선순위)
        lst.append(need)
    else:  # 자리가 남아있으면
        lst.append(1)  # 무조건 1 이상 넣어야 함.

lst.sort()

cnt = 0
for i in range(N):
    if M - lst[i] >= 0:
        cnt += 1
        M -= lst[i]
    else:
        break

print(cnt)