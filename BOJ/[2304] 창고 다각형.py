N = int(input())
lst = []
for _ in range(N):
    L, H = map(int, input().split())
    lst.append([L, H])

lst.sort(key=lambda x:x[0])
st = lst[0][0]
ed = lst[-1][0]
box = [0]*(ed+1)

for a in lst:
    box[a[0]] = a[1]
print(box)
result = box[:]
for i in range(st, ed):
    if result[i] > result[i+1]:
        result[i+1] = result[i]
    if result[i] < result[i+1]:
        continue
print(result)
result2 = box[:]
for i in range(ed, st-1, -1):
    if result2[i] > result2[i-1]:
        result2[i-1] = result2[i]
print(result2)
answer = [0]*(ed+1)
for i in range(st, ed):
    if result[i] != result2[i]:
        answer[i] = result[i]
    else:
        answer[i] = result[i]
        break
for i in range(ed, st-1, -1):
    if result[i] != result2[i]:
        answer[i] = result2[i]
    else:
        break
print(answer)
print(sum(answer))