N = int(input())
words = []
for _ in range(N):
    words.append(input())

new_words = sorted(words, key=lambda x:(len(x), x))
print(new_words[0])
for i in range(1, N):
    if new_words[i] != new_words[i-1]:
        print(new_words[i])
