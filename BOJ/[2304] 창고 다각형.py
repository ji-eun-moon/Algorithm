N = int(input())
box = [0]*1001  # L 범위가 1000 까지 이므로
# 기둥 높이 입력 받기 : L - x좌표, H - 높이
Max = 0  # 최대 높이
ed = 0  # 마지막 인덱스
for _ in range(N):
    L, H = map(int, input().split())
    box[L] = H
    Max = max(Max, H)
    ed = max(ed, L)

box = box[:ed+1]  # 마지막 인덱스까지 잘라버리기

# 최댓값 인덱스 모으기
Max_lst = []
for idx in range(len(box)):
    if box[idx] == Max:
        Max_lst.append(idx)
Max_st = Max_lst[0]  # 첫번째 최댓값
Max_ed = Max_lst[-1]  # 마지막 최댓갔
# 최댓값 사이에 있는 것들은 전부 최댓값으로 저장
for i in range(Max_st, Max_ed+1):
    box[i] = Max

# 앞 인덱스가 뒤 인덱스보다 크면 뒤 인덱스에 앞 인덱스 값 저장하고 최대 높이가 나오면 break
# 앞에서부터 탐색
for i in range(ed):
    if box[i] != Max and (box[i] >= box[i+1]):
        box[i+1] = box[i]
    if box[i] == Max:
        break
# 뒤에서부터 탐색
for i in range(ed):
    if box[ed-i] != Max and (box[ed-i] >= box[ed-i-1]):
        box[ed-i-1] = box[ed-i]
    if box[ed-i] == Max:
        break

print(sum(box))
