L = int(input())
cake = [0]*(L+1)
N = int(input())
people = [0]*(N+1)

person = N+1
Max = 0
for n in range(1, N+1):
    P, K = map(int, input().split())  # P번부터 K번까지 원함
    if Max < (K-P+1):
        Max = (K-P+1)
        person = n
    elif Max == (K-P+1):
        if person > n:
            person = n
    for i in range(P, K+1):
        if cake[i] == 0:
            cake[i] = n
print(person)

for i in range(1, L+1):
    if cake[i] != 0:
        people[cake[i]] += 1

Max = 0
answer = N+2
for i in range(1, N+1):
    if Max < people[i]:
        Max = people[i]
        Maxi = i
    elif Max == people[i]:
        if Maxi > i:
            Maxi = i

print(Maxi)