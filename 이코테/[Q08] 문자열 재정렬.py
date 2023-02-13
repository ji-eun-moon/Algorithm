lst = list(input())
alpha = []

sum = 0
for a in lst:
    if a.isalpha():
        alpha.append(a)
    else:
        sum += int(a)

# alpha.sort()
# 버블 정렬
for i in range(len(alpha)-1, 0, -1):
    for j in range(i):
        if ord(alpha[j]) > ord(alpha[j+1]):
            alpha[j], alpha[j+1] = alpha[j+1], alpha[j]

for a in alpha:
    print(a, end='')
print(sum)