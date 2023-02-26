N = int(input())  # 스위치 개수
lst = list(map(int, input().split()))  # 스위치 상태 - 1 켜짐 0 꺼짐
st = int(input())  # 학생 수

reverse_switch = {0:1, 1:0}

def boy(num):
    for i in range(len(lst)):
        if (i+1) % num == 0:  # 스위치 번호가 받은 수의 배수이면
            lst[i] = reverse_switch[lst[i]]

def girl(num):
    for i in range(num-1):  # 맨 앞부터 받은 수 전까지 확인
        if num-1-(i+1) >= 0 and num-1+(i+1) < N:  # 인덱스 범위 확인
            if lst[num-1-(i+1)] != lst[num-1+(i+1)]:
                break
            if lst[num-1-(i+1)] == lst[num-1+(i+1)]:
                lst[num-1-(i+1)] = reverse_switch[lst[num-1-(i+1)]]
                lst[num-1+(i+1)] = reverse_switch[lst[num-1+(i+1)]]
    lst[num-1] = reverse_switch[lst[num-1]]

for _ in range(st):
    a, b = map(int, input().split())  # 성별(1 남 2 여), 받은 수
    if a == 1:
        boy(b)
    elif a == 2:
        girl(b)

print_num = N//20 + bool(N % 20)  # 출력할 줄의 수
for i in range(print_num):
    if len(lst) > 20:
        for _ in range(20):  # 20개씩 프린트하고 프린트한 것 삭제
            print(lst[0], end=' ')
            lst.pop(0)
        print()
    elif len(lst) <= 20:  # 파일 길이가 20 이하일 경우
        for x in lst:  # 그대로 프린트
            print(x, end=' ')
print()
