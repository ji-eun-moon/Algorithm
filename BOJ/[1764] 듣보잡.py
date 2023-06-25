N, M = map(int, input().split())
dic = {}

for _ in range(N):
    name = input()
    dic.setdefault(name, 0)
    dic[name] += 1

for _ in range(M):
    name = input()
    dic.setdefault(name, 0)
    dic[name] += 1

lst = []
for key, value in dic.items():
    if value == 2:
        lst.append(key)

lst.sort()
print(len(lst))
for name in lst:
    print(name)