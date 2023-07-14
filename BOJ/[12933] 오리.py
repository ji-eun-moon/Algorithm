sound = input()  # 녹음한 소리
N = len(sound)
duck = 'quack'

lst = []
for i in range(N):
    if sound[i] == 'q':
        lst.append(['q'])
    elif sound[i] == 'u':
        flag = 0
        for a in lst:
            if len(a) == 1:
                a.append('u')
                flag = 1
                break
        if flag == 0:
            result = -1
            break
    elif sound[i] == 'a':
        flag = 0
        for a in lst:
            if len(a) == 2:
                a.append('a')
                flag = 1
                break
        if flag == 0:
            result = -1
            break
    elif sound[i] == 'c':
        flag = 0
        for a in lst:
            if len(a) == 3:
                a.append('c')
                flag = 1
                break
        if flag == 0:
            result = -1
            break
    elif sound[i] == 'k':
        flag = 0
        for a in lst:
            if len(a) == 4:

                flag = 1
        if flag == 0:
            result = -1
            break

if result != -1:
    result = 0
    for a in lst:
        if len(a) == 5:
            result += 1

